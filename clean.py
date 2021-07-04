import discord, datetime, colorama, os, time

from discord.ext import commands
from colorama import Fore, init
from os import system


today = datetime.datetime.now()
date_time = today.strftime("%H:%M:%S")
colorama.init()
os.system(f'mode 80,15 & title Slean')

print("\033[31m")
os.system('cls')
token = input("[+] TOKEN : ")
print("\033[34m")
prefix = input("[+] PREFIX : ")

client = commands.Bot(command_prefix = prefix, self_bot = True)
client.remove_command("help")

@client.event
async def on_ready():
    print("\033[0m")
    os.system('cls')
    print(f">>> {date_time} | [\033[36mEVENTS\033[0m] | Prêt à supprmier tout tes DM ? {client.user.name}.") 
    print(f">>> {date_time} |  [\033[33mHELP\033[0m]  | {prefix}clear")

@client.command()
async def clear(ctx, limit: int=None):
    passed = 0
    fail = 0
    async for msg in ctx.message.channel.history( limit = limit ):
        if msg.author.id == client.user.id:
            try:
                await msg.delete()
                passed += 1
            except:
                fail += 1
    print(f">>> {date_time} | [\033[32mRESULT\033[0m] | \033[34m{passed}\033[0m message supprimé. \033[31m{fail} failed.\033[0m")
    print()
    print(f"[©] By >''SkZ™#9999 ")
    exit()

try:
    client.run(token, bot=False)
except:
    os.system('cls')
    print(f"[X] Le token fournis est invalide !")
    input()