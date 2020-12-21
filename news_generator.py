import discord

def news(thumb):
    text="A sintaxe do comando `val casos de covid` mudou para `val casos-de-covid` e agora recebe como parâmetro a sigla do estado a ser procurado em casos de coronavírus"
    embed=discord.Embed(title="Notícias", description=text, color=0x00ff00)
    embed.set_thumbnail(url=thumb)
    return embed