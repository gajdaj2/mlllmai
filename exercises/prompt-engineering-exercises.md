# Ćwiczenia: Prompt Engineering

Poniższe ćwiczenia pozwolą Ci praktycznie zastosować techniki Prompt Engineering.
Pracuj z dowolnym modelem językowym (np. GitHub Copilot Chat, ChatGPT, Claude).

> Przed wykonaniem ćwiczeń zapoznaj się z [przewodnikiem Prompt Engineering](../docs/prompt-engineering.md).

---

## Poziom 1 – Podstawowy

### Ćwiczenie 1.1 – Porównanie promptów ogólnych i szczegółowych

**Cel:** Zobaczyć, jak precyzyjność promptu wpływa na jakość odpowiedzi.

**Zadanie:**
Wyślij do modelu kolejno oba prompty i porównaj odpowiedzi:

**Prompt A (ogólny):**
```
Napisz mi coś o bazach danych.
```

**Prompt B (szczegółowy):**
```
Napisz zwięzłe porównanie baz danych SQL i NoSQL (maks. 200 słów).
Uwzględnij: model danych, przypadki użycia, przykłady popularnych systemów.
Skieruj tekst do programisty z 1 rokiem doświadczenia.
```

**Pytania do refleksji:**
- Która odpowiedź jest bardziej użyteczna?
- Jakie elementy Promptu B sprawiły, że wynik był lepszy?

---

### Ćwiczenie 1.2 – Role Prompting

**Cel:** Nauczyć się, jak rola wpływa na odpowiedź modelu.

**Zadanie:**
Wyślij to samo pytanie z trzema różnymi rolami i porównaj odpowiedzi:

**Pytanie bazowe:** „Jak zacząć naukę programowania?"

**Wersja 1:**
```
Jak zacząć naukę programowania?
```

**Wersja 2:**
```
Jesteś doświadczonym mentorem programowania z 10-letnim stażem w nauczaniu
początkujących. Jak zacząć naukę programowania? Odpowiedz osobie, która
nigdy wcześniej nie pisała kodu.
```

**Wersja 3:**
```
Jesteś CTO startupu technologicznego. Jak zacząć naukę programowania?
Odpowiedz osobie, która chce jak najszybciej zdobyć pracę jako junior developer.
```

**Pytania do refleksji:**
- Jak różnią się odpowiedzi?
- Kiedy rola jest szczególnie ważna?

---

### Ćwiczenie 1.3 – Formatowanie wyjścia

**Cel:** Kontrolować format odpowiedzi modelu.

**Zadanie:**
Poproś model o tę samą informację w różnych formatach:

```
Podaj 5 najważniejszych zasad pisania czystego kodu.
Format: lista punktowana
```

```
Podaj 5 najważniejszych zasad pisania czystego kodu.
Format: tabela z kolumnami: Zasada | Opis (1 zdanie) | Przykład naruszenia
```

```
Podaj 5 najważniejszych zasad pisania czystego kodu.
Format: JSON, gdzie każdy element ma pola: "nazwa", "opis", "przykład"
```

---

## Poziom 2 – Średniozaawansowany

### Ćwiczenie 2.1 – Few-shot Prompting

**Cel:** Nauczyć model wzorca przez przykłady.

**Zadanie:**
Użyj poniższego promptu few-shot do klasyfikacji komunikatów błędów:

```
Klasyfikuj komunikat błędu jako jeden z typów: SIECIOWY, BAZODANOWY, AUTORYZACJA, LOGIKA_BIZNESOWA, NIEZNANY.

Wejście: "Connection refused to host 192.168.1.1:5432"
Typ: SIECIOWY

Wejście: "duplicate key value violates unique constraint 'users_email_key'"
Typ: BAZODANOWY

Wejście: "JWT token has expired"
Typ: AUTORYZACJA

Wejście: "Order total cannot be negative"
Typ: LOGIKA_BIZNESOWA

Wejście: "Cannot read properties of undefined (reading 'map')"
Typ:
```

**Zadanie rozszerzone:**
Dodaj 2 własne przykłady i poproś model o klasyfikację 5 nowych komunikatów błędów.

---

### Ćwiczenie 2.2 – Chain-of-Thought

**Cel:** Poprawić jakość rozumowania przez instrukcję krok-po-kroku.

**Zadanie:**
Porównaj odpowiedzi na oba prompty:

**Prompt bez CoT:**
```
Projekt ma 3 mikrousługi. Każda przetwarza 1000 żądań/sekundę. Baza danych
obsługuje maks. 500 połączeń. Każda usługa utrzymuje pulę 5 połączeń.
Czy system zadziała poprawnie przy pełnym obciążeniu?
```

**Prompt z CoT:**
```
Projekt ma 3 mikrousługi. Każda przetwarza 1000 żądań/sekundę. Baza danych
obsługuje maks. 500 połączeń. Każda usługa utrzymuje pulę 5 połączeń.
Czy system zadziała poprawnie przy pełnym obciążeniu?

Rozwiąż krok po kroku:
1. Oblicz łączną liczbę połączeń do bazy danych
2. Porównaj z limitem bazy danych
3. Wyciągnij wniosek i zaproponuj rozwiązanie jeśli potrzebne
```

---

### Ćwiczenie 2.3 – Iteracyjne doskonalenie promptu

**Cel:** Rozwinąć umiejętność iteracyjnego ulepszania promptów.

**Zadanie:**
Zacznij od ogólnego promptu i iteracyjnie go udoskonalaj w 3 krokach:

**Wersja 1:**
```
Napisz funkcję w Pythonie do walidacji danych.
```

**Wersja 2** (po przejrzeniu V1, doprecyzuj):
```
Napisz funkcję Python 3.11 walidującą dane użytkownika z formularza rejestracji.
Waliduj: imię (2-50 znaków), email (format RFC 5321), hasło (min. 8 znaków, cyfra, wielka litera).
```

**Wersja 3** (po przejrzeniu V2, doprecyzuj dalej):
```
Jesteś doświadczonym programistą Python.
Napisz funkcję Python 3.11 walidującą dane użytkownika z formularza rejestracji.
Waliduj: imię (2-50 znaków, tylko litery i spacje), email (format RFC 5321), hasło (min. 8 znaków, cyfra, wielka litera).
Wymagania:
- Type hints
- Docstring (Google style)
- Zwróć słownik: {"pole": "komunikat błędu"} lub pusty słownik jeśli dane poprawne
- Nie używaj zewnętrznych bibliotek
- Dodaj testy jednostkowe używając pytest
```

**Pytania do refleksji:**
- Jak zmieniał się wynik z każdą iteracją?
- Które elementy promptu miały największy wpływ?

---

## Poziom 3 – Zaawansowany

### Ćwiczenie 3.1 – Projektowanie systemu z AI

**Cel:** Użyć AI jako asystenta w architekturze oprogramowania.

**Zadanie:**
Użyj poniższego promptu i przejdź przez pełny proces projektowania:

```
Jesteś architektem rozwiązań z 10-letnim doświadczeniem w systemach rozproszonych.

Kontekst: Startup e-commerce chce zbudować platformę obsługującą:
- 10 000 aktywnych użytkowników jednocześnie
- Katalog 500 000 produktów
- Przetwarzanie 100 zamówień na minutę w szczycie

Zadanie: Zaproponuj architekturę systemu.
Uwzględnij: bazy danych, cache, kolejki wiadomości, API gateway.

Format odpowiedzi:
1. Diagram architektury (tekstowy)
2. Uzasadnienie wyboru każdej technologii
3. Potencjalne wąskie gardła i jak im zapobiegać
4. Szacowany koszt miesięczny (AWS/GCP)
```

---

### Ćwiczenie 3.2 – Prompt dla code review

**Cel:** Tworzyć prompty do analizy i recenzji kodu.

**Zadanie:**
Napisz prompt do code review poniższego fragmentu i oceń wynik:

```python
def get_user(id):
    conn = psycopg2.connect("host=localhost dbname=mydb user=admin ******")
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM users WHERE id = {id}")
    result = cursor.fetchone()
    return result
```

**Twój prompt powinien poprosić o:**
- Identyfikację błędów bezpieczeństwa
- Identyfikację błędów jakości kodu
- Propozycję poprawionej wersji
- Wyjaśnienie każdej zmiany

---

### Ćwiczenie 3.3 – Meta-prompting

**Cel:** Używać AI do tworzenia lepszych promptów.

**Zadanie:**
Poproś model o pomoc w stworzeniu lepszego promptu:

```
Chcę stworzyć prompt, który pomoże mi generować opisy commitów Git
zgodne z Conventional Commits (feat, fix, docs, etc.).

Pomóż mi zaprojektować optymalny prompt, który:
1. Przyjmuje diff z git jako wejście
2. Generuje opis commitu w formacie Conventional Commits
3. Opcjonalnie dodaje treść (body) jeśli zmiana jest złożona

Zaproponuj prompt, a następnie przetestuj go na przykładowym diffie.
```

---

## Samoocena

Po wykonaniu ćwiczeń odpowiedz na pytania:

- [ ] Rozumiem różnicę między promptem ogólnym a szczegółowym
- [ ] Potrafię stosować technikę Role Prompting
- [ ] Potrafię definiować format wyjścia w promptach
- [ ] Rozumiem i potrafię stosować Few-shot Prompting
- [ ] Potrafię używać Chain-of-Thought do złożonych zadań
- [ ] Potrafię iteracyjnie doskonalić prompty
- [ ] Potrafię ocenić jakość odpowiedzi i zidentyfikować braki promptu
