from fastapi import FastAPI, Request, Depends, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from sqlmodel import Session, select
from .database import init_db, engine
from .models import Expense
from .routers import expenses
from fastapi.staticfiles import StaticFiles
app = FastAPI(title="Expense Tracker")



# Serve static files (CSS, JS, images)
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Initialize Jinja2 templates
templates = Jinja2Templates(directory="app/templates")

@app.on_event("startup")
def on_startup():
    init_db()

# Include API routes
app.include_router(expenses.router)


# 🟢 Home Page – Form + Table
@app.get("/")
def home(request: Request, session: Session = Depends(lambda: Session(engine))):
    expenses = session.exec(select(Expense)).all()
    return templates.TemplateResponse("index.html", {"request": request, "expenses": expenses})


# 🟣 Handle Form Submission
@app.post("/add-expense")
def add_expense_form(
    request: Request,
    amount: float = Form(...),
    category: str = Form(...),
    date: str = Form(...),
    description: str = Form(""),
    session: Session = Depends(lambda: Session(engine))
):
    expense = Expense(amount=amount, category=category, date=date, description=description)
    session.add(expense)
    session.commit()
    return RedirectResponse("/", status_code=303)


# 🟡 Summary Page
@app.get("/summary-page")
def summary_page(request: Request, session: Session = Depends(lambda: Session(engine))):
    expenses = session.exec(select(Expense)).all()
    total = sum(e.amount for e in expenses)
    per_category = {}
    for e in expenses:
        per_category[e.category] = per_category.get(e.category, 0) + e.amount

    return templates.TemplateResponse("summary.html", {
        "request": request,
        "total": total,
        "per_category": per_category
    })
