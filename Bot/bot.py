import discord
from discord.ext import commands
from dotenv import dotenv_values




# Setup the bot
intents = discord.Intents.default()
intents.message_content = True
config = dotenv_values(".env")
channelName = "tm_alert"
client = commands.Bot(command_prefix='!',intents=intents)








@client.event
async def on_ready():
    print(f'Bot has logged in as {client.user}')


@client.command()
async def check(ctx):
    # allow the user to check which concerts and sections they are looking at

    if ctx.channel.name == channelName:
        print(ctx.author.id)
        await ctx.channel.send("Hello")

@client.command()
async def add(ctx,args):
    # add <link> <section(s)>
    # sections are space separated
    pass

@client.command()
async def remove(ctx,args):
    # remove <index>
    # index based on the check command
    pass






client.run(config["DISCORD_TOKEN"])