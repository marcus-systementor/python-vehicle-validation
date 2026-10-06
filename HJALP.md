# Hjälp – validera en regel i taget

Öppna bara ledtråden för ditt aktuella steg. Börja med **frågan**. Prova en ändring och kör `python main.py` innan du läser den tydligare ledtråden. En nekad operation ska returnera `False` **utan att ändra** `is_running`, `speed` eller `fuel`.

## Steg 1 – undersök

**Första ledtråd:** Följ värdena i den ordning `main.py` anropar methods. Vad är speed precis före `brake(100)`?

**Mer hjälp:** Startvärdet är `0`. Starter-koden lägger till `50` trots att bilen är stoppad och drar sedan bort `100`. Jämför detta med sista utskriften. Det finns inget syntaxfel att laga.

## Steg 2 – start()

**Första ledtråd:** Vilket bool-attribute berättar om bilen redan är startad?

**Mer hjälp:** Undersök `self.is_running` **innan** tilldelningen i `start()`. Om den redan betyder ”startad”, vilken return-signal ska anroparen få? Placera kontrollen så att den tidigt kan avsluta methoden.

## Steg 3 – stop()

**Första ledtråd:** Vilket värde på samma attribute betyder ”redan stoppad”?

**Mer hjälp:** Använd samma ordning som i steg 2: kontroll först, eventuell tidig `return False`, sedan den redan fungerande ändringen och `return True`. Ett nytt Car-object börjar med `False` i `is_running`.

## Steg 4 – acceleration och state

**Första ledtråd:** Innan speed ökar, vad måste vara sant om fordonet?

**Mer hjälp:** `self.is_running` beskriver tillståndet. För ett stoppat object ska methoden nå `return False` **före** `self.speed += amount`. Prova både före och efter `start()` på samma object.

## Steg 5 – acceleration och argument

**Första ledtråd:** Är `-5` eller `0` en rimlig ökning av speed?

**Mer hjälp:** Kontrollera `amount` separat från `is_running`. Bara ett värde större än `0` får nå raden som ändrar speed. Behåll båda kontrollerna; en startad bil gör inte ett negativt argument giltigt.

## Steg 6 – bromsning

**Första ledtråd:** Hur påverkar `speed -= amount` speed när amount är negativt? Vad bör hända om amount är större än speed?

**Mer hjälp:** Stoppa först 0/negativt amount. När speed redan är 0 finns inget att bromsa. Om ett positivt amount är minst lika stort som speed, välj `0` som nytt speed-värde. Annars kan den vanliga subtraktionen användas. Kontrollera med speed `20` och amount `-5`, `50` och `5` i separata försök.

## Steg 7 – tankning

**Första ledtråd:** Vilka två frågor måste besvaras innan `fuel` ökar?

**Mer hjälp:** Först: är `amount` större än 0? Sedan: skulle `self.fuel + amount` bli större än `self.max_fuel`? Ett nekande svar returnerar `False` före ändringen. En tankning som inte får plats avvisas helt.

## Steg 8 – manuella scenarier

**Första ledtråd:** Använder två av dina kontroller samma Car-object och påverkar därför varandras startvärden?

**Mer hjälp:** Skapa ett nytt object för ett scenario som kräver speed `0` och fuel `20`. Skriv ut return-värde och state före/efter. Om ett `False` ändå följs av ändrat state, gå till den methoden och kontrollera om en tilldelning sker **före** valideringen.

## Om Python visar en traceback

1. Läs sista raden: vilket fel anger Python?
2. Leta upp filnamn och radnummer ovanför.
3. Läs den raden i din aktuella fil. Kontrollera indrag, stavning och om methoden verkligen finns.
4. Ändra en sak och kör igen. Tillfälliga `print()` av ett värde kan hjälpa; ta bort dem när du förstått felet.

Om `python` inte hittas, prova `py` eller `python3` med samma `main.py`. Om filen inte hittas, öppna terminalen i mappen med `README.md`, `vehicle.py` och `main.py`. När du frågar om hjälp: skicka stegnummer, anrop, förväntat och faktiskt return-värde/state samt eventuell sista rad i traceback.
