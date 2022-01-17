import discord
from discord.ext import commands,tasks
import os
import random
import Youtube_Read

client = commands.Bot(command_prefix = '_m ')

@client.event
async def on_ready():
    print('Le bot est prêt à être utilisé'.format(client))
    print('---------------------------------------------')



################################################ Commandes Réponses #####################################################

@client.command(name="chkounwldl97ba",help="Qui est le plus gros fdp de ce groupe ?")
async def chkounwldl97ba(ctx):
    Usernames = ['Moet ','Pipsou ','Doksi ','Utakata ','Way Wooo ','Moquet ','Bizar ','Mgeder ']
    await ctx.send(''.join(random.choice(Usernames)))

@client.command(name="c'est le",help="C'est qui ce mec")
async def cestle(ctx):
    await ctx.send('WAY WOOOOO')

@client.command(name="chien",help="ouaf ouaf boula")
async def chien(ctx):
    await ctx.send('pipi')

@client.command(name="teamlol",help="Les 5 mecs qui vont jouer")
async def teamlol(ctx):
    Usernames = ['Moet ','Pipsou ','Doksi ','Utakata ','Way ','Moquet ','Bizar ','Mgeder ']
    random.shuffle(Usernames)
    await ctx.send(Usernames[i] for i in range (5))

@client.command(name="supprimer",help="Entrez le nombre de messages à supprimer")
async def supprimer(ctx, nombre_messages: int):
    messages = await ctx.channel.history(limit=nombre_messages + 1).flatten()

    for each_message in messages:
        await each_message.delete()

@client.command(name="insulte",help="Insulte un mec du groupe")
async def insulte(ctx, arg: str):
    Usernames = [arg + ' 97ba', arg + ' kathezou', arg + ' wld l97ba','Gangbang ' + arg + ' à 16h']
    await ctx.send(''.join(random.choice(Usernames)))

@client.command(name="eske",help="Est-ce que ... ?")
async def eske(ctx):
    choice = ['Oui', 'Non']
    await ctx.send(''.join(random.choice(choice)))


################################################ Commandes musique #####################################################

@client.command(name="join",help="Rejoins le channel vocal")
async def join(ctx):
    if not ctx.message.author.voice:
        await ctx.send("{} n'est pas connecté à un channel vocal".format(ctx.message.author.name))
        return
    else:
        channel = ctx.author.voice.channel
        await channel.connect()

@client.command(name="leave",help="Quitte le channel vocal")
async def leave(ctx):
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_connected():
        await voice_client.disconnect()
    else:
        await ctx.send("The bot is not connected to a voice channel.")

client.run("OTMyMDUwOTk3MjYwNDc2NDQ2.YeNWIg.4lm4AGaTPAA4X4sNvN9NDRLcMaw")
