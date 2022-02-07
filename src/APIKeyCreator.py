import boto3
import os

USAGE_PLAN_ID = os.getenv('USAGE_PLAN_ID')

client = boto3.client('apigateway')

def get_created_API_key_id():
    response = client.create_api_key(
        name='pythonkey-test',
        description='Test API Key creation with bot3',
        enabled=True
    )
    id = response['id']
    print('API key created ...... id ' + id)

    response = client.get_api_key(
        apiKey=id,
        includeValue=True
    )
    print('Get API key ......')
    print(response)
    return id


def create_usage_plan_key(api_key_id):
    print('\n Adding key to usage plan .... ID ' + USAGE_PLAN_ID)
    response = client.create_usage_plan_key(
        usagePlanId=USAGE_PLAN_ID,
        keyId=api_key_id,
        keyType='API_KEY'
    )
    print('Usage plan created ...')
    print(response)



def create_API_key_and_add_to_usage_plan():
    api_key_id = get_created_API_key_id()
    create_usage_plan_key(api_key_id)


create_API_key_and_add_to_usage_plan()
