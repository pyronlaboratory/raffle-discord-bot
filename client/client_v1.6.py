import asyncio
import discord
from discord.ext import commands
from itertools import cycle

'''
handling background events - change bot status
'''

TOKEN = "?"

client = commands.Bot(command_prefix = '.')
status = ['Rest','Crawl']

async def change_status():
      await client.wait_until_ready()
      msgs = cycle(status)

      while not client.is_closed:
            current_status = next(msgs)
            await client.change_presence(activity=discord.Game(name=current_status))
            await asyncio.sleep(5)

@client.event
async def on_ready():
      #await client.change_presence(activity=discord.Game(name="Live"))
      print("Powering up the bot")
      print('\nBot_Name: {}\nBot_ID: {}\nConnected Servers: {}\n'.format(
        client.user.name,  #Bot Name
        client.user.id,         #Bot ID
        len(client.guilds))  #Number of servers currently connected to
    )
      

@client.command()
async def logout(ctx):
      await client.logout()
      

client.loop.create_task(change_status()) 
client.run(TOKEN)
