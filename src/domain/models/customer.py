import uuid
from datetime import datetime


class Customer:
    def __init__(self, data: dict, _id: str = None):
        self._id = _id if _id else str(uuid.uuid4())
        self._data = data
        self._created_at = datetime.now().isoformat()
        self._updated_at = datetime.now().isoformat()
        self._data.update({'id': self._id})

    @property
    def id(self):
        return self._id

    @property
    def created_at(self):
        return self._created_at

    @property
    def updated_at(self):
        return self._updated_at

    @property
    def get_data(self):
        return self._data
