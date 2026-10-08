# Validering – skydda ett objects state

Ett program kan fungera utan att krascha men ändå tillåta saker som inte borde vara möjliga. Det är problemet i den här labben. Python gör exakt vad vi har sagt åt det att göra; vi har ännu inte sagt **vilka förändringar som är tillåtna**.

Du får en **färdig, körbar** version av ett litet fordonsprogram. Du ska inte bygga en ny class från noll. I stället undersöker du orimliga resultat och lägger till enkla `if`-kontroller i befintliga methods. `Vehicle` och `Car` är samma bekanta domän som tidigare. Inheritance är bara bakgrund, inte det nya momentet.

## Mål och avgränsning

Efter labben ska du kunna förklara varför validering behövs, upptäcka ett orimligt state, kontrollera state och ett argument **innan** en method ändrar något, och använda `if` för att avbryta en otillåten operation. Skillnaden är viktig:

```text
syntaktiskt korrekt ≠ logiskt korrekt ≠ skyddat av programmets regler
```

En enkel arbetsmodell är **operation → kontrollera regler → tillåten? → ändra state eller ändra inget**. Vi använder bara variables, `if`/`else`, methods och andra delar du redan kan. Inga paket, filer, `input()` eller exception handling behövs. Vi utgår från att `amount` är ett vanligt `int`; text som indata ingår inte. Detta är **manuell kontroll**, inte en labb om automatiserade test.

Räkna med ungefär 1–2 timmar i egen takt. En fungerande kontrollpunkt är ett bra ställe att pausa. Gör gärna en liten `commit` efter varje steg som fungerar.

## Utgångsläge: kör innan du ändrar

Om du får labben som en publik GitHub-template: välj **Use this template → Create a new repository**, skapa ett eget **Private** repository och klona ditt eget repository. Filerna du arbetar i är [vehicle.py](vehicle.py) och [main.py](main.py). Kör från mappen med denna README:

```text
python main.py
```

På Windows kan `py main.py` fungera, och på vissa datorer `python3 main.py`. Programmet ska **inte krascha**. Det skapar en Car som börjar stoppad, med `speed = 0`, `fuel = 20` och `max_fuel = 40`. Sedan gör det fyra tveksamma saker. I startversionen returnerar alla operations-methods `True` utan att fråga om operationen borde vara tillåten. Sista raden blir:

```text
Final: False -50 10
```

Alltså: bilen är stoppad, har negativ speed och har förlorat fuel av en ”tankning”. Koden går att köra, men programmets regler saknas. I denna labb betyder `True` att operationen tilläts; `False` betyder att en regel stoppade den **utan att något state ändrades**. Behåll denna enkla regel i alla methods. Ett felaktigt argument ska inte tyst göras om till ett annat värde.

Du kan lägga till **tillfälliga vanliga `print()`-anrop** längst ned i `main.py` för stegens kontroller. Skapa gärna ett nytt Car-object för varje scenario så att tidigare operationer inte påverkar nästa. Ta bort tillfälliga rader efter kontrollen eller behåll tydliga manuella exempel. Ändra själva reglerna i [vehicle.py](vehicle.py), där objectet äger sitt state.

## Steg 1 – observera problemet

**Problemet:** `stop()`, `accelerate()`, `brake()` och `refuel()` kan säga ”lyckades” även när resultatet blir orimligt.

**Prova:** Kör den oförändrade startkoden med `python main.py`. Läs varje operation och den sista raden. Prova också tillfälligt att byta `car.brake(100)` till `car.brake(20)` och kör igen; återställ `100` efteråt.

**Observera:** Med `100` blir speed `-50`, medan `20` lämnar speed `30` efter den tidigare accelerationen. Inget av fallen ger en traceback. Betyder det att reglerna är korrekta? Vilket state är orimligt?

**Uppgift:** Ändra ännu inte `vehicle.py`. Skriv två korta svar i [REFLECTION.md](REFLECTION.md): vilka handlingar borde ha stoppats, och varför räcker inte ”programmet kraschar inte” som kvalitetsmått?

**Kontrollpunkt:** Kör igen efter att du återställt `brake(100)`: sista raden är åter `Final: False -50 10`. Du kan peka på minst två orimliga resultat och deras anrop i `main.py`.

**Commit:** `Inspect invalid vehicle states`

## Steg 2 – validera start()

**Problemet:** `start()` returnerar `True` även när fordonet redan är startat.

**Prova:** Lägg till en tillfällig Car längst ned i `main.py` och anropa `start()` två gånger. Skriv ut båda return-värdena och `is_running`. Innan din ändring blir båda svaren `True`.

**Observera:** Det andra anropet ändrar inget i verkligheten, men påstår ändå att en ny start lyckades.

**Uppgift:** I `Vehicle.start()`, kontrollera först `self.is_running`. Om den redan är `True`, returnera `False` **innan** state ändras. Behåll den befintliga vägen som sätter state och returnerar `True` vid en riktig start. Skriv `if`-satsen själv.

**Kontrollpunkt:** Kör med två start-anrop på ett nytt object: svaren ska vara `True`, `False`, och `is_running` ska fortfarande vara `True`. Prova att skapa ännu en ny Car: den ska börja stoppad.

**Commit:** `Validate vehicle start`

## Steg 3 – validera stop()

**Problemet:** `stop()` returnerar `True` när fordonet redan är stoppat.

**Prova:** Skapa en ny Car och skriv ut resultaten av `stop()`, `start()`, `stop()`, `stop()` i den ordningen. Före ändringen lyckas båda stop-anropen enligt return-värdet.

**Observera:** Det första och sista stoppförsöket har inget nytt att stoppa.

**Uppgift:** Gör en motsvarande kontroll i `Vehicle.stop()`. Om `self.is_running` redan är `False`, returnera `False` utan att ändra state. Annars ska stoppet fungera som förut. Ändra inte `start()` igen.

**Kontrollpunkt:** De fyra svaren från ett nytt object ska bli `False`, `True`, `True`, `False`. Slutligt `is_running` är `False`. Prova också ett enda `stop()` direkt efter att du skapat en annan Car: det ska ge `False`.

**Commit:** `Validate vehicle stop`

## Steg 4 – accelerera bara när fordonet är startat

**Problemet:** Startkoden kan öka `speed` trots att `is_running` är `False`.

**Prova:** Skapa en ny Car. Skriv ut resultat och speed efter `accelerate(10)` före start. Starta sedan samma Car och prova `accelerate(10)` igen.

**Observera:** Före valideringen ökar speed redan vid första anropet. Vilket attribute talar om om acceleration är tillåten?

**Uppgift:** I `Vehicle.accelerate(amount)`, kontrollera `self.is_running` **före** raden som ökar speed. Om fordonet är stoppat: returnera `False` och behåll speed. Behåll `True` när en tillåten acceleration har ändrat speed. Vänta med att kontrollera själva `amount` till nästa steg.

**Kontrollpunkt:** På ett nytt object ger `accelerate(10)` före start `False` och speed `0`. Efter `start()` ger `accelerate(10)` `True` och speed `10`. Prova med `5` efter start: speed blir `15`.

**Commit:** `Require running vehicle to accelerate`

## Steg 5 – validera argumentet amount

**Problemet:** Även ett startat fordon kan få lägre speed av `accelerate(-5)` eller rapportera en meningslös `accelerate(0)` som lyckad.

**Prova:** Skapa en ny Car, starta den och prova `accelerate(-5)`, `accelerate(0)` och `accelerate(10)`. Skriv ut return-värde och speed efter varje försök.

**Observera:** Här räcker det inte att kontrollera objectets state. Argumentet `amount` måste också vara rimligt.

**Uppgift:** Lägg till en separat kontroll i `accelerate(amount)`: bara värden **större än 0** är tillåtna. Vid 0 eller negativt värde ska methoden returnera `False` utan att ändra speed. Behåll kontrollen av `is_running` från steg 4. Ingen konvertering eller exception handling behövs.

**Kontrollpunkt:** Från speed `0` ger `-5` och `0` svaren `False`, `False` och speed förblir `0`; `10` ger `True` och speed `10`. Prova `5` efteråt: speed blir `15`.

**Commit:** `Validate acceleration amount`

## Steg 6 – skydda speed vid bromsning

**Problemet:** `brake(50)` från speed `20` ger `-30`. Ett negativt amount skulle tvärtom öka speed.

**Prova:** På en ny, startad Car: accelerera till `20`. Prova först `brake(-5)` och skriv ut speed, sedan `brake(50)`. Gör försöken i denna ordning så du kan se om det negativa värdet ändrade något.

**Observera:** Speed bör aldrig bli negativ i vår lilla modell. En bromsning med 0 eller negativt amount ska inte accepteras. Om speed redan är 0 finns inget att bromsa.

**Uppgift:** I `Vehicle.brake(amount)`, avvisa 0/negativt amount och avvisa bromsning när speed redan är 0; svara då `False` utan state-ändring. För ett positivt amount som är **minst** aktuell speed: sätt speed till `0` och returnera `True`. För ett mindre positivt amount: minska speed och returnera `True`. Skriv själv de enkla `if`/`else`-delarna.

**Kontrollpunkt:** Från speed `20` ger `brake(-5)` `False` och speed är kvar på `20`. `brake(50)` ger `True` och speed `0`, inte `-30`. Ett nytt `brake(10)` ger `False` och speed `0`. Prova även speed `20` och `brake(5)`: speed ska bli `15`.

**Commit:** `Prevent negative speed`

## Steg 7 – validera tankning

**Problemet:** `refuel(-10)` tar bort fuel. `refuel(30)` från fuel `20` skulle ge `50`, trots att `max_fuel` är `40`.

**Prova:** Skapa en ny Car och kontrollera `fuel` och `max_fuel`. Prova tillfälligt `refuel(-10)` och `refuel(30)` och läs fuel efter varje anrop.

**Observera:** En tankning ska öka fuel med ett positivt antal liter, men aldrig förbi maxkapaciteten. Här validerar du argumentet och vad den **nya** mängden skulle bli.

**Uppgift:** I `Vehicle.refuel(amount)`, avvisa 0/negativt amount och en tankning där `self.fuel + amount` skulle bli större än `self.max_fuel`. Returnera `False` utan ändring i båda fallen. Om hela mängden får plats, lägg till den och returnera `True`. I denna labb görs **ingen delvis tankning**.

**Kontrollpunkt:** Från fuel `20` ger `refuel(-10)` `False`, `refuel(30)` `False` och fuel är fortfarande `20`. `refuel(10)` ger `True` och fuel `30`; ytterligare `refuel(10)` ger `True` och fuel `40`; därefter ger `refuel(1)` `False` och fuel `40`. Prova också `refuel(0)`: `False`, oförändrat state.

**Commit:** `Validate refueling`

## Steg 8 – gör manuella scenarier

**Problemet:** En regel kan se rätt ut i en enda situation men vara fel i en annan.

**Prova:** Använd vanliga Car-objects och `print()` i `main.py`; **inga automatiserade test** behövs. Skapa ett nytt object för varje rad där tidigare handlingar annars kan påverka resultatet. Förutsäg svar och slutligt state innan du kör:

| Scenario | Förväntat efter steg 2–7 |
| --- | --- |
| Starta ett stoppat fordon | `True`, `is_running` blir `True`. |
| Starta det igen | `False`, state oförändrat. |
| Accelerera ett startat fordon med `10` | `True`, speed ökar med `10`. |
| Accelerera ett stoppat fordon med `10` | `False`, speed oförändrad. |
| Accelerera med `-5` eller `0` | `False`, speed oförändrad. |
| Bromsa från speed `20` med `50` | `True`, speed blir `0`. |
| Tanka `-10` liter | `False`, fuel oförändrat. |
| Tanka från `20` med `30` liter | `False`, fuel förblir `20`. |

**Observera:** Skillnaden mot startkoden är inte att Python slutat krascha – den kraschade aldrig. Skillnaden är att orimliga operationer nu stoppas av programmets regler.

**Uppgift:** Samla några tydliga manuella anrop i `main.py`. Skriv ut både return-värde och relevanta attributes **före och efter** varje scenario. Behåll bara kontroller som du själv kan förklara. Kör med `python main.py` och jämför tabellen rad för rad.

**Kontrollpunkt:** Alla scenarier i tabellen ger förväntat resultat. Vid varje `False` är `is_running`, `speed` och `fuel` oförändrade för det objectet. Prova ett eget rimligt värde, till exempel `brake(5)` från speed `20`: det ska ge `True` och speed `15`.

**Commit:** `Complete validation lab`

## Avsluta

Svara med egna ord i [REFLECTION.md](REFLECTION.md). Om något inte stämmer, använd [HJALP.md](HJALP.md) stegvis: förutsäg, kör, jämför, ändra en sak och kör igen. Vi löser inte inmatning av text eller andra fel under exekvering här; fokus är **validering**: får den begärda operationen förändra objectets state?
