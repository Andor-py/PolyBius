import discord
from discord.ext import commands, tasks
import asyncio
from colorama import Fore, Style, Back
import yt_dlp  # Assurez-vous que cette ligne est présente
import os  # Pour la gestion des fichiers
import re  # Importer la bibliothèque pour nettoyer le nom du fichier
from utils import log, random_cooldown
import config_selfbot
import langs
from datetime import datetime


class ToolsCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.auto_bump_task = None
        self.auto_bump_channel = None
        self.auto_bump_count = 0


    @commands.command()
    async def bump(self, ctx: commands.Context):
        message_split = ctx.message.content.split()
        if isinstance(ctx.channel, discord.DMChannel) or isinstance(ctx.channel, discord.GroupChannel):
            await ctx.message.edit(langs.tool_bump_not_found[config_selfbot.lang], delete_after=config_selfbot.deltime)
            return

        try:
            await ctx.guild.fetch_member(302050872383242240)
        except discord.NotFound:
            await ctx.message.edit(langs.tool_bump_not_found[config_selfbot.lang], delete_after=config_selfbot.deltime)
            return

        try:
            count = int(message_split[1])
        except Exception:
            await ctx.message.edit(f"{langs.spam_invalid[config_selfbot.lang]}!", delete_after=config_selfbot.deltime)
            return

        if count >= 100:
            await ctx.message.edit(langs.spam_too_much[config_selfbot.lang], delete_after=config_selfbot.deltime)
            return

        await ctx.message.edit(f"{langs.tool_bump[config_selfbot.lang]} {count} {langs.tool_bump_two[config_selfbot.lang]}", delete_after=config_selfbot.deltime)

        command = [_ for _ in await ctx.channel.application_commands() if _.name == 'bump' and _.application_id == 302050872383242240][0]

        for i in range(count):
            await command.__call__(channel=ctx.channel)
            log.success(f"""Bumped {ctx.guild.name}({ctx.guild.id}) for the {i + 1} time.
Still need to bump {count - i - 1} time in {ctx.channel.name}({ctx.channel.id}).""")
            await asyncio.sleep(random_cooldown(7200, 7387))



    @commands.command()
    async def autobump(self, ctx: commands.Context):
        if self.auto_bump_task is not None and self.auto_bump_task.is_running():
            await ctx.message.edit("~~On auto bump ça !~~ C'est pas bon", delete_after=config_selfbot.deltime)
            return

        self.auto_bump_channel = ctx.channel
        self.auto_bump_task = self.auto_bump.start()
        await ctx.message.edit("On auto bump ça !", delete_after=config_selfbot.deltime)

    @tasks.loop(hours=2)
    async def auto_bump(self):
        if self.auto_bump_channel is not None:
            command = next((cmd for cmd in await self.auto_bump_channel.application_commands() if cmd.name == 'bump' and cmd.application_id == 302050872383242240), None)
            
            if command is not None:
                await command(self.auto_bump_channel)
                self.auto_bump_count += 1
                log.success(f"Auto-bumped {self.auto_bump_channel.guild.name}({self.auto_bump_channel.guild.id}) for the {self.auto_bump_count} time in {self.auto_bump_channel.name}({self.auto_bump_channel.id}).")

    @commands.command()
    async def stopautobump(self, ctx: commands.Context):
        if self.auto_bump_task is not None and self.auto_bump_task.is_running():
            self.auto_bump_task.cancel()
            self.auto_bump_task = None
            self.auto_bump_channel = None
            self.auto_bump_count = 0
            await ctx.message.edit("on stop tout !", delete_after=config_selfbot.deltime)
        else:
            await ctx.message.edit("y'as rien a stopé...", delete_after=config_selfbot.deltime)




    @commands.command()
    async def dmall(self, ctx: commands.Context):
        message_split = ctx.message.content.split()
        dmall_content = ctx.message.content.replace(f"{message_split[0]} ", "")
        try:
            message_split[1]
        except Exception:
            await ctx.message.edit(langs.raid_dm_all_fail[config_selfbot.lang], delete_after=config_selfbot.deltime)
            return

        friends = self.bot.friends

        log.separate_text("DM ALL")

        print(f"{Fore.BLUE}Friends Counter: {len(friends)} | Message:\n{dmall_content}{Style.RESET_ALL}")

        await ctx.message.edit(langs.raid_dm_all[config_selfbot.lang])

        for friend in friends:
            try:
                await friend.user.send(dmall_content)
                log.success(f"@{friend.user.name}({friend.user.id})")
                await asyncio.sleep(random_cooldown(0.5, 2))
            except discord.Forbidden:
                log.fail(f"@{friend.user.name}({friend.user.id})")
            except discord.CaptchaRequired:
                log.important("Captcha Required!")
                log.separate("DM ALL")
                await ctx.message.edit(langs.raid_dm_all_captcha[config_selfbot.lang], delete_after=config_selfbot.deltime)
                return

        log.separate("DM ALL")


        await ctx.message.edit(langs.raid_dm_all_success[config_selfbot.lang], delete_after=config_selfbot.deltime)

    @commands.command()
    async def closealldm(self, ctx: commands.Context):

        await ctx.message.edit(langs.tool_close_dms[config_selfbot.lang])

        for dm_channel in self.bot.private_channels:
            if isinstance(dm_channel, discord.DMChannel) and dm_channel.me.id == self.bot.user.id:
                await dm_channel.close()
                await asyncio.sleep(random_cooldown(0.5, 2))
        
        await ctx.message.edit(langs.tool_close_dms_success[config_selfbot.lang], delete_after=config_selfbot.deltime)

    @commands.command()
    async def botclosedm(self, ctx: commands.Context):
        
        await ctx.message.edit(langs.tool_close_dms_bots[config_selfbot.lang])

        for dm_channel in self.bot.private_channels:
            if isinstance(dm_channel, discord.DMChannel) and dm_channel.recipient.bot:
                await dm_channel.close()
                await asyncio.sleep(random_cooldown(0.5, 2))

        await ctx.message.edit(langs.tool_close_dms_bots_success[config_selfbot.lang], delete_after=config_selfbot.deltime)



    @commands.command()
    async def mp3(self, ctx, url: str):
        status_message = await ctx.send("Conversion en cours...")  # Message de statut

        # Récupérer l'heure actuelle et la formater pour le nom du fichier
        current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        # Nouveau nom de fichier
        new_file_name = f"Votre_fichier_{current_time}.mp3"

        # Dossier de téléchargement
        download_dir = 'downloads'

        # Définir les options pour yt-dlp
        options = {
            'format': 'bestaudio/best',
            'outtmpl': f'{download_dir}/%(title)s.%(ext)s',  # Télécharge avec le nom original dans le dossier downloads
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }

        try:
            with yt_dlp.YoutubeDL(options) as ydl:
                info = ydl.extract_info(url, download=True)  # Télécharger et extraire l'audio
                original_file_name = ydl.prepare_filename(info).replace('.webm', '.mp3')

            # Chemin complet vers le fichier téléchargé
            original_file_path = os.path.join(download_dir, os.path.basename(original_file_name))

            # Nouveau chemin avec le nouveau nom
            new_file_path = os.path.join(download_dir, new_file_name)

            # Renommer le fichier téléchargé
            os.rename(original_file_path, new_file_path)

            # Envoyer le fichier MP3 à l'utilisateur
            await ctx.send("Voici votre fichier:", file=discord.File(new_file_path))

        except Exception as e:
            await ctx.send(f"Erreur lors du téléchargement ou du renommage : {str(e)}")

        finally:
            # Supprimer le message de statut
            await status_message.delete()



    @commands.command()
    async def opus(self, ctx, url: str = None):
        if ctx.message.attachments:
            attachment = ctx.message.attachments[0]
            status_message = await ctx.send("Conversion en cours...")  # Message de statut
            
            opus_file = f'downloads/{attachment.filename.rsplit(".", 1)[0]}.opus'

            # Téléchargez le fichier et convertissez-le
            await attachment.save(f'downloads/{attachment.filename}')
            os.system(f"ffmpeg -y -i downloads/{attachment.filename} -c:a libopus -b:a 192k -strict -2 {opus_file}")
            
            # Envoyez le fichier en tant que note vocale
            await ctx.send(file=discord.File(opus_file))

            # Supprimez le message de commande et le message de statut
            await ctx.message.delete()
            await status_message.delete()  # Supprimer le message "Conversion en cours..."

        elif url:
            status_message = await ctx.send("Conversion en cours...")  # Message de statut
            
            # Ajoutez ici votre logique de téléchargement depuis l'URL et de conversion
            # Par exemple :
            # os.system(f"ffmpeg -y -i '{url}' -c:a libopus -b:a 192k -strict -2 {opus_file}")
            
            # Envoyer le fichier après conversion
            await ctx.send(file=discord.File(opus_file))

            # Supprimez le message de commande et le message de statut
            await ctx.message.delete()
            await status_message.delete()  # Supprimer le message "Conversion en cours..."



