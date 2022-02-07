import json
import os

import APIKeyCreator as api_key_creator

USAGE_PLAN_ID = os.getenv('USAGE_PLAN_ID')
KEY_NAME = os.getenv('KEY_NAME')
KEY_DESC = os.getenv('KEY_DESC')

def lambda_handler(event, context):
    key_name = KEY_NAME
    key_description = KEY_DESC
    usage_plan_id = USAGE_PLAN_ID
    api_key_id = api_key_creator.create_API_key_and_add_to_usage_plan(key_name, key_description, usage_plan_id)
    return {
        'statusCode': 200,
        'body': json.dumps({'api_key_id':api_key_id})
    }
