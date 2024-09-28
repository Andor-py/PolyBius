import discord
from discord.ext import commands, tasks
import asyncio
import time
from colorama import Fore, Style, Back
from utils import log, random_cooldown

import config_selfbot
import langs



class FakeItCommands(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot
        self.sniped_messages: dict = {}


    @commands.command()
    async def kit(self, ctx: commands.Context):
        DISPLAY_NAME = "Emma ~ <3"
        PRONOUNS = "She/Her"
        BIO = "˚　　　　✦　　.　　. 　 ˚✦　.　 　　.　　　　　　 ✦　　🌙 　˚　.　 *　　 .　　˚　　　. ✦ 　　　　.   　 　　　˚　　　　　*　✦　 　　✦　　　.　　.　　　✦　　˚ 　　　🌃 　˚　.🪐　 *　　.*　✦　..　　˚　　　.✦"
        IMAGE_PATH = r"\\PolyBius\\utils\\PdP.png"  # Utilisation de raw string

        try:
            with open('nuclear_icon.png', 'rb') as image:
                nuclear_icon = image.read()
        # Vous pouvez faire d'autres opérations avec `nuclear_icon` ici
        except IOError as e:
            print("Erreur lors de l'ouverture du fichier :", e)

        try:
            # Créer un groupe privé avec votre compte
            group_channel = await self.bot.create_group()

            # Renommer le groupe en "Kit"
            await group_channel.edit(name="Kit PolyBius", icon=nuclear_icon)

            # Envoyer le message avec les informations de configuration
            message_content = f"""
Nom:
```
{DISPLAY_NAME}
```
Pronoms:
```
{PRONOUNS}
```
Bio: 
```
{BIO}
```
Pdp: https://i.imgur.com/tXocsqo.png """

            msg = await group_channel.send(message_content)
            await group_channel.send(f"<@{self.bot.user.id}>")
            await msg.unack()
            await ctx.message.delete()



        except Exception as e:
            await ctx.send(f"Failed to send setup information: {str(e)}", delete_after=5)


@commands.command()
async def connectvc(self, ctx: commands.Context):
        message_split = ctx.message.content.split()
        try:
            count = int(message_split[1])  # Tenter de convertir la deuxième partie en entier
        except Exception:
            await ctx.message.edit(content="envoi impossible!", delete_after=config_selfbot.deltime)
            return

        if count >= 1000:
            await ctx.message.edit(content="nombre trop grand", delete_after=config_selfbot.deltime)
            return

        await ctx.message.edit(content="_ _", delete_after=3)

        for i in range(count):
            # Attendre un intervalle aléatoire entre 60 et 70 secondes
            cooldown_time = 35
            sent_message = await ctx.send("_ _", delete_after=0.7)
            log.success(f"Message envoyé {i + 1} fois sur {ctx.guild.name} dans {ctx.channel.name}.")
            await asyncio.sleep(cooldown_time)

@commands.command()
async def connectvc(self, ctx: commands.Context):
        message_split = ctx.message.content.split()
        try:
            count = int(message_split[1])  # Tenter de convertir la deuxième partie en entier
        except Exception:
            await ctx.message.edit(content="envoi impossible!", delete_after=config_selfbot.deltime)
            return

        if count >= 1000:
            await ctx.message.edit(content="nombre trop grand", delete_after=config_selfbot.deltime)
            return

        await ctx.message.edit(content="_ _", delete_after=3)

        for i in range(count):
            # Attendre un intervalle aléatoire entre 60 et 70 secondes
            cooldown_time = 35
            sent_message = await ctx.send("_ _", delete_after=0.7)
            log.success(f"Message envoyé {i + 1} fois sur {ctx.guild.name} dans {ctx.channel.name}.")
            await asyncio.sleep(cooldown_time)