#   ▄████████    ▄██████▄   ▄██████▄     ▄██████▄     ▄███████▄     ███     
#  ███    ███   ███    ███ ███    ███   ███    ███   ███    ███ ▀█████████▄ 
#  ███    █▀    ███    █▀  ███    ███   ███    █▀    ███    ███    ▀███▀▀██ 
# ▄███▄▄▄      ▄███        ███    ███  ▄███          ███    ███     ███   ▀ 
#▀▀███▀▀▀     ▀▀███ ████▄  ███    ███ ▀▀███ ████▄  ▀█████████▀      ███     
#  ███    █▄    ███    ███ ███    ███   ███    ███   ███            ███     
#  ███    ███   ███    ███ ███    ███   ███    ███   ███            ███     
#  ██████████   ████████▀   ▀██████▀    ████████▀   ▄████▀         ▄████▀   
#                                                                           
#
#                Code written by @humbleness on discord
#     Use this skidded loader yalls fucking projects i dont fucking care
#
import os
import time
import random
import threading
import fade
import psutil
import platform
from colorama import Fore, Style, init
from pystyle import Colors, Colorate, Center

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def update_title():
    while True:
        title = "[Py Loader] " + ''.join(random.choices("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", k=30))
        os.system(f"title {title}" if os.name == 'nt' else f"\033]0;{title}\007")
        time.sleep(0.1)       
    
def get_system_info():
    red_dash = f"{Fore.YELLOW}-{Style.RESET_ALL}"
    print(Center.XCenter(faded_text))
    print("\n")
    print(f"\r    [{red_dash}]System: {platform.system()}")
    print(f"\r    [{red_dash}]Release: {platform.release()}")
    print(f"\r    [{red_dash}]Version: {platform.version()}")
    print(f"\r    [{red_dash}]Machine: {platform.machine()}")
    print(f"\r    [{red_dash}]Processor: {platform.processor()}")
    print(f"\r    [{red_dash}]CPU Count: {psutil.cpu_count(logical=False)}")
    print(f"\r    [{red_dash}]Logical CPUs: {psutil.cpu_count(logical=True)}")
    countdown = f"{Fore.YELLOW}5.00{Style.RESET_ALL}"
    print(f"\r    [{red_dash}]Closing In {countdown} seconds!", end='')
    
text = """
                         ██▓███ ▓██   ██▓    ██▓     ▒█████   ▄▄▄      ▓█████▄ ▓█████  ██▀███  
                        ▓██░  ██▒▒██  ██▒   ▓██▒    ▒██▒  ██▒▒████▄    ▒██▀ ██▌▓█   ▀ ▓██ ▒ ██▒
                        ▓██░ ██▓▒ ▒██ ██░   ▒██░    ▒██░  ██▒▒██  ▀█▄  ░██   █▌▒███   ▓██ ░▄█ ▒
                        ▒██▄█▓▒ ▒ ░ ▐██▓░   ▒██░    ▒██   ██░░██▄▄▄▄██ ░▓█▄   ▌▒▓█  ▄ ▒██▀▀█▄  
                        ▒██▒ ░  ░ ░ ██▒▓░   ░██████▒░ ████▓▒░ ▓█   ▓██▒░▒████▓ ░▒████▒░██▓ ▒██▒
                        ▒▓▒░ ░  ░  ██▒▒▒    ░ ▒░▓  ░░ ▒░▒░▒░  ▒▒   ▓▒█░ ▒▒▓  ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░
                        ░▒ ░     ▓██ ░▒░    ░ ░ ▒  ░  ░ ▒ ▒░   ▒   ▒▒ ░ ░ ▒  ▒  ░ ░  ░  ░▒ ░ ▒░
                        ░░       ▒ ▒ ░░       ░ ░   ░ ░ ░ ▒    ░   ▒    ░ ░  ░    ░     ░░   ░ 
                                 ░ ░            ░  ░    ░ ░        ░  ░   ░       ░  ░   ░     
                                 ░ ░                                    ░                      
"""
faded_text = fade.fire(text)

def main():
    clear_console()
    threading.Thread(target=update_title, daemon=True).start()
    red_dash = f"{Fore.YELLOW}-{Style.RESET_ALL}"
    
    print(Center.XCenter(faded_text))
    input(f"\r    [{red_dash}] Enter Key: ")
    time.sleep(1.5)
    
    clear_console()
    
    print(Center.XCenter(faded_text))
    print(f"\r    [{red_dash}] Authenticating...", end='')
    time.sleep(2.3)
    clear_console()
    
    countdown = f"{Fore.YELLOW}5.00{Style.RESET_ALL}"
    print(Center.XCenter(faded_text))
    print(f"\r    [{red_dash}] Printing Console Info In {countdown} seconds!", end='')
    time.sleep(5)
    clear_console()
    get_system_info()
    time.sleep(10)
    
if __name__ == "__main__":
    main()
