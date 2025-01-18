import time
import json

from typing import Dict, Optional
from VintedWrapper import VintedWrapper
from VintedScraper import VintedScraper


def search_and_display_new_items(scraper, search_params, seen_items):
    """
    Fonction pour rechercher de nouveaux articles et afficher les résultats non vus.
    Retourne un JSON avec tous les items trouvés.
    """
    print("Requête en cours...")
    items = scraper.search(params=search_params)
    new_items_found = False

    # Liste pour stocker les articles trouvés
    new_items = []

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

            # Ajouter l'article trouvé à la liste
            new_items.append({
                "title": title,
                "url": item_url,
                "image_url": image_url,
                "brand_name": brand_name
            })

    if not new_items_found:
        print("Aucun nouvel article trouvé.")
        return {}

    # Retourner un JSON avec tous les articles trouvés
    return json.dumps({"new_items": new_items}, indent=4)


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
            result_json = search_and_display_new_items(scraper, search_params, seen_items)
            
            # Si des éléments sont trouvés, on les retourne
            if result_json:
                yield result_json            
            time.sleep(interval)
    except KeyboardInterrupt:
        print("Arrêt du programme.")
