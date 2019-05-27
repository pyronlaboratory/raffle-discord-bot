import discord
from discord.ext import commands

TOKEN = "?"

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
      print("Powering up the bot")

@client.event
async def on_message(message):
      channel = message.channel
      if message.content.startswith('.ping'):
            await channel.send('pong')

      if message.content.startswith('.echo'):
            msg = message.content.split()
            output = ""
            for words in msg[1:]:
                  output += words
                  output += " "
            await channel.send(output)
            
client.run(TOKEN)
