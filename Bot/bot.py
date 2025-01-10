import discord
from dotenv import dotenv_values
intents = discord.Intents.default()
intents.message_content = True
config = dotenv_values(".env")

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'Bot has logged in as {client.user}')

@client.event
async def on_message(message):

    # ignore own message
    if message.author == client.user:
        return

    

client.run(config["DISCORD_TOKEN"])