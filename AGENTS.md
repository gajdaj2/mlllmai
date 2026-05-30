# AGENTS.md — Bookstore Workshop Project

> Ten plik jest automatycznie czytany przez Copilot CLI. Definiuje konwencje projektu.

## Opis projektu

Aplikacja **Bookstore** — sklep z książkami online. Backend (FastAPI) wystawia REST API
do zarządzania katalogiem książek, koszykiem i zamówieniami. Frontend (React) konsumuje to API.
Repo służy jako baza ćwiczeń warsztatu Copilot CLI dla testerów.

## Stack technologiczny

**Backend:**
- Python 3.12+
- FastAPI 0.115+
- Pydantic 2.x
- SQLite (in-memory dla testów)

**Frontend:**
- Node.js 22+
- React 18 + Vite
- TypeScript

**Testy:**
- pytest 8.x + pytest-asyncio + httpx
- pytest-bdd (BDD scenarios)
- Playwright dla Pythona 1.49+
- Locust dla performance
- ruff (linter + formatter)

## Konwencje testów

### Lokalizacja
```
tests/
├── api/              # Testy REST API (httpx)
├── e2e/              # Testy E2E (Playwright)
├── pages/            # Page Objects
├── features/         # BDD feature files + step defs
├── performance/      # Locust
└── conftest.py       # Wspólne fixtures
```

### Nazewnictwo
- Pliki testów: `test_<endpoint_or_feature>.py`
- Klasy testów: `TestEndpointName`
- Funkcje testów: `test_<scenario>_<expected>` (np. `test_create_book_with_valid_data_returns_201`)
- Page Objects: `<Page>Page` w `tests/pages/<page>_page.py`

### Wzorce
- **API tests:** `httpx.AsyncClient`, fixtures w `conftest.py`. Zawsze async (`@pytest.mark.asyncio`).
- **E2E tests:** Playwright Page fixture, Page Object pattern obowiązkowy dla flow'ów >2 kroki.
- **Parametrize** dla podobnych przypadków zamiast osobnych testów.
- **Markers:**
  - `@pytest.mark.smoke` — must-pass przed PR merge.
  - `@pytest.mark.api`, `@pytest.mark.e2e`, `@pytest.mark.performance`.
  - `@pytest.mark.slow` — pomijane w PR check, uruchamiane nightly.

### Locators (Playwright)
- ✅ `page.get_by_role("button", name="Submit")`
- ✅ `page.get_by_test_id("submit-button")` jeśli jest data-testid
- ✅ `page.get_by_label("Email")`
- ❌ CSS selectors (`page.locator(".btn-primary")`)
- ❌ XPath
- ❌ `page.wait_for_timeout()` — używaj `expect()`

### Asercje
- `expect(locator).to_be_visible()` (Playwright — z auto-wait)
- `assert response.status_code == 201` (API)
- Każdy test ma co najmniej 1 znaczącą asercję
- Czytelne komunikaty: `assert ..., "Expected book to be created, got status X"`

### Czego unikać

- `time.sleep()` — w Playwright użyj `expect()`, w API użyj polling przez fixture.
- `print()` — używaj `logging` (`logger = logging.getLogger(__name__)`).
- Hardcoded URLs — `BASE_URL` w fixturze konfiguracyjnej.
- Hardcoded credentials — `pytest-env` lub `.env` (nigdy nie commituj).
- Setup/teardown w każdym teście — fixture z `scope="session"` lub `"function"`.
- Magic numbers — stałe na górze pliku.

## Komendy

```bash
# Uruchomienie API (do testów E2E i API)
cd sample-app/api && uvicorn main:app --reload

# Uruchomienie frontendu
cd sample-app/frontend && npm run dev

# Testy
pytest                           # wszystkie
pytest -m smoke                  # tylko smoke
pytest -m "api and not slow"     # api ale nie slow
pytest tests/e2e/ --headed       # E2E z widoczną przeglądarką
pytest -k "test_create_book"     # pojedynczy test

# Linter
ruff check .
ruff format .

# Performance
locust -f tests/performance/locustfile.py --host http://localhost:8000
```

## Format bug reportów

Wszystkie bug reporty (generowane przez agent `bug-reporter` lub ręcznie) używają formatu:

```markdown
## Tytuł
<krótki opis, max 80 znaków>

## Severity
<Krytyczna / Wysoka / Średnia / Niska>

## Środowisko
- Aplikacja: <wersja>
- Środowisko: <dev / test / staging / prod>
- Przeglądarka: <nazwa + wersja>
- OS: <nazwa + wersja>

## Kroki reprodukcji
1. ...
2. ...

## Oczekiwany rezultat
<co powinno się stać>

## Faktyczny rezultat
<co się stało>

## Załączniki
- <screenshoty, logi>

## Sugerowana przyczyna
<jeśli widać z logów, opcjonalnie>
```

## Customer agents

Repo zawiera 3 custom agenty w `.github/agents/`:

- `bug-reporter.agent.md` — przekształca surowe notatki w bug report.
- `test-writer-python.agent.md` — pisze testy pytest+httpx.
- `test-reviewer.agent.md` — przegląda testy i wskazuje problemy.

## MCP

Konfiguracja w `.copilot/mcp-config.json`:

- **github** (built-in) — issues, PRs, releases.
- **playwright** — sterowanie przeglądarką (eksploracja, generowanie testów E2E).

## Język

- Dokumentacja, komentarze w README/AGENTS.md: **polski**.
- Kod (komentarze, docstrings): **angielski** (standard branżowy).
- Bug reporty, raporty dla biznesu: **polski**.
