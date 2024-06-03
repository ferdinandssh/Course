#!/usr/bin/python

# import yaml
import ruamel.yaml
import sys

yaml = ruamel.yaml.YAML()
yaml.width = 4096
yaml.preserve_quotes = True
yaml.boolean_representation = ['False', 'True']
table_list = [

# P0 [table_name,folder namespace,team name]

 ['table_name','namespace','team_4']

]

def _derive_error_channel(team):
    CHANNEL_MAP = {
        'team_1': ['slack://', 'pagerduty:'],
    }

    return(CHANNEL_MAP.get(team))

def _derive_label(team):
    LABEL_MAP = {
        'team_1': 'team_name',
        'team_2': 'team_name',
        'team_3': 'team_name,
        'team_4': 'team_name'
    }

    return(LABEL_MAP.get(team))

def _derive_owner(team):
    LABEL_MAP = {
        'team_1': 'owner_name',
        'team_2': 'owner_name',
        'team_3': 'owner_name,
        'team_4': 'owner_name'
    }

    return(LABEL_MAP.get(team))

def _derive_cost_team(dataset):
    LABEL_MAP = {
        'dataset': 'cos_team',
    }

    return(LABEL_MAP.get(dataset))

def update_yaml(file_dir,team):
    error_list_notify = _derive_error_channel(team)
    try:
        with open(file_dir) as f:
            yaml_output = yaml.load(f)                         
            yaml_output['owner'] = _derive_owner(team)  
            if yaml_output['behavior'].get("retry"):           
                yaml_output['behavior']['retry']['count'] = 7
            else:
                yaml_output['behavior']['retry'] = {'count':7}
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
            yaml_output['labels']['product_p0_tag'] = _derive_label(team)
            if yaml_output['labels'].get('cost_attributed_team'):
                table_dataset = each[0].split(".")
                yaml_output['labels']['cost_attributed_team'] = _derive_cost_team(table_dataset[1])
            else:
                table_dataset = each[0].split(".")
                cost_team_name = _derive_cost_team(table_dataset[1])
                data_append = {'cost_attributed_team': cost_team_name}
                yaml_output['labels'].update(data_append) 
            if yaml_output['labels'].get('pdg_priority_table_tag'):
                del yaml_output['labels']['pdg_priority_table_tag']            
            with open(file_dir, 'w') as f:
                yaml.dump(yaml_output,f)
    except Exception as e:
        print(e)


for each in table_list:
    job_dir = each[0].split(".")
    file_dir = '/Users/ferdinand.sanjaya/Documents/p-godata-id/{}/jobs/bigquery/{}/{}/{}/job.yaml'.format(each[1],job_dir[0],job_dir[1],job_dir[2])
    team = each[2]
    print("Working on : {}".format(each[0]))
    update_yaml(file_dir,team)
    print("Job : {} Done!!".format(each[0]))