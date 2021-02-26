import discord
from discord.ext import commands

TOKEN = "ODE0Nzk1NDc1NTIwOTc4OTU0.YDjDaw.2Zn6OecEIrnmvQ28oKmRntNI-Tg"

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
