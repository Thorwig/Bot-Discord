import discord
from discord.ext import commands,tasks
import os
import random
from youtube_dl import YoutubeDL
from dotenv import load_dotenv
from discord.utils import get
from discord import FFmpegPCMAudio
from discord import TextChannel
from os import system



client = commands.Bot(command_prefix = '_m ')
players = {}


@client.event
async def on_ready():
    print('Le bot est prêt à être utilisé'.format(client))
    print('---------------------------------------------')

################################################ Commandes Réponses #####################################################

@client.command(name="chkounwldl97ba",help="Qui est le plus gros fdp de ce groupe ?")
async def chkounwldl97ba(ctx):
    Usernames = ['Moet ','Pipsou ','Doksi ','Utakata ','Way Wooo ','Moquet ','Bizar ','Mgeder ']
    await ctx.send(''.join(random.choice(Usernames)))

@client.command(help="C'est qui ce mec")
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

@client.command(name='join', help='Tells the bot to join the voice channel')
async def join(ctx):
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()


@client.command(name="leave",help="Quitte le channel vocal")
async def leave(ctx):
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_connected():
        await voice_client.disconnect()
    else:
        await ctx.send("Le bot n'est pas connecté à un channel vocal")

@client.command(pass_context = True)
async def play(ctx, url):
    YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist': 'True'}
    FFMPEG_OPTIONS = {
        'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    voice = get(client.voice_clients, guild=ctx.guild)

    if not voice.is_playing():
        with YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
        URL = info['url']
        voice.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
        voice.is_playing()
        await ctx.send('Ecoute ce banger')
    else:
        await ctx.send("T'as déja de la musique.\nPq tu me casse les couilles")
        return

@client.command(name='pause', help='Mettre en pause')
async def pause(ctx):
    voice = get(client.voice_clients, guild=ctx.guild)

    if voice.is_playing():
        voice.pause()
        await ctx.send("Me dis pas quoi faire fdp")
    
@client.command(name='resume', help='Continuer la musique')
async def resume(ctx):
    voice = get(client.voice_clients, guild=ctx.guild)

    if not voice.is_playing():
        voice.resume()
        await ctx.send('Ecoute moi ce banger')

@client.command(name='stop', help='Arrêter la musique')
async def stop(ctx):
    voice = get(client.voice_clients, guild=ctx.guild)

    if voice.is_playing():
        voice.stop()
        await ctx.send('Ok Jaret')



client.run("OTMyMDUwOTk3MjYwNDc2NDQ2.YeNWIg.4lm4AGaTPAA4X4sNvN9NDRLcMaw")
