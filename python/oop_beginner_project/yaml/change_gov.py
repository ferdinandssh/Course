# python3 ../change_gov.py


#!/usr/bin/python
# import yaml
import ruamel.yaml
import sys

yaml = ruamel.yaml.YAML()
yaml.width = 4096
yaml.preserve_quotes = True
yaml.boolean_representation = ['False', 'True']
__list = [
    # {'column_1':'description1',
    # 'column_2': 'description2'}
]



def update_yaml(file_dir, __value):
    try:
        with open(file_dir) as f:
            yaml_output = yaml.load(f)   
            yaml_output['description'] = __value
            with open(file_dir, 'w') as f:
                yaml.dump(yaml_output,f)
    except Exception as e:
        print(e)


for key, value in __list[0].items():
    print(f"Working on : {key}")
    job_file_dir = f'/Users/ferdinand.sanjaya/Documents/p-godata-id/gov/columns/{key}.yaml'
    update_yaml(job_file_dir, value)
