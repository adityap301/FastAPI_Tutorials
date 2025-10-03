from pydantic import BaseModel
from pydantic import field_validator, ValidationError

class Product(BaseModel):
    id: str | None = None
    name: str
    description: str
    price: float
    quantity: int

    @field_validator('description', mode='after')    
    @classmethod
    def is_valid_len(cls, desc: str) -> str:
        if len(desc) < 5:
            raise ValueError("Description should be at least 5 charaters long")
        return desc
