# Python Opdracht: Boeken Zoeker

Deze opdracht heeft als doel om je kennis van Python en externe API's te testen door het bouwen van een applicatie die
gebruik maakt van de Open Library API. Je gaat een programma schrijven dat gebruikers in staat stelt om boeken te
zoeken, favorieten te beheren, en deze op te slaan in een CSV-bestand.

## Vereisten

* Python 3.x
* `requests` library (geïnstalleerd via pip)
* Basiskennis van het werken met API's, JSON en CSV-bestanden in Python.

## Stap 1: Voorbereiding

Installeer de benodigde library via pip:

```bash
pip install requests
```

## Stap 2: Script Setup

Maak een nieuw Python script genaamd book_finder.py.

## Stap 3: Import Statements

Voeg de volgende imports toe aan het begin van je script:

```python
import requests
import csv
```

## Stap 4: Globale Variabele

Definieer een globale lijst genaamd favorites om de favoriete boeken op te slaan:

```python
favorites = []
```

## Stap 5: Functies Implementeren

### 5.1 search_books

**Doel**: Implementeer een functie om boeken te zoeken met de Open Library API.

**Vereisten:**

* Maak een GET-verzoek naar de API met de zoekterm.
* Implementeer foutafhandeling.
* Filter de resultaten op basis van optionele filters als deze zijn opgegeven.
* Beperk de uitvoer tot de eerste 10 resultaten.

### 5.2 save_books

**Doel**: Schrijf de lijst van favoriete boeken naar een CSV-bestand.

**Vereisten:**

Open het CSV-bestand in append-modus.
Schrijf voor elk boek de titel en de auteur in het bestand.

### 5.3 add_to_favorites

**Doel:** Voeg een boek toe aan de lijst van favorieten.

**Vereisten:**

* Voeg het boekobject toe aan de lijst.
* Bevestig de toevoeging aan de gebruiker.

### 5.4 remove_from_favorites

**Doel:** Verwijder een boek uit de lijst van favorieten.

**Vereisten:**

* Controleer of de gegeven index geldig is.
* Verwijder het boek en informeer de gebruiker.

### 5.5 show_favorites

**Doel:** Toon alle boeken in de lijst van favorieten.

**Vereisten:**

* Print elk boek met titel en auteur.

## Stap 6: Hoofdmenu Functie

**Doel:** Creëer een interactieve menu loop voor gebruikersinteractie.

**Vereisten:**

* Toon opties zoals zoeken, toevoegen/verwijderen van favorieten, en opslaan van favorieten.
* Verwerk gebruikerskeuzes en roep de juiste functies aan.
* Implementeer foutafhandeling voor gebruikersinvoer.
Stap 7: Programma Starten
Zorg ervoor dat het programma start door de main_menu functie aan te roepen wanneer het script direct wordt uitgevoerd: