# Otwarte Pull Requests — stan na 2026-05-25

| # | Tytuł | Autor | Modyfikowane obszary | Status CI | Czas otwarcia |
|---|---|---|---|---|---|
| #423 | feat: Stripe Apple Pay integration | @jankowalski | frontend/checkout, backend/payments | ✅ green | 2 dni |
| #422 | refactor: extract OrderService | @anna.nowak | backend/orders | ❌ 3 testy failed | 4 dni |
| #421 | feat: 3-step checkout wizard | @anna.nowak | frontend/checkout | ✅ green, review needed | 1 dzień |
| #420 | feat: POST /orders/draft endpoint | @marek.dabrowski | backend/orders | ✅ green | 1 dzień |
| #419 | fix: race condition in ISBN index | @marek.dabrowski | backend/books | ✅ green | 3 dni |
| #418 | feat: BLIK + Apple Pay (Stripe) | @jankowalski | frontend/checkout, backend/payments | ⚠️ flaky tests | 5 dni |
| #417 | feat: GET /users/me/orders | @kasia.wojcik | backend/users | ✅ green | 2 dni |
| #416 | docs: Stripe setup README | @kasia.wojcik | docs | ✅ green | 1 dzień |
| #415 | feat: book tags schema migration | @marek.dabrowski | backend/books, db | ❌ migration test failed | 6 dni |
| #414 | fix: cart persistence in Safari | @anna.nowak | frontend/cart | ✅ green | 3 dni |
| #412 | feat: POST /books accepts tags | @marek.dabrowski | backend/books | ✅ green | 4 dni |
| #411 | chore: bump FastAPI to 0.115 | @kasia.wojcik | backend (all) | ✅ green | 7 dni |
| #410 | feat: order status push notifications | @piotr.zielinski (mobile) | mobile/notifications | ✅ green | 3 dni |
| #409 | feat: GET /books?tag= query | @marek.dabrowski | backend/books | ✅ green | 4 dni |
| #408 | docs: API examples in docs/api/ | @kasia.wojcik | docs | ✅ green | 1 dzień |
| #407 | perf: PostgreSQL index on books.isbn | @marek.dabrowski | db | ✅ green | 5 dni |
| #406 | fix: search supports Polish chars | @anna.nowak | backend/search | ✅ green | 6 dni |
| #404 | feat: rate limiting on /auth/login | @kasia.wojcik | backend/auth | ✅ green | 8 dni |
| #403 | feat: dark mode | @anna.nowak | frontend/ui | ✅ green | 4 dni |
| #402 | feat: Stripe webhook handler | @jankowalski | backend/payments | ⚠️ flaky tests | 6 dni |
| #400 | fix: 422 on negative payment amount | @jankowalski | backend/payments | ✅ green | 7 dni |
| #398 | feat: ISBN-10 validation | @marek.dabrowski | backend/books | ✅ green | 9 dni |
| #395 | feat: filter by category + tags | @anna.nowak | frontend/books | ✅ green | 10 dni |
| #391 | feat: recommendations endpoint | @marek.dabrowski | backend/books | ⚠️ flaky tests | 12 dni |
| #388 | feat: related books component | @anna.nowak | frontend/books | ✅ green | 8 dni |
| #385 | refactor: JWT authorization (BREAKING) | @marek.dabrowski | backend (all chronione) | ❌ 12 testów failed | 14 dni |

## Zespół

- **@marek.dabrowski** — backend (lead)
- **@kasia.wojcik** — backend
- **@anna.nowak** — frontend (lead)
- **@jankowalski** — frontend + payments
- **@piotr.zielinski** — mobile

## QA team (3 osoby, dostępne)

- **Tomek** — automation lead, Python/Playwright
- **Magda** — manualny + API
- **Damian** — performance + security
