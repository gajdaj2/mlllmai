"""
UWAGA: Ten plik jest CELOWO zepsuty.
Zawiera anti-patterns które studenci mają znaleźć podczas ćwiczenia 6.5.
NIE używaj tego kodu jako wzorca.
"""

import requests
import time


def test_books():
    r = requests.post("http://localhost:8000/books",
                      json={"title": "Test"})
    time.sleep(2)
    assert r.status_code == 201


def test_books_again():
    r = requests.post("http://localhost:8000/books",
                      json={"title": "Test"})
    time.sleep(2)
    assert r.status_code == 201


def test_get_book():
    r = requests.get("http://localhost:8000/books/1")
    assert r


def test_delete():
    requests.delete("http://localhost:8000/books/1",
                    headers={"Authorization": "Bearer test-token"})
    # No assertion at all


def test_login_flow():
    # Mega długi test robiący 10 rzeczy
    r1 = requests.post("http://localhost:8000/auth/login",
                       json={"username": "test_editor", "password": "test"})
    token = r1.json()["access_token"]
    time.sleep(1)

    r2 = requests.post("http://localhost:8000/books",
                       json={"title": "Book 1", "author": "Author",
                             "isbn": "1234567890123", "price": 10},
                       headers={"Authorization": "Bearer " + token})
    book_id = r2.json()["id"]
    time.sleep(1)

    r3 = requests.get("http://localhost:8000/books/" + str(book_id))
    time.sleep(1)

    r4 = requests.delete("http://localhost:8000/books/" + str(book_id),
                         headers={"Authorization": "Bearer " + token})
    time.sleep(1)

    try:
        assert r1.status_code == 200
        assert r2.status_code == 201
        assert r3.status_code == 200
        assert r4.status_code == 204
    except Exception:
        pass


def test_invalid_title():
    r = requests.post("http://localhost:8000/books",
                      json={"title": "", "author": "X", "isbn": "1234567890123", "price": 10},
                      headers={"Authorization": "Bearer test-token"})
    assert r.status_code == 422


def test_invalid_isbn():
    r = requests.post("http://localhost:8000/books",
                      json={"title": "X", "author": "X", "isbn": "abc", "price": 10},
                      headers={"Authorization": "Bearer test-token"})
    assert r.status_code == 422


def test_invalid_price():
    r = requests.post("http://localhost:8000/books",
                      json={"title": "X", "author": "X", "isbn": "1234567890123", "price": -1},
                      headers={"Authorization": "Bearer test-token"})
    assert r.status_code == 422
