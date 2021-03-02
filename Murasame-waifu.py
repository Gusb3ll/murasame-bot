import discord
import os, requests, json, random, asyncio, http.client, textwrap, lorem
from pathlib import Path
from dotenv import load_dotenv

env_path = Path('.', '.env')

load_dotenv(dotenv_path=env_path)
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

shutdown_words_head = ["$shutdown", "$Shutdown", "$SHUTDOWN"]
shutdown_words_res = ["See ya!", "Goodbye, master", "See you later, master", "Well, goodbye then"]
capital_M = ["$murasamemaru", "$murasama"]
command_help = ["$Help", "$help"]
H_pics = ['OwO.png', 'OwO2.png', 'OwO3.png', 'ayase2.png', 'ayase3.png', 'ayase4.png', 'ayase5.png', 'ayase6.png', 
          'hazuki1.png', 'mayu1.png', 'mayu2.png', 'mayu3.png', 'Mako1.png', 'Mako2.png', 'Mura1.png', 'Mura2.png', 'Mura3.png',
          'Mura4.png', 'Mura5.png']
gusbell_words = ["Gusbell is a god", "Hey! He is my **real** master", "Why are you talking about him?"]

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
        await message.channel.send('Available commands : ```$quote $Murasamemaru $Murasama $info $18```')
    elif msg.startswith('$Help'):
        await message.channel.send('Available commands : ```$quote $Murasamemaru $Murasama $info $18```')
    elif msg.startswith('$HELP'):
        await message.channel.send('Available commands : ```$quote $Murasamemaru $Murasama $info $18```')

    if msg.startswith('Hi'):
        await message.channel.send('Hello, my master!')

    if msg.startswith('Murasame'):
        await message.channel.send('Yes?')
    
    if client.user in message.mentions:
        if "Shut up" in message.content:
            await message.channel.send('No you, shut up')
        elif "Fuck you" in message.content:
            await message.channel.send('No, you go fuck yourself')
        elif "fuck you" in message.content:
            await message.channel.send('No, you go fuck yourself')
        elif "nigger" in message.content:
            await message.channel.send('bruh')
        else:
            await message.channel.send('Nya!')
            
    if msg.startswith('Do you want to stay with me?'):
        await message.channel.send('Well, master...')
        await asyncio.sleep(3)
        await message.channel.send('I am sure we can....')
        await asyncio.sleep(3)
        await message.channel.send('Hehe hehe')

    if any(word in msg for word in capital_M):
        await message.channel.send("Hey! Don't forget to capitalize the **M**")

    if msg.startswith('Gusbell'):
        await message.channel.send(random.choice(gusbell_words))

    if msg.startswith('OwO'):
        await message.channel.send('OwO')

    if msg.startswith('o/'):
        await message.channel.send('\o/ \o/')

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

    if msg.startswith('$quote'):
        quote = get_quote()
        await message.channel.send(quote)
    
    if msg.startswith('$info'):
        await message.channel.send('Made by Gusbell to store his H-loli pictures collection and do more shitty lolicon stuff | https://github.com/Gusb3ll/murasame-bot')
    
    if msg.startswith('$GusbellRightNow'):
        await message.channel.send('Gusbell is fapping')

    if msg.startswith('$18'):
        await message.channel.send(file=discord.File(random.choice(H_pics), spoiler=True))

    if any(word in msg for word in shutdown_words_head):
        if message.author.id == 297306376542224385:
            await message.channel.send(random.choice(shutdown_words_res))
            await client.logout()
        else:
            await message.channel.send("You don't have permission to use this command, only **Gusbell** can!")
    
    if msg.startswith('$kill'):
        if message.author.id == 297306376542224384:
            await message.channel.send('AHHHHHH!!!!')
            await client.logout()
        else:
            async with message.channel.typing():
                await message.channel.send("You can't kill me!")
                await asyncio.sleep(2)
                await message.channel.send("I'm a ghost!")

client.run(TOKEN)
