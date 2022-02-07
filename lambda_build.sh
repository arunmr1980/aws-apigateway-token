rm api-key-gen.zip
zip -vrj api-key-gen src/* -i '*.py'
aws lambda update-function-code --function-name api-token-generator --zip-file fileb://api-key-gen.zip
