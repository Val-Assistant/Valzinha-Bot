import os
from datetime import datetime
from random import randrange
import discord
from dotenv import load_dotenv
from web_func import scrapping, previsao_do_tempo, covid_cases
from discord.utils import get
from re import *
afk=[]
muted=[]
after=False
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
client = discord.Client()

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.listening, name="val ajuda"))
    print(f'Sistema: {client.user} está conectada ao Discord!')
    canal = client.get_channel(int(os.getenv("ID_CANAL")))
    #await canal.send(f"Olá a todos, Val preparada pra mais um dia de trabalho ^-^")

@client.event
async def on_member_join(member):
    await member.send(
        f'Olá {member.name}, bem vindo ao server!'
    )
    #svg = open("img/member_join.svg", 'r')
    #content = svg.read()
    #content.replace("Member Name", member.name)
    #svg2 = open("img/member_join.svg", "w")
    #svg2.write(content)
    #canal = client.get_channel(int(os.getenv("ID_CANAL")))
    #await canal.send(f"Olá {member.mention}, bem vindo ao server mais Top do BR!", file=discord.File("member_join.svg"))

@client.event
async def on_message(message):
    for user in muted:
        if (user == "<@" + str(message.author.id) + ">"):
            await message.delete()
    for i in afk:
        if(str(i)) in message.content.lower():
            await message.channel.send("O usuário está em modo AFK!")
        if i==message.author.id:
            await message.channel.send("Olá, bem vindo de volta >~<!")
            afk.pop(0)
    print("Mensagem - " + message.author.name +  ": " + message.content)
    if message.content.split()[0].lower() == "val":
        print(message.content.split()[1].lower())
        if message.content.split()[1].lower() == "bicuda":
            a=discord.File("img/bico1.gif")
            b=discord.File("img/bico2.gif")
            c=discord.File("img/bico3.gif")
            user=message.content.split()[2]
            embedVal=discord.Embed(title="Bicuda", description=message.author.mention + " deu uma bicuda em " + user + ", nossa!", color=0x00ff00)
            bname=['bico1.gif', 'bico2.gif', 'bico3.gif']
            bb=bname[randrange(0, len(bname) - 1)]
            embedVal.set_thumbnail(url=message.author.avatar_url)
            embedVal.set_image(url="attachment://" + bb)
            hoje1 = datetime.today()
            hoje = hoje1.strftime("%a/%d/%m/%Y %H:%M")
            embedVal.set_footer(text=f"Pedido por {message.author.name} em {hoje}")
            await message.channel.send(message.author.mention, embed=embedVal, file=discord.File("img/"+bb))
        if message.content.split()[1].lower() == "abraço":
            a=discord.File("img/ab1.gif")
            b=discord.File("img/ab2.gif")
            c=discord.File("img/ab3.gif")
            d=discord.File("img/ab4.gif")
            e=discord.File("img/ab5.gif")
            f=discord.File("img/ab6.gif")
            user=message.content.split()[2]
            embedVar=discord.Embed(title="Abraço", description=message.author.mention + " deu um abraço em " + user + ", nossa, que fofo!", color=0x00ff00)
            ab_name=["ab1.gif", "ab2.gif", "ab3.gif", "ab4.gif", "ab5.gif", "ab6.gif"]
            aa=ab_name[randrange(0, len(ab_name) - 1)]
            embedVar.set_image(url="attachment://" + aa)
            embedVar.set_thumbnail(url=message.author.avatar_url)
            hoje1 = datetime.today()
            hoje = hoje1.strftime("%a/%d/%m/%Y %H:%M")
            embedVar.set_footer(text=f"Pedido por {message.author.name} em {hoje}")
            await message.channel.send(message.author.mention, embed=embedVar, file=discord.File("img/"+aa))
        if message.content.split()[1].lower() == "beijar":
            a=discord.File("img/bj1.gif")
            b=discord.File("img/bj2.gif")
            c=discord.File("img/bj3.gif")
            d=discord.File("img/bj4.gif")
            d=discord.File("img/bj5.gif")
            e=discord.File("img/j6.gif")
            user=message.content.split()[2]
            embedVar=discord.Embed(title="Beijo", description=message.author.mention + " deu um beijo em " + user + ", meu deuuuuuuuuuuuuuuuussss :3", color=0x00ff00)
            kname=["bj1.gif", "bj2.gif", "bj3.gif", "bj4.gif", "bj5.gif", "j6.gif"]
            kk=kname[randrange(0, len(kname) - 1)]
            embedVar.set_thumbnail(url=message.author.avatar_url)
            embedVar.set_image(url="attachment://" + kk)
            hoje1 = datetime.today()
            hoje = hoje1.strftime("%a/%d/%m/%Y %H:%M")
            embedVar.set_footer(text=f"Pedido por {message.author.name} em {hoje}")
            await message.channel.send(message.author.mention, embed=embedVar, file=discord.File("img/" + kk))
        if message.content.split()[1].lower() == "atirar":
            a=discord.File("img/s1.gif")
            b=discord.File("img/s2.jpg")
            c=discord.File("img/s3.gif")
            d=discord.File("img/s4.gif")
            e=discord.File("img/s5.gif")
            user=message.content.split()[2]
            embedVar=discord.Embed(title="Atirar", description=message.author.mention + " deu um tiro em " + user + ", doeu hein!", color=0x00ff00)
            embedVar.set_thumbnail(url=message.author.avatar_url)
            tiro_name=["s1.gif", "s2.jpg", 's3.gif', 's4.gif', 's5.gif']
            aa = tiro_name[randrange(0, len(tiro_name) - 1)]
            embedVar.set_image(url="attachment://" + aa)
            hoje1 = datetime.today()
            hoje = hoje1.strftime("%a/%d/%m/%Y %H:%M")
            embedVar.set_footer(text=f"Pedido por {message.author.name} em {hoje}")
            await message.channel.send(message.author.mention, embed=embedVar, file=discord.File("img/" + aa))
        if message.content.split()[1].lower() == "vidente":
            answers=["Hmmf, mas é óbvio", "Não queria te decepcionar mas, não", "SIIIIIIM, MAS É CLARO", "E você ainda pergunta?", "Tenho dúvidas, mas acho que sim", "Sim, mas é claro", "Estou incerta"]
            await message.channel.send(message.author.mention + "\n" + "<:na:786301269618851880> | " + answers[randrange(0, len(answers) -1 )])
        if message.content.split()[1].lower() == "afk":
            afk.append(message.author.id)
            await message.channel.send("Agora você está em modo AFK!")
        if message.content.split()[1].lower() == "mute":
            user=message.content.split()[2]
            muted.append(user)
        if message.content.split()[1].lower() == "unmute":
            muted.pop(0)
        if message.content.split()[1].lower() == "info":
            embedVar=discord.Embed(title="Val Uchiha", description="""
Criador: `D4rkDev#5159`

Biblioteca: `discord.py`

GitHub: `https://github.com/Val-Assistant/Val-Bot-For-Discord`

Prefixo: `val`

Comando de ajuda: `val ajuda`

Rodando em (4) servers.
            """, color=0x00ff00)
            await message.channel.send(message.author.mention,embed=embedVar)
        if message.content.split()[1].lower() == "cara-coroa":
            n=randrange(0, 3)
            if n==1:
                moeda="Cara"
            else:
                moeda="Coroa "
            embedVar=discord.Embed(title="Cara ou coroa", description=f"E o resultado foii... {moeda} <:money:786588565698117652> ! Digite `val cara-coroa` para jogar a moeda novamente!", color=0x00ff00)
            await message.channel.send(embed=embedVar)
        if message.content.split()[1].lower() == "noticias":
            a=discord.File("img/jornal.jpg")
            embedVar=discord.Embed(title="Notícias", description=scrapping(), color=0x00ff00)
            embedVar.set_image(url="attachment://jornal.jpg")
            await message.channel.send(embed=embedVar, file=a)
        if "casos" == message.content.split()[1].lower():
            await message.channel.send(covid_cases())
        if "piada" == message.content.split()[1].lower():
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
        if "tempo" == message.content.split()[1].lower():
            await message.channel.send(previsao_do_tempo())
        if message.content.split()[1].lower() == "carreira":
            with open("money.txt", "r+") as f:
                if message.author.name in f.read():
                    await message.channel.send("Você já começou uma carreira!")
                else:
                    f.write(message.author.name + ": 100\n")
                    f.flush()
        if message.content.split()[1].lower() == "money":
            with open("money.txt", "r+") as f:
                txt=f.read()
                position=txt.find(message.author.name)
                end=txt.find("\n", position)
                two_dot=txt.find(":", position, end)
                money=txt[two_dot+2:end]
                embedVar=discord.Embed(description=f"Dinheiro Atual: `{money}`")
                embedVar.set_thumbnail(url="https://publicdomainvectors.org/photos/1541014380.png")
                embedVar.set_author(name=message.author.name, icon_url=message.author.avatar_url)
                await message.channel.send(embed=embedVar)
                if position==-1:
                    await message.channel.send("Começe uma carreira através do comando `val carreira` para ganhar seu dinheiro!")
        if message.content.split()[1].lower() == "trabalhar":
            ganhou=randrange(100, 1000)
            with open("money.txt", "r+") as f:
                txt=f.read()
                position=txt.find(message.author.name)
                end=txt.find("\n", position)
                two_dot=txt.find(":", position, end)
                money=txt[two_dot+2:end]
                money_novo=int(money)+ganhou
                old_strip=txt[position:end+1]
                new=old_strip.replace(money, str(money_novo))
                print("veio: " + old_strip)
                print('novo: ' + new)
                print('texto: ' + txt)
                txt=txt.replace(old_strip, new)
                nf=open("money.txt", "w")
                nf.write(txt)
                embedVar=discord.Embed(title="Trabalho", description=f"Você trabalhou e ganhou {str(ganhou)} dinheiros!", color=0x00ff00)
                embedVar.set_thumbnail(url=message.author.avatar_url)
                embedVar.set_image(url="https://acegif.com/wp-content/uploads/gif-funny-work-48.gif")
                await message.channel.send(embed=embedVar)
        if message.content.split()[1].lower() == "ship":
            user1=message.content.split()[2].lower()
            user2=message.content.split()[3].lower()
            heart=discord.File("img/cola.gif")
            casal=randrange(0, 101)
            explain=""
            if casal>=80:
                explain="Nosssaaaaa, se ainda não casaram estou realmente surpresa!"
            if casal==100:
                explain="Meu deuss, são almas gêmeas, vocês são um caso raro!"
            if casal<=60:
                explain="Os dois combinam! Formariam um ótimo casal :)"
            if casal<=40:
                explain="Éeeeee, com um pouco de persistência eles conseguem!"
            if casal<=20:
                explain="As chances são praticamente impossíveis! Mas nada que o amor não resolva =)"
            embedVar=discord.Embed(title="Ship", description=f"{user1} e {user2}\n\nA chance do casal é de {casal}%\n\n{explain}", color=0x00ff00)
            embedVar.set_image(url="attachment://cola.gif")
            await message.channel.send(message.author.mention, embed=embedVar, file=heart)
        if message.content.split()[1].lower() == "avatar":
            try:
                user = client.get_user(int(message.content.split()[2][2:len(message.content.split()[2])-1]))
            except:
                user=message.author
            embedVar=discord.Embed(title=user.name)
            embedVar.set_image(url=user.avatar_url)
            embedVar.set_footer(text=f"URL = {user.avatar_url}")
            await message.channel.send(embed=embedVar)
        if message.content.split()[1].lower() == "sugerir":
            hoje1 = datetime.today()
            hoje = hoje1.strftime("%a/%d/%m/%Y %H:%M")
            sugestao = " ".join(message.content.split()[2:])
            embedVal=discord.Embed(title="Sugestão", description=f"Por {message.author.mention}\n\nConteúdo: {sugestao}\n\nHorário: `{hoje}`", color=0x00ff00)
            await message.channel.send(embed=embedVal)
            await message.delete()
        if message.content.split()[1].lower() == "hentai":
            await message.channel.send(message.author.mention + ", não gosto dessas coisas...")
        if message.content.split()[1].lower() == "userinfo":
            embedVar=discord.Embed(title='Informações', description=f"Nome: `{message.author.name}`\n\nNick: `{message.author.nick}`\n\nID: `{message.author.id}`\n\nChegou em: `{message.author.joined_at}`\n\nAtividades agora `{message.author.activities}`", color=0x00ff00)
            embedVar.set_thumbnail(url=message.author.avatar_url)
            await message.channel.send(embed=embedVar)
        if message.content.split()[1].lower() == "limpar":
            n=int(message.content.split()[2])
            async for i in message.channel.history(limit=n):
                await i.delete()

        if message.content.split()[1].lower() == "ajuda":
            await message.add_reaction("👍")
            embedVal=discord.Embed(title="Val Uchiha", description="""
A Val é um bot de propósito geral com foco em NLP e em organização do server, veja seus comandos> 
    
Atos:
`beijar`, `abraço`, `bicuda`, `atirar`
    
Moderação:
`sugerir`, `mute`, `userinfo`, `info`, `avatar`, `limpar`

Utilidades:
`casos de covid`, `tempo`, `noticias`
    
Diversão:
`piada`, `vidente`, `hentai`, `cara-coroa`
    
NLP:
Risadas, Feliz aniversário 

Economia:
`carreira`, `trabalhar`
            """, color=0x00ff00)
            await message.channel.send(message.author.mention, embed=embedVal)
    if message.author == client.user:
        return
    #if "val" in message.content.lower() and "oi" in message.content.lower():
    #    pos = [
    #        "Olá, tudo bem?",
    #        "Online!",
    #        "Val a disposição!",
    #        "Bom dia!",
    #        "Olá, estou conectada!"
    #    ]
    #   await message.channel.send(pos[randrange(0, len(pos))])
    if "feliz aniversário" in message.content.lower():
        await message.channel.send("Feliz aniversário pra vc!")
    #if "kkk" in message.content.lower():
     #   await message.channel.send("kkkkkkkkkk")
    if "número" in message.content.lower() and "aleatório" in message.content.lower():
        await message.channel.send(str(randrange(0, 100)))
    if "criador" in message.content.lower():
        await message.channel.send("Cauê Alves, Github: @caue-alves, Email: caue.mendes.rodrigues.alves@gmail.com")
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