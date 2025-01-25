import discord
from dotenv import load_dotenv
import os
import json
import asyncio
import sys

# Ajouter le répertoire parent au chemin de recherche
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import main  # Importer la fonction main
# Charger les variables d'environnement depuis le fichier .env
load_dotenv()

# Accéder à la variable d'environnement
TOKEN_BOT = os.getenv("TOKEN_DISCORD")
ID_SALON_PANT_RALPH_LAUREN = 1330176773668864022  # Remplacer par l'ID du salon où tu veux envoyer les messages

intents = discord.Intents.default()
intents.messages = True  # S'assurer que l'intent pour les messages est activé
intents.message_content = True  # Activer l'intent pour lire le contenu des messages

client = discord.Client(intents=intents)

async def send_item_message(channel, item_data):
    """Envoie un message dans le salon Discord avec les informations des items."""
    for item in item_data['new_items']:
        title = item['title']
        url = item['url']
        image_url = item['image_url']
        brand_name = item['brand_name']

        # Créer un message formaté avec les données
        message = f"**{title}**\n" \
                  f"**Marque:** {brand_name}\n" \
                  f"**Prix:** Voir sur [Vinted]({url})\n" \
                  f"**Image:** {image_url}"

        # Envoyer le message dans le salon spécifié
        await channel.send(message)

@client.event
async def on_ready():
    print(f'Nous avons connecté le bot en tant que {client.user}')

    # Obtenir le salon Discord
    channel = client.get_channel(ID_SALON_PANT_RALPH_LAUREN)

    # Paramètres de recherche
    search_text = "Pantalon de pyjama Ralph Lauren"
    price_from = 20
    price_to = 40
    interval = 30  # Intervalle de 30 secondes entre chaque recherche

    # Appeler la fonction main() pour récupérer les articles
    generator = main(search_text, price_from, price_to, interval)

    # Itérer sur le générateur avec une boucle classique
    try:
        async for listJSON in generator:
            item_data = json.loads(listJSON)  # Convertir le JSON en dictionnaire

            # Afficher proprement chaque article
            print("\nNouvel article détecté :")
            for item in item_data['new_items']:
                print(f"  - **Titre :** {item.get('title', 'N/A')}")
                print(f"    **URL :** {item.get('url', 'N/A')}")
                print(f"    **Image :** {item.get('image_url', 'N/A')}")
                print(f"    **Marque :** {item.get('brand_name', 'N/A')}")
                print(f"    **Prix :** {item.get('price', 'N/A')}")
                print("-" * 40)  # Ligne de séparation pour plus de clarté

            await send_item_message(channel, item_data)  # Envoyer les informations des items
    except KeyboardInterrupt:
        print("Programme interrompu.")

client.run(TOKEN_BOT)
