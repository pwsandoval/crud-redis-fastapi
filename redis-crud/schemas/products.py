from datetime import date
from uuid import uuid4

from pydantic import BaseModel, Field


def generate_id():
    return str(uuid4())


def generate_date():
    return str(date.today())


class Product(BaseModel):
    id: str = Field(default_factory=generate_id)
    name: str
    price: float
    created_at: date = Field(default_factory=generate_date)
