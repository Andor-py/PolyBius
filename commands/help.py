import discord
from discord.ext import commands
import asyncio
import random

import config_selfbot
import langs

class HelpCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx):
        poetry = {
            "fr": [
            "Par ANDOR",
            ],
            "en": [
            "Your attitude determines your direction.",
            "Progress, not perfection.",
            "Embrace the challenges, for they are the stepping stones to success.",
            "Embrace failure as a stepping stone, not a stumbling block.",
            "The only limits that exist are the ones you place on yourself.",
            "Courage is not the absence of fear but the triumph over it.",
            "Dreams don't work unless you do",
            "Opportunities don't happen. You create them.",
            "Don't wait for the perfect moment; take the moment and make it perfect.",
            "The only way to do great work is to love what you do.",
            "Believe you can, and you're halfway there.",
            "Don't watch the clock; do what it does. Keep going"
            ],
        }


        await ctx.message.edit(f"""__**{config_selfbot.selfbot_name} :**__ 
  "{random.choice(poetry[config_selfbot.lang])}"

  📂| __**Utils:**__
 `{config_selfbot.prefix}ping`: {langs.help_general_ping[config_selfbot.lang]}.
 `{config_selfbot.prefix}snipe`: {langs.help_general_snipe[config_selfbot.lang]}
 `{config_selfbot.prefix}snipepic`: Snipe la derniere image supprimée.
 `{config_selfbot.prefix}clear`: {langs.help_general_clear[config_selfbot.lang]}
 `{config_selfbot.prefix}userinfo`: {langs.help_general_user_info[config_selfbot.lang]}.
  🎤| __**Voice:**__
 `{config_selfbot.prefix}joinvc <voice_channel_id>`: {langs.help_voice_vc[config_selfbot.lang]}.
 `{config_selfbot.prefix}joincam <voice_channel_id>`: {langs.help_voice_cam[config_selfbot.lang]}.
 `{config_selfbot.prefix}leavevc`: {langs.help_voice_leave[config_selfbot.lang]}.
  🎲| __**Fun:**__
 `{config_selfbot.prefix}cat`: {langs.help_fun_cat[config_selfbot.lang]}.
 `{config_selfbot.prefix}good`: {langs.help_fun_good[config_selfbot.lang]}.
 `{config_selfbot.prefix}gift <random/nerd/poor>`: {langs.help_fun_gift[config_selfbot.lang]}.
 `{config_selfbot.prefix}hack`: {langs.help_fun_hack[config_selfbot.lang]}.
 `{config_selfbot.prefix}howfemboy`: {langs.help_fun_femboy[config_selfbot.lang]}.
  🏯| __**Raid:**__
 `{config_selfbot.prefix}spam`: Spam. (`{config_selfbot.prefix}spam` 2 hello).
 `{config_selfbot.prefix}call`: {langs.help_fun_call[config_selfbot.lang]}.
 `{config_selfbot.prefix}flood`: Flood.
 `{config_selfbot.prefix}kickall`: {langs.help_raid_kick[config_selfbot.lang]}.
 `{config_selfbot.prefix}banall`: {langs.help_raid_banall[config_selfbot.lang]}
 `{config_selfbot.prefix}nuke`: Supprime tout les rôles, salons, invitations, permitions et les membres d'un serveur. 
  🔧| __**Tools:**__
 `{config_selfbot.prefix}closealldm`: {langs.help_tools_close_dm[config_selfbot.lang]}.
 `{config_selfbot.prefix}botclosedm`: {langs.help_tools_close_dm_bots[config_selfbot.lang]}.
 `{config_selfbot.prefix}dmall`: {langs.help_raid_dmall[config_selfbot.lang]}
 `{config_selfbot.prefix}bump`: bump un nombre donné de fois un serveur. (`{config_selfbot.prefix}bump 2`)
 `{config_selfbot.prefix}autobump`: bump un nombre ilimité de fois un serveur.
 `{config_selfbot.prefix}stopautobump`: Stop l'autobump.
  😎| __**Fake It:**__
  `{config_selfbot.prefix}kit`: vous crée une conversation dm avec tout ce qu'il faut pour se faire un bon profil de catfish.
  `{config_selfbot.prefix}autoxp`: Genere un nobre defini de messages phantome pour vous faire xp sans rien faire.
  `{config_selfbot.prefix}connectvc`: Siplement un nom plus discret pour la commande `{config_selfbot.prefix}autoxp`(La commande reste la meme.)

  ⚙️| __**Config:**__
 `{config_selfbot.prefix}nitrosniper`: {langs.help_general_sniper[config_selfbot.lang]}.
 `{config_selfbot.prefix}restart`: {langs.help_config_restart[config_selfbot.lang]}.
 `{config_selfbot.prefix}stop`: {langs.help_config_stop[config_selfbot.lang]}.
 `{config_selfbot.prefix}lang`""")
        await asyncio.sleep(config_selfbot.deltime)
        await ctx.message.delete()
   

