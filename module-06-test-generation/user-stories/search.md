# User Story: Wyszukiwanie książek

**Jako** użytkownik
**Chcę** szukać książek po tytule lub autorze
**Aby** szybko znaleźć interesującą mnie pozycję

## Acceptance criteria

- Pole search w nawigacji, placeholder "Szukaj książki...".
- Wyszukiwanie po naciśnięciu Enter LUB po 500ms od ostatniego znaku (debounce).
- Wyniki: pasujące tytuły LUB autorzy (case-insensitive, contains).
- Liczba wyników widoczna nad listą: "Znaleziono N książek".
- Pusta lista: "Nie znaleziono książek dla: {query}".
- Pusta query → return all books (jak na liście głównej).
- URL aktualizuje się: /books?q={query}.
- Refresh strony zachowuje query w URL.

## Edge cases

- Query z polskimi znakami: "Mickiewicz", "Żmichowska" — działa.
- Query z tylko spacjami → pokazuje wszystkie (jak pusty).
- Query bardzo długi (>200 znaków) → trimming + komunikat.
- SQL injection: `'; DROP TABLE books; --` → bezpiecznie escape'owane.
