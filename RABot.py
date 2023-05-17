import discord
import logging
from discord.ext import commands
import os
from dotenv import load_dotenv
from funcs.IndexRet import qna
from utils.utils import generate_directory_structure

# Load environment variables from .env file
load_dotenv() 
DISCORD_BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")

COURSES = [x[0] for x in generate_directory_structure('./storage')]

client = discord.Client(intents=discord.Intents.default())
# handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

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
        for course in COURSES:
            if course in message.content:
                await message.channel.send(qna(course, message.content[13:-23]))
                break


# client.run(DISCORD_BOT_TOKEN, log_handler=handler)
client.run(DISCORD_BOT_TOKEN)
