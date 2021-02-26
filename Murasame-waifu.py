import discord, os, time
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    channel = client.get_channel(814559928340447243)
    print('Murasame has logged in!')
    await channel.send('Murasame-chan is now online!')


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
        time.sleep(1)
        await message.channel.send('I am sure we can....')
        time.sleep(1)
        await message.channel.send('Hehe hehe')

    if message.content.startswith('!Shutdown'):
        await message.channel.send('Shutting down...')
        await client.logout()

client.run(TOKEN)
