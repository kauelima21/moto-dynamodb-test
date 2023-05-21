from abc import ABC, abstractmethod
from src.interfaces.models.customer_data import CustomerData


class CustomerRepository(ABC):
    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def get_by_id(self, _id: str):
        pass

    @abstractmethod
    def store(self, data: CustomerData):
        pass
