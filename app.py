import discord
from discord.ext import commands, tasks
import random
from itertools import cycle
from discord.utils import get
import os

bot = commands.Bot(command_prefix='$')

#BlackRabbit001

@bot.event
async def on_ready():
    status = cycle(['$help', '$info', 'prefix = $'])
    await bot.change_presence(activity=discord.Game(next(status)))
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
	
#client now isn't defined like client but like bot so correct type is: await ctx.send(msg)


sfw_message = '*hint: bot sending sfw commands only into sfw channel! check #sfw if this is sfw channel it is ok*'



@bot.command()
async def greet(ctx):
    await ctx.send(":smiley: :wave: Hello, there! :heart: ")

@bot.command()
async def cat(ctx):
  channel = bot.get_channel(623200282217545728)
  randomlist = ['https://media2.giphy.com/media/JIX9t2j0ZTN9S/200w.webp?cid=790b7611398f812db0b6a71b54e076ca2b47099d66f1e121&rid=200w.webp','https://media0.giphy.com/media/mlvseq9yvZhba/giphy.webp?cid=790b7611398f812db0b6a71b54e076ca2b47099d66fe121&rid=giphy.webp','https://media3.giphy.com/media/13CoXDiaCcCoyk/200.webp?cid=790b7611398f812db0b6a71b54e076ca2b47099d66f1e121&rid=200.webp']
  await channel.send(random.choice(randomlist))
  await ctx.send(sfw_message)


#problem solved - imported random

@bot.command()
async def dog(ctx):
 channel = bot.get_channel(623200282217545728)
 randomlist = ['https://media0.giphy.com/media/4Zo41lhzKt6iZ8xff9/giphy.webp?cid=790b761139768976647e0ed59d69a651fe5147950a7194e9&rid=giphy.webp','https://media.giphy.com/media/21GCae4djDWtP5soiY/giphy.gif','https://media0.giphy.com/media/k2Da0Uzaxo9xe/200.webp?cid=790b761139768976647e0ed59d69a651fe5147950a7194e9&rid=200.webp ', 'https://media.giphy.com/media/QvBoMEcQ7DQXK/giphy.gif ', ' https://media.giphy.com/media/syhXT4VR0D3iM/giphy.gif ', ' https://media.giphy.com/media/U7ZUd5eXfHMgE/giphy.gif ', ' https://media.giphy.com/media/3zlnLYzubrKzGHW9pM/giphy.gif ', ' https://media.giphy.com/media/1ToYwxru1X4Gc/giphy.gif ', ' https://media.giphy.com/media/tR8dmuLBm5OAE/giphy.gif ', ' https://media.giphy.com/media/P7hIImx7r1sas/giphy.gif ']
 await channel.send(random.choice(randomlist))
 await ctx.send(sfw_message)
 
@bot.command()
async def rabbit(ctx):
 channel = bot.get_channel(623200282217545728)
 randomlist = ['https://media.giphy.com/media/N6QMlgXmovw40/giphy.gif ', ' https://media.giphy.com/media/zYKAv43m7MbAI/giphy.gif ', ' https://media.giphy.com/media/8nv5NfqUxWJt6/giphy.gif ', ' https://media.giphy.com/media/10CVvg9noXwPu0/giphy.gif ', ' https://media.giphy.com/media/7MIUT26hrGy76/giphy.gif ', ' https://media.giphy.com/media/laEzcttbkwPzq/giphy.gif ', ' https://media.giphy.com/media/g2n5wagSFzBMk/giphy.gif ', ' https://media.giphy.com/media/14tf9peZdntGxO/giphy.gif ', ' https://media.giphy.com/media/129FklkXsetHl6/giphy.gif ', ' https://media.giphy.com/media/sWyM7JpUxvV9m/giphy.gif ', ' ']
 await channel.send(random.choice(randomlist))
 await ctx.send(sfw_message)
 
 
@bot.command()
async def trump(ctx):
 channel = bot.get_channel(623200282217545728)
 randomlist = ['https://media.giphy.com/media/hPPx8yk3Bmqys/giphy.gif ', ' https://media.giphy.com/media/xTiTnHXbRoaZ1B1Mo8/giphy.gif ', ' https://media.giphy.com/media/E9oadOOmD27jG/giphy.gif ', ' https://media.giphy.com/media/ckIT1yCv6wIyk/giphy.gif ', ' https://media.giphy.com/media/rzKSHEMN0lVkc/giphy.gif ', ' https://media.giphy.com/media/7JI6mrDzbBHJcROiCZ/giphy.gif ', ' https://media.giphy.com/media/9VyXtiyGwPNFPL51sA/giphy.gif ', ' https://media.giphy.com/media/ySFtYLc51D3pK/giphy.gif ', '']
 await channel.send(random.choice(randomlist))
 await ctx.send(sfw_message)
 
@bot.command()
async def info(ctx):
    embed = discord.Embed(title="Website", description="http://rabbit001.cf", color=0xeee657)

    # give info about you here
    embed.add_field(name="Author", value="Blackrabbit001#7046")

    # Shows the number of servers the bot is member of.
    embed.add_field(name="Server count", value=f"189")

    # give users a link to invite thsi bot to their server
    embed.add_field(name="Invite", value="https://discordapp.com/api/oauth2/authorize?client_id=601785377593753601&permissions=8&scope=bot")

    await ctx.send(embed=embed)

bot.remove_command('help')

# NSFW #https://cdn.discordapp.com/attachments/622754558862688256/622755203153920020/Hnet-image_1.gif

@bot.command()
async def nsfw(ctx):
    check_role = get(ctx.message.guild.roles, name='Leader')
    if check_role in ctx.author.roles:
       channel = bot.get_channel(601008621123403776)
       randomlist = ['https://cdn.someecards.com/posts/imagefromios-42-m6fQfC.jpg ', ' https://cdn.someecards.com/posts/imagefromios-39-N59YZ9.jpg ', ' https://cdn.discordapp.com/attachments/622754558862688256/622755203153920020/Hnet-image_1.gif ', '  https://cdn.discordapp.com/attachments/622754558862688256/622755203153920020/Hnet-image_1.gif ', ' https://img-9gag-fun.9cache.com/photo/aZ7ppwW_460swp.webp ', ' https://img-9gag-fun.9cache.com/photo/a5Rr7YN_460swp.webp ', ' https://img-9gag-fun.9cache.com/photo/a2R5mBe_460swp.webp', 'https://img-9gag-fun.9cache.com/photo/aY7LwV7_460swp.webp ', ' https://img-9gag-fun.9cache.com/photo/aV0eXww_460swp.webp ', ' https://img-9gag-fun.9cache.com/photo/avonL0n_460swp.webp ', ' https://img-9gag-fun.9cache.com/photo/aPRWy1Q_460swp.webp ', ' https://img-9gag-fun.9cache.com/photo/avonZ8d_460swp.webp ', ' https://img-9gag-fun.9cache.com/photo/a1RXZeD_460swp.webp ', ' https://img-9gag-fun.9cache.com/photo/a2R5NAD_460swp.webp ', ' https://img-9gag-fun.9cache.com/photo/aO0vqwv_460swp.webp ', ' https://img-9gag-fun.9cache.com/photo/am5zX94_460swp.webp ', ' https://img-9gag-fun.9cache.com/photo/a7wdLmx_460swp.webp ', ' https://img-9gag-fun.9cache.com/photo/aMY91Ax_460swp.webp ', ' https://img-9gag-fun.9cache.com/photo/a0Rj8OO_460swp.webp ', ' https://img-9gag-fun.9cache.com/photo/a0Rj8YB_460swp.webp ', ' https://img-9gag-fun.9cache.com/photo/aV0ez38_460swp.webp ', ' https://img-9gag-fun.9cache.com/photo/aGgDK0K_460swp.webp ']
       await channel.send(random.choice(randomlist))
       await ctx.send('*hint: bot sending nsfw commands only into nsfw channel! check #nsfw*')

 #bot will send message to definned channel iahve to find how someone can it define by command like !nsfw-set-(CHANNEL_ID)

 
 # NSFW

@bot.command()
async def help(ctx):
    embed = discord.Embed(title="__**Commands:**__", description="", color=0xeee657)

    embed.add_field(name="$greet", value="Gives a nice greet message", inline=False)
    embed.add_field(name="$cat", value="Gives a cute cat gif to lighten up the mood.", inline=False)
    embed.add_field(name="$dog", value="Gives a cute dog gif to lighten up the mood", inline=False)
    embed.add_field(name="$rabbit", value="Gives a cute rabbit gif to lighten up the mood", inline=False)
    embed.add_field(name="$trump", value="Gives a funny Donald trump gif", inline=False)
    embed.add_field(name="$info", value="Gives a little info about the bot", inline=False)
    embed.add_field(name="$help", value="Gives this message", inline=False)

    await ctx.send(embed=embed)
 
bot.run(os.getenv('BOT_TOKEN'))
