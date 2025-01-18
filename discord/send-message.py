import discord
from dotenv import load_dotenv
import os
import discord

# Charger les variables d'environnement depuis le fichier .env
load_dotenv()

# Accéder à la variable d'environnement
TOKEN_BOT = os.getenv("TOKEN_DISCORD")

intents = discord.Intents.default()
intents.messages = True  # S'assurer que l'intent pour les messages est activé
intents.message_content = True  # Activer l'intent pour lire le contenu des messages

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Nous avons connecté le bot en tant que {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # Débogage pour vérifier si le message est bien reçu
    print(f"Message reçu : {message.content} dans le canal {message.channel.name}")

    # Vérifier si le message provient d'un serveur (guild)
    if message.guild:  # Si le message vient d'un serveur
        if message.content.startswith("!hello"):
            await message.channel.send(f"Hello {message.author.name}, welcome to {message.guild.name}!")

client.run(TOKEN_BOT)