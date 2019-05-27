import discord
from discord.ext import commands

TOKEN = "NTgyNDYyOTgzOTgxMTA1MTU1.XOuLqw.7zxUwjOfL4ElXnyEo57p9bxOv2Y"

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
      print("Powering up the bot")

@client.event
async def on_message(message):
      author = message.author
      content = message.content
      print("{} texted: {}".format(author, content))

@client.event
async def on_message_delete(message):
      author = message.author
      content = message.content
      channel = message.channel
      await channel.send('{} deleted this thread: {}'.format(author, content))


client.run(TOKEN)
