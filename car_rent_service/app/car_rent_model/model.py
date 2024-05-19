from pydantic import BaseModel
from typing import Optional

class Car(BaseModel):
    id: Optional[int]
    make: str
    model: str
    year: int
    price_per_day: float
