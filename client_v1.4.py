import discord
from discord.ext import commands

import datetime as dt
from datetime import datetime

TOKEN = "?"

#setting date configurations
delta = dt.timedelta(days=1)
last = datetime.now() - delta

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
      print("Powering up the bot")


@client.command(pass_context=True)
async def logs(ctx, amount=100,):
      channel = ctx.message.channel
      messages = []
      print('Getting logs from {}'.format(last))
      async for message in channel.history(limit=int(amount), after=last):
            messages.append(message.content)
            
      print(messages)
      
      
client.run(TOKEN)
