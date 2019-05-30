import json

import discord
from discord.ext import commands

import datetime as dt
from datetime import datetime

'''
discord-raffle-bot:
version: 1.0
nature: private

Ronnie's Creative Lab Inc:
server invite: **************

'''


#loading token.json for discord bot
TOKEN=""

with open('token.json') as json_file:  
    data = json.load(json_file)
    TOKEN = data['TOKEN']


#setting date configurations
delta = dt.timedelta(hours=1)
last = datetime.now() - delta


client = commands.Bot(command_prefix='.')

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="Raffle"))
    print("Powering up the bot")
    print('\nBot_Name: {}\nBot_ID: {}\nConnected Servers: {}\n'.format(
        client.user.name,  #Bot Name
        client.user.id,         #Bot ID
        len(client.guilds))  #Number of servers currently connected to
    )


@client.event
async def on_message(message):
    channel = message.channel

    if message.content.startswith('.collect_applications'):
        async for message in channel.history(after=last):
            if message.content == "":
                application_form = message.embeds
                for details in application_form:
                    print(details.description)
                    
        await channel.send('Applications Collected!')
        
    
    if message.content.startswith('.collect_links'):
        async for message in channel.history(after=last):
            if message.content == "":
                posted_links = message.embeds
                for link in posted_links:
                    print(link.field)
                    
        await channel.send('Links Collected!')

            
client.run(TOKEN)
