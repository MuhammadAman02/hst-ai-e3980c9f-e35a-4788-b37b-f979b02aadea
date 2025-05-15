from pydantic import BaseModel, Field
from datetime import datetime

class Transaction(BaseModel):
    amount: float = Field(..., gt=0)
    merchant: str
    timestamp: datetime = Field(default_factory=datetime.now)
    card_number: str = Field(..., min_length=13, max_length=19)