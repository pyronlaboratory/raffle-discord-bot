import discord
from discord.ext import commands

'''
event handling and using discords' command processing
'''


TOKEN = "?"

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
      print("Powering up the bot")

@client.event
async def on_message(message):
      print("A new message!")
      await client.process_commands(message)

@client.command()
async def ping(ctx):
      await ctx.channel.send("Pong!")

@client.command()
async def echo(ctx, *args):
      output = ""
      for words in args:
            output += words
            output += " "
      await ctx.channel.send(output)

client.run(TOKEN)
