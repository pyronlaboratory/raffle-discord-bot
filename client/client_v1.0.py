import discord
from discord.ext import commands

TOKEN = "?"

client = commands.Bot(command_prefix = '.')

client.run(TOKEN)
