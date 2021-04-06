### MADE BY GUSBELL ###

import discord
import os, requests, json, random, asyncio

from etc import picture, words, rich

from pathlib import Path
from dotenv import load_dotenv
from vndb_thigh_highs import VNDB, Config
from vndb_thigh_highs.models import VN
from vndb_thigh_highs.models.operators import search
from vndb_thigh_highs.cache import Cache

env_path = Path('.', '.env')

load_dotenv(dotenv_path=env_path)
TOKEN = os.getenv('DISCORD_TOKEN')
SECRET_KEY = os.getenv('SECRET')
VNDB_USER = os.getenv('VNDB_user')
VNDB_PASSWORD = os.getenv('VNDB_pass')

client = discord.Client()

### BOT FUNCTION ###

def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return(quote)

def get_VisualNovel(owo):
    config = Config()
    config.set_login(VNDB_USER, VNDB_PASSWORD)
    config.cache = Cache("etc/VN_Cache.json")
    vndb = VNDB(config=config)
    vn_search = vndb.get_vn(search(VN.title, owo))
    vn = vn_search[0]
    return vn.title

def get_database_stats():
    config = Config()
    config.set_login(VNDB_USER, VNDB_PASSWORD)
    vndb = VNDB(config=config)
    vndb_stats = vndb.dbstats()
    return vndb_stats

### END OF BOT FUNCTION ###

@client.event
async def on_ready():
    print('Murasame has logged in as {0.user}!'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content

    if any(word in msg for word in words.Help_words):
        await message.channel.send('Available commands : ```$quote $Murasamemaru $Murasama $info $18 $vn```')

    if msg.startswith('Hi'):
        await message.channel.send(words.Hello_words)

    if msg.startswith('Murasame'):
        await message.channel.send('Yes?')
    
    if client.user in message.mentions:
        if any(word in msg for word in words.Bad_words):
            await message.channel.send(random.choice(words.Bad_words_response))
        else:
            await message.channel.send('Nya!')
            
    if msg.startswith('Do you want to stay with me?'):
        await message.channel.send('Well, master...')
        await asyncio.sleep(3)
        await message.channel.send('I am sure we can....')
        await asyncio.sleep(3)
        await message.channel.send('Hehe hehe')

    if msg.startswith('Why'):
        await message.channel.send("I don't know")

    if msg.startswith('Sex'):
        await message.channel.send('Sex?')
        await asyncio.sleep(1)
        await message.channel.send('What?')

    if any(word in msg for word in words.Capital_M):
        await message.channel.send("Hey! Don't forget to capitalize the **M**")

    if msg.startswith('Gusbell'):
        await message.channel.send(random.choice(words.Gusbell_words))

    if msg.startswith('OwO'):
        await message.channel.send('OwO')

    if msg.startswith('$Murasamemaru'):
        async with message.channel.typing():
            await asyncio.sleep(2)
            await message.channel.send("Hmmph, nice question")
            await asyncio.sleep(4)
            await message.channel.send("Murasamemaru is a devine sword given to this village by the god")
            await asyncio.sleep(3)
            await message.channel.send("They say that, this sword have potential to purified the curse spirit")
            await asyncio.sleep(2)
            await message.channel.send("Tho, only selected one can only wield this divine sword")
            await asyncio.sleep(5)
            await message.channel.send("Maybe it could be you!")

    if msg.startswith('$Murasama'):
        await message.channel.send("That sword is from Terraria!") 

    if msg.startswith('Recommend me a game'):
        await message.channel.send('https://store.steampowered.com/app/1144400/SenrenBanka/')

    if msg.startswith('$quote'):
        quote = get_quote()
        await message.channel.send(quote)
    
    if msg.startswith('$info'):
        await message.channel.send('Made by Gusbell to store his H-loli pictures collection and do more shitty lolicon stuff | https://github.com/Gusb3ll/murasame-bot')
    
    if msg.startswith('$GusbellRightNow') or msg.startswith('$Gusbell'):
        await message.channel.send('Gusbell is playing Apex legend')

    if msg.startswith('$BechamRightNow'):
        await message.channel.send('Playing MaiMai D====>')
    
    if msg.startswith('$InstinctlyRightNow'):
        await message.channel.send('How do I know?')
        await asyncio.sleep(2)
        await message.channel.send('dumbass')

    if msg.startswith('$MirimRightNow'):
        await message.channel.send('||Mirim is in love <3||')

    if msg.startswith('$Flynny'):
        await message.channel.send('More like')
        await asyncio.sleep(2)
        await message.channel.send('ProjectAce')
        await asyncio.sleep(1)
        await message.channel.send('or ACE')

    if msg.startswith('$18'):
        await message.channel.send(file=discord.File(random.choice(picture.H_pictures), spoiler=True))

    if any(word in msg for word in words.Shutdown_words_start):
        if message.author.id == 297306376542224385:
            await message.channel.send(random.choice(words.Shutdown_words_response))
            await client.logout()
        else:
            async with message.channel.typing():
                await asyncio.sleep(1)
                await message.channel.send("You don't have permission to use this command, only **Gusbell** can!")
    
    if any(word in msg for word in words.Kill_words):
        if message.author.id == 297306376542224385:
            await message.channel.send('AHHHHHH!!!!')
            await client.logout()
        else:
            async with message.channel.typing():
                await asyncio.sleep(2)
                await message.channel.send("You can't kill me!")
                await asyncio.sleep(1)
                await message.channel.send("I'm a ghost!")
        
    if msg.startswith('$vn'):
        if message.content[4:] == "":
            await message.channel.send("You need to give me the visual novel name!")
            await asyncio.sleep(1)
            await message.channel.send('```Example : Senren * Banka```')
        else:
            async with message.channel.typing():
                id = message.content[4:]
                print(id)
                response = get_VisualNovel(id)
                print(response)
                await asyncio.sleep(0.5)
                await message.channel.send(response)

    if msg.startswith('$dbstats'):
        stats = get_database_stats()
        await message.channel.send("Statics for VNDB database :")
        await asyncio.sleep(1)
        await message.channel.send(stats)

    if msg.startswith('$rich'):
        if message.content[6:] == "Google":
            rich.Google()
            await message.channel.send(file=discord.File('rich1.png'))
            await asyncio.sleep(1)
            os.remove("rich1.png")
        elif message.content[6:] == "Tesla":
            rich.Tesla()
            await message.channel.send(file=discord.File('rich2.png'))
            await asyncio.sleep(1)
            os.remove("rich2.png")
        else:
            await message.channel.send("No stock founded")

    if msg.startswith('$join'):
        channel = message.author.voice.channel
        await channel.connect()

    if msg.startswith('$minecraft'):
        await message.chenn
        
client.run(TOKEN)

##############################
