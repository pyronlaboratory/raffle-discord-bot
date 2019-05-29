import discord
from discord.ext import commands

'''
setting up the bot - Command prefix set to (.)
'''

TOKEN = "?"

client = commands.Bot(command_prefix = '.')

client.run(TOKEN)
