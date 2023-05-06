import pytest
from src.infra.moto.dynamo import DynamoMock
from moto import mock_dynamodb


@mock_dynamodb
def test_it_should_return_items_from_a_table():
    customer = {
        'id': 5,
        'first_name': 'John',
        'last_name': 'Doe',
        'email': 'john@example.com'
    }
    table = DynamoMock('customers')
    table.save(customer)
    assert table.find() == [customer]


if __name__ == '__main__':
    pytest.main()
