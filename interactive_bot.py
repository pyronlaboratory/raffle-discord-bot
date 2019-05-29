import discord
from discord.ext import commands
import asyncio

TOKEN = "?"

RAFFLE=""
ENTRANT_FIRST_NAME=""
ENTRANT_LAST_NAME=""
ENTRANT_EMAIL_ID=""
ENTRANT_SHOE_SIZE=""
NUMBER_OF_THREADS=""

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
      print("Powering up the bot")
      
@client.event
async def on_message(message):
      #Avoid replying to bot
      if message.author == client.user:
            return
      
      #Initiating the chat with the bot
      if message.content.startswith('Hi'):
            
            channel = message.channel
            
            msg = 'Hello {0.author.mention}'.format(message)
            msg += ", I'm Raffle Bot! I'd be assisting you with the raffle entries.\n Do you wish to proceed? (Y/N)"
            await channel.send(msg)

            #Waiting for user response to proceed
            def check_1(m):
                  if m.channel == channel:
                        return True

            msg = await client.wait_for('message', check=check_1)
            
            if msg.content != 'Y' and msg.content != 'N' and msg.content != 'Hi':
                  await channel.send("That seems to be an invalid response, {0.author.mention}. Why don't you start again afresh with a Hi!".format(msg))

            elif msg.content == 'Y':
                  msg = "That's awesome, {0.author.mention}. Lets get you in a raffle!".format(msg)
                  msg += "\nHere is a list of the raffles we support, please pick a number\n"
                  msg += "1. One Block Down\n"
                  msg += "2. Footpatrol\n"
                  await channel.send(msg)

                  def check_2(m):
                        if m.channel == channel:
                              return True

                  msg = await client.wait_for('message', check=check_2)
                  
                  
                  if msg.content != '1' and msg.content != '2':
                        await channel.send("That seems to be an invalid response, {0.author.mention}. Why don't you start again afresh with a Hi!".format(msg))

                  elif msg.content == '1':
                        
                        #Store Raffle preference
                        RAFFLE="OneBlockDown"
                        print(RAFFLE)
                        
                        msg = "Great, could you help me with some details {0.author.mention}?".format(msg)
                        msg += "\nCould you please enter your first name?"
                        await channel.send(msg)

                        def check_3(m):
                              if m.channel == channel:
                                    return True

                        msg = await client.wait_for('message', check=check_3)

                        #Store first name
                        ENTRANT_FIRST_NAME = msg.content
                        print(ENTRANT_FIRST_NAME)

                        msg = "That's looks like a pretty nice first name, {0.author.mention}".format(msg)
                        msg += "\nCould you please enter your last name?"
                        await channel.send(msg)

                        def check_4(m):
                              if m.channel == channel:
                                    return True

                        msg = await client.wait_for('message', check=check_4)

                        #Store last name
                        ENTRANT_LAST_NAME = msg.content
                        print(ENTRANT_LAST_NAME)

                        msg = "Now that we have your name, {0.author.mention}".format(msg)
                        msg += "\nCould you please enter an email address you wish to use for the raffle?"
                        await channel.send(msg)

                        def check_5(m):
                              if m.channel == channel:
                                    return True

                        msg = await client.wait_for('message', check=check_5)

                        #Store email address
                        ENTRANT_EMAIL_ID = msg.content
                        print(ENTRANT_EMAIL_ID)

                        msg = "What shoe size do you prefer, {0.author.mention}".format(msg)
                        msg += "\nWe follow US standards, so please enter accordingly!"
                        await channel.send(msg)

                        def check_6(m):
                              if m.channel == channel:
                                    return True

                        msg = await client.wait_for('message', check=check_6)

                        #Store shoe size
                        ENTRANT_SHOE_SIZE = msg.content
                        print(ENTRANT_SHOE_SIZE)

                        msg = "That's Great, {0.author.mention}".format(msg)
                        msg += "\nOne final detail, how many entries would you like to have?!\n You can have a max. of 10 "
                        await channel.send(msg)

                        def check_7(m):
                              if m.channel == channel:
                                    return True

                        msg = await client.wait_for('message', check=check_7)

                        #Store number of threads
                        NUMBER_OF_THREADS = msg.content
                        print(NUMBER_OF_THREADS)

                        msg = "That's it {0.author.mention}!".format(msg)
                        msg += ", We wish you good luck! "
                        await channel.send(msg)

                        

                  elif msg.content == '2':
                        
                        #Store Raffle preference
                        RAFFLE="Footpatrol"
                        print(RAFFLE)
                        
                        msg = "Great, could you help me with some details {0.author.mention}?".format(msg)
                        msg += "\nCould you please enter your first name?"
                        await channel.send(msg)

                        def check_8(m):
                              if m.channel == channel:
                                    return True

                        msg = await client.wait_for('message', check=check_8)

                        #Store first name
                        ENTRANT_FIRST_NAME = msg.content
                        print(ENTRANT_FIRST_NAME)

                        msg = "That's looks like a pretty nice first name, {0.author.mention}".format(msg)
                        msg += "\nCould you please enter your last name?"
                        await channel.send(msg)

                        def check_9(m):
                              if m.channel == channel:
                                    return True

                        msg = await client.wait_for('message', check=check_9)

                        #Store last name
                        ENTRANT_LAST_NAME = msg.content
                        print(ENTRANT_LAST_NAME)

                        msg = "Now that we have your name, {0.author.mention}".format(msg)
                        msg += "\nCould you please enter an email address you wish to use for the raffle?"
                        await channel.send(msg)

                        def check_10(m):
                              if m.channel == channel:
                                    return True

                        msg = await client.wait_for('message', check=check_10)

                        #Store email address
                        ENTRANT_EMAIL_ID = msg.content
                        print(ENTRANT_EMAIL_ID)

                        msg = "What shoe size do you prefer, {0.author.mention}".format(msg)
                        msg += "\nWe follow US standards, so please enter accordingly!"
                        await channel.send(msg)

                        def check_11(m):
                              if m.channel == channel:
                                    return True

                        msg = await client.wait_for('message', check=check_11)

                        #Store shoe size
                        ENTRANT_SHOE_SIZE = msg.content
                        print(ENTRANT_SHOE_SIZE)

                        msg = "That's Great, {0.author.mention}".format(msg)
                        msg += "\nOne final detail, how many entries would you like to have?!\n You can have a max. of 10 "
                        await channel.send(msg)

                        def check_12(m):
                              if m.channel == channel:
                                    return True

                        msg = await client.wait_for('message', check=check_12)

                        #Store number of threads
                        NUMBER_OF_THREADS = msg.content
                        print(NUMBER_OF_THREADS)

                        msg = "That's it {0.author.mention}".format(msg)
                        msg += ", We wish you good luck! "
                        await channel.send(msg)

            elif msg.content == 'N':
                  await channel.send("Maybe someother day then, {0.author.mention}. Good day!".format(msg))

client.run(TOKEN)
