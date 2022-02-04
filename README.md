# API Key generation

Generates an API key and add that to a usage plan

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
