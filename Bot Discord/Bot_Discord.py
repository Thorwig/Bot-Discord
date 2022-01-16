from distutils import command
from discord.ext import commands
import random

class BOTMOUADTEST(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="$")
    
    async def on_ready(self):
        print('We have logged in as {0.user}'.format(self))
        
    async def on_message(ctx):
        if ctx.author == bot.user:
            return
    async def crazyresponse(ctx):
        if ctx.content.startswith('chkoun wld l97ba?'):
            Usernames = ['Moet ','Pipsou ','Doksi ','Utakata ','Way Wooo ','Moquet ','Bizar ','Mgeder ']
            await ctx.channel.send(''.join(random.choice(Usernames)))

        if ctx.content.startswith(('Chien').lower()):
            await ctx.channel.send('pipi')

        if ctx.content.startswith("C'est le ?"):
            await ctx.channel.send('WAY WOOOOO')

        if ctx.content.startswith("Qui tape le xanax ?"):
            await ctx.channel.send('HAMZA')

        if ctx.content.startswith("Team lol"):
            Usernames = ['Moet ','Pipsou ','Doksi ','Utakata ','Way ','Moquet ','Bizar ','Mgeder ']
            random.shuffle(Usernames)
            await ctx.channel.send(Usernames[i] for i in range (5))
        
        if ctx.content.startswith("eske"):
            choice = ['Oui', 'Non']
            await ctx.channel.send(''.join(random.choice(choice)))

        if ctx.content.startswith("!encaisse"):
            membername = str(ctx.content.split()[1])
            await ctx.channel.send(membername + " nos")

        if ctx.content.startswith("!insulte soumiya"):
            Usernames = ['Soumiya 97ba ','Soumiya kathezou ','Soumiya kan7wiha ','Gangbang Soumiya à 16h ','Site pour voir le bukkake de Soumiya : www.bukakesoumiya.com ',"C'est bon frère, laisse la tranquille ",'Ntm toi aussi, respecte ','Le WAY WOOOO ']
            await ctx.channel.send(''.join(random.choice(Usernames)))

bot = BOTMOUADTEST()
bot.run("OTMyMDUwOTk3MjYwNDc2NDQ2.YeNWIg.4lm4AGaTPAA4X4sNvN9NDRLcMaw")