import os
import boto3
import json

username = 'temp3'
password = 'Test@1234'

def lambda_handler(event, context):
    username = 'test'
    password = 'test'
    
    client = boto3.client('cognito-idp', region_name="eu-west-2")
    response = client.initiate_auth(
        ClientId="clientid",
        AuthFlow='USER_PASSWORD_AUTH',
        AuthParameters={
            'USERNAME': username,
            'PASSWORD': password
        }
    )

    print(response)
    
    print('AccessToken', response['AuthenticationResult']['IdToken'])
    print('RefreshToken', response['AuthenticationResult']['RefreshToken'])
    
    access_token = response['AuthenticationResult']['AccessToken']
    id_token=response['AuthenticationResult']['IdToken']
    client = boto3.client('cognito-idp', region_name='eu-west-2')
    response = client.get_user(
        AccessToken=access_token
    )
    
    attr_sub = None
    for attr in response['UserAttributes']:
        if attr['Name'] == 'sub':
            attr_sub = attr['Value']
            break
    
    print('UserSub', attr_sub)

    return {
        'statusCode': 200,
        'body': response
    }
