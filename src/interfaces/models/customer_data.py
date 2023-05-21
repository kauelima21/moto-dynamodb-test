from typing import TypedDict, Optional
from src.domain.value_objects.cpf import Cpf
from src.domain.value_objects.email import Email


class CustomerData(TypedDict, total=False):
    id: Optional[str]
    first_name: str
    last_name: str
    email: Email
    created_at: str
    updated_at: str
    # cpf: Cpf
