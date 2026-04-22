"""
Publish a test event to SNS with type=order.
"""
import json
import os

import boto3

LOCALSTACK_URL = os.environ.get("LOCALSTACK_ENDPOINT", "http://localhost:4566")
REGION = "us-east-1"
CONFIG_FILE = "/tmp/poc_config.json"


def publish():
    with open(CONFIG_FILE) as f:
        config = json.load(f)

    sns = boto3.client(
        "sns",
        endpoint_url=LOCALSTACK_URL,
        region_name=REGION,
        aws_access_key_id="test",
        aws_secret_access_key="test",
    )

    response = sns.publish(
        TopicArn=config["topic_arn"],
        Message=json.dumps({"orderId": "ORD-001", "amount": 99.99, "currency": "USD"}),
        Subject="New purchase event",
        MessageAttributes={
            "type": {"DataType": "String", "StringValue": "order"}
        },
    )
    print(f"[publish] Message ID: {response['MessageId']}")
    print("[publish] Sent with MessageAttribute type=order")


if __name__ == "__main__":
    publish()
