# API Key generation

Generates an API key and add that to a usage plan

## Setup and deploy in lambda

1. Add a usage plan in AWS API gateway
2. Setup a lambda function in AWS lambda
3. Create zip file and deploy code to lambda using lambda_build.sh
4. Add API gateway permissions to lambda security group
5. Add the following environment variables
- KEY_NAME : Name of the key
- KEY_DESC : Description of API key
- USAGE_PLAN_ID : id of the Usage plan to which the key is to be added
Note: Suggest converting these to request data if integrated to API gateway
6. Test lambda

## Setting up API keys

### API gateway

1. Create the API on API gateway
2. Set Authorizer required as 'true' in all relevant methods

### Usage plans

1. Create a usage plan
2. Configure throttling, burst and quota appropriately
3. Create API Key
4. Add API Key to usage plan

### Client

1. Send API key in a request-header 'x-api-key'


## aws-cli

1. Create API Key
```
> aws apigateway create-api-key --name 'my-key' --description 'Testing key gen' --enabled
```

2. Add the key to a usage plan
```
> aws apigateway create-usage-plan-key --usage-plan-id <usage plan id> --key-id <api_key_id> --key-type 'API_KEY'
```
