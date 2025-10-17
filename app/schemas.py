from pydantic import BaseModel
from datetime import date
from typing import Optional, Dict, List


class ExpenseCreate(BaseModel):
    amount: float
    category: str
    date: date
    description: Optional[str] = None


class ExpenseRead(BaseModel):
    id: int
    amount: float
    category: str
    date: date
    description: Optional[str] = None

    class Config:
        orm_mode = True


class SummaryResponse(BaseModel):
    total: float
    per_category: Dict[str, float]
