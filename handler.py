import json

def get(event, context):

    response = {
        "statusCode": 200,
        "body": "Funcionou trocado!"
    }

    return response

def post(event, context):

    response = {
        "statusCode": 200,
        "body": json.dumps(event.get("body"))
    }

    return response
