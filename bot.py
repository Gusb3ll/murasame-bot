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

    if message.content.startswith('Hi'):
        await message.channel.send('Hello, my master!')

    if message.content.startswith('Murasame'):
        await message.channel.send('Yes?')

    if message.content.startswith('Do you want to stay with me?'):
        await message.channel.send('Well, master...')
        await message.channel.send('I am sure we can....')
        await message.channel.send('Hehe hehe')

client.run(TOKEN)
