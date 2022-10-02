import discord
from discord.ext import commands
import random
from decouple import config

bot = commands.Bot(command_prefix = "!", case_insensitive = True)

@bot.event
async def on_ready():
    print("Estou conectado como {0.user}" .format(bot))

# Chama atenção a quem chamar palavrâo
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if "palavrão" in message.content:   
        await message.channel.send(f"Por favor, {message.author.name}, não ofender os demais usuários!") 

    await bot.process_commands(message)

# Olá usuário
@bot.command(name = "oi")
async def send_hello(ctx):
    name = ctx.author.name
    response = "Olá, " + name
    await ctx.send(response)


# laçamento de dado
@bot.command(name = "dado")
async def given_away(ctx, number):
    var = random.randint(1, int(number))
    await ctx.send(f"O número que saiu no dado foi {var}")

TOKEN = config("TOKEN")
bot.run(TOKEN)