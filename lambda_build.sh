rm api-key-gen.zip
zip -vrj api-key-gen src/* -i '*.py'
#zip -u api-key-gen.zip lambda_function.py
#cd packages
#zip -r9 ../fee.zip .
#cd ..
aws lambda update-function-code --function-name api-token-generator --zip-file fileb://api-key-gen.zip
