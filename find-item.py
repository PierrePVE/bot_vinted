import requests

url = "https://vinted3.p.rapidapi.com/getSearch"

querystring = {"country":"fr","page":"1","keyword":"pantalon pyjama","brands":"88","order":"newest_first","minPrice":"0","maxPrice":"20"}

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