import os
from random import randrange
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if "val" in message.content.lower():
        pos = [
            "Olá, tudo bem?",
            "Online!",
            "Val a disposição!",
            "Bom dia!",
            "Olá, estou conectada"
        ]
        await message.channel.send(pos[randrange(0, len(pos))])
    if "feliz aniversário" in message.content.lower():
        await message.channel.send("Feliz aniversário pra vc!")
    if "kkk" in message.content.lower():
        await message.channel.send("kkkkkkkkkk")
    if "piada" in message.content.lower():
        piadas = ["O que o pagodeiro foi fazer na igreja?\nfoi cantar pá-god",
              "Por que o Napoleão sempre era chamada para festas?\nPor que ele era bom-na-party",
              "Você conhece a piada do ponêi?\nPô nem eu", "Qual é o rei dos queijos\n o reiqueijão",
              "O que o pato falou pra pata?\nvem quá", "POr que a velhinha não tem relógio\nPor que ela era sem hora",
              "O que a xuxa foi fazer no bar?\nfoi beber ca sasha"]
        await message.channel.send(piadas[randrange(0, len(piadas))])
        await message.channel.send("kkkkkkkkkk")

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Olá {member.name}, bem vindo ao Server mais top!!'
    )

client.run(TOKEN)