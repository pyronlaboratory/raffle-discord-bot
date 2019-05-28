import asyncio
import discord
from discord.ext import commands
from itertools import cycle

TOKEN = "?"

client = commands.Bot(command_prefix = '.')
status = ['Resting','Crawling']

@client.event
async def on_ready():
      print("Powering up the bot")


@client.command()
async def logout(ctx):
      await client.logout()
      
      
client.run(TOKEN)
