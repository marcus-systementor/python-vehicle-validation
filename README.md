# Validering – skydda objektets state

**state (tillstånd)** = de aktuella värden som beskriver objektet, exempelvis `speed` och `fuel`.

## Vad går labben ut på?

Programmet fungerar redan och kraschar inte. Problemet är att det tillåter saker som inte borde vara möjliga.

Du ska inte bygga ett nytt program. Du ska lägga till enkla `if`-kontroller i de methods som redan finns.

Så här ska varje operation fungera:

```text
operation
↓
kontrollera regeln
↓
tillåten?
├── ja → ändra state → True
└── nej → ändra inget → False
```

## Filerna du arbetar med

```text
vehicle.py
→ här ändrar du reglerna

main.py
→ här kör och kontrollerar du programmet

REFLECTION.md
→ här svarar du kort på reflektionsfrågorna

HJALP.md
→ öppna om du fastnar
```

(Mappen `facit/`, om den finns lokalt, är lärarmaterial.)

## Starta här

Klona eller öppna ditt eget repo enligt lärarens instruktion och öppna en terminal i mappen där `README.md`, `main.py` och `vehicle.py` finns. Kör sedan:

```bash
python main.py
```

Om `python` inte fungerar: prova `py main.py` eller `python3 main.py`.

Läs utskriften från början till slut. Ändra inget ännu.

## Vad är fel?

| Situation | Vad programmet tillåter |
|---|---|
| Stoppa en redan stoppad bil | operationen rapporteras som lyckad |
| Accelerera när bilen är stoppad | speed ökar ändå |
| Bromsa för mycket | speed kan bli negativ |
| Tanka negativ mängd | fuel minskar |

Programmet kraschar inte. Det betyder inte att programmets regler är korrekta.

## Så arbetar du

```text
1. Läs ett steg.
2. Förutsäg vad som borde hända.
3. Ändra EN method i vehicle.py.
4. Kör main.py.
5. Kontrollera return-värde och state.
6. Commit när steget fungerar.
```

Ändra en sak i taget. Gör gärna en liten commit efter varje färdigt steg.

---

## Steg 1 – Undersök programmet

**Gör:** Kör `main.py` och läs de fyra testen.

Fundera:
- Vilka operationer borde ha stoppats?
- Vilka state-värden blir orimliga?

Ändra ingen kod ännu.

**Klar när:** Du kan förklara minst två problem med startprogrammet.

## Steg 2 – `start()`

**Gör:** Om bilen redan är startad ska `start()` returnera `False` och inte ändra state.

**Klar när:**

```text
första start() → True
andra start() → False
```

**Commit:** `Validate start`

## Steg 3 – `stop()`

**Gör:** Om bilen redan är stoppad ska `stop()` returnera `False`.

**Klar när:** Du kan visa att ett extra stopp nekas (och att `start()` följt av `stop()` fortfarande ger `True`).

**Commit:** `Validate stop`

## Steg 4 – `accelerate()`

### 4A – bilen måste vara startad

**Gör:** Om `is_running` är `False` ska `accelerate()` returnera `False` och speed ska inte ändras.

**Klar när:** Acceleration före `start()` ger `False`; efter `start()` ger den `True`.

### 4B – amount måste vara större än 0

**Gör:** Om `amount` är 0 eller negativt ska `accelerate()` returnera `False` och speed ska inte ändras.

**Klar när:** `accelerate(-5)` och `accelerate(0)` ger `False`, medan `accelerate(10)` ger `True` och speed `10`.

**Commit:** `Validate accelerate`

## Steg 5 – `brake()`

**Gör:** Lägg in tre regler:

```text
amount måste vara > 0
speed 0 → inget att bromsa
för stor bromsning → speed blir 0, aldrig negativ
```

Nekade fall returnerar `False` utan ändring. Tillåtna fall returnerar `True`.

**Klar när:** Från speed `20` ger `brake(-5)` `False` (speed `20`), `brake(5)` ger `True` (speed `15`), `brake(50)` ger `True` (speed `0`) och ett nytt `brake(10)` ger `False`.

**Commit:** `Validate brake`

## Steg 6 – `refuel()`

**Gör:** Lägg in två regler:

```text
amount måste vara > 0
fuel får inte gå över max_fuel
```

Ingen delvis tankning: om hela mängden inte får plats, returnera `False` och ändra inget.

**Klar när:** Från fuel `20` ger `refuel(-10)` och `refuel(30)` `False` (fuel `20`), medan `refuel(10)` ger `True` (fuel `30`).

**Commit:** `Validate refuel`

## Steg 7 – Kontrollera programmet

**Gör:** Kör `main.py` igen och läs utskrifterna. Lägg gärna till några egna `print()`-rader med nya `Car`-objekt för fall du vill testa, till exempel:

- starta två gånger
- accelerera före start
- tanka över `max_fuel`

**Klar när:** Varje `False` har lämnat `is_running`, `speed` och `fuel` oförändrade, och varje `True` har ändrat state som förväntat.

**Commit:** `Complete validation lab`

---

## Kom ihåg

- `True` = operationen tillåts
- `False` = operationen stoppas och state ändras inte
- ändra reglerna i `vehicle.py`
- använd `main.py` för att kontrollera resultatet
- ändra en sak i taget
- använd `HJALP.md` om du fastnar

När du är klar: svara på frågorna i `REFLECTION.md`.

---

*Not (lärare): om labben delas som GitHub-template väljer studenten **Use this template → Create a new repository**, skapar ett eget privat repo och klonar det.*
