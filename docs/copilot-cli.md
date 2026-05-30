# GitHub Copilot CLI – Przewodnik

GitHub Copilot CLI to rozszerzenie dla GitHub CLI (`gh`), które pozwala uzyskiwać pomoc AI bezpośrednio w terminalu – do wyjaśniania poleceń shell i generowania nowych poleceń na podstawie opisu w języku naturalnym.

## Instalacja

### 1. Zainstaluj GitHub CLI

```bash
# macOS (Homebrew)
brew install gh

# Ubuntu/Debian
(type -p wget >/dev/null || (sudo apt update && sudo apt-get install wget -y)) \
  && sudo mkdir -p -m 755 /etc/apt/keyrings \
  && wget -qO- https://cli.github.com/packages/githubcli-archive-keyring.gpg \
     | sudo tee /etc/apt/keyrings/githubcli-archive-keyring.gpg > /dev/null \
  && sudo chmod go+r /etc/apt/keyrings/githubcli-archive-keyring.gpg \
  && echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" \
     | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null \
  && sudo apt update \
  && sudo apt install gh -y

# Windows (winget)
winget install --id GitHub.cli
```

### 2. Uwierzytelnij się w GitHub

```bash
gh auth login
```

### 3. Zainstaluj rozszerzenie Copilot

```bash
gh extension install github/gh-copilot
```

## Dostępne polecenia

| Polecenie | Opis |
|---|---|
| `gh copilot explain "<polecenie>"` | Wyjaśnia podane polecenie shell |
| `gh copilot suggest "<opis zadania>"` | Proponuje polecenie na podstawie opisu |

## Polecenie `explain`

Używaj `explain`, gdy natrafisz na nieznane lub skomplikowane polecenie i chcesz zrozumieć, co ono robi.

### Przykłady

```bash
# Wyjaśnienie polecenia find
gh copilot explain "find . -name '*.log' -mtime +7 -delete"

# Wyjaśnienie polecenia awk
gh copilot explain "awk 'NR==2{print}' plik.txt"

# Wyjaśnienie pipeline
gh copilot explain "ps aux | grep nginx | awk '{print $2}' | xargs kill"

# Wyjaśnienie polecenia git
gh copilot explain "git log --oneline --graph --all --decorate"

# Wyjaśnienie polecenia curl
gh copilot explain "curl -X POST -H 'Content-Type: application/json' -d '{\"key\":\"value\"}' https://api.example.com/endpoint"
```

## Polecenie `suggest`

Używaj `suggest`, gdy chcesz wykonać zadanie, ale nie pamiętasz lub nie znasz odpowiedniego polecenia.

### Przykłady

```bash
# Znajdź duże pliki
gh copilot suggest "znajdź 10 największych plików w bieżącym katalogu"

# Operacje na plikach
gh copilot suggest "skompresuj wszystkie pliki .log starsze niż 30 dni"

# Git
gh copilot suggest "pokaż wszystkie commity z ostatniego tygodnia z moim adresem email"

# Procesy
gh copilot suggest "wylistuj wszystkie procesy nasłuchujące na porcie 8080"

# Sieć
gh copilot suggest "sprawdź czy host example.com jest osiągalny i zmierz czas odpowiedzi"

# Docker
gh copilot suggest "usuń wszystkie zatrzymane kontenery i nieużywane obrazy Docker"
```

## Tryby `suggest`

Po uruchomieniu `gh copilot suggest` możesz wybrać typ sugestii:

- **generic** – ogólne polecenie shell (domyślne)
- **git** – polecenie Git
- **gh** – polecenie GitHub CLI

```bash
# Bezpośrednie wskazanie trybu
gh copilot suggest -t git "cofnij ostatni commit bez utraty zmian"
gh copilot suggest -t gh "wylistuj otwarte PR w moim repozytorium"
```

## Aliasy (skróty)

Dla wygody możesz skonfigurować aliasy:

```bash
# Dodaj do ~/.bashrc lub ~/.zshrc
alias '??'='gh copilot suggest -t generic'
alias 'git?'='gh copilot suggest -t git'
alias 'gh?'='gh copilot suggest -t gh'
```

Po ponownym załadowaniu shellu:

```bash
?? "usuń duplikaty linii z pliku tekstowego"
git? "zmień autora ostatniego commitu"
gh? "sklonuj wszystkie repozytoria organizacji"
```

## Wskazówki

1. **Opisuj cel, nie składnię** – zamiast pytać o flagę, opisz co chcesz osiągnąć.
2. **Podawaj kontekst** – np. „używam Ubuntu 22.04" lub „pracuję z plikami CSV".
3. **Iteruj** – jeśli propozycja nie jest idealna, doprecyzuj opis.
4. **Weryfikuj** – zawsze sprawdź sugerowane polecenie przed uruchomieniem z uprawnieniami root lub na produkcji.

## Ćwiczenia

Przejdź do [ćwiczeń Copilot CLI](../exercises/copilot-cli-exercises.md), aby utrwalić wiedzę w praktyce.
