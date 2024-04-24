# Python Opdracht: Boeken Zoeker

Deze opdracht heeft als doel om je kennis van Python en externe API's te testen door het bouwen van een applicatie die gebruik maakt van de Open Library API. Je gaat een programma schrijven dat gebruikers in staat stelt om boeken te zoeken, favorieten te beheren, en deze op te slaan in een CSV-bestand.

## Vereisten

* Python 3.x
* `requests` library (geïnstalleerd via pip)
* We gaan in deze opdracht werken met API's, JSON en CSV-bestanden in Python.

## Stap 1: Voorbereiding

Installeer de benodigde library via pip:

```bash
pip install requests
```

## Stap 2: Script Setup

Maak een nieuw Python script genaamd `book_finder.py`. Dit script zal de hoofdcode van je applicatie bevatten.

## Stap 3: Import Statements

Voeg de volgende imports toe aan het begin van je script:

```python
import requests
import csv
```

De `requests` library wordt gebruikt om HTTP-verzoeken te maken naar de Open Library API, en de `csv` library wordt gebruikt om met CSV-bestanden te werken.

## Stap 4: Globale Variabele

Definieer een globale lijst genaamd `favorites` om de favoriete boeken op te slaan:

```python
favorites = []
```

Deze lijst zal worden gebruikt om de favoriete boeken van de gebruiker op te slaan tijdens de uitvoering van het programma.

## Stap 5: Functies Implementeren

In deze stap ga je verschillende functies implementeren die de kernfunctionaliteit van je applicatie vormen. Elke functie heeft een specifiek doel en vereisten die hieronder worden beschreven.

### 5.1 load_favorites

**Doel**: Laad de favorieten uit een CSV-bestand.

**Vereisten**:

* Open het CSV-bestand in leesmodus met behulp van de `open()` functie in Python.
* Gebruik de `csv.reader()` functie om de inhoud van het bestand te lezen.
* Voeg elk boek toe aan de `favorites` lijst met de `append()` methode.
* Gebruik een `try/except` blok om een `FileNotFoundError` te vangen voor het geval het bestand niet bestaat.
* De functie heeft een standaard parameter `filename='favorieten.csv'`.

### 5.2 search_books

**Doel**: Implementeer een functie om boeken te zoeken met de Open Library API.

**Vereisten**:

* Bestudeer de Open Library API documentatie (https://openlibrary.org/dev/docs/api/search) om te begrijpen hoe je een zoekopdracht moet opstellen. Let op de structuur van de URL en de parameters die je kunt gebruiken om je zoekopdracht te verfijnen.
* Gebruik de `requests.get()` functie om een GET-verzoek te maken naar de API. De URL is "https://openlibrary.org/search.json" en de zoekterm moet worden doorgegeven als een parameter.
* Controleer de statuscode van het responsobject. Als de statuscode 200 is, ga dan verder met de verwerking. Anders, print een foutmelding.
* Gebruik de `json()` methode op het responsobject om de JSON-inhoud te parseren.
* Beperk de uitvoer tot de eerste 10 resultaten door slicing toe te passen op de lijst van boeken.
* Gebruik een `try/except` blok om een `requests.RequestException` te vangen voor het geval er een fout optreedt bij het maken van het verzoek. Print een foutmelding en retourneer een lege lijst in dit geval.

### 5.3 save_books

**Doel**: Schrijf de lijst van favoriete boeken naar een CSV-bestand.

**Vereisten**:

* Open het CSV-bestand in schrijfmodus met behulp van de `open()` functie in Python.
* Gebruik de `csv.writer()` functie om een schrijverobject te maken.
* Voor elk boek in de `favorites` lijst, roep de `writerow()` methode aan op het schrijverobject om de titel en de auteur van het boek in het bestand te schrijven.
* De functie heeft een standaard parameter `filename='favorieten.csv'`.

### 5.4 add_to_favorites

**Doel**: Voeg een boek toe aan de lijst van favorieten.

**Vereisten**:

* Voeg het boekobject toe aan de `favorites` lijst met de `append()` methode.
* Gebruik de `print()` functie om te bevestigen dat het boek is toegevoegd.
* De functie gebruikt standaardwaarden voor de titel en de auteur als deze niet beschikbaar zijn in het boekobject.

### 5.5 remove_from_favorites

**Doel**: Verwijder een boek uit de lijst van favorieten.

**Vereisten**:

* Controleer of de gegeven index geldig is door te controleren of deze binnen het bereik van de `favorites` lijst valt.
* Gebruik de `pop()` methode op de `favorites` lijst om het boek te verwijderen.
* Gebruik de `print()` functie om te bevestigen dat het boek is verwijderd.
* De functie gebruikt standaardwaarden voor de titel en de auteur als deze niet beschikbaar zijn in het boekobject.

### 5.6 show_favorites

**Doel**: Toon alle boeken in de lijst van favorieten.

**Vereisten**:

* Gebruik een `for` loop en de `enumerate()` functie om door de `favorites` lijst te itereren en elk boek met zijn index en titel te printen.
* De functie gebruikt standaardwaarden voor de titel en de auteur als deze niet beschikbaar zijn in het boekobject.

## Stap 6: Hoofdmenu Functie

**Doel**: Creëer een interactieve menu loop voor gebruikersinteractie.

**Vereisten**:

* Implementeer de volgende menu-opties:
    1. Zoek naar boeken: Wanneer deze optie wordt geselecteerd, roep de `search_books` functie aan.
    2. Toon favorieten: Wanneer deze optie wordt geselecteerd, roep de `show_favorites` functie aan.
    3. Voeg toe aan favorieten: Wanneer deze optie wordt geselecteerd, vraag de gebruiker om de index van het boek dat ze willen toevoegen aan hun favorieten en roep de `add_to_favorites` functie aan. Als er geen zoekresultaten beschikbaar zijn, geef dan een foutmelding.
    4. Verwijder uit favorieten: Wanneer deze optie wordt geselecteerd, vraag de gebruiker om de index van het boek dat ze willen verwijderen uit hun favorieten en roep de `remove_from_favorites` functie aan. Als er geen favorieten beschikbaar zijn, geef dan een foutmelding.
    5. Sla favorieten op: Wanneer deze optie wordt geselecteerd, roep de `save_books` functie aan en print een bevestigingsbericht.
    6. Exit: Wanneer deze optie wordt geselecteerd, beëindig het programma.
* Gebruik een `while` loop om het menu continu te tonen totdat de gebruiker ervoor kiest om te stoppen.
* Gebruik de `input()` functie om de keuze van de gebruiker te krijgen.
* Gebruik een reeks `if/elif/else` statements om de juiste functie aan te roepen op basis van de keuze van de gebruiker.
* Implementeer foutafhandeling voor ongeldige gebruikersinvoer.
* De functie maakt gebruik van een variabele `last_search_results` om de resultaten van de laatste zoekopdracht bij te houden.

## Stap 7: Programma Starten

Zorg ervoor dat het programma start door de `load_favorites` en `main_menu` functies aan te roepen wanneer het script direct wordt uitgevoerd:

```python
load_favorites()
main_menu()
```

## Stap 8: Uitvoeren van het Script

Voer het script uit en test de functionaliteit van de Boeken Zoeker. 

Om het script uit te voeren, open je de terminal en navigeer je naar de map waarin je `book_finder.py` hebt opgeslagen. Typ vervolgens het volgende commando in de terminal:

```bash
python main.py
```