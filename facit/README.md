# Facit – endast för lokal lärargranskning

**Ta bort hela `facit/` innan studentmallen publiceras.** Mappen finns lokalt för granskning och är ignorerad av `.gitignore` som extra skydd. Kontrollera ändå exakt vilka filer som publiceras.

Detta är ett möjligt lösningsförslag. Studentens kod behöver inte se exakt likadan ut om den uppfyller samma regler och studenten kan förklara hur den fungerar. Jämför med labbens regler och kör [main.py](main.py) från repositoryts rot med `python facit/main.py`.

Alla operations-methods returnerar `True` när den begärda operationen tillåts och `False` när en regel stoppar den. Vid `False` ändras inget state. I denna enkla modell ger en för stor positiv inbromsning speed `0`; bromsning vid speed `0` avvisas. Tankning som skulle överskrida `max_fuel` avvisas helt, utan delvis påfyllning. Ingen fil-lagring eller exception handling används.
