import uuid
from datetime import datetime
from typing import Optional
from src.interfaces.models.customer_data import CustomerData


class Customer:
    def __init__(self, data: CustomerData, _id: Optional[str] = None):
        self._id = _id or str(uuid.uuid4())
        self._data = data
        self._created_at = datetime.now().isoformat()
        self._updated_at = datetime.now().isoformat()
        self._data.update(
            {
                'id': self._id,
                'created_at': self._created_at,
                'updated_at': self._updated_at
            }
        )

    @property
    def id(self) -> str:
        return self._id

    @property
    def created_at(self) -> str:
        return self._created_at

    @property
    def updated_at(self) -> str:
        return self._updated_at

    @property
    def get_data(self) -> CustomerData:
        return self._data
