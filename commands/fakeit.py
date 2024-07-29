import discord
from discord.ext import commands
import asyncio
import time

from utils import random_cooldown
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



        except Exception as e:
            await ctx.send(f"Failed to send setup information: {str(e)}", delete_after=5)
