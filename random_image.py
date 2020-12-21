import discord
from random import randrange

def get_random_image_from_array(array : list, title : str, desc : str, color, member):
    img=array[randrange(0, len(array))]
    embed=discord.Embed(title=title, description=desc, color=color)
    embed.set_image(url=img)
    embed.set_thumbnail(url=member.avatar_url)
    return embed