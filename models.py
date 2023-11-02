from pydantic import BaseModel

class Order(BaseModel):
    ID: int
    Price: float
    Tax: float
