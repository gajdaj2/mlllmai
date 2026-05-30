# Prompt Engineering – Przewodnik

Prompt Engineering to sztuka i nauka formułowania zapytań (promptów) do modeli językowych (LLM) w taki sposób, aby uzyskiwać dokładne, przydatne i spójne odpowiedzi.

## Czym jest prompt?

**Prompt** to tekst wejściowy przekazywany do modelu AI. Jakość promptu ma bezpośredni wpływ na jakość odpowiedzi – dobrze skonstruowany prompt pozwala w pełni wykorzystać możliwości modelu.

## Anatomia dobrego promptu

Skuteczny prompt często zawiera następujące elementy:

```
[Rola / Persona]       – Kim jest model?
[Kontekst]             – Tło sytuacji lub zadania
[Instrukcja / Zadanie] – Co konkretnie ma zrobić model?
[Format wyjścia]       – Jak ma wyglądać odpowiedź?
[Przykłady]            – Opcjonalne wzorce zachowania
[Ograniczenia]         – Czego model ma unikać?
```

### Przykład

```
Rola: Jesteś doświadczonym inżynierem oprogramowania znającym Python.
Kontekst: Pracuję nad API REST w FastAPI, które obsługuje dane użytkowników.
Zadanie: Napisz funkcję walidującą adres e-mail i numer telefonu (format E.164).
Format: Zwróć kod Pythona z docstringiem i przykładem użycia.
Ograniczenia: Nie używaj zewnętrznych bibliotek – tylko standardowa biblioteka Pythona.
```

## Techniki Prompt Engineering

### 1. Zero-shot Prompting

Podajesz instrukcję bez żadnych przykładów – model odpowiada na podstawie swojej wiedzy.

```
Przetłumacz poniższe zdanie na język angielski:
"Sztuczna inteligencja zmienia sposób, w jaki pracujemy."
```

**Kiedy stosować:** proste, jednoznaczne zadania, które model dobrze rozumie z opisu.

---

### 2. Few-shot Prompting

Podajesz kilka przykładów wejścia i oczekiwanego wyjścia, aby „nauczyć" model wzorca odpowiedzi.

```
Klasyfikuj nastrój recenzji jako POZYTYWNY lub NEGATYWNY.

Recenzja: "Produkt świetny, polecam!"
Nastrój: POZYTYWNY

Recenzja: "Bardzo rozczarowany jakością."
Nastrój: NEGATYWNY

Recenzja: "Dostawa szybka, ale opakowanie uszkodzone."
Nastrój:
```

**Kiedy stosować:** gdy zadanie ma konkretny format lub pattern, który trudno opisać słowami.

---

### 3. Chain-of-Thought (CoT)

Prosisz model o rozumowanie krok po kroku przed podaniem odpowiedzi końcowej. Znacznie poprawia dokładność w zadaniach wymagających logiki lub obliczeń.

```
Rozwiąż poniższe zadanie, wypisując każdy krok rozumowania:

W sklepie jest 48 jabłek. Sprzedano 1/3. Z pozostałych jabłek
połowa uległa zepsuciu. Ile jabłek zostało zdatnych do sprzedaży?

Krok po kroku:
```

**Kiedy stosować:** zadania matematyczne, logiczne, wieloetapowe analizy.

---

### 4. Role Prompting

Przypisujesz modelowi konkretną rolę lub personę, co wpływa na styl, ton i głębokość odpowiedzi.

```
Jesteś starszym architektem rozwiązań chmurowych z 15-letnim doświadczeniem
w AWS i Azure. Twoim zadaniem jest ocena poniższej architektury pod kątem
skalowalności, bezpieczeństwa i kosztów.

[opis architektury]
```

**Kiedy stosować:** gdy potrzebujesz odpowiedzi z określonej perspektywy eksperckiej.

---

### 5. Self-Consistency

Generujesz kilka odpowiedzi na to samo pytanie i wybierasz najczęściej powtarzającą się lub syntetujesz je w jedną.

```
Odpowiedz na pytanie na trzy różne sposoby, stosując różne podejścia,
a następnie wskaż, które rozwiązanie jest najlepsze i dlaczego:

[pytanie]
```

---

### 6. Iteracyjne doprecyzowanie

Zamiast tworzyć jeden „idealny" prompt, iteracyjnie go udoskonalasz na podstawie wyników.

```
Wersja 1: "Napisz kod sortujący listę."
Wersja 2: "Napisz funkcję Pythona sortującą listę liczb całkowitych malejąco."
Wersja 3: "Napisz funkcję Pythona sortującą listę liczb całkowitych malejąco.
           Uwzględnij obsługę pustej listy i elementów None. Dodaj type hints."
```

---

### 7. Prompt z formatem wyjścia (Output Format)

Określasz dokładny format, w jakim model ma zwrócić odpowiedź.

```
Przeanalizuj poniższy kod i zwróć wynik w formacie JSON:
{
  "błędy": [...],
  "ostrzeżenia": [...],
  "sugestie": [...],
  "ocena_jakości": "1-10"
}

[kod do analizy]
```

---

### 8. Negative Prompting

Jasno określasz, czego model ma **nie** robić.

```
Wyjaśnij działanie algorytmu quicksort.
NIE używaj pseudokodu ani kodu źródłowego.
NIE zakładaj, że czytelnik zna inne algorytmy sortowania.
Skieruj wyjaśnienie do osoby, która dopiero zaczyna naukę programowania.
```

## Typowe błędy w promptach

| Błąd | Przykład źle | Przykład lepiej |
|---|---|---|
| Zbyt ogólny prompt | „Napisz mi coś o AI" | „Napisz 3-zdaniowe podsumowanie zastosowań AI w medycynie diagnostycznej" |
| Brak kontekstu | „Napraw błąd w kodzie" | „Napraw błąd `KeyError: 'name'` w poniższym fragmencie kodu Python 3.11" |
| Sprzeczne instrukcje | „Bądź zwięzły, ale wyczerpująco opisz każdy aspekt" | „Opisz najważniejsze 3 aspekty w maksymalnie 5 zdaniach każdy" |
| Brak formatu | „Daj mi listę zaleceń" | „Podaj 5 zaleceń jako ponumerowaną listę, każde w jednym zdaniu" |

## Najlepsze praktyki

1. **Bądź konkretny** – im precyzyjniejszy prompt, tym lepsza odpowiedź.
2. **Podawaj kontekst** – tło, środowisko, ograniczenia techniczne.
3. **Definiuj rolę** – przypisz modelowi odpowiednią ekspertyzę.
4. **Określ format** – JSON, lista, akapit, kod – model dostosuje wyjście.
5. **Iteruj** – traktuj tworzenie promptu jako proces, nie jednorazowe działanie.
6. **Testuj różne sformułowania** – małe zmiany w promptach mogą dawać bardzo różne wyniki.
7. **Weryfikuj wyniki** – AI może się mylić; zawsze sprawdzaj krytyczne informacje.

## Ćwiczenia

Przejdź do [ćwiczeń Prompt Engineering](../exercises/prompt-engineering-exercises.md), aby utrwalić wiedzę w praktyce.
