# PRRI-CognitiveAgents2026

Upute za preuzimanje i pokretanje igre.

Ova igra se pokreće lokalno preko Python servera. Nakon pokretanja servera igra se otvara u web pregledniku na adresi `http://localhost:5000`.

---

## 1. Preuzimanje igre

Preuzmite datoteku:

```text
PRRI-CognitiveAgents2026.zip
```

Datoteku preuzmite s mjesta gdje je objavljena igra.

Nakon preuzimanja nemojte pokretati igru direktno iz ZIP datoteke. ZIP datoteku prvo treba raspakirati.

---

## 2. Raspakiravanje ZIP datoteke

Raspakirajte datoteku `PRRI-CognitiveAgents2026.zip` na željenu lokaciju na računalu.

Primjer lokacije na Windowsu:

```text
C:\PRRI\PRRI-CognitiveAgents2026
```

Nakon raspakiravanja trebali biste imati mapu:

```text
PRRI-CognitiveAgents2026
```

Unutar nje se nalazi više datoteka i mapa, a za pokretanje igre najvažnija je mapa:

```text
src
```

U mapi `src` nalaze se `server.py`, `requirements.txt` i ostale datoteke potrebne za pokretanje igre.

---

## 3. Potrebno prije pokretanja

Prije pokretanja igre potrebno je imati instaliran Python.

Provjera je li Python instaliran:

```bash
python --version
```

Ako ova komanda ne radi, pokušajte:

```bash
python3 --version
```

Ako Python nije instaliran, potrebno ga je instalirati prije nastavka.

---

## 4. Otvaranje terminala u mapi `src`

Otvorite terminal, Command Prompt ili PowerShell.

Zatim se premjestite u mapu `src`.

Primjer:

```bash
cd PRRI-CognitiveAgents2026/src
```

Ako je projekt spremljen npr. u `C:\PRRI`, onda bi komanda mogla biti:

```powershell
cd C:\PRRI\PRRI-CognitiveAgents2026\src
```

Važno: sve sljedeće komande trebaju se pokretati iz mape `src`.

---

## 5. Instalacija potrebnih paketa

U mapi `src` pokrenite:

```bash
pip install -r requirements.txt
```

Ako koristite Linux ili macOS, možda trebate koristiti:

```bash
pip3 install -r requirements.txt
```

Ova komanda instalira Python pakete potrebne za rad igre i kognitivnih agenata.

Ako dobijete grešku da `pip` ne postoji, pokušajte:

```bash
python -m pip install -r requirements.txt
```

ili:

```bash
python3 -m pip install -r requirements.txt
```

---

## 6. Treniranje kognitivnih agenata

Prije prvog pokretanja igre potrebno je istrenirati kognitivne agente.

Pokrenite ove komande jednu po jednu:

```bash
python server.py --trainEngineer
python server.py --trainAnalyst
python server.py --trainCartographer
python server.py --trainNarrator
```

Ako koristite Linux ili macOS, možda trebate koristiti `python3`:

```bash
python3 server.py --trainEngineer
python3 server.py --trainAnalyst
python3 server.py --trainCartographer
python3 server.py --trainNarrator
```

Treniranje je potrebno napraviti prije prvog igranja. Ako su agenti već istrenirani i podaci nisu mijenjani, ovaj korak obično nije potrebno ponavljati svaki put.

---

## 7. Pokretanje igre

Nakon instalacije paketa i treniranja agenata, pokrenite server:

```bash
python server.py
```

ili, ako koristite Linux/macOS:

```bash
python3 server.py
```

Nakon pokretanja servera terminal mora ostati otvoren. Nemojte ga zatvarati dok igrate igru, jer se igra pokreće preko tog lokalnog servera.

---

## 8. Otvaranje igre u pregledniku

Kada je server pokrenut, otvorite web preglednik i upišite:

```text
http://localhost:5000
```

Igra bi se tada trebala otvoriti u pregledniku.

Ako se stranica ne otvori, provjerite:

- je li terminal i dalje otvoren,
- je li `server.py` pokrenut bez greške,
- jeste li u preglednik upisali točnu adresu,
- koristite li adresu `http://localhost:5000`.

---

## 9. Testiranje agenata

Ako želite testirati agente bez pokretanja cijele igre, u mapi `src` možete pokrenuti:

```bash
python chat-test_engineer.py
python chat-test_analyst.py
python chat-test_cartographer.py
```

Na Linuxu/macOS-u možete koristiti:

```bash
python3 chat-test_engineer.py
python3 chat-test_analyst.py
python3 chat-test_cartographer.py
```

Ovo služi samo za provjeru rada agenata i nije potrebno za obično igranje.

---

## 10. Uređivanje igre u Twineu

Ako želite uređivati samu Twine priču, otvorite datoteku:

```text
The Last Command.twee
```

u programu Twine.

Nakon uređivanja priče potrebno je ponovno objaviti HTML verziju igre. Iz Twinea koristite opciju **Publish to File** i spremite rezultat kao:

```text
src/templates/index.html
```

Važno: ako mijenjate samo `index.html`, a kasnije ponovno izvezete igru iz Twinea, ručne promjene u `index.html` mogu se izgubiti. Najsigurnije je glavne promjene priče raditi u `.twee` datoteci.

---

## 11. Najčešći problemi

### `python` nije prepoznat kao komanda

Provjerite je li Python instaliran i dodan u PATH. Pokušajte koristiti:

```bash
python3
```

umjesto:

```bash
python
```

### `pip` nije prepoznat kao komanda

Pokušajte:

```bash
python -m pip install -r requirements.txt
```

ili:

```bash
python3 -m pip install -r requirements.txt
```

### Igra se ne otvara na `http://localhost:5000`

Provjerite je li server pokrenut i je li terminal ostao otvoren.

### Agenti ne odgovaraju ili se pojavljuju greške s agentima

Ponovno pokrenite treniranje agenata:

```bash
python server.py --trainEngineer
python server.py --trainAnalyst
python server.py --trainCartographer
python server.py --trainNarrator
```

### Otvorili ste ZIP, ali igra se ne pokreće

ZIP datoteku treba prvo raspakirati. Igru ne pokretati direktno iz ZIP pregleda.

---

## 12. Kratka verzija komandi

### Windows primjer

```powershell
cd C:\PRRI\PRRI-CognitiveAgents2026\src
pip install -r requirements.txt
python server.py --trainEngineer
python server.py --trainAnalyst
python server.py --trainCartographer
python server.py --trainNarrator
python server.py
```

Zatim u pregledniku otvoriti:

```text
http://localhost:5000
```

### Linux/macOS primjer

```bash
cd PRRI-CognitiveAgents2026/src
pip3 install -r requirements.txt
python3 server.py --trainEngineer
python3 server.py --trainAnalyst
python3 server.py --trainCartographer
python3 server.py --trainNarrator
python3 server.py
```

Zatim u pregledniku otvoriti:

```text
http://localhost:5000
```

---

## 13. Napomena

Igra je lokalna web igra. To znači da se ne pokreće dvostrukim klikom na HTML datoteku, nego preko datoteke `server.py`.

Server se pokreće u terminalu, a igra se igra u web pregledniku.
