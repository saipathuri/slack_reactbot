from __future__ import print_function
import json
import boto3

def get_group(event):
    body = event['body']
    print(body)
    params = body.split("&")
    ch_id = params[3]
    tokens = ch_id.split("=")
    return tokens[1]

def get_count(event):
    body = event['body']
    print(body)
    params = body.split("&")
    count_whole = params[-3]
    if count_whole[0:4] == 'text':
        text = count_whole.split("=")[1]
        if text != "" and text.isdigit():
            return int(text)
        else:
            return 10
    else:
        return 10

# Creates a response that complies with API Gateway Lambda Proxy Integration
def make_response(body, status_code, headers={'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*'}):
    response = dict()
    response['headers'] = headers
    response['statusCode'] = status_code
    response['body'] = json.dumps(body)
    response['isBase64Encoded'] = False

    return response

def lambda_handler(event, context):
    print("Received event: " + json.dumps(event, indent=2))
    group = get_group(event)
    count = get_count(event)
    data = {"group":group, "count": count}
    payload = json.dumps(data)
    print(payload)
    client = boto3.client('lambda')
    r = client.invoke(
        FunctionName="slackReactReceiver",
        InvocationType="Event",
        Payload=payload)
    print(r)
    return make_response("Done", 200)
