import discord
import os, requests, json, random, asyncio
from pathlib import Path
from dotenv import load_dotenv

env_path = Path('.', '.env')

load_dotenv(dotenv_path=env_path)
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

shutdown_words_head = ["$shutdown", "$Shutdown", "$SHUTDOWN"]
shutdown_words_res = ["See ya!", "Love you, master!", "<3"]
capital_M = ["$murasamemaru", "$murasama"]
command_help = ["$Help", "$help"]
H_pics = ['OwO.png', 'OwO2.png']

def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return(quote)

@client.event
async def on_ready():
    print('Murasame has logged in as {0.user}!'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content

    if msg.startswith('$help'):
        await message.channel.send('Available commands : $quote, $Murasamemaru, $Murasama')
    elif msg.startswith('$Help'):
        await message.channel.send('Available commands : $quote, $Murasamemaru, $Murasama')

    if msg.startswith('Hi'):
        await message.channel.send('Hello, my master!')

    if msg.startswith('Murasame'):
        await message.channel.send('Yes?')
    
    if client.user in message.mentions:
        await message.channel.send('Nya!')

    if msg.startswith('Do you want to stay with me?'):
        await message.channel.send('Well, master...')
        await asyncio.sleep(3)
        await message.channel.send('I am sure we can....')
        await asyncio.sleep(3)
        await message.channel.send('Hehe hehe')

    if any(word in msg for word in capital_M):
        await message.channel.send("Hey! Don't forget to capitalize the M.")

    if msg.startswith('$Murasamemaru'):
        await asyncio.sleep(2)
        await message.channel.send("Hmmph, nice question.")
        await asyncio.sleep(4)
        await message.channel.send("Murasamemaru is a devine sword given to this village by the god.")
        await asyncio.sleep(3)
        await message.channel.send("They say that, this sword have potential to purified the curse spirit")
        await asyncio.sleep(2)
        await message.channel.send("Tho, only selected one can only wield this divine sword!")
        await asyncio.sleep(3)
        await message.channel.send("Maybe it could be you, master!")

    if msg.startswith('$Murasama'):
        await message.channel.send("That sword is from Terraria!")

    if msg.startswith('$quote'):
        quote = get_quote()
        await message.channel.send(quote)

    if any(word in msg for word in shutdown_words_head):
        await message.channel.send(random.choice(shutdown_words_res))
        await client.logout()
    
    if msg.startswith('$18'):
        await message.channel.send(file=discord.File(random.choice(H_pics)))

client.run(TOKEN)
