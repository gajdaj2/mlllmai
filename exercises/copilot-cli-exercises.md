# Ćwiczenia: GitHub Copilot CLI

Poniższe ćwiczenia pomogą Ci opanować pracę z GitHub Copilot CLI w praktyce.
Każde ćwiczenie zawiera cel, zadanie i wskazówkę.

> **Wymagania:** zainstalowany `gh` i rozszerzenie `gh copilot`.
> Szczegóły instalacji znajdziesz w [przewodniku Copilot CLI](../docs/copilot-cli.md).

---

## Poziom 1 – Podstawowy

### Ćwiczenie 1.1 – Wyjaśnianie poleceń `find`

**Cel:** Nauczyć się korzystać z `gh copilot explain`.

**Zadanie:**
Poproś Copilot o wyjaśnienie każdego z poniższych poleceń:

```bash
gh copilot explain "find /var/log -name '*.log' -size +10M -mtime +30"
gh copilot explain "find . -type f -not -path './.git/*' | wc -l"
```

**Pytania do refleksji:**
- Co robi każda z flag?
- W jakich sytuacjach użyłbyś/użyłabyś tych poleceń?

---

### Ćwiczenie 1.2 – Sugerowanie poleceń shell

**Cel:** Nauczyć się korzystać z `gh copilot suggest`.

**Zadanie:**
Użyj `gh copilot suggest`, aby uzyskać polecenia dla poniższych zadań:

1. „Wylistuj wszystkie pliki w bieżącym katalogu posortowane według rozmiaru, od największego"
2. „Pokaż 20 ostatnich linii pliku app.log i odświeżaj je na bieżąco"
3. „Sprawdź, który proces używa portu 3000"

**Oczekiwane polecenia (sprawdź, czy Copilot zaproponował podobne):**

```bash
# 1
ls -lSh

# 2
tail -f -n 20 app.log

# 3
lsof -i :3000
# lub
ss -tlnp | grep 3000
```

---

### Ćwiczenie 1.3 – Polecenia Git

**Cel:** Korzystać z `gh copilot suggest -t git`.

**Zadanie:**
Użyj trybu `git`, aby uzyskać polecenia dla:

1. „Pokaż różnicę między bieżącą gałęzią a main"
2. „Cofnij ostatni commit, zachowując zmiany w staging area"
3. „Znajdź commit, który wprowadził tekst 'TODO: fixme'"

---

## Poziom 2 – Średniozaawansowany

### Ćwiczenie 2.1 – Wyjaśnianie złożonych potoków

**Cel:** Rozumieć złożone polecenia z użyciem potoków.

**Zadanie:**
Wyjaśnij następujące polecenia i opisz własnymi słowami, co każde z nich robi:

```bash
gh copilot explain "cat /etc/passwd | awk -F: '{print $1, $3}' | sort -k2 -n | head -5"

gh copilot explain "du -ah . | sort -rh | head -20"

gh copilot explain "ss -tunap | grep ESTABLISHED | awk '{print $5}' | cut -d: -f1 | sort | uniq -c | sort -rn"
```

---

### Ćwiczenie 2.2 – Tworzenie aliasów

**Cel:** Skonfigurować aliasy dla często używanych operacji Copilot CLI.

**Zadanie:**
Dodaj do swojego pliku `~/.bashrc` lub `~/.zshrc` aliasy:

```bash
alias '??'='gh copilot suggest -t generic'
alias 'git?'='gh copilot suggest -t git'
alias 'gh?'='gh copilot suggest -t gh'
```

Następnie przetestuj je:

```bash
?? "znajdź pliki większe niż 1 GB"
git? "pokaż historię konkretnego pliku"
gh? "pobierz listę moich repozytoriów"
```

---

### Ćwiczenie 2.3 – Automatyzacja zadań DevOps

**Cel:** Używać Copilot CLI do zadań administracyjnych.

**Zadanie:**
Użyj `gh copilot suggest`, aby uzyskać polecenia do:

1. „Zrób backup katalogu /home/user/projekty do pliku tar.gz z datą w nazwie"
2. „Sprawdź dostępność miejsca na dysku i wyślij alert jeśli zajęte jest więcej niż 80%"
3. „Wylistuj wszystkie uruchomione kontenery Docker z ich adresami IP"

---

## Poziom 3 – Zaawansowany

### Ćwiczenie 3.1 – Skrypt powłoki z pomocą Copilot

**Cel:** Zbudować kompletny skrypt z pomocą Copilot CLI.

**Zadanie:**
Korzystając wyłącznie z `gh copilot suggest`, zbuduj skrypt, który:
1. Sprawdza, czy katalog podany jako argument istnieje
2. Liczy pliki według rozszerzenia
3. Wypisuje podsumowanie w czytelnym formacie

**Wskazówka:**
Buduj skrypt iteracyjnie – pytaj o jeden element na raz:
- „sprawdź czy katalog podany jako $1 istnieje"
- „policz pliki według rozszerzenia w katalogu"
- itd.

---

### Ćwiczenie 3.2 – GitHub CLI z Copilot

**Cel:** Automatyzować operacje na repozytoriach GitHub.

**Zadanie:**
Użyj `gh copilot suggest -t gh`, aby wykonać:

1. „Wylistuj wszystkie otwarte Issues w bieżącym repozytorium z etykietą 'bug'"
2. „Utwórz nowy branch, przesuń na niego zmiany i otwórz Pull Request"
3. „Pobierz statystyki gwiazdek dla mojego repozytorium"

---

## Samoocena

Po wykonaniu ćwiczeń odpowiedz na pytania:

- [ ] Potrafię wyjaśnić dowolne polecenie shell używając Copilot CLI
- [ ] Potrafię sugerować polecenia dla zadań opisanych w języku naturalnym
- [ ] Potrafię wybrać odpowiedni tryb sugestii (generic / git / gh)
- [ ] Skonfigurowałem/am aliasy dla wygodniejszej pracy
- [ ] Potrafię ocenić poprawność zaproponowanego polecenia przed jego uruchomieniem
