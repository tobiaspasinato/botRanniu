import discord
import requests
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
async def pokeinfo(ctx, nombre : str):
    try:
        response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{nombre.lower()}')
        if response.status_code == 200:
            data = response.json()
            
            # Crear embed
            embed = discord.Embed(
                title=f"Información de {data['name'].capitalize()}",
                color=0x3498db
            )
            
            # Agregar campos
            embed.add_field(name="Altura", value=f"{data['height']/10} m", inline=True)
            embed.add_field(name="Peso", value=f"{data['weight']/10} kg", inline=True)
            embed.add_field(name="ID", value=data['id'], inline=True)
            
            # Agregar imagen
            embed.set_image(url=data['sprites']['other']['official-artwork']['front_default'])
            
            # Imagen pequeña (opcional)
            embed.set_thumbnail(url=data['sprites']['front_default'])
            
            await ctx.send(embed=embed)
        else:
            await ctx.send('Pokemon no encontrado.')
    except Exception as e:
        await ctx.send(f'Error al obtener información: {str(e)}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if "hello" in message.content.lower():
        await message.channel.send(f'Hello {message.author.name}!')
    
    await bot.process_commands(message)

bot.run(token)
