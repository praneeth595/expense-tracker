from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from typing import List
from ..database import engine
from ..models import Expense
from ..schemas import ExpenseCreate, ExpenseRead, SummaryResponse
from fastapi.responses import StreamingResponse
import csv
import io

router = APIRouter(prefix="/api", tags=["Expenses"])

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
        #capitalizing all the category so {Food | food | FOod} will belongs to same category
        normalized_category = e.category.strip().capitalize()
        per_category[normalized_category] = per_category.get(normalized_category, 0) + e.amount
    return {"total": total, "per_category": per_category}



@router.get("/export")
def export_expenses(session: Session = Depends(get_session)):
    expenses = session.exec(select(Expense)).all()
    output=io.StringIO()
    fieldnames=["ID", "Amount", "Category", "Date", "Description"]
    writer=csv.DictWriter(output,fieldnames=fieldnames)
    writer.writeheader()
    for e in expenses:
        writer.writerow({"ID":e.id, "Amount":e.amount, "Category":e.category, "Date":e.date, "Description":e.description})
    output.seek(0)
    return StreamingResponse(iter([output.getvalue()]),media_type="text/csv")