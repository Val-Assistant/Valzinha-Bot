import os
from datetime import datetime
from random import randrange
import discord
from web_func import scrapping, previsao_do_tempo, covid_cases
from googlesearch import search
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF, renderPM
from random_image import *
from news_generator import *
import asyncio
afk=[]
players = {}
muted=[]
after=False
TOKEN = '👀'

intents = discord.Intents.default()
intents.presences = True
intents.members = True
intents.typing = True
intents.reactions = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="val ajuda"))
    print(f'Sistema: {client.user} está conectada ao Discord!')
    #canal = client.get_channel(int(os.getenv("ID_CANAL")))
    #await canal.send(f"Olá a todos, Val preparada pra mais um dia de trabalho ^-^")

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Olá {member.name}, bem vindo ao server!'
    )

bug = None

@client.event
async def on_message(message):
    global bug
    if bug and message.author != client.user:
        owner=client.get_user(754491870880596120)
        await owner.create_dm()
        embedVar=discord.Embed(title="Bug Report", description=message.content, color=0x00ff00)
        await owner.dm_channel.send(embed=embedVar)
        bug=False
    for i in afk:
        if(str(i)) in message.content.lower():
            await message.delete()
            await message.channel.send("O usuário está em modo AFK!")
        if i==message.author.id:
            await message.channel.send("Olá, bem vindo de volta >~<!")
            afk.pop(0)
    print("Mensagem - " + message.author.name +  ": " + message.content)
    if message.content.split()[0].lower() == "val":
        print(message.content.split()[1].lower())
        if message.content.split()[1].lower() == "toc-toc":
            await message.channel.send("Sai daqui seu idiota!")
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
        if message.content.split()[1].lower() == "carinho":
            url=[
                "https://i.pinimg.com/originals/2e/27/d5/2e27d5d124bc2a62ddeb5dc9e7a73dd8.gif",
                "https://media1.tenor.com/images/bb5608910848ba61808c8f28caf6ec7d/tenor.gif?itemid=11039783",
                "https://i.pinimg.com/originals/c2/34/cd/c234cdcb3af7bed21ccbba2293470b8c.gif",
                "https://i.imgur.com/UWbKpx8.gif",
                "https://i.pinimg.com/originals/e3/e2/58/e3e2588fbae9422f2bd4813c324b1298.gif",
                "https://media.tenor.com/images/a671268253717ff877474fd019ef73e9/tenor.gif",
                "https://giffiles.alphacoders.com/187/187369.gif"
            ]
            embedVar=get_random_image_from_array(url, "Carinho", f"{message.author.mention} fez carinho em {message.content.split()[2]}, fofinho!", 0x00ff00, message.author)
            await message.channel.send(embed=embedVar)
        if message.content.split()[1].lower() == "matar":
            url=[
                "https://media4.giphy.com/media/BTV1vUcOWht2U/200.gif",
                "https://i.pinimg.com/originals/9b/bc/10/9bbc10969b7558185c4c6cc915f1ff41.gif",
                "https://thumbs.gfycat.com/AmazingSpottedIguanodon-size_restricted.gif",
                "https://media1.tenor.com/images/dd2c031cdf47a2bd9588e09b542d3a84/tenor.gif?itemid=5790550",
                "https://media1.giphy.com/media/l4FGvTL3rGuoo1Oy4/giphy.gif",
                "https://media0.giphy.com/media/deaabWAgiawzyiMNZS/200.gif"
            ]
            embedVar=get_random_image_from_array(url, "Matar", f"{message.author.mention} matou {message.content.split()[2]}, meu deus! Que horrô!", 0x00ff00, message.author)
            await message.channel.send(embed=embedVar)
        if message.content.split()[1].lower() == "comer":
            await message.channel.send(f"{message.author.mention}, vai com calma aí meu jovem!")
        if message.content.split()[1].lower() == "tapear":
            url=[
                "https://media.tenor.com/images/6dbd997e3e79f21b7841b244833325c0/tenor.gif",
                "https://www.intoxianime.com/wp-content/uploads/2017/04/tumblr_ooub8fIHkT1qz64n4o2_400.gif",
                "https://i.pinimg.com/originals/65/57/f6/6557f684d6ffcd3cd4558f695c6d8956.gif",
                "https://media1.tenor.com/images/3fd96f4dcba48de453f2ab3acd657b53/tenor.gif?itemid=14358509",
                "https://i.imgur.com/5lzn5sb.gif",
                "https://i.pinimg.com/originals/a1/cf/c4/a1cfc41d9b12c1d4b4aa201712f8eb5a.gif"
            ]
            embedVar=get_random_image_from_array(url, "Tapa", f"{message.author.mention} deu um tapa em {message.content.split()[2]}, nossa, doeu!", 0x00ff00, message.author)
            await message.channel.send(embed=embedVar)
        if message.content.split()[1].lower() == "soco":
            url=[
                "https://i.pinimg.com/originals/8d/50/60/8d50607e59db86b5afcc21304194ba57.gif",
                "https://i.pinimg.com/originals/f3/ec/8c/f3ec8c256cb22279c14bfdc48c92e5ab.gif",
                "https://i.pinimg.com/originals/bc/96/17/bc9617a2460e4640fcd9cf474bea2c10.gif",
                "https://i.imgur.com/g91XPGA.gif",
                "https://cdn172.picsart.com/222035215014201.gif?to=min&r=1024",
                "https://steamuserimages-a.akamaihd.net/ugc/450706552928252485/50C9662E10390987F8FD69686922BFD974A4FD0D/"
            ]
            embedVar=get_random_image_from_array(url, "Soco", f"{message.author.mention} deu um socão em {message.content.split()[2]}, nossa!", 0x00ff00, message.author)
            await message.channel.send(embed=embedVar)
        if message.content.split()[1].lower() == "chorar":
            url=[
                "https://i.pinimg.com/originals/b4/b1/64/b4b1640525ecadfa1030e6096f3ec842.gif",
                "https://i.pinimg.com/originals/e0/fb/b2/e0fbb27f7f829805155140f94fe86a2e.gif",
                "https://pa1.narvii.com/5729/7239144f9492a477092d05271e10657b9e1a335b_hq.gif",
                "https://media.tenor.com/images/19089cd2b4970740debff2cdfc43329a/tenor.gif",
                "https://i.pinimg.com/originals/9d/cb/2b/9dcb2b83c29e6c70b4971e718cabe958.gif",
                "https://media3.giphy.com/media/1eEB6YXgMrAeAgKwyL/giphy.gif",
                "https://data.whicdn.com/images/320214384/original.gif"
            ]
            embedVar=get_random_image_from_array(url, "Chorar", f"{message.author.mention} ficou triste e chorou, *snfiff*, opa, entrou um cisco no meu olho.", 0x00ff00, message.author)
            await message.channel.send(embed=embedVar)
        if message.content.split()[1].lower() == "gritar":
            url=[
                "https://thumbs.gfycat.com/AffectionateVerifiableHorsefly-size_restricted.gif",
                "https://i.pinimg.com/originals/49/0e/9f/490e9f19bb5ab96cb703f2526ada3529.gif",
                "https://media0.giphy.com/media/9sSrddsom3yb6/200.gif",
                "https://pa1.narvii.com/6220/a93aefb0726de740a9a63f6ed1d7efbcc3ce9026_hq.gif",
                "https://i.pinimg.com/originals/b7/c4/c0/b7c4c0be88d27484e0145ab0d822f1d4.gif",
                "https://4.bp.blogspot.com/-WoSv7JH2IBc/Vwa_MEKHdLI/AAAAAAAAhHY/HS5L_kADw0sTI9KFUGIBN2ASGTwxguMoQ/s1600/tumblr_o4mzf8Bhzp1tmp8rdo2_r1_500.gif"
            ]
            embedVar=get_random_image_from_array(url, "Gritar", f"{message.author.mention} deu um gritãaaaaaooooooooo!", 0x00ff00, message.author)
            await message.channel.send(embed=embedVar)
        if message.content.split()[1].lower() == "morder":
            url=[
                "https://media1.tenor.com/images/f3f503705c36781b7f63c6d60c95a9d2/tenor.gif?itemid=17570122",
                "https://media1.tenor.com/images/f308e2fe3f1b3a41754727f8629e5b56/tenor.gif?itemid=12390216",
                "https://i.pinimg.com/originals/17/9a/16/179a16220f6cf2712073ccdc759ff3e1.gif",
                "https://i.gifer.com/np4.gif",
                "https://media1.tenor.com/images/6b42070f19e228d7a4ed76d4b35672cd/tenor.gif?itemid=9051585"
            ]
            embedVar=get_random_image_from_array(url, "Morder", f"{message.author.mention} deu uma mordida em {message.content.split()[2]}, nossa!", 0x00ff00, message.author)
            await message.channel.send(embed=embedVar)
        if message.content.split()[1].lower() == "vidente":
            answers=["Hmmf, mas é óbvio", "Não queria te decepcionar mas, não", "SIIIIIIM, MAS É CLARO", "E você ainda pergunta?", "Tenho dúvidas, mas acho que sim", "Sim, mas é claro", "Estou incerta"]
            await message.channel.send(message.author.mention + "\n" + "<:na:786301269618851880> | " + answers[randrange(0, len(answers) -1 )])
        if message.content.split()[1].lower() == "afk":
            afk.append(message.author.id)
            await message.channel.send("Agora você está em modo AFK!")
        if message.content.split()[1].lower() == "mute":
            user_id=message.content.split()[2][2:len(message.content.split()[2]) - 1]
            print(user_id)
            member = message.guild.get_member(int(user_id))
            user=client.get_user(int(user_id))
            print(f"Tipo do membro: {type(member)}\n\nTipo do Usuário{type(user)}")
            names=[]
            for i in message.guild.roles:
                names.append(i.name)
            if "muted" not in names:
                role = await message.guild.create_role(name="muted")
                for channel in message.guild.channels:
                    await channel.set_permissions(role, send_messages=False)
            try:
                for i in message.guild.roles:
                    if i.name=="muted":
                        await member.add_roles(i)
            except:
                pass
        if message.content.split()[1].lower() == "fodasse":
            url=[
                "https://i.pinimg.com/236x/a6/1f/32/a61f325117c7aa0481f8f7294f90274a.jpg",
                "https://i.pinimg.com/236x/42/7d/3c/427d3cef78762937c67926bc01da34fc.jpg",
                "https://i.pinimg.com/originals/80/4c/23/804c23fd1fbf90721130e60cfe9541cd.jpg",
                "https://i.pinimg.com/originals/94/6f/9c/946f9ceb91f7dfc172e1426284102bd7.jpg",
                "https://i.pinimg.com/236x/17/a5/51/17a55134d40e16172fd2d8e490f5be00.jpg",
                "https://i.pinimg.com/236x/1f/2a/e9/1f2ae9e48f4de4f6b6c573d55218708c.jpg",
                "https://i.pinimg.com/236x/7e/c9/a0/7ec9a017ced03f6831c6151fda463ac2.jpg",
                "https://i.pinimg.com/564x/e8/23/dc/e823dcd34b123df918b9dffd62c0656e.jpg",
                "https://i.ytimg.com/vi/-ulI7-vv-Gw/hqdefault.jpg",
                "https://images.uncyc.org/pt/thumb/2/2c/Fodase12.jpg/120px-Fodase12.jpg",
                "https://i.pinimg.com/236x/a6/4a/4b/a64a4b386e5c51152d295775e8106432.jpg",
                "https://i.pinimg.com/originals/6a/ad/e0/6aade0debad4f5a0a095f2138ce4c5ef.jpg",
                "https://i.pinimg.com/236x/73/65/d7/7365d7b47e3d9c34f121f7b8042c70ff.jpg"
            ]
            embedVar=discord.Embed(title="FODASSE", description=message.author.mention + " invocou o sagrado poder do **FODASSE**", color=0x00ff00)
            embedVar.set_image(url=url[randrange(0, len(url)-1)])
            await message.channel.send(embed=embedVar)
        if message.content.split()[1].lower() == "laranjo":
            with open("laranjo.svg", "r") as l:
                read=l.read()
                text=message.content.split()[2:]
                read = read.replace("meodeos", " ".join(text))
                wl=open("laranjo.svg", "w")
                wl.write(read)
            drawing = svg2rlg("laranjo.svg")
            renderPM.drawToFile(drawing, "result.png", fmt="PNG")
            await message.channel.send(file=discord.File("result.png"))
            read = read.replace(" ".join(text), "meodeos")
            wl=open("laranjo.svg", "w")
            wl.write(read)
            os.remove("result.png")
        if message.content.split()[1].lower() == "bhcareca":
            with open("bh.svg", "r") as l:
                read=l.read()
                text=message.content.split()[2:]
                read = read.replace("fodasse?", " ".join(text))
                wl=open("bh.svg", "w")
                wl.write(read)
            drawing = svg2rlg("bh.svg")
            renderPM.drawToFile(drawing, "resultbh.png", fmt="PNG")
            await message.channel.send(file=discord.File("resultbh.png"))
            read = read.replace(" ".join(text), "fodasse?")
            wl=open("bh.svg", "w")
            wl.write(read)
            os.remove("resultbh.png")
        if message.content.split()[1].lower() == "tv":
            with open("tv.svg", "r") as l:
                read=l.read()
                text=message.content.split()[2:]
                read = read.replace("meodeos", " ".join(text))
                wl=open("tv.svg", "w")
                wl.write(read)
            drawing = svg2rlg("tv.svg")
            renderPM.drawToFile(drawing, "resulttv.png", fmt="PNG")
            await message.channel.send(file=discord.File("resulttv.png"))
            read = read.replace(" ".join(text), "meodeos")
            wl=open("tv.svg", "w")
            wl.write(read)
            os.remove("resulttv.png")
        if message.content.split()[1].lower() == "warn":
            member_id=message.content.split()[2][2:len(message.content.split()[2])-1]
            member=message.guild.get_member(int(member_id))
            if "warn 1/3" in [y.name.lower() for y in member.roles]:
                names=[]
                for i in message.guild.roles:
                    names.append(i.name)
                if "warn 2/3" not in names:
                    role = await message.guild.create_role(name="warn 2/3")
                else:
                    for i in message.guild.roles:
                        if i.name=="warn 2/3":
                            role = i
                await member.add_roles(role)
            if "warn 2/3" in [y.name.lower() for y in member.roles]:
                names=[]
                for i in message.guild.roles:
                    names.append(i.name)
                if "warn 3/3" not in names:
                    role = await message.guild.create_role(name="warn 3/3")
                else:
                    for i in message.guild.roles:
                        if i.name=="warn 3/3":
                            role = i
                await member.add_roles(role)
            else:
                names=[]
                for i in message.guild.roles:
                    names.append(i.name)
                if "warn 1/3" not in names:
                    role = await message.guild.create_role(name="warn 1/3")
                else:
                    for i in message.guild.roles:
                        if i.name=="warn 1/3":
                            role = i
                await member.add_roles(role)
            if "warn 3/3" in [y.name.lower() for y in member.roles]:
                await member.ban()
                await message.channel.send(f"O usuário {member.name} foi banido devido aos seus 3 warns")
            await message.channel.send(f"Usuário {message.content.split()[2]} avisado com sucesso!")
        if message.content.split()[1].lower() == "unmute":
            user_id=message.content.split()[2][2:len(message.content.split()[2]) - 1]
            member = message.guild.get_member(int(user_id))
            a=None
            for i in message.guild.roles:
                if i.name=="muted":
                    await member.remove_roles(i)
        if message.content.split()[1].lower() == "trancar":
            await message.channel.set_permissions(message.guild.default_role, send_messages=False)
            await message.channel.send(message.author.mention + ", o chat foi travado com sucesso!")
        if message.content.split()[1].lower() == "destrancar":
            await message.channel.set_permissions(message.guild.default_role, send_messages=True)
            await message.channel.send(message.author.mention + ", o chat foi destravado com sucesso!")
        if message.content.split()[1].lower() == "serverinfo":
            embedVar=discord.Embed(title=message.guild.name, description=f"🎟 Nome: `{message.guild.name}`\n\n📆 Descrição: {message.guild.description}\n\n✨ ID: `{message.guild.id}`\n\n😀 N° de emojis: `{len(message.guild.emojis)}`\n\n🪐 Região: `{message.guild.region}`\n\n💎 Boosts: {message.guild.premium_subscription_count}\n\n🎈 Membros: `{len(message.guild.members)}`", color=0x00ff00)
            await message.channel.send(embed=embedVar)
        if message.content.split()[1].lower() == "info":
            embedVar=discord.Embed(title="Val Uchiha", description=f"""
:superhero: | Criador: `D4rkDev#5159`

:books: | Biblioteca: `discord.py`

<:gh:788130052985585675> | GitHub: `https://github.com/Val-Assistant/Val-Bot-For-Discord`

:exclamation: | Prefixo: `val`

:tools: | Comandos: `52`

<:db:788130846401364040> | Comando de ajuda: `val ajuda`

Rodando em ({len(client.guilds)}) servers.
            """, color=0x00ff00)
            await message.channel.send(message.author.mention,embed=embedVar)
        if message.content.split()[1].lower() == "ado":
            try:
                p=[
                f"{message.content.split()[2]} é viado",
                f"{message.content.split()[2]} está cagado",
                f"{message.content.split()[2]} é um abençoado",
                f"{message.content.split()[2]} é safado",
                f"{message.content.split()[2]} é dotado de muita gadice"
                ]
                await message.channel.send(p[randrange(0, len(p))])
            except:
                await message.channel.send("Mencione um usuário!")
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
        if "casos-de-covid" == message.content.split()[1].lower():
            await message.channel.send(covid_cases(message.content.split()[2].upper()))
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
                    f.write(str(message.author.id) + ": 100\n")
                    f.flush()
                    await message.channel.send("Carreira começada!")
        if message.content.split()[1].lower() == "money":
            with open("money.txt", "r+") as f:
                txt=f.read()
                position=txt.find(str(message.author.id))
                end=txt.find("\n", position)
                two_dot=txt.find(":", position, end)
                money=txt[two_dot+2:end]
                embedVar=discord.Embed(description=f"Dinheiro Atual: `{money}`", color=0x00ff00)
                embedVar.set_thumbnail(url="https://publicdomainvectors.org/photos/1541014380.png")
                embedVar.set_author(name=message.author.name, icon_url=message.author.avatar_url)
                await message.channel.send(embed=embedVar)
                if position==-1:
                    await message.channel.send("Começe uma carreira através do comando `val carreira` para ganhar seu dinheiro!")
        if message.content.split()[1].lower() == "trabalhar":
            hoje1 = datetime.today()
            hoje = hoje1.strftime("%H")
            if int(hoje) > 16 and int(hoje) < 18:
                ganhou=randrange(100, 1000)
                with open("money.txt", "r+") as f:
                    txt=f.read()
                    position=txt.find(str(message.author.id))
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
            else:
                await message.channel.send("Você pode trabalhar apenas das 16 até as 18!")
        if message.content.split()[1].lower() == "apostar":
            win=randrange(1, 3)
            try:
                value=int(message.content.split()[2])
            except:
                value=100
            more=0
            print(win)
            if win==2:
                color=0x00ff00
                more+=(value*5)
                embedVar=discord.Embed(title="Aposta", description=f"Parabéns! Você ganhou {value*5}!", color=color)
            else:
                color=0xff0000
                more-=value
                embedVar=discord.Embed(title="Aposta", description=f"Você perdeu {value} por apostar errado, mais sorte da próxima vez!", color=color)
            with open("money.txt", "r+") as f:
                txt=f.read()
                position=txt.find(str(message.author.id))
                end=txt.find("\n", position)
                two_dot=txt.find(":", position, end)
                money=txt[two_dot+2:end]
                if int(money)>=more:
                    money_novo = int(money)+more
                    old_strip=txt[position:end+1]
                    new=old_strip.replace(money, str(money_novo))
                    txt=txt.replace(old_strip, new)
                    nf=open("money.txt", "w")
                    nf.write(txt)
                else:
                    embedVar=discord.Embed(title="Aposta", description="Você não tem dinheiro o suficiente para realizar a aposta", color=0xff0000)
                await message.channel.send(embed=embedVar)
        if message.content.split()[1].lower() == "pão":
            await message.channel.send("Pão é bom! Compre pão bom demais na || comi o cu de quem leu kkkkkkkkk ||")
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
        if message.content.split()[1].lower() == "falar":
            channel_id=message.content.split()[2][2:len(message.content.split()[2]) - 1]
            print(channel_id)
            chn=None
            for channel in message.guild.channels:
                if channel.id == int(channel_id):
                    chn=channel
            await chn.send(" ".join(message.content.split()[3:]))
        if message.content.split()[1].lower() == "yu-gi-oh":
            url=[
                "https://i.pinimg.com/474x/f4/1d/78/f41d78d4252bef206bf2bf7300f7cdee.jpg",
                "https://pm1.narvii.com/6840/0051e710d3445e80eb742fe88de27a0109f85a9ev2_00.jpg",
                "https://i.pinimg.com/474x/9b/77/f6/9b77f60f9dbb839ed866a9b8220c1134.jpg",
                "https://images7.memedroid.com/images/UPLOADED792/5b9ae6f9e5d93.jpeg",
                "https://i.pinimg.com/originals/a4/9c/c1/a49cc15bd60b41c8a9e177f9da49bc12.jpg",
                "https://i.pinimg.com/originals/47/b6/be/47b6be4b453eff155d97c40e685d7b56.jpg",
                "https://pics.me.me/trap-card-quando-esta-carta-0-usada-o-seu-oponente-53962280.png",
                "https://i.pinimg.com/474x/f0/f8/c0/f0f8c0d4d54353f72627ab4afd33662d.jpg",
                "https://i.pinimg.com/originals/d0/a0/c2/d0a0c2a0cb58439ec6929bed3b1461e2.jpg",
                "https://pm1.narvii.com/6337/5c2ffe73da146f6e16acc7a8d44091bcc21995a3_00.jpg",
                "https://i.pinimg.com/236x/b5/9c/a2/b59ca20f38a0ca4daeb8a1d362e02bf3.jpg",
                "https://i.pinimg.com/474x/f1/b8/fa/f1b8fada6c208723b87ee6d943efbf3f.jpg",
                "https://i.pinimg.com/564x/bd/e5/51/bde551bd485c148332841e0ecb4aa7ea.jpg",
                "https://i.pinimg.com/236x/52/91/6b/52916b39f21a7be4acd560c580e5c218.jpg",
                "https://i.pinimg.com/236x/b5/b9/dd/b5b9dd84f8a943ec1bc4e1be431d2d44.jpg",
                "https://i.pinimg.com/236x/b8/50/97/b850972f25a46966de4339b387974844.jpg",
                "https://i.ytimg.com/vi/9X9S82zh9_A/hqdefault.jpg",
                "https://pm1.narvii.com/6533/9e5b47630497eac34c2baf34926f4dc38e327b79_hq.jpg",
                "https://i.pinimg.com/originals/c2/09/7b/c2097beaa06a82642808b52c314321e5.png",
                "https://i.pinimg.com/474x/90/21/ee/9021ee381b616aafbf7fd87253cf61da.jpg",
                "https://i.pinimg.com/originals/08/6b/71/086b71aad9896a2b38d0a029e293e95f.jpg",
                "https://i.pinimg.com/736x/99/43/a8/9943a8a8709eb1110fdf35ce9691fa91.jpg",
                "https://pm1.narvii.com/6324/3d1f70e4d4b3dcb28b68339ef193afcfa2f7a0af_hq.jpg",
                "https://i.pinimg.com/474x/2d/e9/b6/2de9b6a8d332bdc49792bebf672d7c69.jpg",
                "https://i.pinimg.com/236x/dd/d7/6f/ddd76ff5cc43f752ebcb1dcbaf97447a.jpg"
            ]
            embedVar=discord.Embed(title="Yu-gi-oh", description="Carta invocada!", color=0x00ff00)
            file=url[randrange(0, len(url) - 1)]
            embedVar.set_image(url=file)
            await message.channel.send(embed=embedVar)
        if message.content.split()[1].lower() == "avatar":
            try:
                user = client.get_user(int(message.content.split()[2][2:len(message.content.split()[2])-1]))
            except:
                user=message.author
            embedVar=discord.Embed(title=user.name, color=0x00ff00)
            embedVar.set_image(url=user.avatar_url)
            embedVar.set_footer(text=f"URL = {user.avatar_url}")
            await message.channel.send(embed=embedVar)
        if message.content.split()[1].lower() == "easter-egg":
            embedVar=discord.Embed(title="Easter Eggs descobertos:", description="`?`, `Roi`, `<?>`")
            await message.channel.send(embed=embedVar)
        if message.content.split()[1].lower() == "sugerir":
            hoje1 = datetime.today()
            hoje = hoje1.strftime("%a/%d/%m/%Y %H:%M")
            sugestao = " ".join(message.content.split()[2:])
            embedVal=discord.Embed(title="Sugestão", description=f"Por {message.author.mention}\n\nConteúdo: {sugestao}\n\nHorário: `{hoje}`", color=0x00ff00)
            await message.channel.send(embed=embedVal)
            await message.delete()
        if message.content.split()[1].lower() == "entrar":
            try:
                canal = message.author.voice.channel
                vc = await canal.connect()
                await message.channel.send("Conectada ao canal " + canal.name + "!")
            except:
                await message.channel.send(message.author.mention + ", você precisa estar conectado a algum canal de voz!")
        if message.content.split()[1].lower() == "sair":
            try:
                for vc in client.voice_clients:
                    if vc.guild == message.guild:
                        await vc.disconnect()
                        await message.channel.send("Desconectada!")
            except:
                await message.channel.send("Como vou sair se nunca entrei?")
        if message.content.split()[1].lower() == "tocar":
            yt_url=message.content.split()[2]
            if len(client.voice_clients) != 0:
                canal = message.author.voice.channel
                player = await canal.create_ytdl_player('ytsearch: {}'.format(yt_url))
                player.start()
        if message.content.split()[1].lower() == "cronômetro":
            try:
                tempo = int(message.content.split()[2])
                await message.channel.send(f"Cronômetro setado para {tempo} segundo(s)")
            except:
                await message.channel.send("Um número de tempo de espera!")
                tempo=0
            await asyncio.sleep(tempo)
            await message.channel.send("Acabou!")
        if message.content.split()[1].lower() == "gado":
            try:
                p=[
                    f"{message.content.split()[2]} é gado dms",
                    f"{message.content.split()[2]} meu deus, o cara deve jogar frifas faz anos pra ser tão gado!",
                    f"{message.content.split()[2]} é um homem da igreja",
                    f"{message.content.split()[2]} éee, mais ou menos sabe",
                    f"{message.content.split()[2]} esse aí é foda, gadice 0!"
                ]
                await message.channel.send(p[randrange(0, len(p))])
            except:
                await message.channel.send("Mencione um usuário!")
        if message.content.split()[1].lower() == "cancelar":
            user=message.content.split()[2]
            mot=["ser foda demais", "comer o cu de quem leu"]
            embedVar=discord.Embed(title="Cancelamento", description=user + " foi cancelado por " + mot[randrange(0, 2)])
            embedVar.set_thumbnail(url=message.author.avatar_url)
            await message.channel.send(embed=embedVar)
        if message.content.split()[1].lower() == "hentai":
            await message.channel.send(message.author.mention + ", não gosto dessas coisas...")
        if message.content.split()[1].lower() == "userinfo":
            embedVar=discord.Embed(title='Informações', description=f"Nome: `{message.author.name}`\n\nNick: `{message.author.nick}`\n\nID: `{message.author.id}`\n\nChegou em: `{message.author.joined_at}`\n\nAtividades agora `{message.author.activities}`", color=0x00ff00)
            embedVar.set_thumbnail(url=message.author.avatar_url)
            await message.channel.send(embed=embedVar)
        if message.content.split()[1].lower() == "google":
            retorno = search(" ".join(message.content.split()[2:]), num_results=10)
            embedVar=discord.Embed(title="Resultados da pesquisa por " + ' '.join(message.content.split()[2:]), description="\n\n".join(retorno))
            embedVar.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/Google_%22G%22_Logo.svg/753px-Google_%22G%22_Logo.svg.png")
            embedVar.set_author(name=message.author.name, icon_url=message.author.avatar_url)
            await message.channel.send(embed=embedVar)
        if message.content.split()[1].lower() == "limpar":
            n=int(message.content.split()[2])
            async for i in message.channel.history(limit=n):
                await i.delete()
            await message.channel.send("Chat limpo por " + message.author.mention)
        if message.content.split()[1].lower() == "adicionar-role":
            role_id=message.content.split()[2][3:len(message.content.split()[2]) - 1]
            print(role_id)
            role=None
            for i in message.guild.roles:
                if i.id == int(role_id):
                    role=i
            member_id=message.content.split()[3][2:len(message.content.split()[2]) - 2]
            member=message.guild.get_member(int(member_id))
            try:
                await member.add_roles(role)
                await message.channel.send(f"Role: {message.content.split()[2]} adicionada com sucesso ao membro {message.content.split()[3]}")
            except:
                await message.channel.send(f"Erro!ræy a role {message.content.split()[2]} não pode ser adicionada!")
        if message.content.split()[1].lower() == "remover-role":
            role_id=message.content.split()[2][3:len(message.content.split()[2]) - 1]
            print(role_id)
            role=None
            for i in message.guild.roles:
                if i.id == int(role_id):
                    role=i
            member_id=message.content.split()[3][2:len(message.content.split()[2]) - 2]
            member=message.guild.get_member(int(member_id))
            try:
                await member.remove_roles(role)
                await message.channel.send(f"Role: {message.content.split()[2]} removida com sucesso do membro {message.content.split()[3]}")
            except:
                await message.channel.send(f"Erro! a role {message.content.split()[2]} não pode ser removida!")
        if message.content.split()[1].lower() == "kick":
            user_id=message.content.split()[2][2:len(message.content.split()[2]) - 1]
            member=message.guild.get_member(int(user_id))
            reason=" ".join(message.content.split()[3:])
            await member.kick()
            await message.channel.send(f"O usuário {member.name} foi kickado por '{reason}'")
        if message.content.split()[1].lower() == "ræy":
            embedVar=discord.Embed(title="Ræy", description="Ræy, um nome que ficará marcado em minha história...\nEle era um cara difícil de descrever, não era dos mais animados mas ainda sim transmitia sua forma de ver o mundo através de seus memes e de sua comédia. Amava cosplays e tinha uma inegável cara de mulher. Ele, de nome real Alex, era alguém de personalidade forte e memorável, digo era, pois infelizmente Alex nos deixou após ser atropelado, sei que ele está nos vendo seja daonde for, e quero que saiba por todos do server que nós o amamos.")
            embedVar.set_thumbnail(url='https://cdn.discordapp.com/avatars/786751179022663700/5f5e7a6e5a491160343c145b62b0f9e0.png?size=256')
            embedVar.set_author(name="LANCHONETE MEMES", icon_url="https://cdn.discordapp.com/icons/783180612311449610/c888fb4aeb42912af1e60de1f19e4310.png?size=256")
            await message.channel.send("@everyone", embed=embedVar)
        if message.content.split()[1].lower() == "ban":
            user_id=message.content.split()[2][2:len(message.content.split()[2]) - 1]
            member=message.guild.get_member(int(user_id))
            reason=" ".join(message.content.split()[3:])
            await member.ban()
            await message.channel.send(f"O usuário {member.name} foi banido por '{reason}'")
        if message.content.split()[1].lower() == "l-update":
            await message.channel.send(embed=news(client.user.avatar_url))
        if message.content.split()[1].lower() == "ajuda":
            await message.add_reaction("👍")
            embedVal=discord.Embed(title="Valzinha", description="""
<:cor:786985664683835452> A Val é um bot de propósito geral com foco em NLP e em organização do server, veja seus comandos> 

<:return:786972739290398780> | Prefixo: `val`
    
<:return:786972739290398780> | Roleplay:
`beijar`, `abraço`, `bicuda`, `atirar`, `carinho`, `matar`, `comer`, `tapear`, `soco`, `chorar`, `gritar`, `morder`
    
<:return:786972739290398780> | Moderação:
`sugerir`, `mute`, `avatar`, `limpar`, `trancar`, `destrancar`, `ban`, `kick`, `falar`

<:return:786972739290398780> | Utilidades:
`casos-de-covid`, `tempo`, `noticias`, `google`, `cronômetro`
    
<:return:786972739290398780> | Diversão:
`piada`, `vidente`, `hentai`, `cara-coroa`, `easter-egg`, `yu-gi-oh`, `fodasse`, `laranjo`, `tv`, `bhcareca`, `pão`, `ado`, `gado`
    
<:return:786972739290398780> | NLP:
Risadas, Feliz aniversário, `ræy`

<:return:786972739290398780> | Economia:
`carreira`, `trabalhar`, `money`, `apostar`

<:return:786972739290398780> | Outros:
`userinfo`, `info`, `criador`, `toc-toc`, `l-update`

<:speak:786974134520774676> | Bugs, dúvidas? Entre no nosso [server de apoio](https://discord.gg/a9FU2awhYw) ou reaja a uma mensagem minha com o emoji :bug: e nos conte qual problema você teve!
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
    if "roi" == message.content.lower():
        await message.channel.send("Letícia né?")
    if "número" in message.content.lower() and "aleatório" in message.content.lower():
        await message.channel.send(str(randrange(0, 100)))
    if "criador" == message.content.split()[1]:
        await message.channel.send("D4rkDev#5159, Github: @caue-alves, Email: caue.mendes.rodrigues.alves@gmail.com")
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
@client.event
async def on_member_ban(guild, user):
    await user.create_dm()
    await user.dm_channel.send("Você foi banido do sv, tente se comportar para não ser banido de outros")

@client.event
async def on_reaction_add(reaction, user):
    print('addado')
    if "🐛" in reaction.emoji and reaction.message.author == client.user:
        embedVar=discord.Embed(title="Reportar Bug", description="Vi que você reconheceu um bug, por favor descreva em detalhes o problema que afetou sua experiência com o bot Valzinha")
        global bug
        bug=True
        await reaction.message.channel.send(embed=embedVar)
        await user.create_dm()
        embed2=discord.Embed(description="Vi que você reportou um bug, o que vc acha de entrar no meu [server de apoio](https://discord.gg/a9FU2awhYw) para aprender a me usar melhor e ajudar a me melhorar reportando mais bugs como esse?")
        await user.dm_channel.send(embed=embed2)
client.run(TOKEN)
