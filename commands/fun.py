import discord
from discord.ext import commands
import asyncio
import random
import requests
import json
import base64
import time  # Import pour obtenir le timestamp

import config_selfbot
import langs


class FunCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.good_person = config_selfbot.good_person
        self.badwords = config_selfbot.badwords
        self.good_person_list = config_selfbot.good_person_list

    @commands.command()
    async def good(self, ctx):
        if self.good_person:
            self.good_person = False
            await ctx.message.edit(f"🔥 Good Person {langs.disable[config_selfbot.lang]}")
            await asyncio.sleep(config_selfbot.deltime)
            await ctx.message.delete()
        else:
            self.good_person = True
            await ctx.message.edit(f"🌈 Good Person {langs.enable[config_selfbot.lang]}")
            await asyncio.sleep(config_selfbot.deltime)
            await ctx.message.delete()

    @commands.Cog.listener()
    async def on_message(self, ctx):
        if self.good_person and ctx.author.id == self.bot.user.id:
            if any(word in ctx.content.lower() for word in self.badwords):
                await ctx.edit(random.choice(self.good_person_list))

    @commands.command()
    async def hack(self, ctx):
        if ctx.message.mentions:
            user = ctx.message.mentions[0]
        else:
            try:
                user = self.bot.get_user(int(ctx.message.content.split()[1]))
            except Exception:
                user = ctx.author
        
        await ctx.message.edit(f"---{langs.fun_hack_step_one[config_selfbot.lang]} <@{user.id}>---")
        await asyncio.sleep(3.1)
        await ctx.channel.send(f"{langs.fun_hack_step_two[config_selfbot.lang]}...")
        await asyncio.sleep(3.1)
        await ctx.channel.send(f"{langs.fun_hack_step_three[config_selfbot.lang]} **{user.name}@gmail.com**")
        await asyncio.sleep(3.1)
        await ctx.channel.send(langs.fun_hack_step_four[config_selfbot.lang])
        await asyncio.sleep(3.1)
        await ctx.channel.send(f"{langs.fun_hack_step_five[config_selfbot.lang]} <@{user.id}>")
        
        # Nouvelle ligne : "minaje du token" avec fautes d'orthographe
        await asyncio.sleep(3.1)
        await ctx.channel.send("minaje du token...")
        
        # Encodage Base64 de l'ID de l'utilisateur
        user_id_base64 = base64.b64encode(str(user.id).encode('utf-8')).decode('utf-8')[:-2]  # Retirer les deux derniers caractères
        
        # Calcul du timestamp
        unix_timestamp = int(time.time()) -1293840000
        unix_timestamp_base64 = base64.b64encode(str(unix_timestamp).encode('utf-8')).decode('utf-8')[:-8]  # Retirer les deux derniers caractères
        
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        alphabet2 = "abcdefghijklmnopqrstuvwxyz"
        numbers = "0123456789"
        fintoken = ''.join(random.choice(numbers) for _ in range(1))
        debuttoken = ''.join(random.choice(alphabet + alphabet2 + numbers) for _ in range(4))

        # Message final
        final_message = f"Token de <@{user.id}> : `{user_id_base64}.{debuttoken}_{fintoken}.`||Mdrr tkt c pour de fo||"
        # Envoi du premier message de token
        final_message_display = await ctx.channel.send(f"Token de <@{user.id}> : `{user_id_base64}.#####.############################`")
        await asyncio.sleep(3.1)
        
        # Modifications des trois dernières lignes
        await asyncio.sleep(1.3)
        await final_message_display.edit(f"Token de <@{user.id}> : `{user_id_base64}.{debuttoken}_{fintoken}.############################`")
        await ctx.channel.send(f"-# ||Tout ceci est bien évidemment une blague.||")

    @commands.command()
    async def cat(self, ctx):
        response = requests.get('https://api.thecatapi.com/v1/images/search')
        if response.status_code == 200:
            data = json.loads(response.text)
            cat_image_url = data[0]['url']
            await ctx.message.edit(cat_image_url)
        else:
            await ctx.message.edit(f"Failed to fetch a cute cat: {response.text}")
            await asyncio.sleep(config_selfbot.deltime)
            await ctx.message.delete()

    @commands.command()
    async def gift(self, ctx):
        try:
            gift_type = ctx.message.content.split()[1]
        except Exception:
            gift_type = "random"
        

        if gift_type == "poor":
            await ctx.message.edit("discord.gift/vhnuzE2YkNCZ7sfYHHKebKXB")
        elif gift_type == "nerd":
            await ctx.message.edit("discord.gift/Udzwm3hrQECQBnEEFFCEwdSq")
        else:
            alphabet = "abcdefghijklmnopqrstuvwxyz"
            numbers = "0123456789"
            gift_code = ''.join(random.choice(alphabet + numbers) for _ in range(16))
            await ctx.message.edit(f"discord.gift/{gift_code}")

    @commands.command()
    async def howfemboy(self, ctx):
        if ctx.message.mentions:
            user = ctx.message.mentions[0]
        else:
            try:
                user = self.bot.get_user(int(ctx.message.content.split()[1]))
            except Exception:
                user = ctx.author

        rng = random.randint(1, 100)

        if rng >= 85:
            await ctx.message.edit(f"<@{user.id}> {langs.is_[config_selfbot.lang]} **{rng}%** [femboy](https://tenor.com/bQmRX.gif) 💅!")
        if rng >= 75:
            await ctx.message.edit(f"<@{user.id}> {langs.is_[config_selfbot.lang]} **{rng}%** [femboy](https://tenor.com/bUyzv.gif) 😈!")
        else:
            await ctx.message.edit(f"<@{user.id}> {langs.is_[config_selfbot.lang]} **{rng}%** femboy!")
