# Stap 3: Import Statements
import requests
import csv

# Stap 4: Globale Variabele
favorites = []

# Stap 5.1: Load favorites (functie)
def load_favorites(filename='favorieten.csv'):
    """
    Deze functie laadt de favorieten uit een CSV-bestand.
    De functie leest de favoriete boeken vanuit het bestand en voegt ze toe aan de globale lijst van favoriete boeken.
    """
    try:
        with open(filename, mode='r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                if row:  # Zorg ervoor dat lege regels worden genegeerd
                    book = {'title': row[0], 'author_name': [row[1]]}
                    favorites.append(book)
    except FileNotFoundError:
        print("Geen bestaand favorietenbestand gevonden. Een nieuwe zal worden aangemaakt bij het opslaan.")


# Stap 5.2: Search books (functie)
def search_books(query):
    """
    Deze functie zoekt boeken via de Open Library API. De functie neemt een zoekopdracht als invoer en retourneert
    een lijst van boeken die overeenkomen met de zoekopdracht.
    """
    url = "https://openlibrary.org/search.json"
    try:
        response = requests.get(url, params={'q': query})
        if response.status_code == 200:
            books = response.json()['docs'][:10]
            return books
        else:
            print(f"Er is een fout opgetreden: {response.status_code}")
            return []
    except requests.RequestException as e:
        print(f"Er is een fout opgetreden: {e}")
        return []


# Stap 5.3: Save books (functie)
def save_books(filename='favorieten.csv'):
    """
    Deze functie slaat de favorieten op in een CSV-bestand.
    """
    with open(filename, mode='w', newline='') as file:  # Gebruik 'w' om het bestand te overschrijven
        writer = csv.writer(file)
        for book in favorites:
            writer.writerow([book.get('title', 'Onbekende titel'), book.get('author_name', ['Onbekende auteur'])[0]])


# Stap 5.4: Add to favorites (functie)
def add_to_favorites(book):
    """
    Deze functie voegt een boek toe aan de favorietenlijst.
    """
    favorites.append(book)
    print("Boek toegevoegd aan favorieten.")


# Stap 5.5: Remove from favorites (functie)
def remove_from_favorites(index):
    """
    Deze functie verwijdert een boek uit de favorietenlijst.
    """
    if 0 <= index < len(favorites):
        removed_book = favorites.pop(index)
        print(
            f"Boek verwijderd: {removed_book.get('title', 'Onbekende titel')} - {removed_book.get('author_name', ['Onbekende auteur'])[0]}")
    else:
        print("Ongeldige index.")


# Stap 5.6: Show favorites (functie)
def show_favorites():
    """
    Deze functie toont de favorietenlijst.
    """
    for idx, book in enumerate(favorites):
        print(f"{idx + 1}. {book.get('title', 'Onbekende titel')} - {book.get('author_name', ['Onbekende auteur'])[0]}")


# Stap 6: Main menu (functie)
def main_menu():
    """
    Deze functie toont het hoofdmenu en verwerkt gebruikersinvoer.
    """
    last_search_results = []
    while True:
        print("\nWelkom bij de Boeken Zoeker!")
        print("1. Zoek naar boeken")
        print("2. Toon favorieten")
        print("3. Voeg toe aan favorieten")
        print("4. Verwijder uit favorieten")
        print("5. Sla favorieten op")
        print("6. Exit")
        choice = input("Maak uw keuze (1-6): ")

        if choice == '1':
            query = input("Voer de zoekterm in: ")
            last_search_results = search_books(query)
            if last_search_results:
                print("\nZoekresultaten:")
                for idx, book in enumerate(last_search_results):
                    print(
                        f"{idx + 1}. {book.get('title', 'Onbekende titel')} - {book.get('author_name', [
                            'Onbekende auteur'])[0]}")
            else:
                print("Geen resultaten gevonden.")
        elif choice == '2':
            print("\nFavorieten:")
            show_favorites()
        elif choice == '3':
            if last_search_results:
                index = int(input("Voer de index van het boek in om toe te voegen: ")) - 1
                if 0 <= index < len(last_search_results):
                    add_to_favorites(last_search_results[index])
                else:
                    print("Ongeldige index.")
            else:
                print("Geen zoekresultaten beschikbaar. Voer eerst een zoekopdracht uit.")
        elif choice == '4':
            if favorites:
                index = int(input("Voer de index van het boek in om te verwijderen: ")) - 1
                remove_from_favorites(index)
            else:
                print("Geen favorieten beschikbaar. Voeg eerst een favoriet toe.")
        elif choice == '5':
            save_books()
            print("Favorieten zijn opgeslagen.")
        elif choice == '6':
            print("Bedankt voor het gebruiken van de Boeken Zoeker. Tot ziens!")
            break
        else:
            print("Ongeldige keuze, probeer het opnieuw.")


# Stap 7: Laad favorieten bij het starten van het programma
load_favorites()

# Stap 8: Start van het programma
main_menu()
