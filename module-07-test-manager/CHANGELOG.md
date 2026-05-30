# Changelog — Bookstore 2.5

> Release planowany: 2026-06-15  
> Sprint: Q2-S6  
> Liczba zmian: 23 PR-y, 8 issue zamkniętych

## Added (nowe funkcjonalności)

### Frontend
- **#421** Nowa strona checkout z 3-krokowym wizardem (adres → płatność → potwierdzenie).
- **#418** Wsparcie dla płatności BLIK i Apple Pay (integracja Stripe).
- **#403** Dark mode w UI (toggle w nawigacji, persisted w localStorage).
- **#395** Filtrowanie listy książek po kategorii + tagach.
- **#388** Komponent "Powiązane książki" na stronie szczegółów.

### Backend
- **#420** Nowy endpoint `POST /orders/draft` — szkic zamówienia (do checkout).
- **#417** Endpoint `GET /users/me/orders` — historia zamówień użytkownika.
- **#402** Webhook z Stripe (`POST /webhooks/stripe`) do potwierdzania płatności.
- **#391** Endpoint `GET /books/recommendations` — rekomendacje (collaborative filtering, prosty algorytm).

### Mobile
- **#410** Push notifications dla statusu zamówienia (FCM).

## Changed (zmiany w istniejących)

- **#415** Schema `Book` — dodane pole `tags` (lista stringów). Migracja DB w deploymencie.
- **#412** Endpoint `POST /books` — przyjmuje teraz `tags` (opcjonalne, default `[]`).
- **#409** Endpoint `GET /books` — nowy parametr query `?tag=...` (filtrowanie).
- **#398** Walidacja ISBN — rozszerzona o ISBN-10 (poprzednio tylko ISBN-13).
- **#385** Refactor authorization — JWT zamiast prostego tokena testowego (BREAKING dla testów!).

## Fixed (poprawki)

- **#419** Bug: duplikat książki przy concurrent POST (race condition w `_isbn_index`).
- **#414** Bug: koszyk gubi pozycje po refresh w niektórych przeglądarkach (Safari).
- **#406** Bug: search nie obsługiwał polskich znaków (Ż, Ć, Ó, ...).
- **#400** Bug: 500 zamiast 422 przy płatności z ujemną kwotą.

## Security

- **#411** Bumped FastAPI 0.110 → 0.115 (CVE-2024-XXXXX).
- **#404** Rate limiting na `/auth/login` (5 prób / 15 min / IP).

## Performance

- **#407** Index na `books.isbn` w PostgreSQL — query speedup 100x.
- **#393** Cache rekomendacji w Redis (TTL 1h).

## Documentation

- **#416** Zaktualizowane README.md z instrukcją Stripe setup.
- **#408** Nowy folder `docs/api/` z OpenAPI examples.

---

## Komentarz Tech Lead

> Release dość duży — łącznie 23 PR-y. Główne ryzyko: refactor authorization (#385) ma wpływ na
> wszystkie endpointy chronione. Integracja Stripe (#418) to nowy obszar — wymaga end-to-end testów
> w środowisku staging z prawdziwymi sandbox keys. Migracja DB (#415) wymaga regresji wszystkich
> endpointów `/books`.
