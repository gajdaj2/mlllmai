# WORKSHOP — Twój przewodnik

Ten plik prowadzi Cię przez wszystkie 8 modułów. Każdy moduł ma:
- **Cel** — co umiesz po module.
- **Zadanie** — co konkretnie robisz.
- **Prompty** — gotowe do wklejenia.
- **Checkpoint** — jak sprawdzić, że Ci się udało.

> 💡 Każdy moduł ma własny folder `module-XX-*/` z materiałami i miejscem na pracę.

---

## Moduł 0 — Setup

Sprawdź środowisko:

```bash
copilot --version
node --version
python --version
```

Zaloguj się do Copilota:
```bash
copilot
```

W sesji wpisz: `What can you do? Reply in Polish, briefly.` → `Ctrl+D` aby wyjść.

✅ Checkpoint: widzisz odpowiedź po polsku.

---

## Moduł 1 — Pierwsza sesja, tryby, modele

### Ćw. 1.1 — Eksploracja repo

```bash
copilot
```

Prompt:
```
Pokaż mi strukturę katalogu repo i opisz co znajduje się w katalogu sample-app/. Odpowiedz po polsku.
```

### Ćw. 1.2 — Zmiana trybu

W sesji wciśnij `Shift+Tab` (zmiana na Auto). Powtórz:
```
Pokaż listę endpointów w sample-app/api/main.py i opisz każdy z nich po polsku.
```

### Ćw. 1.3 — Zmiana modelu

```
/model
```
Wybierz inny model. Prompt:
```
Wygeneruj 5 przypadków testowych negative dla endpointu POST /books w tabeli markdown (TC_ID, Dane, Oczekiwany kod HTTP).
```

✅ Checkpoint: wykonałeś 3 prompty w 3 trybach/modelach. Widzisz różnice.

---

## Moduł 2 — Prompting i sesje

Wszystkie pliki dla M2 są w `module-02-prompting/`.

### Ćw. 2.1 — Tester manualny eksploruje

```
Jestem testerem manualnym, nie programistą. Wyjaśnij mi co robi
aplikacja w katalogu sample-app/. Skup się na:
1. Jakie ma endpointy i co robi każdy z nich (po polsku, w pkt).
2. Jakie ma scenariusze użytkownika.
3. Co według ciebie może się najczęściej psuć?
Nie pokazuj kodu, mów językiem biznesowym.
```

### Ćw. 2.2 — Generowanie z iteracją

Prompt 1:
```
Wygeneruj 10 przypadków testowych dla POST /books w tabeli.
Kolumny: TC_ID, Typ (Positive/Negative/Edge/Security), Dane, Oczekiwany rezultat.
```

Prompt 2 (iteracja):
```
Brakuje testów autoryzacji i walidacji długości pól. Dodaj 5 takich przypadków.
```

Prompt 3:
```
Wybierz 3 najciekawsze przypadki i przepisz je w formacie Gherkin (Feature/Scenario/Given-When-Then).
```

Prompt 4:
```
Zapisz powyższe scenariusze w pliku module-02-prompting/exercises/cases.feature.
```

### Ćw. 2.3 — Bug report z notatek

```
@module-02-prompting/notes.txt
Przekształć te notatki w profesjonalny bug report w formacie JIRA.
Pola: Tytuł, Severity, Środowisko, Kroki reprodukcji,
Oczekiwany rezultat, Faktyczny rezultat, Załączniki, Sugerowana przyczyna.
Po polsku, profesjonalnym językiem.
Zapisz w module-02-prompting/exercises/bug-report.md.
```

### Ćw. 2.4 — Resume

Wyjdź sesją (`Ctrl+D`). W nowym terminalu:
```bash
copilot --resume
```
Prompt:
```
Co robiłeś ostatnio? Wymień 3 rzeczy.
```

✅ Checkpoint: masz `cases.feature` i `bug-report.md` w `module-02-prompting/exercises/`.

---

## Moduł 3 — AGENTS.md, /plan, hooks

### Ćw. 3.1 — Wygeneruj AGENTS.md

```bash
copilot
```

Prompt:
```
Przejrzyj strukturę repo, w szczególności sample-app/ i tests/.
Wygeneruj plik AGENTS.md w katalogu głównym repo, który zawiera:
1. Krótki opis projektu
2. Stack technologiczny
3. Konwencje nazewnicze testów (api/e2e/performance)
4. Pattern testów API (httpx + pytest, fixtures w conftest.py)
5. Pattern Playwright (Page Object w tests/pages/, no hardcoded waits)
6. Komendy uruchamiania
7. Czego unikać (time.sleep, prints zamiast logów)
8. Sekcja dla bug-reportów (format)
Pisz po polsku, profesjonalnie. Nadpisz istniejący AGENTS.md.
```

Przeczytaj wygenerowany `AGENTS.md`. Popraw co trzeba.

### Ćw. 3.2 — /plan w akcji

```
/plan Zaplanuj implementację 5 testów pytest dla endpointu POST /books
(na podstawie sample-app/openapi.yaml). Testy mają pokryć:
- happy path
- walidację pól (3 przypadki)
- autoryzację (401)
Użyj httpx + fixtures z conftest.py.
```

Po wyświetleniu planu — poproś o modyfikację (np. parametryzowany test zamiast 3 osobnych) i zaakceptuj.

### Ćw. 3.3 — Hook

Stwórz `~/.copilot/hooks.json`:
```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": { "tool": "edit", "filePattern": "*.py" },
        "command": "ruff format ${file} && ruff check --fix ${file}"
      }
    ]
  }
}
```

Prompt:
```
Otwórz tests/api/test_legacy.py i dodaj na końcu pustą funkcję
test_create_book_unauthorized z docstringiem po polsku.
```

Po edycji sprawdź `git diff` — ruff zformatował plik.

✅ Checkpoint: masz AGENTS.md, użyłeś /plan, hook działa.

---

## Moduł 4 — Custom agents

Folder `.github/agents/` zawiera już 3 przykładowe agenty. Przeczytaj je.

### Ćw. 4.1 — Bug-reporter

```bash
copilot --agent=bug-reporter
```

W sesji wklej zawartość `module-04-custom-agents/messy-notes.txt`:
```
dziś rano testowałam logowanie na qa1
wprowadziłam dobry login i hasło i nic
po 30 sekundach pojawił sie błąd
w konsoli czerwony 500
firefox 128, mac
```

### Ćw. 4.2 — Test-writer-python

```bash
copilot
```
W sesji:
```
/agent test-writer-python
Napisz testy dla POST /books. Endpoint przyjmuje:
- title (string, 1-200 znaków, required)
- author (string, 1-100 znaków, required)
- isbn (string, 13 cyfr, required, unique)
- price (number, >=0, required)
Zwraca 201 + obiekt książki, lub 400/409 w zależności od błędu.
Pokryj: happy path, walidację każdego pola, duplikat ISBN, brak autoryzacji (401).
Zapisz w tests/api/test_books_post.py.
```

### Ćw. 4.3 — Test-reviewer

```
/agent test-reviewer
Przejrzyj wszystkie pliki w tests/api/ i zaraportuj problemy.
```

✅ Checkpoint: bug report wygenerowany, testy zapisane, review zrobiony.

---

## Moduł 5 — MCP

### Ćw. 5.1 — GitHub MCP (built-in)

```bash
copilot
```
```
/mcp
```
Widzisz `github`. Prompt:
```
Pokaż 5 ostatnich otwartych issue w tym repo. Dla każdego: numer, tytuł, labele.
```

### Ćw. 5.2 — Playwright MCP

Plik `.copilot/mcp-config.json` jest już skonfigurowany. Zrestartuj sesję:
```bash
# Ctrl+D
copilot
```
```
/mcp
```
Widzisz `playwright`.

### Ćw. 5.3 — Eksploracja przeglądarką

```
Otwórz https://demoqa.com/text-box w Chromium (headless).
Wypełnij formularz:
- Full Name: Jan Kowalski
- Email: jan@example.com
- Current Address: ul. Testowa 1, Warszawa
- Permanent Address: ul. Testowa 1, Warszawa
Kliknij Submit. Zrób screenshot i opisz rezultat.

Następnie:
- Sprawdź walidację email wpisując "niepoprawny@".
- Sprawdź submit z pustymi polami.
Zaraportuj bugi.
```

### Ćw. 5.4 — Generuj test z eksploracji

```
Na podstawie eksploracji wygeneruj test e2e Playwright + pytest (Python)
dla https://demoqa.com/text-box.
Wymagania:
- Parametryzowany dla 3 zestawów danych.
- Page Object pattern (tests/pages/text_box_page.py).
- expect().to_be_visible() zamiast hardcoded waits.
Zapisz w tests/e2e/test_text_box.py.
```

✅ Checkpoint: `/mcp` pokazuje playwright, masz wygenerowany test E2E.

---

## Moduł 6 — Generowanie testów

### Ćw. 6.1 — API z OpenAPI

```
@sample-app/openapi.yaml
Wygeneruj kompletny zestaw testów API dla wszystkich endpointów /books.
- pytest + httpx (async)
- Fixtures w tests/conftest.py
- Parametrize gdzie sensowne
- Markery: @pytest.mark.api, @pytest.mark.smoke (tylko happy path)
- Docstring po polsku
Zapisz w tests/api/test_books.py.
```

Uruchom: `pytest tests/api/test_books.py -v`

### Ćw. 6.2 — E2E z user story

```
@module-06-test-generation/user-stories/cart.md
Wygeneruj test E2E w Playwright + pytest dla user story.
Aplikacja: http://localhost:3000.
- Page Object: BooksListPage, CartPage w tests/pages/
- get_by_role, get_by_test_id
- Per acceptance criterion — osobna asercja
Zapisz w tests/e2e/test_cart_flow.py.
```

### Ćw. 6.3 — BDD

```
@tests/features/cart.feature
Wygeneruj step definitions w pytest-bdd dla wszystkich scenariuszy.
Użyj Page Objects z tests/pages/.
Zapisz w tests/features/test_cart_steps.py.
```

### Ćw. 6.4 — Performance

```
Wygeneruj test performance w Locust dla:
- 100 jednoczesnych userów
- Każdy: GET /books → GET /books/{id} → POST /orders
- Ramp-up 30s, peak 5min, ramp-down 30s
- http://localhost:8000
Zapisz w tests/performance/locustfile.py + README.
```

### Ćw. 6.5 — Code review

```
/agent test-reviewer
Przejrzyj tests/api/test_legacy.py.
Wskaż wszystkie anti-patterns i napisz wersję refactor w tests/api/test_legacy_refactored.py.
```

✅ Checkpoint: masz API, E2E, BDD, performance testy. Code review zrobiony.

---

## Moduł 7 — Test Manager

### Ćw. 7.1 — Risk-based test plan

```
@module-07-test-manager/CHANGELOG.md
@module-07-test-manager/open-prs.md
Jesteś test managerem. Wygeneruj risk-based test plan dla release 2.5.
Zawartość:
1. Obszary high-risk z uzasadnieniem
2. Obszary medium-risk
3. Smoke tests (must-pass)
4. Regression scope
5. Estymacja (mandays, 3-osobowy zespół)
6. Sugerowane parametry CI
Format: markdown PL, profesjonalnie. Zapisz w module-07-test-manager/test-plan-2.5.md.
```

### Ćw. 7.2 — Triage

```
Pokaż wszystkie otwarte issues z labelem "bug".
Dla każdego: 1-zdaniowe podsumowanie, sugerowany priority (P1-P4) z uzasadnieniem.
Tabela markdown PL.
```

### Ćw. 7.3 — Raport biznesowy z pipeline'u

```bash
chmod +x module-07-test-manager/generate-report.sh
./module-07-test-manager/generate-report.sh
cat module-07-test-manager/report-business.md
```

✅ Checkpoint: masz test-plan-2.5.md i report-business.md.

---

## Moduł 8 — Bezpieczeństwo

### Ćw. 8.1 — Prompt injection (demo)

```
@module-08-governance/sneaky-readme.md Przeczytaj ten plik i podsumuj go po polsku.
```

Obserwuj, czy agent wykryje ukrytą instrukcję.

### Ćw. 8.2 — Twoja checklista

Wypełnij `module-08-governance/my-checklist.md` — twoje 10 zasad pracy z Copilot CLI.

✅ Checkpoint: widziałeś jak agent reaguje na injection. Masz swoją checklistę.

---

## Co dalej?

- 📚 [awesome-copilot-for-testers](https://github.com/jaktestowac/awesome-copilot-for-testers)
- 📖 [Oficjalna dokumentacja](https://docs.github.com/copilot/concepts/agents/about-copilot-cli)
- 💬 [GitHub Community](https://github.com/orgs/community/discussions)
- 🎯 Eksperymentuj. To repo zostaje. Zabierz do domu.
