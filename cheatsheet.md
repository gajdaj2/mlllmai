# Copilot CLI — cheatsheet

## Uruchomienie

| Komenda | Opis |
|---|---|
| `copilot` | Sesja interaktywna |
| `copilot --resume` | Wznów ostatnią sesję |
| `copilot -p "prompt"` | Tryb programatyczny (CI) |
| `copilot --agent=NAME` | Konkretny custom agent |
| `copilot --model=MODEL` | Konkretny model |
| `copilot --experimental` | Tryby eksperymentalne |
| `copilot --allow-all-tools` | Bez pytania o zgodę (OSTROŻNIE!) |

## Slash commands w sesji

| Komenda | Opis |
|---|---|
| `/help` | Lista komend |
| `/model` | Zmiana modelu |
| `/agent NAME` | Wywołanie custom agenta |
| `/plan PROMPT` | Zaplanuj zadanie |
| `/research PROMPT` | Głębsze badanie (subagent Research) |
| `/mcp` | Lista MCP serwerów |
| `/clear` | Wyczyść kontekst |
| `/resume` | Wznów sesję |
| `/exit` | Wyjście |
| `/changelog` | Co nowego |
| `/feedback` | Zgłoś feedback |
| `/experimental` | Features w preview |
| `/delegate TASK` | Odlot do Copilot coding agent (cloud) |
| `/fleet` | Orchestracja subagentów (experimental) |

## Skróty klawiszowe

| Klawisz | Akcja |
|---|---|
| `Shift+Tab` | Cykl trybów: Approval → Auto → Autopilot |
| `Ctrl+C` | Przerwij bieżącą akcję |
| `Ctrl+D` | Wyjście z sesji |
| `Tab` | Autocomplete (np. `@plik.py`) |

## Tryby pracy

| Tryb | Kiedy używać |
|---|---|
| **Approval** (default) | Nowe/nieznane repo, prod-code, pierwszy raz |
| **Auto** | Sandbox, znane zadania, eksperymenty |
| **Autopilot** | Długie zadania (refactor, big features), gdy zostawiasz agenta |

## Zmienne kontekstowe w prompcie

```
@plik.py                    # Dołącz plik
@katalog/                   # Dołącz katalog (zalecane oszczędnie)
```

## Hierarchia konfiguracji

```
~/.copilot/AGENTS.md              # User-level konwencje
~/.copilot/agents/*.agent.md      # User-level custom agents
~/.copilot/mcp-config.json        # User-level MCP
~/.copilot/hooks.json             # User-level hooks

<repo>/AGENTS.md                  # Repo-level konwencje
<repo>/.github/agents/*.agent.md  # Repo-level custom agents  
<repo>/.copilot/mcp-config.json   # Repo-level MCP
```

> Repo nadpisuje User. Custom agent może mieć własną konfigurację MCP.

## Modele (premium requests)

| Model | Premium | Notatki |
|---|---|---|
| Claude Sonnet 4.5 | ✅ | Default, najlepszy balans |
| GPT-5 | ✅ | Alternatywa, dobry w długim kontekście |
| GPT-5 mini | ❌ | Za darmo, dobry dla prostych zadań |
| GPT-4.1 | ❌ | Za darmo, fallback |

## Anti-patterns (NIE rób tego)

❌ `time.sleep()` w testach Playwright  
❌ `--allow-all-tools` w produkcji  
❌ Wpychanie sekretów do prompta  
❌ Akceptowanie kodu bez uruchomienia  
❌ Bez AGENTS.md w projekcie  
❌ Custom agents w `/tmp/` (zgubisz)  
❌ Generowanie 50 testów jednym promptem (iteruj!)  
❌ Ignorowanie pytań o zgodę w Approval  

## Quick prompts dla testera

**Generowanie:**
```
Wygeneruj N przypadków testowych dla <endpoint/feature> w tabeli markdown.
Kolumny: TC_ID, Typ, Dane, Oczekiwany rezultat.
```

**Bug report:**
```
@notes.txt
Przekształć w bug report JIRA: tytuł, severity, środowisko, kroki,
expected/actual, sugerowana przyczyna. PL.
```

**Code review:**
```
/agent test-reviewer
Przejrzyj <plik> i wypisz anti-patterns.
```

**Test plan:**
```
@CHANGELOG.md
Risk-based test plan: high/medium-risk, smoke, regression scope,
estymacja w mandays dla zespołu 3-osobowego. PL.
```
