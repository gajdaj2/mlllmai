# language: pl
Funkcja: Koszyk zakupowy
  Jako użytkownik Bookstore
  Chcę dodawać książki do koszyka i zarządzać jego zawartością
  Aby móc złożyć zamówienie

  Założenia:
    Zakładając, że aplikacja działa na http://localhost:3000
    Oraz jestem zalogowany jako "test_user"
    Oraz na liście jest co najmniej 5 książek

  Scenariusz: Dodanie pojedynczej książki do koszyka
    Mając użytkownika na stronie listy książek
    Kiedy kliknę "Add to cart" na pierwszej książce
    Wtedy powinien pojawić się toast "Added to cart"
    Oraz ikona koszyka powinna pokazywać "1"

  Scenariusz: Dodanie tej samej książki dwa razy zwiększa ilość
    Mając użytkownika na stronie listy książek
    Kiedy kliknę "Add to cart" na pierwszej książce
    Oraz kliknę "Add to cart" na pierwszej książce ponownie
    Wtedy ikona koszyka powinna pokazywać "2"
    Oraz w koszyku powinna być 1 pozycja z ilością "2"

  Szablon scenariusza: Walidacja ilości w koszyku
    Mając użytkownika z 1 książką w koszyku
    Kiedy zmienię ilość na "<ilosc>"
    Wtedy stan koszyka powinien być "<oczekiwany_stan>"

    Przykłady:
      | ilosc | oczekiwany_stan       |
      | 0     | pusty                 |
      | 5     | 5 sztuk tej książki   |
      | 99    | 99 sztuk tej książki  |

  Scenariusz: Niezalogowany użytkownik jest przekierowany na login
    Mając niezalogowanego użytkownika na liście książek
    Kiedy kliknę "Add to cart" na pierwszej książce
    Wtedy zostanę przekierowany na "/login"
    Oraz zobaczę komunikat "Zaloguj się, aby dodać do koszyka"

  Scenariusz: Refresh zachowuje zawartość koszyka
    Mając użytkownika z 3 książkami w koszyku
    Kiedy odświeżę stronę
    Wtedy koszyk powinien zawierać 3 książki
