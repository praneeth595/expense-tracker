# 💰 Expense Tracker (FastAPI + SQLModel)

### 🧩 Mini Full-Stack Application

---

## 📘 About the Project

The **Expense Tracker** is a FastAPI-based web app that helps users **record, view, summarize, and export their daily expenses**.

### ✨ Features

* ➕ Add new expenses via form or API
* 📋 View all expenses in a table
* 📊 Generate summaries (total & category-wise)
* 💾 Export data to CSV format
* ✅ API testing with Pytest

---
## References used to build this project
https://www.youtube.com/watch?v=Lu8lXXlstvM&t=5137s
https://ssojet.com/parse-and-generate-formats/parse-and-generate-csv-in-fastapi/
ChatGpt

## 🚀 Steps to Run the Project Locally

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/<your-username>/expense-tracker.git
cd expense-tracker
```

**or**
Download the ZIP file from GitHub → Extract it to any folder .

---

### 2️⃣ Create a Virtual Environment

#### 🪟 On Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

#### 🐧 On macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

### 3️⃣ Install Dependencies

If extracted from ZIP, navigate into the folder first:

```bash
cd expense-tracker-main
```

Then install dependencies:

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Initialize the Database

Open a Python shell:

```bash
python
```

Then run:

```python
from app.database import init_db
init_db()
exit()
```

✅ This creates a local **SQLite database** file named `database.db`.

---

### 5️⃣ Run the FastAPI Server

```bash
uvicorn app.main:app --reload
```

Once started, open in your browser:

* 🌐 **Home Page:** [http://127.0.0.1:8000](http://127.0.0.1:8000)
* ⚙️ **Swagger UI:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

### 6️⃣ Test the Application

To run all automated API tests:

```bash
pytest -v
```

✅ You should see:

```
tests/test_summary.py::test_summary PASSED
============================= 1 passed in 2.3s =============================
```

---

## 🧪 Screenshots – Backend API Testing (Swagger UI)

### ➕ Testing Add Expense API

![testing (2)](https://github.com/user-attachments/assets/83adbbd0-e167-4186-9dde-5d3d42a58a03)

### 📋 Testing GET Expenses API

![getexpenses](https://github.com/user-attachments/assets/769cfa9d-4975-4b47-b170-6401dd95a441)

### 💾 Testing Download CSV API

![test\_export](https://github.com/user-attachments/assets/81db0046-9360-4332-a16a-a73d8f71b62a)

---

## 🖥️ Frontend UI

### 💡 Application Screens

| Screenshot                                                                                                                    | Description                         |
| ----------------------------------------------------------------------------------------------------------------------------- | ----------------------------------- |
| ![Screenshot\_17-10-2025\_224048\_127 0 0 1](https://github.com/user-attachments/assets/2aa3bec4-63a4-4497-b6f8-0772657b8ef6) | Expense Tracker Home Page           |
| ![Screenshot\_17-10-2025\_224041\_127 0 0 1](https://github.com/user-attachments/assets/f63e9637-76e0-4fa5-97c3-74d54b456bb6) | Expense Form and Expense Table View |

---



# 💰 Expense Tracker – Full Technical Description

---

##  Project Architecture Overview


```
Frontend (Jinja2 HTML Templates)
        ↓
FastAPI Routes (main.py)
        ↓
API Router Layer (expenses.py)
        ↓
Database Layer (SQLModel + SQLite)
```


## Project Flow (End-to-End Explanation)

###  1️ User Interaction (Frontend)

**File:** `templates/index.html`
**Role:** Provides the user interface to input and view expenses.

* The user fills the form → amount, category, date, and description.
* The form uses method `POST` → `/add-expense`.
* When the form is submitted, FastAPI receives this data as form request.

After the form is submitted:

* The new expense is added to the database.
* The page reloads and lists all expenses from `/api/expenses`.

The same HTML also:
* Provides a link to view **summary** (`/summary-page`) and **export CSV** (`/api/export`).

---

### 2️⃣ FastAPI Main Application

**File:** `app/main.py`
**Role:** Central entry point of the project.

It performs:

* **App initialization**
* **Router registration**
* **Template rendering**
* **Internal API calls via `httpx`**

---

####  Main Components Inside `main.py`:

 **Home Route (`/`)**

✅ What it does:

* Internally calls `/api/expenses` using httpx (so that frontend remains separate from DB logic).
* Fetches all expenses and passes them to `index.html` for display.

4️ **Summary Page (`/summary-page`)**

✅ What it does:

* Calls `/api/summary`
* Renders a summary table in `summary.html`

---

###  3️ Database Layer

#### **File:** `app/database.py`

**Purpose:** Defines and initializes the database.


###  4️ Data Model Layer

#### **File:** `app/models.py`

**Purpose:** Defines the structure of the `Expense` table in the database.

###  5️ Schema Layer

#### **File:** `app/schemas.py`

**Purpose:** Defines how data is validated and transferred between frontend, backend, and database.

✅ Why schemas are used:

* When you add or fetch data via API, Pydantic validates the format (e.g., ensures `amount` is a float and `date` is valid).

---

### 🔗 6️ API Router Layer

#### **File:** `app/routers/expenses.py`

**Purpose:** Implements all **core backend logic** — adding, viewing, summarizing, filtering, and exporting expenses.

---

####  (1) Add Expense

✅ Handles adding a new expense into the database.

---

####  (2) Get All Expenses

####  (3) Get Summary

✅ Computes:

* Overall total spending
* Category-wise totals (case-insensitive) normalized for all types ex: Food,food,FOOD

---





✅ Streams a CSV file of all  expenses to download.

---

### 7️ Frontend Templates

#### **File:** `templates/index.html`

**Purpose:** Renders form, table, and links for summary/export.

* Displays a form for adding new expenses.
* Lists all existing expenses in a table.
* Includes links for:

  * `View Summary`
  * `Export CSV`


#### **File:** `templates/summary.html`

**Purpose:** Renders summary data.

Displays:

* Total spending
* Category-wise totals (looped via Jinja2)



###  8️ CSS Styling

**File:** `static/style.css`
**Purpose:** Adds minimal styling for form, table, and buttons.



## 🔍 Directory Structure

```
expense-tracker/
│
├── app/
│   ├── main.py                → Entry point for FastAPI app
│   ├── database.py            → Database setup and initialization
│   ├── models.py              → Expense table schema (SQLModel)
│   ├── schemas.py             → Request/response validation (Pydantic)
│   ├── routers/
│   │   └── expenses.py        → All backend API endpoints
│   └── templates/
│       ├── index.html         → Main UI (add + view expenses)
│       └── summary.html       → Summary totals page
│
├── static/
│   └── style.css              → Styling for the UI
│
├── database.db                → SQLite database file (auto-created)
├── requirements.txt           → Dependencies
└── README.md                  → Documentation
```

---



