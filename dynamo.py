import boto3
import os

def retrieve_dynamo_secret(key):
    dynamo = boto3.client("dynamodb")

    response = dynamo.get_item(
        TableName=os.environ["DYNAMO_NAME"],
        Key={
            "EntryHash": {
                "S": key
            }
        }
    )

    return response["Item"]["Value"]["S"].encode("utf-8")