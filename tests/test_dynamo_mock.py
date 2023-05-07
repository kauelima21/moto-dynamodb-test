import pytest
from moto import mock_dynamodb
from src.infra.moto.dynamo import DynamoMock
from src.domain.models.customer import Customer


@mock_dynamodb
def test_it_should_create_a_new_record():
    customer_data = {
        'first_name': 'John',
        'last_name': 'Doe',
        'email': 'john@example.com'
    }
    customer = Customer(customer_data)
    table = DynamoMock('customers')
    saved_record = table.save(customer.get_data)
    assert saved_record


@mock_dynamodb
def test_it_should_return_items_from_a_table():
    customer_data = {
        'first_name': 'John',
        'last_name': 'Doe',
        'email': 'john@example.com'
    }
    customer = Customer(customer_data)
    table = DynamoMock('customers')
    table.save(customer.get_data)
    assert table.find() == [customer.get_data]


@mock_dynamodb
def test_it_should_return_an_item_by_id():
    customer_data = {
        'first_name': 'John',
        'last_name': 'Doe',
        'email': 'john@example.com'
    }
    customer = Customer(customer_data)
    table = DynamoMock('customers')
    table.save(customer.get_data)
    assert table.find_by_id(customer.id) == customer.get_data


if __name__ == '__main__':
    pytest.main()
