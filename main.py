import time
from typing import Dict, Optional
from VintedWrapper import VintedWrapper
from VintedScraper import VintedScraper


def search_and_display_new_items(scraper, search_params, seen_items):
    """
    Fonction pour rechercher de nouveaux articles et afficher les résultats non vus.
    """
    print("Requête en cours...")
    items = scraper.search(params=search_params)
    new_items_found = False

    for item in items:
        item_url = item.url if item.url else 'No URL found'

        if item_url not in seen_items:  # Vérifie si l'article est nouveau
            # Marque l'article comme vu
            seen_items.add(item_url)
            new_items_found = True

            # Extraction des informations souhaitées
            title = item.title
            image_url = item.photos[0].url if item.photos else 'No image available'
            brand_name = item.brand.title if item.brand else 'No brand available'

            # Affichage formaté
            print(f"Nom de l'article: {title}")
            print(f"URL de l'article: {item_url}")
            print(f"URL de l'image: {image_url}")
            print(f"Nom de la marque: {brand_name}")
            print('-' * 50)

    if not new_items_found:
        print("Aucun nouvel article trouvé.")


def main(search_text: str, price_from: Optional[int] = None, price_to: Optional[int] = None, interval: int = 30):
    """
    Fonction principale qui initialise le scraper et exécute la recherche en boucle.

    Args:
        search_text (str): Mots-clés pour la recherche.
        price_from (Optional[int]): Prix minimum (peut être None).
        price_to (Optional[int]): Prix maximum (peut être None).
        interval (int): Intervalle en secondes entre chaque recherche (par défaut 30).
    """
    # Configuration de base
    base_url = "https://www.vinted.fr"  # Remplace par le bon domaine pour ton pays
    user_agent = None  # Utilise un agent aléatoire si None
    session_cookie = None  # Laisse à None si tu veux que le cookie soit généré automatiquement
    proxies: Dict = {}  # Exemple : {"http": "http://proxy:port", "https": "https://proxy:port"} si nécessaire

    # Initialisation du scraper
    scraper = VintedScraper(baseurl=base_url, agent=user_agent, session_cookie=session_cookie, proxies=proxies)

    # Paramètres de recherche
    search_params = {
        "currency": "EUR",
        "search_text": search_text,
    }
    if price_from is not None:
        search_params["price_from"] = price_from
    if price_to is not None:
        search_params["price_to"] = price_to

    # Liste pour stocker les URLs des articles déjà affichés
    seen_items = set()

    # Boucle pour exécuter des requêtes toutes les x secondes
    try:
        while True:
            search_and_display_new_items(scraper, search_params, seen_items)
            time.sleep(interval)
    except KeyboardInterrupt:
        print("Arrêt du programme.")


if __name__ == "__main__":
    # Exemple d'utilisation : ces valeurs peuvent être saisies dynamiquement
    search_text = input("Entrez les mots-clés de recherche : ")

    # Les prix sont optionnels
    price_from = input("Entrez le prix minimum (en euros, laisser vide si non applicable) : ")
    price_to = input("Entrez le prix maximum (en euros, laisser vide si non applicable) : ")

    # Convertir les valeurs en entiers ou les laisser à None si vide
    price_from = int(price_from) if price_from.strip() else None
    price_to = int(price_to) if price_to.strip() else None

    interval = int(input("Entrez l'intervalle en secondes entre les recherches : "))

    main(search_text, price_from, price_to, interval)
