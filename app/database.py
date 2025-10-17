from sqlmodel import SQLModel, create_engine

# SQLite Database file (saved locally)
sqlite_url = "sqlite:///./expenses.db"

engine = create_engine(sqlite_url, echo=True)

def init_db():
    SQLModel.metadata.create_all(engine)
