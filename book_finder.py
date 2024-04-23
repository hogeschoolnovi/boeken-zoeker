import requests
import csv

# Globale variabele
favorites = []


def search_books(query, filter_type=None, filter_value=None):
    """
    Deze functie zoekt boeken via de Open Library API met optionele filters.
    De functie neemt een zoekopdracht en optionele filtertype en filterwaarde als invoer.
    Het retourneert een lijst van boeken die overeenkomen met de zoekopdracht en voldoen aan de filtercriteria.
    """

    url = "https://openlibrary.org/search.json"
    try:
        response = requests.get(url, params={'q': query})
        response.raise_for_status()
        books = response.json()['docs'][:10]

        if filter_type and filter_value:
            books = [book for book in books if
                     filter_type in book and filter_value.lower() in book[filter_type][0].lower()]

        return books
    except requests.RequestException as e:
        print(f"Er is een fout opgetreden: {e}")
        return []


def save_books(filename='favorieten.csv'):
    """
    Deze functie slaat de favorieten op in een CSV-bestand.
    De functie neemt een bestandsnaam als invoer en schrijft de favoriete boeken naar dit bestand in CSV-formaat.
    """
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        for book in favorites:
            writer.writerow([book.get('title', 'Onbekende titel'), book.get('author_name', ['Onbekende auteur'])[0]])


def add_to_favorites(book):
    """
    Deze functie voegt een boek toe aan de favorietenlijst.
    De functie neemt een boek als invoer en voegt het toe aan de globale lijst van favoriete boeken.
    """
    favorites.append(book)
    print("Boek toegevoegd aan favorieten.")


def remove_from_favorites(index):
    """
    Deze functie verwijdert een boek uit de favorietenlijst.
    De functie neemt een index als invoer en verwijdert het boek op die positie uit de globale lijst van favoriete boeken.
    """
    if 0 <= index < len(favorites):
        removed_book = favorites.pop(index)
        print(
            f"Boek verwijderd: {removed_book.get('title', 'Onbekende titel')} - {removed_book.get('author_name', ['Onbekende auteur'])[0]}")
    else:
        print("Ongeldige index.")


def show_favorites():
    """
    Deze functie toont de favorietenlijst.
    De functie print de titel en auteur van elk boek in de globale lijst van favoriete boeken.
    """
    for idx, book in enumerate(favorites):
        print(f"{idx + 1}. {book.get('title', 'Onbekende titel')} - {book.get('author_name', ['Onbekende auteur'])[0]}")


def main_menu():
    """
    Deze functie toont het hoofdmenu en verwerkt gebruikersinvoer.
    De functie print het menu, neemt de gebruikerskeuze als invoer en roept de bijbehorende functie aan.
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
            filter_type = input("Filter op type (title, author_name, publish_year) of laat leeg: ")
            last_search_results = search_books(query, filter_type if filter_type else None)
            if last_search_results:
                print("\nZoekresultaten:")
                for idx, book in enumerate(last_search_results):
                    print(
                        f"{idx + 1}. {book.get('title', 'Onbekende titel')} - {book.get('author_name', ['Onbekende auteur'])[0]}")
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


# Start van het programma
main_menu()
