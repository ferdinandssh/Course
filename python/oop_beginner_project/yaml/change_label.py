#!/usr/bin/python

# import yaml
import ruamel.yaml
import sys

yaml = ruamel.yaml.YAML()
yaml.width = 4096
yaml.preserve_quotes = True
yaml.boolean_representation = ['False', 'True']
table_list = [

# # SETTING AWAL
#  ['table_name','namespace','team_4']

# EDIT
    ['data-gojek-id-mart.care_unit.detail_agent_experience_email_gsheet','communication_platform','FALSE']
    ,['data-gojek-id-mart.care_unit.detail_bid_service_type_location_all_countries','communication_platform','TRUE']
    ,['data-gojek-id-mart.care_unit.detail_care_agent_profile','communication_platform','TRUE']
    ,['data-gojek-id-mart.care_unit.detail_care_company_loss','communication_platform','TRUE']
    ,['data-gojek-id-mart.care_unit.detail_chatbot_selfserve_daily','communication_platform','TRUE']
    ,['data-gojek-id-mart.care_unit.detail_csat_manual_case','communication_platform','FALSE']
    ,['data-gojek-id-mart.care_unit.detail_driver_attribute','communication_platform','FALSE']
    ,['data-gojek-id-mart.care_unit.detail_gopay_merchant_issue_mapping','communication_platform','TRUE']
    ,['data-gojek-id-mart.care_unit.detail_gopay_portal_usage','communication_platform','FALSE']
    ,['data-gojek-id-mart.care_unit.detail_helpcenter_clickstream','communication_platform','TRUE']
    ,['data-gojek-id-mart.care_unit.detail_helpify_articles','communication_platform','TRUE']
    ,['data-gojek-id-mart.care_unit.detail_helpify_static_field','communication_platform','FALSE']
    ,['data-gojek-id-mart.care_unit.detail_litmus_experiment','communication_platform','TRUE']
    ,['data-gojek-id-mart.care_unit.detail_manual_agent_case_handling_time_per_department_daily','communication_platform','TRUE']
    ,['data-gojek-id-mart.care_unit.detail_manual_case_handling_time','communication_platform','FALSE']
    ,['data-gojek-id-mart.care_unit.detail_mcu_resolution_time_tracker_daily','communication_platform','TRUE']
    ,['data-gojek-id-mart.care_unit.detail_no_order_audit_service_area_threshold_vn','communication_platform','FALSE']
    ,['data-gojek-id-mart.care_unit.detail_salesforce_inbox_message','communication_platform','FALSE']
    ,['data-gojek-id-mart.care_unit.detail_service_case','communication_platform','TRUE']
    ,['data-gojek-id-mart.care_unit.detail_service_case_ccu','communication_platform','TRUE']
    ,['data-gojek-id-mart.care_unit.detail_service_case_dcu','communication_platform','TRUE']
    ,['data-gojek-id-mart.care_unit.detail_service_case_history','communication_platform','TRUE']
    ,['data-gojek-id-mart.care_unit.detail_service_case_history_mcu','communication_platform','FALSE']
    ,['data-gojek-id-mart.care_unit.detail_service_case_history_mcu_snapshot','communication_platform','FALSE']
    ,['data-gojek-id-mart.care_unit.detail_service_case_mcu','communication_platform','TRUE']
    ,['data-gojek-id-mart.care_unit.federated_care_agent_gsheet','communication_platform','FALSE']
    ,['data-gojek-id-mart.care_unit.federated_care_agent_profile','communication_platform','FALSE']
    ,['data-gojek-id-mart.care_unit.federated_gopay_merchant_issue_mapping','communication_platform','FALSE']
    ,['data-gojek-id-mart.care_unit.federated_helpify_static_fields_gsheet','communication_platform','FALSE']
    ,['data-gojek-id-mart.care_unit.opstech_frontdesk_tokens','communication_platform','FALSE']
    ,['data-gojek-id-mart.care_unit.summary_apology_voucher_redeemed','communication_platform','FALSE']
    ,['data-gojek-id-mart.care_unit.summary_care_defect_rate_per_issue_daily','communication_platform','TRUE']
    ,['data-gojek-id-mart.care_unit.summary_care_defect_rate_per_issue_monthly','communication_platform','TRUE']
    ,['data-gojek-id-mart.care_unit.summary_care_defect_rate_per_issue_weekly','communication_platform','TRUE']
    ,['data-gojek-id-mart.care_unit.summary_ccu_csat_daily','communication_platform','FALSE']
    ,['data-gojek-id-mart.care_unit.summary_ccu_defect_rate_by_issue_name_monthly','communication_platform','FALSE']
    ,['data-gojek-id-mart.care_unit.summary_ccu_defect_rate_by_issue_weekly','communication_platform','FALSE']
    ,['data-gojek-id-mart.care_unit.summary_customer_ticket_retention_movement_monthly','communication_platform','TRUE']
    ,['data-gojek-id-mart.care_unit.summary_driver_online_duration_hourly_all_countries','communication_platform','TRUE']
    ,['data-gojek-id-mart.care_unit.summary_gopay_portal_usage_monthly','communication_platform','FALSE']
    ,['data-gojek-id-mart.care_unit.summary_helpcenter_feedback_daily','communication_platform','TRUE']
    ,['data-gojek-id-mart.care_unit.summary_mcu_percentile_resolution_time_monthly','communication_platform','FALSE']
    ,['data-gojek-id-mart.care_unit.summary_mcu_resolution_tracker_by_issue_queue_monthly','communication_platform','FALSE']
    ,['data-gojek-id-mart.care_unit.summary_mcu_resolution_tracker_by_issue_queue_weekly','communication_platform','FALSE']
    ,['data-gojek-id-mart.care_unit.summary_mcu_resolution_tracker_by_queue_monthly','communication_platform','FALSE']
    ,['data-gojek-id-mart.care_unit.summary_mcu_resolution_tracker_by_queue_weekly','communication_platform','FALSE']
    ,['data-gojek-id-mart.care_unit.summary_mcu_resolution_tracker_overall_monthly','communication_platform','FALSE']
    ,['data-gojek-id-mart.care_unit.summary_mcu_resolution_tracker_overall_weekly','communication_platform','FALSE']
    ,['data-gojek-id-mart.care_unit.summary_mcu_ticket_resolution_by_channel','communication_platform','FALSE']
    ,['data-gojek-id-mart.care_unit.summary_mcu_ticket_resolution_by_channel_issue','communication_platform','FALSE']
    ,['data-gojek-id-mart.care_unit.summary_mcu_ticket_resolution_by_issue','communication_platform','FALSE']
    ,['data-gojek-id-mart.care_unit.summary_mcu_ticket_resolution_by_queue','communication_platform','FALSE']
    ,['data-gojek-id-mart.care_unit.summary_mcu_ticket_resolution_overall','communication_platform','FALSE']
    ,['data-gojek-id-mart.gobiz_platform.detail_gobiz_app_version_clevertap','gofood','FALSE']
    ,['data-gojek-id-mart.gobiz_platform.detail_gobiz_app_version_goid','gofood','FALSE']
    ,['data-gojek-id-mart.gobiz_platform.detail_gobiz_feature_management_outlet','gofood','TRUE']
    ,['data-gojek-id-mart.gobiz_platform.detail_gobiz_feature_management_user','gofood','TRUE']
    ,['data-gojek-id-mart.gobiz_platform.detail_gobiz_merchant_promo_adoption_journey','gofood','FALSE']
    ,['data-gojek-id-mart.gobiz_platform.detail_gobiz_self_serve_user_creation_event','gofood','FALSE']
    ,['data-gojek-id-mart.gobiz_platform.detail_gobiz_self_serve_user_management_event','gofood','FALSE']
    ,['data-gojek-id-mart.gobiz_platform.detail_gobiz_shuffle_campaign_reference','gofood','FALSE']
    ,['data-gojek-id-mart.gobiz_platform.detail_gobiz_web_survey_daily','gofood','FALSE']
    ,['data-gojek-id-mart.gobiz_platform.detail_gobiz_web_survey_response_daily','gofood','FALSE']
    ,['data-gojek-id-mart.gobiz_platform.detail_gofood_booking_before2019','gofood','FALSE']
    ,['data-gojek-id-mart.gobiz_platform.detail_master_merchant_gobiz','gofood','TRUE']
    ,['data-gojek-id-mart.gobiz_platform.detail_merchant_gobiz_event_activity','gofood','TRUE']
    ,['data-gojek-id-mart.gobiz_platform.detail_promo_social_proof_merchant_permutation','gofood','FALSE']
    ,['data-gojek-id-mart.gobiz_platform.federated_gobiz_shuffle_impression_weight','gofood','FALSE']
    ,['data-gojek-id-mart.gobiz_platform.federated_playstore_mapping','gofood','FALSE']
    ,['data-gojek-id-mart.gobiz_platform.federated_user_engagement_gobiz_event_mapping','gofood','FALSE']
    ,['data-gojek-id-mart.gobiz_platform.summary_gobiz_app_version_outlet_analytics_weekly','gofood','TRUE']
    ,['data-gojek-id-mart.gobiz_platform.summary_gobiz_app_version_outlet_weekly','gofood','TRUE']
    ,['data-gojek-id-mart.gobiz_platform.summary_gobiz_device_app_version_daily','gofood','FALSE']
    ,['data-gojek-id-mart.gobiz_platform.summary_gobiz_email_campaign_performance_user_daily','gofood','FALSE']
    ,['data-gojek-id-mart.gobiz_platform.summary_gobiz_inbox_campaign_performance_user_event_daily','gofood','FALSE']
    ,['data-gojek-id-mart.gobiz_platform.summary_gobiz_marketing_campaign_performance_user_device_daily','gofood','FALSE']
    ,['data-gojek-id-mart.gobiz_platform.summary_gobiz_shuffle_campaign_daily','gofood','FALSE']
    ,['data-gojek-id-mart.gobiz_platform.summary_gobiz_shuffle_campaign_performance_user_device_daily','gofood','FALSE']
    ,['data-gojek-id-mart.gobiz_platform.summary_lifecycle_entity_modules_daily','gofood','FALSE']
    ,['data-gojek-id-mart.gobiz_platform.summary_lifecycle_outlet_modules_daily','gofood','FALSE']
    ,['data-gojek-id-mart.gobiz_platform.summary_mcu_classification_daily','gofood','FALSE']
    ,['data-gojek-id-mart.gobiz_platform.summary_merchant_clevertap_event_daily','gofood','TRUE']
    ,['data-gojek-id-mart.gobiz_platform.summary_merchant_lifecycle_state_daily','gofood','TRUE']
    ,['data-gojek-id-mart.gobiz_platform.summary_outlet_name_self_serve_moderation_daily','gofood','FALSE']
    ,['data-gojek-id-mart.gobiz_platform.summary_playstore_classification_daily','gofood','FALSE']
    ,['data-gojek-id-mart.goto_passport.detail_account','gojek_dwh','FALSE']
    ,['data-gojek-id-mart.goto_passport.detail_account_reference','gojek_dwh','FALSE']
    ,['data-gojek-id-mart.identity_communication_platform.detail_anonymization_metrics','communication_platform','FALSE']
    ,['data-gojek-id-mart.identity_communication_platform.detail_call_cost_reference','communication_platform','FALSE']
    ,['data-gojek-id-mart.identity_communication_platform.detail_channel_member','communication_platform','FALSE']
    ,['data-gojek-id-mart.identity_communication_platform.detail_channel_member_bot_campaign','communication_platform','FALSE']
    ,['data-gojek-id-mart.identity_communication_platform.detail_chat','communication_platform','TRUE']
    ,['data-gojek-id-mart.identity_communication_platform.detail_chat_channel','communication_platform','FALSE']
    ,['data-gojek-id-mart.identity_communication_platform.detail_chat_channel_reference','communication_platform','FALSE']
    ,['data-gojek-id-mart.identity_communication_platform.detail_chat_message','communication_platform','FALSE']
    ,['data-gojek-id-mart.identity_communication_platform.detail_chat_message_read_bot','communication_platform','FALSE']
    ,['data-gojek-id-mart.identity_communication_platform.detail_chat_profile','communication_platform','FALSE']
    ,['data-gojek-id-mart.identity_communication_platform.detail_chat_tokopedia','communication_platform','FALSE']
    ,['data-gojek-id-mart.identity_communication_platform.detail_clickstream_customer_reference','communication_platform','TRUE']
    ,['data-gojek-id-mart.identity_communication_platform.detail_communication_budget','communication_platform','FALSE']
    ,['data-gojek-id-mart.identity_communication_platform.detail_communication_email_recipient','communication_platform','FALSE']
    ,['data-gojek-id-mart.identity_communication_platform.detail_country_code','communication_platform','FALSE']
    ,['data-gojek-id-mart.identity_communication_platform.detail_customer_app_version','communication_platform','FALSE']
    ,['data-gojek-id-mart.identity_communication_platform.detail_inbox_campaign','communication_platform','FALSE']
    ,['data-gojek-id-mart.identity_communication_platform.detail_litmus_event','communication_platform','TRUE']
    ,['data-gojek-id-mart.identity_communication_platform.detail_login_unit_cost','communication_platform','FALSE']
    ,['data-gojek-id-mart.identity_communication_platform.detail_push_notification_campaign_manager','communication_platform','FALSE']
    ,['data-gojek-id-mart.identity_communication_platform.detail_sms_cost','communication_platform','FALSE']
    ,['data-gojek-id-mart.identity_communication_platform.detail_support_chat_message','communication_platform','FALSE']
    ,['data-gojek-id-mart.identity_communication_platform.detail_telecom_prefix','communication_platform','FALSE']
    ,['data-gojek-id-mart.identity_communication_platform.detail_user_profile','communication_platform','FALSE']
    ,['data-gojek-id-mart.identity_communication_platform.federated_sms_team_mapping','communication_platform','FALSE']
    ,['data-gojek-id-mart.identity_communication_platform.goid_phone_operators','communication_platform','FALSE']
    ,['data-gojek-id-mart.identity_communication_platform.summary_call_cost_looker_daily','communication_platform','FALSE']
    ,['data-gojek-id-mart.identity_communication_platform.summary_chat_booking_daily','communication_platform','FALSE']
    ,['data-gojek-id-mart.identity_communication_platform.summary_chat_bot_campaign','communication_platform','FALSE']
    ,['data-gojek-id-mart.identity_communication_platform.summary_chat_call','communication_platform','FALSE']
    ,['data-gojek-id-mart.identity_communication_platform.summary_goid_anomaly_logins_daily','communication_platform','FALSE']
    ,['data-gojek-id-mart.identity_communication_platform.summary_goid_dbl_active_users_daily','communication_platform','FALSE']
    ,['data-gojek-id-mart.identity_communication_platform.summary_goid_dbl_daily','communication_platform','FALSE']
    ,['data-gojek-id-mart.identity_communication_platform.summary_goid_dbl_opt_out_daily','communication_platform','FALSE']
    ,['data-gojek-id-mart.identity_communication_platform.summary_goid_dbl_views_daily','communication_platform','FALSE']
    ,['data-gojek-id-mart.identity_communication_platform.summary_goid_login_daily','communication_platform','TRUE']
    ,['data-gojek-id-mart.identity_communication_platform.summary_goid_login_distribution_daily','communication_platform','FALSE']
    ,['data-gojek-id-mart.identity_communication_platform.summary_goid_login_distribution_monthly','communication_platform','FALSE']
    ,['data-gojek-id-mart.identity_communication_platform.summary_goid_logout_daily','communication_platform','TRUE']
    ,['data-gojek-id-mart.identity_communication_platform.summary_login_cost_monthly','communication_platform','FALSE']
    ,['data-gojek-id-mart.identity_communication_platform.summary_mfa_coverage_monthly','communication_platform','FALSE']
    ,['data-gojek-id-mart.identity_communication_platform.summary_mfa_daily','communication_platform','FALSE']
    ,['data-gojek-id-mart.identity_communication_platform.summary_mfa_ttl_daily','communication_platform','FALSE']
    ,['data-gojek-id-mart.identity_communication_platform.summary_number_masking_ceiled_daily','communication_platform','FALSE']
    ,['data-gojek-id-mart.identity_communication_platform.summary_number_masking_platform','communication_platform','FALSE']
    ,['data-gojek-id-mart.identity_communication_platform.summary_one_tap_login_time_distribution','communication_platform','FALSE']
    ,['data-gojek-id-mart.identity_communication_platform.summary_push_notification_campaign_manager_daily','communication_platform','FALSE']
    ,['data-gojek-id-mart.identity_communication_platform.summary_push_notifications_delivery_daily','communication_platform','FALSE']
    ,['data-gojek-id-mart.identity_communication_platform.summary_sms_budgetwise_delivered','communication_platform','FALSE']
    ,['data-gojek-id-mart.identity_communication_platform.summary_sms_daily','communication_platform','FALSE']
    ,['data-gojek-id-mart.identity_communication_platform.summary_sms_delivered_daily','communication_platform','FALSE']
    ,['data-gojek-id-mart.identity_communication_platform.summary_trusted_device_ato_daily','communication_platform','FALSE']
    ,['data-gojek-id-mart.identity_communication_platform.summary_trusted_devices_daily','communication_platform','FALSE']
    ,['data-gojek-id-mart.identity_communication_platform.summary_voip_daily','communication_platform','FALSE']
    ,['data-gojek-id-mart.identity_communication_platform.summary_whatsapp_daily','communication_platform','FALSE']
    ,['data-gojek-id-mart.laundromat.detail_laundromat_contract_master_facet_reference','merchant_platform','FALSE']
    ,['data-gojek-id-mart.laundromat.detail_laundromat_contract_master_transformation','merchant_platform','FALSE']
    ,['data-gojek-id-mart.laundromat.detail_laundromat_fee_inconsistency_issue','merchant_platform','FALSE']
    ,['data-gojek-id-mart.laundromat.detail_laundromat_fee_inconsistency_issue_detail','merchant_platform','TRUE']
    ,['data-gojek-id-mart.laundromat.detail_laundromat_fee_inconsistency_issue_sales_working_sheet','merchant_platform','FALSE']
    ,['data-gojek-id-mart.laundromat.detail_laundromat_fee_master_facet_reference','merchant_platform','FALSE']
    ,['data-gojek-id-mart.laundromat.detail_laundromat_fee_master_transformation','merchant_platform','FALSE']
    ,['data-gojek-id-mart.laundromat.detail_laundromat_master_fee_level','merchant_platform','TRUE']
    ,['data-gojek-id-mart.laundromat.detail_laundromat_master_reference','merchant_platform','TRUE']
    ,['data-gojek-id-mart.laundromat.detail_laundromat_package_master_facet_reference','merchant_platform','FALSE']
    ,['data-gojek-id-mart.laundromat.detail_laundromat_package_master_transformation','merchant_platform','FALSE']
    ,['data-gojek-id-mart.laundromat.detail_laundromat_product_master_facet_reference','merchant_platform','FALSE']
    ,['data-gojek-id-mart.laundromat.detail_laundromat_product_master_transformation','merchant_platform','FALSE']
    ,['data-gojek-id-mart.laundromat.federated_laundromat_contract_master_facet_reference','merchant_platform','FALSE']
    ,['data-gojek-id-mart.laundromat.federated_laundromat_fee_master_facet_reference','merchant_platform','FALSE']
    ,['data-gojek-id-mart.laundromat.federated_laundromat_package_master_facet_reference','merchant_platform','FALSE']
    ,['data-gojek-id-mart.laundromat.federated_laundromat_product_master_facet_reference','merchant_platform','FALSE']
    ,['data-gojek-id-mart.merchant_platform_goto.detail_goto_gojek_master_merchant_outlet_base','merchant_platform','TRUE']
    ,['data-gojek-id-mart.merchant_platform.detail_gobiz_management_profile_change_request_log','merchant_platform','FALSE']
    ,['data-gojek-id-mart.merchant_platform.detail_gobiz_management_profile_change_request_log_with_change_request_count','merchant_platform','TRUE']
    ,['data-gojek-id-mart.merchant_platform.detail_gobiz_user_data_snapshot_daily','merchant_platform','TRUE']
    ,['data-gojek-id-mart.merchant_platform.detail_latest_merchant_onboarding','merchant_platform','TRUE']
    ,['data-gojek-id-mart.merchant_platform.detail_master_merchant_eim','merchant_platform','TRUE']
    ,['data-gojek-id-mart.merchant_platform.detail_master_merchant_location','merchant_platform','TRUE']
    ,['data-gojek-id-mart.merchant_platform.detail_master_merchant_universe','merchant_platform','TRUE']
    ,['data-gojek-id-mart.merchant_platform.detail_master_merchant_vietnam_universe','merchant_platform','TRUE']
    ,['data-gojek-id-mart.merchant_platform.detail_merchant_data_auditor_consistency','merchant_platform','FALSE']
    ,['data-gojek-id-mart.merchant_platform.detail_merchant_data_auditor_validity_cmp','merchant_platform','FALSE']
    ,['data-gojek-id-mart.merchant_platform.detail_merchant_data_auditor_validity_cms','merchant_platform','FALSE']
    ,['data-gojek-id-mart.merchant_platform.detail_merchant_data_auditor_validity_dynamics','merchant_platform','FALSE']
    ,['data-gojek-id-mart.merchant_platform.detail_merchant_data_auditor_validity_error_log','merchant_platform','FALSE']
    ,['data-gojek-id-mart.merchant_platform.detail_merchant_data_auditor_validity_salesforce','merchant_platform','FALSE']
    ,['data-gojek-id-mart.merchant_platform.detail_merchant_data_cmp','merchant_platform','FALSE']
    ,['data-gojek-id-mart.merchant_platform.detail_merchant_data_cms','merchant_platform','FALSE']
    ,['data-gojek-id-mart.merchant_platform.detail_merchant_data_dynamics','merchant_platform','FALSE']
    ,['data-gojek-id-mart.merchant_platform.detail_merchant_data_salesforce','merchant_platform','TRUE']
    ,['data-gojek-id-mart.merchant_platform.detail_merchant_onboarding_followup_reason_code','merchant_platform','FALSE']
    ,['data-gojek-id-mart.merchant_platform.detail_merchant_onboarding_kyc','merchant_platform','FALSE']
    ,['data-gojek-id-mart.merchant_platform.detail_outlet_update_history','merchant_platform','TRUE']
    ,['data-gojek-id-mart.merchant_platform.detail_unmatch_user_outlet_tag','merchant_platform','TRUE']
    ,['data-gojek-id-mart.merchant_platform.federated_detail_holiday_date_for_forecasting','merchant_platform','FALSE']
    ,['data-gojek-id-mart.merchant_platform.federated_merchant_data_auditor_specification','merchant_platform','FALSE']
    ,['data-gojek-id-mart.merchant_platform.federated_merchant_mcc_code_list','merchant_platform','FALSE']
    ,['data-gojek-id-mart.merchant_platform.federated_salesforce_city','merchant_platform','FALSE']
    ,['data-gojek-id-mart.merchant_platform.summary_bucket_sla_kyc_daily','merchant_platform','FALSE']
    ,['data-gojek-id-mart.merchant_platform.summary_bucket_sla_kyc_workdays_daily','merchant_platform','FALSE']
    ,['data-gojek-id-mart.merchant_platform.summary_gobiz_self_serve_add_outlet_journey_daily','merchant_platform','FALSE']
    ,['data-gojek-id-mart.merchant_platform.summary_kyc_followup_reason_daily','merchant_platform','FALSE']
    ,['data-gojek-id-mart.merchant_platform.summary_master_merchant_transaction_universe_daily','merchant_platform','TRUE']
    ,['data-gojek-id-mart.merchant_platform.summary_master_merchant_transaction_universe_monthly','merchant_platform','TRUE']
    ,['data-gojek-id-mart.merchant_platform.summary_master_merchant_transaction_universe_weekly','merchant_platform','TRUE']
    ,['data-gojek-id-mart.merchant_platform.summary_master_merchant_transaction_vietnam_universe_daily','merchant_platform','TRUE']
    ,['data-gojek-id-mart.merchant_platform.summary_mercator_metadata_daily','merchant_platform','TRUE']
    ,['data-gojek-id-mart.merchant_platform.summary_merchant_onboarding_activation_daily','merchant_platform','FALSE']
    ,['data-gojek-id-mart.merchant_platform.summary_merchant_onboarding_add_products_daily','merchant_platform','FALSE']
    ,['data-gojek-id-mart.merchant_platform.summary_merchant_onboarding_funnel_daily','merchant_platform','FALSE']
    ,['data-gojek-id-mart.merchant_platform.summary_merchant_onboarding_journey_daily','merchant_platform','TRUE']
    ,['data-gojek-id-mart.merchant_platform.summary_merchant_onboarding_monitoring_daily','merchant_platform','FALSE']
    ,['data-gojek-id-mart.merchant_platform.summary_merchant_onboarding_monitoring_forecast_and_threshold','merchant_platform','FALSE']
    ,['data-gojek-id-mart.merchant_platform.summary_merchant_onboarding_monitoring_forecast_and_threshold_view','merchant_platform','FALSE']
    ,['data-gojek-id-mart.merchant_platform.summary_merchant_onboarding_presubmission_daily','merchant_platform','FALSE']
    ,['data-gojek-id-mart.merchant_platform.summary_merchant_onboarding_product_activation_by_monthly','merchant_platform','FALSE']
    ,['data-gojek-id-mart.merchant_platform.summary_merchant_onboarding_product_activation_by_weekly','merchant_platform','FALSE']
    ,['data-gojek-id-mart.merchant_platform.summary_merchant_onboarding_product_activation_concluded_by_monthly','merchant_platform','FALSE']
    ,['data-gojek-id-mart.merchant_platform.summary_merchant_onboarding_product_activation_concluded_by_weekly','merchant_platform','FALSE']
    ,['data-gojek-id-mart.merchant_platform.summary_merchant_onboarding_product_activation_rejection_reason_weekly','merchant_platform','FALSE']
    ,['data-gojek-id-mart.merchant_platform.summary_merchant_onboarding_registration_by_monthly','merchant_platform','FALSE']
    ,['data-gojek-id-mart.merchant_platform.summary_merchant_onboarding_registration_by_weekly','merchant_platform','FALSE']
    ,['data-gojek-id-mart.merchant_platform.summary_merchant_onboarding_registration_concluded_by_monthly','merchant_platform','FALSE']
    ,['data-gojek-id-mart.merchant_platform.summary_merchant_onboarding_registration_concluded_by_weekly','merchant_platform','FALSE']
    ,['data-gojek-id-mart.merchant_platform.summary_merchant_onboarding_registration_rejected_reason_by_monthly','merchant_platform','FALSE']
    ,['data-gojek-id-mart.merchant_platform.summary_merchant_onboarding_registration_rejected_reason_by_weekly','merchant_platform','FALSE']
    ,['data-gojek-id-mart.merchant_platform.summary_merchant_onboarding_sla_bucket_daily','merchant_platform','FALSE']
    ,['data-gojek-id-mart.merchant_platform.summary_merchant_onboarding_validation_monitoring_daily','merchant_platform','FALSE']
    ,['data-gojek-id-mart.merchant_platform.summary_merchant_platform_analytic_monthly','merchant_platform','TRUE']
    ,['data-gojek-id-mart.merchant_platform.summary_sla_kyc_daily','merchant_platform','FALSE']
    ,['data-gojek-id-mart.merchant_platform.summary_sla_kyc_workdays_daily','merchant_platform','FALSE']
    ,['data-gojek-id-mart.merchant_platform.summary_third_party_platform_facilitator_aggregator_daily','merchant_platform','FALSE']
    ,['data-gojek-id-mart.pedestal.detail_pedestal_data_issue_incorrect_mapping_entity_and_outlet','merchant_platform','TRUE']
    ,['data-gojek-id-mart.pedestal.federated_merchant_onboarding_mcc_list','merchant_platform','FALSE']
    ,['data-gojek-id-mart.salesforce.detail_billing_group','gojek_dwh','FALSE']
    ,['data-gojek-id-mart.salesforce.detail_case','gojek_dwh','FALSE']
    ,['data-gojek-id-mart.salesforce.detail_case_appeal_reason','gojek_dwh','FALSE']
    ,['data-gojek-id-mart.salesforce.detail_entity','gojek_dwh','FALSE']
    ,['data-gojek-id-mart.salesforce.detail_goes_type','gojek_dwh','FALSE']
    ,['data-gojek-id-mart.salesforce.detail_indonesia_product_outlet','gojek_dwh','FALSE']
    ,['data-gojek-id-mart.salesforce.detail_issue_id','gojek_dwh','FALSE']
    ,['data-gojek-id-mart.salesforce.detail_nanorep','gojek_dwh','FALSE']
    ,['data-gojek-id-mart.salesforce.detail_product_outlet','gojek_dwh','FALSE']
    ,['data-gojek-id-mart.salesforce.detail_service_account','gojek_dwh','FALSE']
    ,['data-gojek-id-mart.salesforce.detail_service_case','gojek_dwh','FALSE']
    ,['data-gojek-id-mart.salesforce.detail_service_case_comment','gojek_dwh','FALSE']
    ,['data-gojek-id-mart.salesforce.detail_service_case_history','gojek_dwh','FALSE']
    ,['data-gojek-id-mart.salesforce.detail_service_completed_milestone','gojek_dwh','FALSE']
    ,['data-gojek-id-mart.salesforce.detail_service_group','gojek_dwh','FALSE']
    ,['data-gojek-id-mart.salesforce.detail_service_record_type','gojek_dwh','FALSE']
    ,['data-gojek-id-mart.salesforce.detail_service_record_type_reference','gojek_dwh','FALSE']
    ,['data-gojek-id-mart.salesforce.detail_service_survey_invitation','gojek_dwh','FALSE']
    ,['data-gojek-id-mart.salesforce.detail_service_survey_response','gojek_dwh','FALSE']
    ,['data-gojek-id-mart.salesforce.detail_service_user','gojek_dwh','FALSE']
    ,['data-gojek-id-mart.salesforce.detail_service_workorder','gojek_dwh','FALSE']

]

def _derive_error_channel(team):
    CHANNEL_MAP = {
        'team_4': ['slack://#gojek-merchant-care-p0-alert'],
    }
    return(CHANNEL_MAP.get(team))

def _derive_label(team):
    LABEL_MAP = {
        'team_4': 'gojek-merchant-care-p0'
    }

    return(LABEL_MAP.get(team))

def _derive_owner(team):
    LABEL_MAP = {
        'team_4': '@data-ops-merchant-care-icp'
    }
    return(LABEL_MAP.get(team))

def _derive_cost_team(dataset):
    LABEL_MAP = {
        'care_unit': 'communication_platform',
        'gobiz_platform': 'merchant_platform',
        'goto_passport': 'communication_platform',
        'identity_communication_platform': 'communication_platform',
        'laundromat': 'merchant_platform',
        'merchant_platform': 'merchant_platform',
        'merchant_platform_goto': 'merchant_platform',
        'pedestal': 'merchant_platform',
        'salesforce': 'communication_platform'
    }
    return(LABEL_MAP.get(dataset))


#SETTING AWAL
# def update_yaml(file_dir,team):
    error_list_notify = _derive_error_channel(team)
    try:
        with open(file_dir) as f:
            yaml_output = yaml.load(f)               
            # Change owner          
            yaml_output['owner'] = _derive_owner(team)  

            # Change retry
            if yaml_output['behavior'].get("retry"):           
                yaml_output['behavior']['retry']['count'] = 7
            else:
                yaml_output['behavior']['retry'] = {'count':7}

            # Notify
            if yaml_output["behavior"].get("notify"):            
                original_list = yaml_output['behavior']['notify']
                for index, value in enumerate(original_list):
                    if value.get('on') == 'failure':              
                        try:
                            yaml_output['behavior']['notify'][index]['channels'].remove("slack://#mp-data-mart-alert")
                        except:
                            pass  
                        tmp_list = yaml_output['behavior']['notify'][index]['channels'] + error_list_notify
                        distinct_list = list(set(tmp_list))
                        yaml_output['behavior']['notify'][index]['channels'] = list(set(tmp_list))
            else:
                yaml_output['behavior']['notify'] = [{'on': 'failure', 'channels':error_list_notify}] 

            #LABELS
            # Product tag      
            yaml_output['labels']['product_p0_tag'] = _derive_label(team)

            # cost team
            if yaml_output['labels'].get('cost_attributed_team'):
                table_dataset = each[0].split(".")
                yaml_output['labels']['cost_attributed_team'] = _derive_cost_team(table_dataset[1])
            else:
                table_dataset = each[0].split(".")
                cost_team_name = _derive_cost_team(table_dataset[1])
                data_append = {'cost_attributed_team': cost_team_name}
                yaml_output['labels'].update(data_append) 
            
            #remove pdg_priority_table_tag
            if yaml_output['labels'].get('pdg_priority_table_tag'):
                del yaml_output['labels']['pdg_priority_table_tag']    
        
            with open(file_dir, 'w') as f:
                yaml.dump(yaml_output,f)
    except Exception as e:
        print(e)

# EDITING
def update_yaml(file_dir,team,critical):
    error_list_notify = _derive_error_channel(team)
    try:
        with open(file_dir) as f:
            yaml_output = yaml.load(f)      
    
            # Remove notify
            if yaml_output["behavior"].get("notify"):            
                original_list = yaml_output['behavior']['notify']
                for index, value in enumerate(original_list):
                    if value.get('on') == 'failure':              
                        try:
                            yaml_output['behavior']['notify'][index]['channels'].remove("slack://#gojek-merchant-care-p0-alert")                            
                        except:
                            pass
                        tmp_list = yaml_output['behavior']['notify'][index]['channels']
                        distinct_list = list(set(tmp_list))
                        if not distinct_list:
                            del yaml_output['behavior']['notify']

            # Remove Product tag 
            if yaml_output['labels'].get('product_p0_tag'):
                del yaml_output['labels']['product_p0_tag']      

            # Remove pdg_priority_table_tag
            if yaml_output['labels'].get('pdg_priority_table_tag'):
                del yaml_output['labels']['pdg_priority_table_tag']                                
            

                    


            # Add Notify
            if critical == 'TRUE':
                # Add notify                
                if yaml_output["behavior"].get("notify"):            
                    original_list = yaml_output['behavior']['notify']
                    for index, value in enumerate(original_list):
                        if value.get('on') == 'failure':              
                            try:
                                yaml_output['behavior']['notify'][index]['channels'].remove("slack://#mp-data-mart-alert")
                            except:
                                pass  
                            tmp_list = yaml_output['behavior']['notify'][index]['channels'] + error_list_notify
                            distinct_list = list(set(tmp_list))
                            yaml_output['behavior']['notify'][index]['channels'] = list(set(tmp_list))
                else:
                    yaml_output['behavior']['notify'] = [{'on': 'failure', 'channels':error_list_notify}] 

                 # Change owner          
                yaml_output['owner'] = _derive_owner(team)  

                # Change retry
                if yaml_output['behavior'].get("retry"):           
                    yaml_output['behavior']['retry']['count'] = 7
                else:
                    yaml_output['behavior']['retry'] = {'count':7}
                
                # Product tag
                yaml_output['labels']['product_p0_tag'] = _derive_label(team)

                # cost team
                if yaml_output['labels'].get('cost_attributed_team'):
                    table_dataset = each[0].split(".")
                    yaml_output['labels']['cost_attributed_team'] = _derive_cost_team(table_dataset[1])
                else:
                    table_dataset = each[0].split(".")
                    cost_team_name = _derive_cost_team(table_dataset[1])
                    data_append = {'cost_attributed_team': cost_team_name}
                    yaml_output['labels'].update(data_append) 
        
            with open(file_dir, 'w') as f:
                yaml.dump(yaml_output,f)
    except Exception as e:
        print(e)


def print_notify_table (file_dir):
    try:    
        with open(file_dir) as f:
            yaml_output = yaml.load(f)  
            if yaml_output["behavior"].get("notify"):
                original_list = yaml_output['behavior']['notify']
                for index, value in enumerate(original_list):
                    if value.get('on') == 'failure':
                        channel_list = yaml_output['behavior']['notify'][index]['channels']
                        for i,value in enumerate (channel_list):
                            try:
                                if yaml_output['behavior']['notify'][index]['channels'][i] == "slack://#gojek-merchant-care-p0-alert":
                                    table =  yaml_output['name']
                                    print(table)
                            except:
                                pass
    except:
        pass

def print_label_table (file_dir):
    try:    
        with open(file_dir) as f:
            yaml_output = yaml.load(f)  
            if yaml_output["labels"].get("product_p0_tag"):
                table =  yaml_output['name']
                print(table)
    except:
        pass

for each in table_list:
    job_dir = each[0].split(".")
    file_dir = '/Users/ferdinand.sanjaya/Documents/p-godata-id/{}/jobs/bigquery/{}/{}/{}/job.yaml'.format(each[1],job_dir[0],job_dir[1],job_dir[2])
    team = 'team_4' #each[2]
    critical = each[2]
    # print("Working on : {}".format(each[0]))
    # update_yaml(file_dir,team,critical)
    # print("Job : {} Done!!".format(each[0]))

    # print_notify_table(file_dir)
    print_label_table(file_dir)
