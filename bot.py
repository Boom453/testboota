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

Bot.run("NjkxMjI4MjgyMTI5MjE5NTk0.Xnn9MA.UmHdUpYZP0y5x3RFzU7EwdDfIUs")
