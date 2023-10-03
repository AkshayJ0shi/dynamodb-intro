from boto3 import resource
from boto3.dynamodb.conditions import Attr, Key
from datetime import datetime

demo_table = resource("dynamodb").Table("new-dynamo-db-table")

def insert():
    print("Inserting inti table...")

    response = demo_table.put_item(
        Item = {
            "customer_id" : "123",
            "order_id" : "dsfsandiognef",
            "status" : "pending",
            "created_at" : datetime.now().isoformat()
        }
    )

    print("Insert Response: " + str(response))

def query_using_partition_key(customer_value):
    response = {}

    filtering_expression = Key("customer_id").eq(customer_value)
    response = demo_table.query(KeyConditionExpression = filtering_expression)

    print(response)

query_using_partition_key("123")