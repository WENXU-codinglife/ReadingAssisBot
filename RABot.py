import discord
import logging
from discord.ext import commands
import os
from dotenv import load_dotenv
from IndexRet import qna

# Load environment variables from .env file
load_dotenv() 
DISCORD_BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")

client = discord.Client(intents=discord.Intents.default())
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    #check if the author of the message is the same as the bot itself.
    if message.author == client.user:
        return 

    if message.content.startswith('Hello'):
        print(message.content)
        await message.channel.send('How can I help you?')

    if message.content.startswith('Question:'):
        await message.channel.send(qna(message.content[6:-23]))

client.run(DISCORD_BOT_TOKEN, log_handler=handler)


