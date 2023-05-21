import re
from typing import NamedTuple
from src.domain.exceptions.email import EmailException


class Email(NamedTuple):
    address: str

    def _validate_address(self) -> str:
        if not re.match(r"[^@]+@[^@]+\.[^@]+", self.address):
            raise EmailException("Endereço de e-mail inválido.")
        return self.address
