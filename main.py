import discord
from discord.ext import commands

TOKEN = " "

bot = commands.Bot(command_prefix= '!')

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} (ID: {bot.user.id})')
    print('-------')


@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

bot.run(TOKEN)