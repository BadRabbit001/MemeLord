# Work with Python xxx
import discord
from discord.ext import commands, tasks
import os
import asyncio
import random
from itertools import cycle
from discord.utils import get
 
client = commands.Bot(command_prefix='!')
#client = discord.Client()
 
#create an arraylist containing phrases you want your bot to switch through.
status = cycle(['with chocolate'])
 
@client.command()
async def lala(ctx):
    check_role = get(ctx.message.guild.roles, name='Leader')
    if check_role in ctx.author.roles:
        await ctx.send("Yes, you are the leader.")
 
    else:
        await ctx.send("You can't use this")
 
@client.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)
 
@client.command()
async def ban(ctx):
    check_role = get(ctx.message.guild.roles, name='BAN-SQUAD')
    if check_role in ctx.author.roles:
        await ctx.send("https://gifimage.net/wp-content/uploads/2017/07/ban-hammer-gif-14.gif")
    else:
        await ctx.send("You can't use this")
   
@client.event
async def on_ready():
    print("Bot Was Deployed Sucessfully !")
    while True:
        await client.change_presence(game=Game(name='with BadRabbit'))
        await asyncio.sleep(3)
        await client.change_presence(game=Game(name='with Generator'))
        await asyncio.sleep(3)
        await client.change_presence(game=Game(name='this Server', type = 3))
        await asyncio.sleep(3)
        await client.change_presence(game=Game(name='Viktor Sheen', type = 2))
        await asyncio.sleep(3)
 
 
@client.event
async def on_message(message):
    message.content = message.content.lower()
    author = '{0.author.mention}'.format(message)
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return
 
    if message.content.startswith('!hello'):
        msg = 'Hello python {0.author.mention}'.format(message)
        await message.author.send(msg)
 
    if message.content.startswith('!fortnite'):
        randomlist = ['Not in stock!','Not in stock!','Not in stock!']
        msg = 'Hello ' + author + '. Your link: '
        await message.author.send(msg + (random.choice(randomlist)))
       
    if message.content.startswith('?ban'):
        msg = 'https://gifimage.net/wp-content/uploads/2017/07/ban-hammer-gif-14.gif'.format(message)
        await message.channel.send(msg)
               
    if message.content.startswith('!Spotify'):
        randomlist = ['https://filemedia.net/33298/67676','https://filemedia.net/33298/66567','https://filemedia.net/33298/65675','https://filemedia.net/33298/655645','https://link-to.net/33298/89787']
        msg = 'Hello ' + author + '. Your link: '
        await message.author.send(msg + (random.choice(randomlist)))
       
    if message.content.startswith('rabbit'):
        msg = 'https://i.pinimg.com/originals/ea/5b/b4/ea5bb42b167972d4121152caded1bcf4.gif'.format(message)
        await message.channel.send(msg)  
           
    if message.content.startswith('!stock'):
        randomlist = ['visit #how-to-gen for commands','visit #how-to-gen for commands','visit #how-to-gen for commands']
        msg = 'Hello ' + author + '. Your link: '
        await message.author.send(msg + (random.choice(randomlist)))
       
    if message.content.startswith('!nord'):
        randomlist = ['https://link-to.net/33298/23421','https://link-to.net/33298/43452','https://link-to.net/33298/23423']
        msg = 'Hello ' + author + '. Your link: '
        await message.author.send(msg + (random.choice(randomlist)))
       
    if message.content.startswith('!spotify'):
        randomlist = ['https://filemedia.net/33298/67676','https://filemedia.net/33298/66567','https://filemedia.net/33298/65675','https://filemedia.net/33298/655645','https://link-to.net/33298/89787']
        msg = 'Hello ' + author + '. Your link: '
        await message.author.send(msg + (random.choice(randomlist)))
 
    if message.content.startswith('!origin'):
        randomlist = ['https://filemedia.net/33298/23412','https://filemedia.net/33298/212313','https://filemedia.net/33298/212234']
        msg = 'Hello ' + author + '. Your link: '
        await message.author.send(msg + (random.choice(randomlist)))
               
    if message.content.startswith('!hulu'):
        randomlist = ['https://filemedia.net/33298/89089','https://filemedia.net/33298/808098','https://filemedia.net/33298/88798']
        msg = 'Hello ' + author + '. Your link: '
        await message.author.send(msg + (random.choice(randomlist)))
       
    if message.content.startswith('!steam'):
        randomlist = ['Not in stock!    ','Not in stock!    ','Not in stock!    ']
        msg = 'Hello ' + author + '. Your link: '
        await message.author.send(msg + (random.choice(randomlist)))
       
    if message.content.startswith('!udemy'):
        randomlist = ['Not in stock!','Not in stock!','Not in stock!']
        msg = 'Hello ' + author + '. Your link: '
        await message.author.send(msg + (random.choice(randomlist)))
               
    if message.content.startswith('!uplay'):
        randomlist = ['https://link-to.net/33298/23342','https://link-to.net/33298/234213','https://link-to.net/33298/234114','https://link-to.net/33298/424215','https://link-to.net/33298/254252']
        msg = 'Hello ' + author + '. Your link: '
        await message.author.send(msg + (random.choice(randomlist)))
       
    if message.content.startswith('!crunchyroll'):
        randomlist = ['Not in stock!','Not in stock!','Not in stock!']
        msg = 'Hello ' + author + '. Your link: '
        await message.author.send(msg + (random.choice(randomlist)))
               
    if message.content.startswith('!scribd'):
        randomlist = ['Not in stock!','Not in stock!','Not in stock!']
        msg = 'Hello ' + author + '. Your link: '
        await message.author.send(msg + (random.choice(randomlist)))
                       
    if message.content.startswith('!familyowner'):
        randomlist = ['Not in stock','Not in stock','Not in stock']
        msg = 'Hello ' + author + '. Your link: '
        await message.author.send(msg + (random.choice(randomlist)))
                               
    if message.content.startswith('!minecraft'):
        randomlist = ['https://link-to.net/33298/5353','https://link-to.net/33298/345353','https://link-to.net/33298/56356']
        msg = 'Hello ' + author + '. Your link: '
        await message.author.send(msg + (random.choice(randomlist)))
       
    if message.content.startswith('!help'):
        await message.author.send("Check #how_to_gen")
       
       
    if message.content.startswith('!purge'):
        args = message.content.split(" ")
        a = int(args[1])
        await message.channel.purge(limit=a)
    await client.process_commands(message)
   
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    change_status.start()
 
@tasks.loop(seconds=5)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))
 
client.run(os.getenv('BOT_TOKEN'))
