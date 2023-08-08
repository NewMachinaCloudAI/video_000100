import json

def lambda_handler(event, context):
    # TODO implement
    
    print("Hey Hey My My Rock and Roll will Never Die!")
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }