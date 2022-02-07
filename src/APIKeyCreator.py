import boto3
import os


client = boto3.client('apigateway')

def get_created_API_key_id(key_name, description):
    response = client.create_api_key(
        name=key_name,
        description=description,
        enabled=True
    )
    id = response['id']
    print('API key created ...... id ' + id)
    print(response)
    return id


def create_usage_plan_key(api_key_id,usage_plan_id):
    print('\n Adding key to usage plan .... ID ' + USAGE_PLAN_ID)
    response = client.create_usage_plan_key(
        usagePlanId=usage_plan_id,
        keyId=api_key_id,
        keyType='API_KEY'
    )
    print('Usage plan created ...')
    print(response)



def create_API_key_and_add_to_usage_plan(key_name, key_description, usage_plan_id):
    api_key_id = get_created_API_key_id(key_name, key_description)
    create_usage_plan_key(api_key_id, usage_plan_id)
    return api_key_id


create_API_key_and_add_to_usage_plan("test key name", "testing api keys ", "kkwvxa")
