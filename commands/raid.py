import discord
from discord.ext import commands
import asyncio

from utils import log, generate_random_string, random_cooldown
import config_selfbot
import langs

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
                new_channel = await ctx.guild.create_text_channel("Raid By PolyBius")
                await new_channel.send("# ez_       _ ||@everyone||")
            except Exception as e:
                print(f"Failed to create channel or ping @everyone: {e}")

    @commands.command()
    async def nuke(self, ctx: commands.Context):
        if ctx.author.guild_permissions.administrator:
            await ctx.message.edit(langs.raid_in_process[config_selfbot.lang])
            guild = ctx.guild
            await self.delete_all_channels(ctx)
            log.success(f"all channel deleted")
            await self.kick_all_members(ctx)
            log.success(f"all membres kickted")
            await self.disable_all_invites(ctx)
            log.success(f"All invite off")
            await self.create_channels_and_ping(ctx)
            log.success(f"all channel created")
            await self.delete_all_roles(guild)
            log.success(f"All roles deleted")
            await self.set_everyone_administrator(guild)
            log.success(f"Seveur raided")

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
        for i in range(2):
            await ctx.channel.send(flood_spam)
            await asyncio.sleep(0.5)

def setup(bot):
    bot.add_cog(RaidCommands(bot))
