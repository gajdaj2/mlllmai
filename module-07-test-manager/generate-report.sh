#!/bin/bash
# generate-report.sh
#
# Generuje raport biznesowy z wyników testów (JUnit XML) używając Copilot CLI
# w trybie programatycznym (-p).
#
# Użycie: ./generate-report.sh

set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPORT_XML="$SCRIPT_DIR/pytest-report.xml"
OUTPUT="$SCRIPT_DIR/report-business.md"

if [[ ! -f "$REPORT_XML" ]]; then
    echo "Error: $REPORT_XML not found" >&2
    exit 1
fi

echo "📊 Generowanie raportu biznesowego z $REPORT_XML..."
echo "   Output: $OUTPUT"
echo ""

copilot -p "
Przeczytaj plik $REPORT_XML (JUnit XML z wynikami pytest).
Wygeneruj raport po polsku dla osób nietechnicznych (business stakeholders).

Raport ma zawierać:

# Raport z testów — Release 2.5

## 1. Podsumowanie wykonawcze
(2-3 zdania: co przeszło, co nie, czy można wypuszczać release)

## 2. Statystyki
- Łącznie testów: X
- Passed: X (Y%)
- Failed: X (Y%)
- Errors: X
- Skipped: X

## 3. Obszary problemowe (Top 3-5)
Dla każdego: krótki opis problemu w języku biznesowym (BEZ terminów: assertion, fixture, mock,
locator, parametrize, async).

Pisz językiem stakeholdera: 'Klient nie może...', 'Funkcja X nie działa w sytuacji Y'.

## 4. Rekomendacja
- ✅ Gotowy do release / ⚠️ Wymaga poprawek / ❌ Blokowany

## 5. Co należy poprawić przed release'em
Lista konkretnych akcji (max 5).

Zapisz wynik do $OUTPUT (nadpisz jeśli istnieje).
" --allow-all-tools

echo ""
echo "✅ Raport wygenerowany:"
echo ""
cat "$OUTPUT"
