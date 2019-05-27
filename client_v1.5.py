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
async def clear(ctx, amount=100,):
      await ctx.channel.purge(limit = int(amount))
      await ctx.channel.send('Messages deleted!')
      
      
client.run(TOKEN)
