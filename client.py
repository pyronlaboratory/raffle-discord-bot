import discord
from discord.ext import commands

TOKEN = "NTgyNDYyOTgzOTgxMTA1MTU1.XOuLqw.7zxUwjOfL4ElXnyEo57p9bxOv2Y"

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
      print("Powering up the bot")


client.run(TOKEN)
