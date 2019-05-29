import discord
from discord.ext import commands

'''
embed message display
'''

TOKEN = "?"

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
      print("Powering up the bot")

@client.command()
async def displayembed(ctx):
      embed_text = discord.Embed(
            title = 'Title Text',
            description = 'This is a textual description',
            colour = discord.Colour.blue()
      )

      embed_text.set_footer(text='designed by www.ronnie94official.co.in')
      embed_text.set_image(url='http://www.ronnie94official.co.in')
      embed_text.set_thumbnail(url='http://www.ronnie94official.co.in')
      embed_text.set_author(
            name='Ronnie'
            icon_url='http://www.ronnie94official.co.in'
      )
      embed_text.add_field(name='stackoverflow', value='[Inline link](https://stackoverflow.com/users/10393917/ronnie)', inline=False)
      embed_text.add_field(name='github', value='https://github.com/ronnielivingsince1994', inline=True)
      embed_text.add_field(name='portfolio', value='http://www.ronnie94official.co.in', inline=True)

      await ctx.channel.send(embed=embed_text)

client.run(TOKEN)
