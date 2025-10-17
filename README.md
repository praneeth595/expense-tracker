# expense-tracker
mini full stack app
💰 Expense Tracker (FastAPI + SQLModel)
📘 About the Project

The Expense Tracker is a FastAPI web app that helps users record, view, summarize, and export their daily expenses.
It includes:

Adding new expenses via form or API

Viewing all expenses in a table

Generating summaries (total & category-wise)

Exporting data to CSV format

API testing with Pytest

🚀 Steps to Run the Project Locally
1️⃣ Clone the Repository
git clone https://github.com/<your-username>/expense-tracker.git
cd expense-tracker

2️⃣ Create a Virtual Environment
On Windows:
python -m venv .venv
.venv\Scripts\activate

On macOS / Linux:
python3 -m venv .venv
source .venv/bin/activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Initialize the Database

Open Python shell:

python


Then run:

from app.database import init_db
init_db()
exit()


✅ This creates a local SQLite database (database.db).

5️⃣ Run the FastAPI Server
uvicorn app.main:app --reload


Once started, open:

🌐 http://127.0.0.1:8000
 — Home Page

⚙️ http://127.0.0.1:8000/docs
 — Swagger UI

6️⃣ Test the Application

To run all API tests:

pytest -v


✅ You should see all test pass successfully.

Screenshots testing backend API's using swagger UI
![testing (2)](https://github.com/user-attachments/assets/83adbbd0-e167-4186-9dde-5d3d42a58a03)

Testing GET expenses  API using swagger
![getexpenses](https://github.com/user-attachments/assets/769cfa9d-4975-4b47-b170-6401dd95a441)

Testing Download CSV  API using swagger
![test_export](https://github.com/user-attachments/assets/81db0046-9360-4332-a16a-a73d8f71b62a)

Frontend Images
![Screenshot_17-10-2025_224048_127 0 0 1](https://github.com/user-attachments/assets/2aa3bec4-63a4-4497-b6f8-0772657b8ef6)
![Screenshot_17-10-2025_224041_127 0 0 1](https://github.com/user-attachments/assets/f63e9637-76e0-4fa5-97c3-74d54b456bb6)



