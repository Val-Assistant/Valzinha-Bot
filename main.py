import os
from random import randrange
import discord
from dotenv import load_dotenv
from web_func import scrapping, previsao_do_tempo, covid_cases
from time import sleep
import schedule
from discord.utils import get

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
    print(message.content)
    print(message.content.split()[0].lower())
    if message.content.split()[0].lower() == "val":
        print(message.content.split()[1].lower())
            #if message.strip()[1].lower() == "adicionar-role" and len(message.strip()) == 4:
             #   role = message.strip()[2]
             #   user = discord.Member(message.strip()[3][1:])
             #   role = get(user.server.roles, name=role)
        if message.content.split()[1].lower() == "bicuda":
            bicos=[discord.File("img/bico1.gif"), discord.File("img/bico2.gif"), discord.File("img/bico3.gif")]
            user=message.content.split()[2]
            await message.channel.send("> " + message.author.mention + " deu uma bicuda em " + user + ", nossa!", file=bicos[randrange(0, len(bicos))])
        if message.content.split()[1].lower() == "abraço":
            ab = [discord.File("img/ab1.gif"), discord.File("img/ab2.gif"), discord.File("img/ab3.gif"), discord.File("img/ab4.gif"), discord.File("img/ab5.gif"), discord.File("img/ab6.gif")]
            user=message.content.split()[2]
            await message.channel.send("> " + message.author.mention + " deu um abraço em " + user + ", nossa, que fofo!", file=ab[randrange(0, len(ab) - 1)])
        if message.content.split()[1].lower() == "beijar":
            bjs = [discord.File("img/bj1.gif"), discord.File("img/bj2.gif"), discord.File("img/bj3.gif"), discord.File("img/bj4.gif"), discord.File("img/bj5.gif"), discord.File("img/j6.gif")]
            user=message.content.split()[2]
            await message.channel.send("> " + message.author.mention + " deu um beijo em " + user + ", meu deuuuuuuuuuuuuuuuussss :3", file=bjs[randrange(0, len(bjs) - 1)])
        if message.content.split()[1].lower() == "atirar":
            tiro = [discord.File("img/s1.gif"), discord.File("img/s2.jpg"), discord.File("img/s3.gif"), discord.File("img/s4.gif"), discord.File("img/s5.gif")]
            user=message.content.split()[2]
            await message.channel.send("> " + message.author.mention + " deu um tiro em " + user + ", doeu hein!", file=tiro[randrange(0, len(tiro) - 1)])
        if message.content.split()[1].lower() == "vidente":
            answers=["Hmmf, mas é óbvio", "Não queria te decepcionar mas, não", "SIIIIIIM, MAS É CLARO", "E você ainda pergunta?", "Tenho dúvidas, mas acho que sim", "Sim, mas é claro", "Estou incerta"]
            await message.channel.send(answers[randrange(0, len(answers) -1 )])
        if message.content.split()[1].lower() == "ajuda":
            await message.channel.send(
"""
```
    # Val Uchiha #
A Val é um bot de propósito geral com foco em NLP e em organização do server, veja seus comandos> 
    
Atos:
beijar, abraço, bicuda, atirar
    
Utilidades:
casos de covid, tempo, notícias
    
Diversão:
piada
    
NLP:
Risadas, Feliz aniversário 
```
                """)
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