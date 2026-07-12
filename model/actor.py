from dataclasses import dataclass
from datetime import date

@dataclass
class Actor:
    id: str
    name: str
    date_of_birth: date

    def __hash__(self):
        return hash(self.id)

    def __str__(self):
        return f'{self.name}'

