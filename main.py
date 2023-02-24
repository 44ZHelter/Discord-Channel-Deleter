import requests
from colorama import Back, Style, Fore
import colorama
colorama.init()
import os, sys

if sys.platform == 'win32':
    os.system('title Discord Channel Deleter By 4ZHelter')
    os.system('cls')

if sys.platform == 'linux':
    os.system('clear')

__BANNER__ = """
 ▄▄·  ▄ .▄ ▄▄▄·  ▐ ▄  ▐ ▄ ▄▄▄ .▄▄▌  ·▄▄▄▄  ▄▄▄ .▄▄▌  ▄▄▄ .▄▄▄▄▄▄▄▄ .▄▄▄  
▐█ ▌▪██▪▐█▐█ ▀█ •█▌▐█•█▌▐█▀▄.▀·██•  ██▪ ██ ▀▄.▀·██•  ▀▄.▀·•██  ▀▄.▀·▀▄ █·
██ ▄▄██▀▐█▄█▀▀█ ▐█▐▐▌▐█▐▐▌▐▀▀▪▄██▪  ▐█· ▐█▌▐▀▀▪▄██▪  ▐▀▀▪▄ ▐█.▪▐▀▀▪▄▐▀▀▄ 
▐███▌██▌▐▀▐█ ▪▐▌██▐█▌██▐█▌▐█▄▄▌▐█▌▐▌██. ██ ▐█▄▄▌▐█▌▐▌▐█▄▄▌ ▐█▌·▐█▄▄▌▐█•█▌
·▀▀▀ ▀▀▀ · ▀  ▀ ▀▀ █▪▀▀ █▪ ▀▀▀ .▀▀▀ ▀▀▀▀▀•  ▀▀▀ .▀▀▀  ▀▀▀  ▀▀▀  ▀▀▀ .▀  ▀

                   __________________________________________
                  |                                          |
                  |  Coded by: https://github.com/44ZHelter  |
                  |__________________________________________|

"""


print(Fore.RED + __BANNER__)

authorization = input(Fore.GREEN + "[?] Enter your discord token: ")

channel_id = input(Fore.GREEN + "[?] Enter the channel ID that you want to delete: ")

headers = {
    'authorization': f'{authorization}'
}

r = requests.delete(f'https://discord.com/api/v9/channels/{channel_id}', headers=headers)
if r.status_code == 200:
    print(f"[!] CHANNEL SUCCESSFULLY DELETED (Channel ID: {channel_id})")
else:
    print("[!] FAILED TO DELETE (Missing permissions or invalid token/channel id)")
 
input()
                                                                                                 