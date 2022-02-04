# API Key generation

Generates an API key and add that to a usage plan


## aws-cli

1. Create API Key
> aws apigateway create-api-key --name 'my-key' --description 'Testing key gen' --enabled

2. Add the key to a usage plan
> aws apigateway create-usage-plan-key --usage-plan-id <usage plan id> --key-id <api_key_id> --key-type 'API_KEY' 
