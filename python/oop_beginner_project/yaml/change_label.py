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
