import discord
from discord.ext import commands
from discord.ext.commands import Bot
import os

Bot = commands.Bot(command_prefix= "!")

@Bot.event
async def on_ready():
     print('я родился!')

@Bot.command()
async def Hello(ctx):
    author = ctx.message.author
    await ctx.send(f"Hello {author.mention}")

token - os.environ.get("BOT_TOKEN")