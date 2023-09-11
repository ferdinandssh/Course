-- https://i-godata-systems-metabase.golabs.io/question/1144-merchant-platform-data-lineage-tools
WITH RECURSIVE
base_table AS (
  SELECT 
    name AS job_name,
    REGEXP_SPLIT_TO_TABLE(REPLACE(REPLACE(ARRAY_TO_STRING(sources, ','), ':', '.'), 'bigquery.//', ''), ',') AS upstream_job_name
  FROM job
),

status_table AS (
  SELECT
    job_name,
    scheduled_at,
    status,
    ROW_NUMBER() OVER(PARTITION BY job_name ORDER BY scheduled_at DESC) AS latest_rank
  FROM job_run
),

recursive_join AS (
  SELECT 
    job_name,
    upstream_job_name,
    1 AS level
  FROM base_table
  WHERE upstream_job_name != ''
    [[AND job_name = {{var_job_name}}]]
  UNION ALL
  SELECT 
    rj.job_name,
    bs.upstream_job_name, 
    level + 1
  FROM recursive_join AS rj
  JOIN base_table AS bs
    ON rj.upstream_job_name = bs.job_name
    AND bs.upstream_job_name != ''
    [[AND CAST(1 AS VARCHAR) != {{var_job_name}}--]] AND level < 1
    [[AND CAST(1 AS VARCHAR) != {{var_first_upstream_job_name}} AND level < 1]]
),

final_result AS (
  SELECT
    rj.*,
    CASE
      WHEN bs.job_name IS NULL OR bs.upstream_job_name IS NULL THEN TRUE
      ELSE FALSE
    END AS last_upstream_job_flag,
    st.scheduled_at,
    st.status,
    CASE
      WHEN st.status = 'success' THEN TRUE
      WHEN st.status != 'success' THEN FALSE
    END AS status_success_flag,
    DIV(SUM(CASE WHEN sp.status = 'success' THEN 1 ELSE 0 END), NULLIF(COUNT(sp.status), 0)) AS last_five_job_success_percentage
  FROM recursive_join AS rj
  LEFT JOIN base_table AS bs
    ON rj.upstream_job_name = bs.job_name
    AND bs.upstream_job_name != ''
  LEFT JOIN status_table AS st
    ON rj.upstream_job_name = st.job_name
    AND st.latest_rank = 1
  LEFT JOIN status_table AS sp
    ON rj.upstream_job_name = sp.job_name
    AND sp.latest_rank <= 5
  GROUP BY 1,2,3,4,5,6,7
)

SELECT DISTINCT
  job_name,
  upstream_job_name,
  level,
  scheduled_at,
  status,
  last_upstream_job_flag,
  last_five_job_success_percentage
FROM final_result
[[WHERE CAST(1 AS VARCHAR) != {{var_job_name}} [[AND level = {{var_level}}]] [[AND CASE WHEN {{var_status}} = 1 THEN status_success_flag ELSE NOT status_success_flag END]] ]]
[[WHERE upstream_job_name = {{var_first_upstream_job_name}}]]
ORDER BY 1,3,5,2

