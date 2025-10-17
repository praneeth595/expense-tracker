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


@app.get("/")
async def home(request: Request):
    transport = httpx.ASGITransport(app=app)
    async with httpx.AsyncClient(transport=transport, base_url="http://testserver") as client:
        res = await client.get("/api/expenses")
        expenses_list = res.json()

    return templates.TemplateResponse(
        "index.html",
        {"request": request, "expenses": expenses_list}
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
