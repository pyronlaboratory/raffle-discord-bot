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

TOKEN=""

#loading token.json for discord bot
with open('token.json') as json_file:  
    data = json.load(json_file)
    TOKEN = data['token']

#setting datetime configurations
delta = dt.timedelta(hours=1)
last = datetime.now() - delta

#store results
def store_links(links):
    file=open("links.txt","a+")
    file.write(links)
    file.close()

client = commands.Bot(command_prefix='.')

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="Raffle"))
    print("Powering up the bot")
    print('\nBot_Name: {}\nBot_ID: {}\nConnected Servers: {}\n'.format(
        client.user.name, #Bot Name
        client.user.id, #Bot ID
        len(client.guilds))  #Number of servers currently connected to
    )


@client.command()
async def apply(ctx):
    channel = ctx.message.author
    embed_text = discord.Embed(
            colour = discord.Colour.blue()
    )
    embed_text.add_field(name='Raffle Entrance', value="[Click me, I'll take you to the raffle fair!](https://localhost)", inline=False)
    embed_text.set_footer(text='designed by www.ronnie94official.co.in')
    await channel.send(embed=embed_text)
    
    
@client.event
async def on_message(message):
    
    global last
    channel = message.channel        
    
    if message.content.startswith('.collect_links') and message.author is "Mr. Smee#0000":
        print(message.author)
        async for message in channel.history(before=last):
            if message.content == "":
                posted_links = message.embeds
                for link in posted_links:
                    for field in link.fields:
                        store_links(str(field))
                        store_links("\n\n")
                   
        await channel.send('Links Collected!')
    await client.process_commands(message)
       
client.run(TOKEN)
