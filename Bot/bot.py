import discord
from discord.ext import commands
from dotenv import dotenv_values
intents = discord.Intents.default()
intents.message_content = True
config = dotenv_values(".env")

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'Bot has logged in as {client.user}')


@bot.command()
async def check(ctx):
    # allow the user to check which concerts and sections they are looking at
    pass
@bot.command
async def add(ctx):
    # add <link> <section(s)>
    # sections are space separated
    pass

@bot.command
async def remove(ctx):
    # remove <index>
    # index based on the check command
    pass


client.run(config["DISCORD_TOKEN"])