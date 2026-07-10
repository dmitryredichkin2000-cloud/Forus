from fastapi import FastAPI

from app.api import books, categories
from app.db.models import create_tables

create_tables()

app = FastAPI(
    title="Forus Books API",
    description="API для работы с книгами и категориями",
    version="1.0.0"
)

@app.get("/")
def root():
    return {
        "message": "Forus Books API работает",
        "docs": "/docs",
        "health": "/health"
    }

@app.get("/health")
def health_check():
    return {
        "status": "ok"
    }

app.include_router(categories.router)
app.include_router(books.router)