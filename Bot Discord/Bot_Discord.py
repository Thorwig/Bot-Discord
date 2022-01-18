import discord
from discord.ext import commands,tasks
import os
import random
from youtube_dl import YoutubeDL
from discord.utils import get
from discord import FFmpegPCMAudio
from discord import TextChannel
from itertools import cycle



client = commands.Bot(command_prefix = '_m ')
players = {}

Usernames_debauche = ['Moet ','Pipsou ','Doksi ','Utakata ','Way Wooo ','Moquet ','Bizar ','Mgeder ']


@client.event
async def on_ready():
    print('Le bot est prêt à être utilisé'.format(client))
    print('---------------------------------------------')

################################################ Commandes Réponses #####################################################

@client.command(name="chkounwldl97ba",help="Qui est le plus gros fdp de ce groupe ?")
async def chkounwldl97ba(ctx):
    
    await ctx.send(''.join(random.choice(Usernames_debauche)))

@client.command(help="C'est qui ce mec")
async def cestle(ctx):
    await ctx.send('WAY WOOOOO')

@client.command(name="chien",help="ouaf ouaf boula")
async def chien(ctx):
    rep =['pipi','ouaf ouaf boula']
    await ctx.send(''.join(random.choice(rep)))

@client.command(name="teamlol",help="Les 5 mecs qui vont jouer")
async def teamlol(ctx):
    random.shuffle(Usernames_debauche)
    await ctx.send(Usernames_debauche[i] for i in range (5))

@client.command(name="supprimer",help="Entrez le nombre de messages à supprimer")
async def supprimer(ctx, nombre_messages: int):
    messages = await ctx.channel.history(limit=nombre_messages + 1).flatten()

    for each_message in messages:
        await each_message.delete()

@client.command(name="insulte",help="Insulte un mec du groupe")
async def insulte(ctx, arg: str):
    insultes = [arg + ' 97ba', arg + ' kathezou', arg + ' wld l97ba','Gangbang ' + arg + ' à 16h','gneu gneu gneu respire frère', 'Non jtm pas toi']
    await ctx.send(''.join(random.choice(insultes)))

@client.command(name="eske",help="Est-ce que ... ?")
async def eske(ctx):
    choice = ['Oui', 'Non']
    await ctx.send(''.join(random.choice(choice)))

@client.command(name="dinguerie",help="Balance une dinguerie")
async def dinguerie(ctx):
    dingueries = ['Je pisse sur tout le monde dans ce groupe à part Mouad, mon roi, mon créateur',
              'Rappel du jour: Doxy est un être détestable qui va te rabaisser pour se sentir existant',
              'Deuxième rappel du jour: Doxy vole les blagues de tout le monde pour se sentir drôle',
              'Rappel du jour: Mangez 5 fruits et légumes par jour et pas 5 big mac pas vrai Amoket',
              'Qui suis-je? Je suis un dictateur ayant vécu au 21ème siècle, je bande sur des filles mineures aux gros seins et je me moque des handicapés.\nEh non je suis pas Momosix. Je suis Utakata',
              "Palmarès poupa: j'ai baisé un oreiller devant 10 personnes",
              "Palmarès soulmore: j'ai zoulou 30 meufs hier pendant que biz filmait. Foutaises ",
              "Thorwig, tu m'as créer à la place de rechercher un stage. C'est bien papa, tu sais déjà que tu vas redoubler comme l'autre con la",
              "Bonjour, NEGRO SALE NEGRO KHANEZ NEGRO PUE YEKH"]
    await ctx.send(''.join(random.choice(dingueries)))

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
        await ctx.send("Toi dégage sale chien")

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

################################################ Messages réguliers #####################################################


################################################ Signalement erreurs #####################################################

@client.event
async def on_command_error(ctx,error):
    if isinstance(error,commands.MissingRequiredArgument):
        await ctx.send('ERREUR. Mon codeur est trop con, il a pas su gérer cette erreur')



client.run("OTMyMDUwOTk3MjYwNDc2NDQ2.YeNWIg.4lm4AGaTPAA4X4sNvN9NDRLcMaw")
