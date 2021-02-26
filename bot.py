import discord, os
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print('Murasame has logged in!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!a'):
        await message.channel.send('Hello, my master!')

client.run(TOKEN)
