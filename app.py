import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()

token = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.all()
intents.messages = True
intents.members = True

bot = commands.Bot(command_prefix=',', intents=intents)

@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

@bot.command()
async def wa(ctx):
    await ctx.send('Deja de tirar cartas puto')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if "hello" in message.content.lower():
        await message.channel.send(f'Hello {message.author.name}!')
    
    await bot.process_commands(message)

bot.run(token)
