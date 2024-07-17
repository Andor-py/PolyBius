import subprocess
try:
    import sys, os, platform
    import ctypes
    import datetime, time
    import threading
    import asyncio
    import config_selfbot
    import langs
    from utils import rpc, log, __version__
    from commands import *
    from colorama import Fore, Style, Back
    import requests
    #import twocaptcha
    import discord
    from discord.ext import commands
    import nacl
except ImportError:
    import sys, os
    if os.name == 'nt':
     subprocess.check_call([sys.executable, "-m", "pip", "install", '-r' , 'requirements.txt'])
    else:
     subprocess.check_call([sys.executable, "-m", "pip3", "install", '-r' , 'requirements.txt'])
    import platform
    import ctypes
    import datetime, time
    import threading
    import asyncio
    import config_selfbot
    import langs
    from utils import rpc, log, __version__
    from commands import *
    from colorama import Fore, Style, Back
    import requests
    #import twocaptcha
    import discord
    from discord.ext import commands
    import nacl

os.system('cls' if os.name == 'nt' else 'clear')
DARK_PURPLE = '\033[38;5;54m'
LIGHT_PURPLE = '\033[38;5;165m'

print(fr"""{DARK_PURPLE}   




     $$$$$$$\            $$\           $$$$$$$\  $$\                     
     $$  __$$\           $$ |          $$  __$$\ \__|                    
     $$ |  $$ | $$$$$$\  $$ |$$\   $$\ $$ |  $$ |$$\ $$\   $$\  $$$$$$$\ 
     $$$$$$$  |$$  __$$\ $$ |$$ |  $$ |$$$$$$$\ |$$ |$$ |  $$ |$$  _____|
     $$  ____/ $$ /  $$ |$$ |$$ |  $$ |$$  __$$\ $$ |$$ |  $$ |\$$$$$$\  
     $$ |      $$ |  $$ |$$ |$$ |  $$ |$$ |  $$ |$$ |$$ |  $$ | \____$$\ 
     $$ |      \$$$$$$  |$$ |\$$$$$$$ |$$$$$$$  |$$ |\$$$$$$  |$$$$$$$  | 
     \__|       \______/ \__| \____$$ |\_______/ \__| \______/ \_______/ 
                             $$\   $$ |                                  
                             \$$$$$$  |               {LIGHT_PURPLE}v{__version__}{DARK_PURPLE}                   
                              \______/                Powered by {LIGHT_PURPLE}Nuclear{Style.RESET_ALL}                             


""")



def set_terminal_title(title):
    system = platform.system()
    if system == 'Windows':
        ctypes.windll.kernel32.SetConsoleTitleW(title)
    elif system == 'Darwin':
        subprocess.run(['osascript', '-e', f'tell application "Terminal" to set custom title of front window to "{title}"'])
    elif system == 'Linux':
        sys.stdout.write(f"\x1b]2;{title}\x07")
        sys.stdout.flush()

try:
   set_terminal_title("| PolyBius Selfbot |")
except Exception as e:
   log.warning(f"Error while trying to change the terminal name: {e}")


if config_selfbot.token == "":
   config_selfbot.token = input("Token: ")

if config_selfbot.lang == "":
   print("""Language Choice / Choix de la langue:
fr: Français
en: English""")
   config_selfbot.lang = input("fr / en: ")

if config_selfbot.prefix == "":
   config_selfbot.prefix = input("Prefix: ")

if config_selfbot.selfbot_name == "":
   config_selfbot.selfbot_name = input("Selfbot name: ")



check_loop = True


# Prevent from starting the selfbot with another discord library
if not discord.__title__ == "discord.py-self":
    log.critical(f"{langs.error_discord_version[config_selfbot.lang]} https://github.com/Sitois/Nuclear/releases/tag/{check_latest_version('Sitois', 'Nuclear-V2')}")
    exit()

# Prevent from starting the selfbot with the broken pip version
if discord.__version__.startswith("2.0.0"):
    log.critical(f"{langs.error_discord_version[config_selfbot.lang]} https://github.com/Sitois/Nuclear-V2/releases/tag/{check_latest_version('Sitois', 'Nuclear-V2')}")
    exit()



log.start(langs.start_text[config_selfbot.lang])



####################
#  start           #
#   setup     !!!  #
####################
today_date = datetime.datetime.today()

# TODO: Finish captcha handler
"""
API_KEY = 'YOUR_API_KEY'


solver = twocaptcha.TwoCaptcha(API_KEY)

async def handle_captcha(exc: discord.CaptchaRequired, bot: commands.Bot) -> str:
    result = solver.solve_captcha(site_key=exc.sitekey, page_url="https://discord.com/")
    return result['code']
"""

# Define the bot instance
bot = commands.Bot(command_prefix=config_selfbot.prefix, self_bot=True, help_command=None)#, captcha_handler=handle_captcha)

# Get the start timestamp to put the time it took to start at on_ready()
start_time = time.time()

@bot.event
async def on_ready():
    global today_date
    global start_time

    log.separate_yellow()

    # Load commands from cogs
    try:
        await bot.add_cog(UtilsCommands(bot))
        log.success(f"Utils Commands: {langs.cog_success[config_selfbot.lang]}")
    except Exception as e:
        log.fail(f"Utils Commands: {langs.cog_fail[config_selfbot.lang]} {e}")
    try:
        await bot.add_cog(FakeItCommands(bot))
        log.success(f"Fake It Commands: {langs.cog_success[config_selfbot.lang]}")
    except Exception as e:
        log.fail(f"Fake It Commands: {langs.cog_fail[config_selfbot.lang]} {e}")
    try:
        await bot.add_cog(VoiceCommands(bot))
        log.success(f"Voice Commands: {langs.cog_success[config_selfbot.lang]}")
    except Exception as e:
        log.fail(f"Voice Commands: {langs.cog_fail[config_selfbot.lang]} {e}")
    try:
        await bot.add_cog(ConfigCommands(bot))
        log.success(f"Config Commands: {langs.cog_success[config_selfbot.lang]}")
    except Exception as e:
        log.fail(f"Config Commands: {langs.cog_fail[config_selfbot.lang]} {e}")
    try:
        await bot.add_cog(RaidCommands(bot))
        log.success(f"Raid Commands: {langs.cog_success[config_selfbot.lang]}")
    except Exception as e:
        log.fail(f"Raid Commands: {langs.cog_fail[config_selfbot.lang]} {e}")
    try:
        await bot.add_cog(ToolsCommands(bot))
        log.success(f"Tools Commands: {langs.cog_success[config_selfbot.lang]}")
    except Exception as e:
        log.fail(f"Tools Commands: {langs.cog_fail[config_selfbot.lang]} {e}")

    # Print when the bot is ready to receive and answer to commands
    log.alert(f"{langs.ready_text[config_selfbot.lang]} @{bot.user.name} ({bot.user.id}), {langs.ready_text_two[config_selfbot.lang]} {round(time.time()) - round(start_time)} {langs.ready_text_three[config_selfbot.lang]}")

    log.separate_magenta()

    assets = {"large_image": config_selfbot.assets["large_image"] if rpc.read_variable_json("large_image") == "VOID" else rpc.read_variable_json("large_image"),
              "large_text": config_selfbot.assets["large_text"] if rpc.read_variable_json("large_text") == "VOID" else rpc.read_variable_json("large_text"),
              "small_image": config_selfbot.assets["small_image"] if rpc.read_variable_json("small_image") == "VOID" else rpc.read_variable_json("small_image"),
              "small_text": config_selfbot.assets["small_text"] if rpc.read_variable_json("small_text") == "VOID" else rpc.read_variable_json("small_text")
             }
    activity = discord.Activity(type=discord.ActivityType.playing,
                                name=config_selfbot.activity_name if rpc.read_variable_json("activity_name") == "VOID" else rpc.read_variable_json("activity_name"),
                                details=config_selfbot.activity_details if rpc.read_variable_json("activity_details") == "VOID" else rpc.read_variable_json("activity_details"),
                                state=config_selfbot.activity_state if rpc.read_variable_json("activity_state") == "VOID" else rpc.read_variable_json("activity_state"),
                                timestamps={"start": time.time()},
                                assets=assets,
                                application_id=config_selfbot.application_id,
                                buttons=[config_selfbot.activity_button_one if rpc.read_variable_json("activity_button_one") == "VOID" else rpc.read_variable_json("activity_button_one"), config_selfbot.activity_button_two if rpc.read_variable_json("activity_button_two") == "VOID" else rpc.read_variable_json("activity_button_two")])




def restart_selfbot():
    python = sys.executable
    os.execl(python, python, *sys.argv)

@bot.command()
async def restart(ctx):
    await ctx.message.edit(langs.restart_command[config_selfbot.lang])
    time.sleep(2)
    await ctx.message.delete()
    restart_selfbot()

@bot.command()
async def stop(ctx):
    await ctx.message.edit(langs.stop_command[config_selfbot.lang])
    time.sleep(2)
    await ctx.message.delete()
    await bot.close()
    exit()

#############
#############


####################
# start the        #
#      selfbot !!  #
####################



def fix_aiohttp():
    """
    This error is from discord.py==1.7.3(it's the last version of discord.py
    that works with user account) that use an old version of aiohttp.

    This should fix this error.
    """
    if os.name == 'nt':
        subprocess.check_call([sys.executable, "-m", "pip", "uninstall", "aiohttp"])
        time.sleep(3)
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-U", "aiohttp"])
    else:
        subprocess.check_call([sys.executable, "-m", "pip3", "uninstall", "aiohttp"])
        time.sleep(3)
        subprocess.check_call([sys.executable, "-m", "pip3", "install", "-U", "aiohttp"])

    log.info(langs.aihottp_success[config_selfbot.lang])
    
    time.sleep(3)

    restart_selfbot()


# Launch the selfbot
# By the way, this is the first and the only moment where we use the token in the selfbot.
try:
    if config_selfbot.discord_log:
        # If `discord_log` in `config_selfbot` is True, enable discord.py-self's logs
        bot.run(config_selfbot.token)
    else:
        # Else, disable discord.py-self's logs
        bot.run(config_selfbot.token, log_handler=None)
except discord.LoginFailure:
    # Log if the passed token is incorrect
    log.critical(langs.token_error[config_selfbot.lang])
except Exception as e:
    # Check what the error is from, and react
    if "400, message='Can not decode content-encoding: br'" in str(e):
        # If the Exception is about the old aiohttp error, it try to fix itself with fix_aiohttp()
        log.warning(langs.aihottp_error[config_selfbot.lang])
        fix_aiohttp()
    elif "4004" in str(e):
        # If the session has closed with 4004 (token has changed), log the error.
        log.critical(langs.expired_token[config_selfbot.lang])
    else:
        # Else, print the Exception.
        log.critical(f"{langs.weird_error[config_selfbot.lang]} {e}")