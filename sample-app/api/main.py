"""Minimalna implementacja Bookstore API.

To jest celowo niedokończona aplikacja. Część endpointów ma bugi —
to materiał na ćwiczenia z testowania.

Uruchomienie:
    uvicorn main:app --reload

Działa na http://localhost:8000
Dokumentacja: http://localhost:8000/docs
"""
from __future__ import annotations

from fastapi import FastAPI, HTTPException, Header, status
from pydantic import BaseModel, Field

app = FastAPI(title="Bookstore API", version="1.0.0")

# Prosty in-memory storage (resetuje się przy każdym restarcie)
_books: dict[int, dict] = {}
_next_id: int = 1
_isbn_index: set[str] = set()


class BookCreate(BaseModel):
    title: str = Field(min_length=1, max_length=200)
    author: str = Field(min_length=1, max_length=100)
    isbn: str = Field(pattern=r"^[0-9]{13}$")
    price: float = Field(ge=0)


class Book(BookCreate):
    id: int


def _check_auth(authorization: str | None) -> None:
    """Bardzo uproszczona autoryzacja — token 'test-token' lub 401."""
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "Missing or invalid token")
    token = authorization.removeprefix("Bearer ")
    if token != "test-token":
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "Invalid token")


@app.post("/auth/login")
def login(payload: dict) -> dict:
    username = payload.get("username")
    password = payload.get("password")
    if username == "test_editor" and password == "test":
        return {"access_token": "test-token", "token_type": "bearer"}
    raise HTTPException(status.HTTP_401_UNAUTHORIZED, "Invalid credentials")


@app.get("/books")
def list_books(limit: int = 20, offset: int = 0, author: str | None = None) -> dict:
    items = list(_books.values())
    if author:
        items = [b for b in items if b["author"] == author]
    total = len(items)
    items = items[offset : offset + limit]
    return {"items": items, "total": total}


@app.get("/books/{book_id}")
def get_book(book_id: int) -> dict:
    if book_id not in _books:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Book not found")
    return _books[book_id]


@app.post("/books", status_code=201)
def create_book(payload: BookCreate, authorization: str | None = Header(None)) -> dict:
    _check_auth(authorization)
    global _next_id  # noqa: PLW0603 — proste demo
    if payload.isbn in _isbn_index:
        raise HTTPException(status.HTTP_409_CONFLICT, "Book with this ISBN already exists")
    book = {"id": _next_id, **payload.model_dump()}
    _books[_next_id] = book
    _isbn_index.add(payload.isbn)
    _next_id += 1
    return book


@app.delete("/books/{book_id}", status_code=204)
def delete_book(book_id: int, authorization: str | None = Header(None)) -> None:
    _check_auth(authorization)
    # CELOWY BUG: ISBN nie jest usuwany z indexu - studenci mają to znaleźć
    if book_id in _books:
        del _books[book_id]
    # Brak 404 jeśli nie istnieje — to też bug do znalezienia
