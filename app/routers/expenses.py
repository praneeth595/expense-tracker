from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from typing import List
from ..database import engine
from ..models import Expense
from ..schemas import ExpenseCreate, ExpenseRead, SummaryResponse

<<<<<<< HEAD
router = APIRouter(tags=["Expenses"])
=======
router = APIRouter(prefix="/api", tags=["Expenses"])
>>>>>>> ca9671d (Initial commit:Without Optional Enhancements)

def get_session():
    with Session(engine) as session:
        yield session

@router.post("/add_expense", response_model=ExpenseRead)
def add_expense(expense_data: ExpenseCreate, session: Session = Depends(get_session)):
    expense = Expense(**expense_data.model_dump())
    session.add(expense)
    session.commit()
    session.refresh(expense)
    return expense

@router.get("/expenses", response_model=List[ExpenseRead])
def get_expenses(session: Session = Depends(get_session)):
    statement = select(Expense)
    results = session.exec(statement).all()
    return results

@router.get("/summary", response_model=SummaryResponse)
def get_summary(session: Session = Depends(get_session)):
    expenses = session.exec(select(Expense)).all()
    total = sum(e.amount for e in expenses)
    per_category = {}
    for e in expenses:
        per_category[e.category] = per_category.get(e.category, 0) + e.amount
    return {"total": total, "per_category": per_category}


