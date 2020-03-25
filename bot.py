import discord
from discord.ext import commands
from discord.ext.commands import Bot
import os

Bot = commands.Bot(command_prefix= "&")

@Bot.event
async def on_ready():
     print('я родился!')
     game = discord.Game("💥 &help 💥   by Boom453#1281")
     await Bot.change_presence(status=discord.Status.idle, activity=game)


@Bot.command()
async def Hello(ctx):
    author = ctx.message.author
    await ctx.send(f"Hello {author.mention}")
   
 async defping():
     await Bot.say("Pong")
     

token = os.environ.get('BOT_TOKEN')
Bot.run(str(token))
