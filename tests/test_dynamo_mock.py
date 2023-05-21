import pytest
from moto import mock_dynamodb
from src.domain.value_objects.email import Email
from src.infra.moto.dynamo import DynamoMock
from src.domain.models.customer import Customer
from src.infra.repositories.moto_customer_repository import MotoCustomerRepository
from src.interfaces.models.customer_data import CustomerData


@pytest.fixture()
def customer_data():
    customer_data: CustomerData = {
        'first_name': 'John',
        'last_name': 'Doe',
        'email': Email('john@example.com')
    }
    yield customer_data


@mock_dynamodb
def test_it_should_create_a_new_record(customer_data):
    customer = Customer(customer_data, "")
    table = DynamoMock('customers')
    repo = MotoCustomerRepository(table)
    saved_record = repo.store(customer.get_data)

    assert saved_record


@mock_dynamodb
def test_it_should_return_items_from_a_table(customer_data):
    customer = Customer(customer_data, "")
    table = DynamoMock('customers')
    repo = MotoCustomerRepository(table)
    repo.store(customer.get_data)

    assert table.find()[0]["id"] == customer.id


@mock_dynamodb
def test_it_should_return_an_item_by_id(customer_data):
    customer = Customer(customer_data, "")
    table = DynamoMock('customers')
    repo = MotoCustomerRepository(table)
    repo.store(customer.get_data)

    assert table.find_by_id(customer.id)


if __name__ == '__main__':
    pytest.main()
