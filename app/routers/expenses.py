from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from typing import List
from ..database import engine
from ..models import Expense
from ..schemas import ExpenseCreate, ExpenseRead, SummaryResponse

# Initialize Router
router = APIRouter(tags=["Expenses"])

# Dependency — provide DB session for each request
def get_session():
    with Session(engine) as session:
        yield session


# 🟢 1️⃣ Add a new expense
@router.post("/add_expense", response_model=ExpenseRead)
def add_expense(expense_data: ExpenseCreate, session: Session = Depends(get_session)):
    """
    Create and save a new expense record in the database.
    """
    expense = Expense(**expense_data.model_dump())  # convert Pydantic model → dict
    session.add(expense)
    session.commit()
    session.refresh(expense)
    return expense


# 🟣 2️⃣ Get all expenses
@router.get("/expenses", response_model=List[ExpenseRead])
def get_expenses(session: Session = Depends(get_session)):
    """
    Retrieve all expenses stored in the database.
    """
    statement = select(Expense)
    results = session.exec(statement).all()
    return results


# 🟡 3️⃣ Get total & category-wise summary
@router.get("/summary", response_model=SummaryResponse)
def get_summary(session: Session = Depends(get_session)):
    """
    Return total spend and category-wise summary of all expenses.
    """
    expenses = session.exec(select(Expense)).all()
    total = sum(e.amount for e in expenses)
    per_category = {}

    for e in expenses:
        per_category[e.category] = per_category.get(e.category, 0) + e.amount

    return {"total": total, "per_category": per_category}
