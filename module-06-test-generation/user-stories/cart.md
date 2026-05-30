# User Story: Dodawanie książki do koszyka

**Jako** zalogowany użytkownik aplikacji Bookstore
**Chcę** dodać książkę do koszyka i przejść do checkout
**Aby** zamówić wybrane książki online

## Acceptance criteria

- Mogę kliknąć "Add to cart" z listy książek (na każdej karcie produktu).
- Po dodaniu widzę toast "Added to cart" przez 3 sekundy.
- Ikona koszyka w nawigacji pokazuje aktualną liczbę produktów.
- Mogę otworzyć koszyk klikając ikonę koszyka.
- W koszyku widzę listę dodanych produktów: tytuł, autor, cena, ilość.
- Mogę zmienić ilość (input number) lub usunąć produkt (X).
- Suma w koszyku aktualizuje się dynamicznie.
- Mogę kliknąć "Checkout" → przejście do strony /checkout.
- Niezalogowany użytkownik widzi przycisk "Add to cart", ale po kliknięciu zostaje
  przekierowany na /login z message "Zaloguj się, aby dodać do koszyka".

## Edge cases

- Dodanie tej samej książki 2x → ilość się zwiększa o 1, nie tworzy duplikatu.
- Ustawienie ilości na 0 → produkt usuwany z koszyka.
- Refresh strony → koszyk się zachowuje (localStorage lub session).
- 50+ pozycji w koszyku → scrollbar w drawerze koszyka.

## UI Notes (z mockupów)

- `data-testid="add-to-cart-{book_id}"` na każdym przycisku Add to cart.
- `data-testid="cart-icon"`, `data-testid="cart-count"`.
- `data-testid="cart-item-{book_id}"` na pozycjach w koszyku.
- `data-testid="checkout-button"`.
