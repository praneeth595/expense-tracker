from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from .database import init_db
from .routers import expenses
import httpx

app = FastAPI(title="Expense Tracker")

@app.on_event("startup")
def on_startup():
    init_db()

# Static + templates setup
app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

#include Api Router
app.include_router(expenses.router)

#Filtering by Category display
@app.get("/")
async def home(request: Request, category: str | None = None):
    params = {}
    if category:
        params["category"] = category

    transport = httpx.ASGITransport(app=app)
    async with httpx.AsyncClient(transport=transport, base_url="http://testserver") as client:
        res = await client.get("/api/expenses", params=params)
        expenses_list = res.json() if res.status_code == 200 else []

    return templates.TemplateResponse(
        "index.html",
        {"request": request, "expenses": expenses_list, "selected_category": category or ""}
    )




@app.get("/summary-page")
async def summary_page(request: Request):
    transport = httpx.ASGITransport(app=app)
    async with httpx.AsyncClient(transport=transport, base_url="http://testserver") as client:
        res = await client.get("/api/summary")
        summary = res.json()

    return templates.TemplateResponse(
        "summary.html",
        {"request": request, "total": summary["total"], "per_category": summary["per_category"]}
    )
