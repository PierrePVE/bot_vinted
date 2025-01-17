import requests

def getCategories():
    url = "https://vinted3.p.rapidapi.com/categories"

    headers = {
        "x-rapidapi-key": "bd1b37c9aemsh59620ec548b7985p1597eajsn8ad074fb20b0",
        "x-rapidapi-host": "vinted3.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)

    print(response.json())

def getMaterials():
    url = "https://vinted3.p.rapidapi.com/materials"

    headers = {
        "x-rapidapi-key": "bd1b37c9aemsh59620ec548b7985p1597eajsn8ad074fb20b0",
        "x-rapidapi-host": "vinted3.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)

    print(response.json())    

def getColors():
    url = "https://vinted3.p.rapidapi.com/colors"

    headers = {
        "x-rapidapi-key": "bd1b37c9aemsh59620ec548b7985p1597eajsn8ad074fb20b0",
        "x-rapidapi-host": "vinted3.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)

    print(response.json()) 

def getConditions():
    url = "https://vinted3.p.rapidapi.com/conditions"

    headers = {
        "x-rapidapi-key": "bd1b37c9aemsh59620ec548b7985p1597eajsn8ad074fb20b0",
        "x-rapidapi-host": "vinted3.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)

    print(response.json())    

def testAPI():
    url = "https://vinted3.p.rapidapi.com/getSearch"

    querystring = {"country":"fr","page":"1","keyword":"casquette","brands":"88","order":"newest_first"}

    headers = {
        "x-rapidapi-key": "bd1b37c9aemsh59620ec548b7985p1597eajsn8ad074fb20b0",
        "x-rapidapi-host": "vinted3.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    print(response.json())

def search(country=None, page=None, keyword=None, category=None, colors=None, materials=None, conditions=None, brands=None, order=None, minPrice=None, maxPrice=None):

    url = "https://vinted3.p.rapidapi.com/getSearch"

    # Construire dynamiquement le querystring en ajoutant seulement les paramètres non nuls
    querystring = {}
    if country: querystring["country"] = country
    if page: querystring["page"] = str(page)  # S'assurer que la page est une chaîne de caractères
    if keyword: querystring["keyword"] = keyword
    if category: querystring["category"] = category
    if colors: querystring["colors"] = colors
    if materials: querystring["materials"] = materials
    if conditions: querystring["conditions"] = conditions
    if brands: querystring["brands"] = brands
    if order: querystring["order"] = order
    if minPrice: querystring["minPrice"] = str(minPrice)  # Convertir en chaîne
    if maxPrice: querystring["maxPrice"] = str(maxPrice)  # Convertir en chaîne

    headers = {
        "x-rapidapi-key": "bd1b37c9aemsh59620ec548b7985p1597eajsn8ad074fb20b0",
        "x-rapidapi-host": "vinted3.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    if response.status_code == 200:
        items = response.json()
        if items:
            print("Résultats de recherche :\n")
            for item in items:
                print("-------------------------------------------------")
                print(f"🎯 **Titre** : {item.get('title', 'Non spécifié')}")
                print(f"🔗 **URL** : {item.get('url', 'Non spécifiée')}")
                print(f"🖼 **Image** : {item.get('image', 'Non spécifiée')}")
                print(f"🏷 **Marque** : {item.get('brand', 'Non spécifiée')}")
                print(f"📏 **Taille** : {item.get('size', 'Non spécifiée')}")
                print(f"💰 **Prix** : {item['price']['amount']['amount']} {item['price']['amount']['currency_code']}")
                print(f"💖 **Favoris** : {item.get('favourites', 'Non spécifié')}")
                print("-------------------------------------------------\n")
        else:
            print("Aucun article trouvé pour les critères de recherche.")
    else:
        print(f"Erreur lors de la requête : {response.status_code}")

def main():
    search(
        country="fr",
        page=1,
        order="newest_first"
    )


#main()
#getColors()
#getMaterials()
#getConditions()
testAPI()