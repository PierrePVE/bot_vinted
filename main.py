from typing import Dict
from VintedWrapper import VintedWrapper
from VintedScraper import VintedScraper

def main():
    # Configuration de base
    base_url = "https://www.vinted.fr"  # Remplace par le bon domaine pour ton pays, par exemple vinted.com, vinted.it, etc.
    user_agent = None  # Utilise un agent aléatoire si None
    session_cookie = None  # Laisse à None si tu veux que le cookie soit généré automatiquement
    proxies: Dict = {}  # Exemple : {"http": "http://proxy:port", "https": "https://proxy:port"} si nécessaire

    # Initialisation du scraper
    scraper = VintedScraper(baseurl=base_url, agent=user_agent, session_cookie=session_cookie, proxies=proxies)

    # Exemple de recherche d'items
    search_params = {
        "search_text": "casquette",  # Exemple de recherche
        "brand_id": 55,  # Optionnel : ID de la marque (exemple pour Louis Vuitton)
       # "size_id": 207,  # Optionnel : ID de taille
        "price_to": 50,  # Optionnel : Prix maximum
        "currency": "EUR",  # Optionnel : Monnaie
    }

    try:
        # Récupération des résultats de recherche
        items = scraper.search(params=search_params)

        # Affichage des résultats
        print(f"Nombre d'items trouvés : {len(items)}")
        for item in items:
            print(f"Nom : {item.title}, Prix : {item.price} {item.currency}, Lien : {item.url}")
    except RuntimeError as e:
        print(f"Erreur lors de la récupération des items : {e}")


if __name__ == "__main__":
    main()
