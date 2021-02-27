import discord, os, time, requests, json, random
from pathlib import Path
from dotenv import load_dotenv

env_path = Path('.', '.env')

load_dotenv(dotenv_path=env_path)
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

shutdown_words_head = ["!shutdown", "!Shutdown", "!SHUTDOWN"]
shutdown_words_res = ["See ya!", "Love you, master!", "<3"]


def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return(quote)

@client.event
async def on_ready():
    channel = client.get_channel(814559928340447243)
    print('Murasame has logged in as {0.user}!'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content

    if msg.startswith('$help'):
        await message.channel.send('Available commands : $quote')

    if msg.startswith('Hi'):
        await message.channel.send('Hello, my master!')

    if msg.startswith('Murasame'):
        await message.channel.send('Yes?')
    
    if msg.startswith('@Murasame'):
        await message.channel.send('Nya!')

    if msg.startswith('Do you want to stay with me?'):
        await message.channel.send('Well, master...')
        time.sleep(1)
        await message.channel.send('I am sure we can....')
        time.sleep(1)
        await message.channel.send('Hehe hehe')

    if msg.startswith('$quote'):
        quote = get_quote()
        await message.channel.send(quote)

    if any(word in msg for word in shutdown_words_head):
        await message.channel.send(random.choice(shutdown_words_res))
        await client.logout()

client.run(TOKEN)
