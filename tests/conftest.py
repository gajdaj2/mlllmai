"""Wspólne fixtures dla testów.

Konwencje:
- Wszystkie testy API używają fixture `client` (httpx.AsyncClient).
- Token dla zalogowanego użytkownika: fixture `auth_token`.
- Cleanup: każda fixture sprząta po sobie (yield + after).
"""
from __future__ import annotations

import os
from typing import AsyncGenerator

import pytest
import pytest_asyncio
from httpx import AsyncClient

BASE_URL = os.getenv("BOOKSTORE_API_URL", "http://localhost:8000")


@pytest_asyncio.fixture
async def client() -> AsyncGenerator[AsyncClient, None]:
    """Async HTTP client dla testów API."""
    async with AsyncClient(base_url=BASE_URL, timeout=10.0) as ac:
        yield ac


@pytest_asyncio.fixture
async def auth_token(client: AsyncClient) -> str:
    """Token JWT dla testowego użytkownika 'test_editor'."""
    response = await client.post(
        "/auth/login",
        json={"username": "test_editor", "password": "test"},
    )
    assert response.status_code == 200, f"Login failed: {response.text}"
    return response.json()["access_token"]


@pytest_asyncio.fixture
async def auth_headers(auth_token: str) -> dict[str, str]:
    """Headers z poprawnym Authorization."""
    return {"Authorization": f"Bearer {auth_token}"}


@pytest_asyncio.fixture
async def created_book(client: AsyncClient, auth_headers: dict[str, str]) -> dict:
    """Tworzy książkę przed testem i usuwa po."""
    payload = {
        "title": "Test Book",
        "author": "Test Author",
        "isbn": "9788373273450",
        "price": 29.99,
    }
    response = await client.post("/books", json=payload, headers=auth_headers)
    book = response.json()
    yield book
    # Cleanup
    await client.delete(f"/books/{book['id']}", headers=auth_headers)
