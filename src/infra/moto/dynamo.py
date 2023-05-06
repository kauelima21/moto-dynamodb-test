import boto3
from botocore.exceptions import ClientError


class DynamoMock:
    def __init__(self, table_name):
        self.table_name = table_name
        self.resource = boto3.resource('dynamodb')
        self.table = self.__create_table()

    def find(self):
        return self.table.scan()['Items']

    def find_by_id(self, _id):
        return self.table.get_item(Key={
            id: _id,
        })['Items']

    def save(self, data):
        try:
            self.table.put_item(Item=data)
        except ClientError:
            return False
        return True

    def __create_table(self):
        return self.resource.create_table(
            TableName=self.table_name,
            KeySchema=[
                {
                    'AttributeName': 'id',
                    'KeyType': 'HASH'
                },
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'id',
                    'AttributeType': 'N'
                },
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 1,
                'WriteCapacityUnits': 1
            }
        )
