import os
from random import randrange
import discord
from dotenv import load_dotenv
from web_func import scrapping, previsao_do_tempo, covid_cases
from time import sleep
import schedule

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

def ProgramaDaVal():
    return scrapping()

def ProgramaDaVal2():
    sleep(20)
    return previsao_do_tempo()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    canal = client.get_channel(int(os.getenv("ID_CANAL")))
    #await canal.send(f"Olá a todos, Val preparada pra mais um dia de trabalho ^-^")
    schedule.every().day.at("10:00").do(ProgramaDaVal)
    schedule.every().day.at("10:00").do(ProgramaDaVal2)

@client.event
async def on_member_join(member):
    print("novo membro")
    svg = open("img/member_join.svg", 'r')
    content = svg.read()
    content.replace("Member Name", member.name)
    svg2 = open("img/member_join.svg", "w")
    svg2.write(content)
    canal = client.get_channel(int(os.getenv("ID_CANAL")))
    await canal.send(f"Olá {member.mention}, bem vindo ao server mais Top do BR!", file=discord.File("member_join.svg"))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if "val" in message.content.lower() and "oi" in message.content.lower():
        pos = [
            "Olá, tudo bem?",
            "Online!",
            "Val a disposição!",
            "Bom dia!",
            "Olá, estou conectada!"
        ]
        await message.channel.send(pos[randrange(0, len(pos))])
    if "feliz aniversário" in message.content.lower():
        await message.channel.send("Feliz aniversário pra vc!")
    if "kkk" in message.content.lower():
        await message.channel.send("kkkkkkkkkk")
    if "piada" in message.content.lower():
        piadas = ["O que o pagodeiro foi fazer na igreja?\nfoi cantar pá-god",
              "Por que o Napoleão sempre era chamado para festas?\nPor que ele era bom-na-party",
              "Você conhece a piada do pônei?\nPô nem eu", "Qual é o rei dos queijos\n o reiqueijão",
              "O que o pato falou pra pata?\nvem quá", "Por que a velhinha não tem relógio\nPor que ela era sem hora",
              "O que a xuxa foi fazer no bar?\nfoi beber ca sasha"]
        img = [
            discord.File("img/laugh.gif"),
            discord.File("img/laugh2.gif"),
            discord.File("img/laugh3.gif"),
            discord.File("img/laugh4.gif")
        ]
        await message.channel.send(piadas[randrange(0, len(piadas))], file=img[randrange(0, len(img))])
        await message.channel.send(f"kkkkkkkkkk")
    if "número" in message.content.lower() and "aleatório" in message.content.lower():
        await message.channel.send(str(randrange(0, 100)))
    if "criador" in message.content.lower():
        await message.channel.send("Cauê Alves, Github: @caue-alves, Email: caue.mendes.rodrigues.alves@gmail.com")
    if "tempo" in message.content.lower():
        await message.channel.send(previsao_do_tempo())
    if "casos de covid" in message.content.lower():
        await message.channel.send(covid_cases())
    if "noticias" in message.content.lower():
        await message.channel.send(scrapping())
    if message.content.lower() == "?":
        await message.channel.send(file=discord.File("img/sera.gif"))
    agressions = [
        "boiola",
        "viado",
        "frouxo",
        "baitola",
        "seu macaco"
    ]
    for i in agressions:
        if i in message.content.lower():
            await message.channel.send("Puliça chegando... Meça suas palavras! Agressões deste porte não são permitidas nesse server!")
            AD = client.get_channel(int((os.getenv("AD_ID"))))
            await AD.send(f"{message.author.mention} + 1 advertência")

client.run(TOKEN)