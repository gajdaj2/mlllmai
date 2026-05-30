# Copilot CLI dla testerów — warsztaty 8h

> Repo ćwiczeniowe na zajęcia. Otwórz w Codespaces (`Code → Codespaces → Create codespace on main`) — Copilot CLI jest preinstalowany.

## Szybki start

1. Otwórz Codespace. Poczekaj aż się załaduje (~2 min).
2. W terminalu sprawdź instalację:
   ```bash
   copilot --version
   ```
3. Zaloguj się (jeśli pierwszy raz):
   ```bash
   copilot
   ```
   Postępuj zgodnie z device flow.
4. Otwórz [WORKSHOP.md](WORKSHOP.md) — Twój przewodnik krok po kroku.

## Struktura repo

```
.
├── AGENTS.md                    # Konwencje dla Copilota (czytane automatycznie)
├── WORKSHOP.md                  # Przewodnik uczestnika
├── cheatsheet.md                # Najważniejsze komendy
├── .copilot/
│   └── mcp-config.json          # Konfiguracja MCP (Playwright)
├── .github/agents/              # Custom agents (test-writer, bug-reporter, ...)
├── .devcontainer/               # Codespaces config
├── sample-app/                  # Aplikacja testowa (Bookstore API + UI)
│   ├── api/                     # FastAPI backend
│   ├── frontend/                # React frontend
│   └── openapi.yaml             # API spec
├── tests/                       # Miejsce na Wasze testy
│   ├── api/
│   ├── e2e/
│   ├── pages/                   # Page Objects (Playwright)
│   ├── features/                # BDD scenariusze
│   └── performance/             # Locust
├── module-01-warmup/            # Ćwiczenia M1
├── module-02-prompting/         # Ćwiczenia M2 (+ materiały do ćwiczeń)
├── module-03-agents-md/         # Ćwiczenia M3
├── module-04-custom-agents/     # Ćwiczenia M4
├── module-05-mcp/               # Ćwiczenia M5
├── module-06-test-generation/   # Ćwiczenia M6
├── module-07-test-manager/      # Ćwiczenia M7
└── module-08-governance/        # Ćwiczenia M8
```

## Zasady

- **Codespaces, nie lokalnie** — wszystko jest preinstalowane.
- **Pracujcie parami** w razie problemu z dostępem do Copilota.
- **Eksperymentujcie** — to repo jest sandboxem. Zepsuć nie da się go trwale.
- **Zadawajcie pytania** — głupich pytań nie ma.

## Wymagania (jeśli ktoś chce lokalnie)

- Node.js 22+
- Python 3.12+
- Konto GitHub z aktywnym planem Copilot (Free wystarcza)
- `npm install -g @github/copilot`
