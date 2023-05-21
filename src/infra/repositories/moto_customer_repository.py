from src.domain.repositories.customer_repository import CustomerRepository
from src.infra.moto.dynamo import DynamoMock
from src.interfaces.models.customer_data import CustomerData


class MotoCustomerRepository(CustomerRepository):
    def __init__(self, dynamo_mock: DynamoMock):
        self.dynamo_mock = dynamo_mock

    def get_all(self):
        self.dynamo_mock.find()

    def get_by_id(self, _id: str):
        self.dynamo_mock.find_by_id(_id)

    def store(self, data: CustomerData) -> bool:
        save_customer = self.dynamo_mock.save({
            'id': data["id"],
            'first_name': data["first_name"],
            'last_name': data["last_name"],
            'email': data["email"].address,
            'created_at': data["created_at"],
            'updated_at': data["updated_at"],
        })
        return save_customer
