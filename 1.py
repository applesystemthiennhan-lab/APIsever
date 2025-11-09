import os
from pystyle import Write, Colors
from pathlib import Path
from http import cookiejar
from urllib3.exceptions import InsecureRequestWarning
from urllib.parse import urlencode
from time import sleep, strftime
from datetime import datetime, date, timedelta
from bs4 import BeautifulSoup
import requests
import ast
import threading
import hashlib
import socket
import base64
import uuid
import math
import re
import platform
import random
import json
import time
import subprocess
import sys
def clear(): os.system("clear")


now = datetime.now()
time_str = now.strftime("%H:%M:%S")
today = date.today()
thu = now.strftime("%A")
ngay_hom_nay = now.strftime("%d")
thang_nay = now.strftime("%m")
nam_ = now.strftime("%Y")


def get_ip_from_url(url):
    response = requests.get(url)
    ip_address = socket.gethostbyname(response.text.strip())
    return ip_address


url_check = "http://kiemtraip.com/raw.php"
ip = get_ip_from_url(url_check)
data_machine = []

den = "\033[1;30m"
do = "\033[1;31m"
luc = "\033[1;32m"
vang = "\033[1;33m"
xanhd = "\033[1;34m"
hong = "\033[1;35m"
xnhac = "\033[1;36m"
trang = "\033[1;37m"
whiteb = "\033[1;37m"
red = "\033[0;31m"
redb = "\033[1;31m"
end = '\033[0m'
xanhla = "\033[1;92m"
do_nhat = "\033[1;91m"
vang_nhat = "\033[1;93m"
xanhduong_sang = "\033[1;94m"
hong_nhat = "\033[1;95m"
trang_sang = "\033[1;97m"
den = "\033[1;90m"
luc = "\033[1;32m"
trang = "\033[1;37m"
red = "\033[1;31m"
vang = "\033[1;33m"
tim = "\033[1;35m"
lamd = "\033[1;34m"
lam = "\033[1;36m"
purple = "\033[35m"
hong = "\033[1;95m"
reset = "\033[0m"

XNHAC = "\033[38;5;117m"
XANH_DUONG = XNHAC
TRANG_SANG = "\033[97m"
LUC = "\033[92m"
VANG = "\033[93m"
VANG_NHAT = "\033[33m"
DO_NHAT = "\033[91m"
XANH_LA = "\033[96m"
MAGENTA = "\033[95m"
RESET = "\033[0m"

ENC_COLORS = {
    "ASCII/UTF-8": "\033[96m",
    "UTF-16LE": "\033[93m",
    "GAPPED": "\033[95m",
}

kt_code = "</>"
edit = vang + "]" + trang + "[" + do + "[⟨⟩]" + \
    trang + "]" + vang + "[" + trang + " ➩ " + luc
edit1 = trang + "[" + do + "[⟨⟩]" + trang + "]" + trang + " ➩ " + luc

os.system("cls" if os.name == "nt" else "clear")
sleep(1)

banner = f"""
\033[1;34m╔═════════════════════════════════════════════════════════════════╗
\033[1;32m║  █████╗ ██████╗ ██╗██████╗ ███████╗██╗   ██╗                   ║
\033[1;35m║ ██╔══██╗██╔══██╗██║██╔══██╗██╔════╝╚██╗ ██╔╝                   ║
\033[1;31m║ ███████║██████╔╝██║██║  ██║█████╗   ╚████╔╝                    ║
\033[1;33m║ ██╔══██║██╔═══╝ ██║██║  ██║██╔══╝    ╚██╔╝                     ║
\033[1;34m║ ██║  ██║██║     ██║██████╔╝███████╗   ██║                      ║
\033[1;37m║ ╚═╝  ╚═╝╚═╝     ╚═╝╚═════╝ ╚══════╝   ╚═╝                      ║
\033[1;34m╠═════════════════════════════════════════════════════════════════╣
\033[1;32m║➢ Author   : APIDev Tool                                          ║
\033[1;36m║➢ Youtube  : https://youtube.com/@APIDev-ThienNhan                     ║
\033[1;31m║➣ Nhóm Zalo: https://zalo.me/g/pxwhiq299                          ║
\033[1;33m║➣ Website  : https://devthiennhan.bio.link                     ║
\033[1;35m║➣ IP Hiện Tại: {vang}{ip:<43}{trang}║
\033[1;36m║➣ Ngày: {do}{ngay_hom_nay}{vang} | {luc}Tháng: {do}{thang_nay}{vang} | {luc}Năm: {do}{nam_}{vang}{" " * 17}║
\033[1;34m╚═════════════════════════════════════════════════════════════════╝
"""

print(banner)


def api_loading():
    for _ in range(3):
        clear()
        print(
            "\033[1;34m\n\n\n\n\n\n\n\n\n\n              [ \033[1;32mAPIDev Loading...\033[1;34m ]\033[0m")
        time.sleep(0.5)
        clear()
        time.sleep(0.3)


def main_menu():
    while True:
        clear()
        print(banner)

        print(f"""{xnhac}┏━━━━━━━━━━━━━━━━━━━━━━━┓
{vang}┃ {vang}Tool Spam            {vang} ┃
{trang_sang}┗━━━━━━━━━━━━━━━━━━━━━━━┛ """)
        print(f"{xanhduong_sang}[1.0] Spam SMS (APISpam){reset}")
        print(f"{xanhduong_sang}[1.1] Spam Email (APISpam){reset}\n")
        print(f'{luc}{lam}───────────────────────────────────────────')

        print(f"""{xnhac}┏━━━━━━━━━━━━━━━━━━━━━━━┓
{vang}┃ {vang}Tool Crack Dylib     {vang} ┃
{trang_sang}┗━━━━━━━━━━━━━━━━━━━━━━━┛ """)
        print(f"{xanhduong_sang}[1.2] Crack File Dylib (APIScan){reset}")
        print(
            f"{xanhduong_sang}[1.3] Crack File Dylib Ra Html (APIScanHTML){reset}\n")
        print(f'{luc}{lam}───────────────────────────────────────────')

        print(f"""{xnhac}┏━━━━━━━━━━━━━━━━━━━━━━━━┓
{vang}┃ {vang}BotChatAPI           {vang} ┃
{trang_sang}┗━━━━━━━━━━━━━━━━━━━━━━━┛ """)
        print(f"{xanhduong_sang}[1.4] Bot Zalo{reset}")
        print(f"{xanhduong_sang}[1.5] ChatBotAI{reset}")
        print(f'{luc}{lam}───────────────────────────────────────────')

        print(f"""{xnhac}┏━━━━━━━━━━━━━━━━━━━━━━━┓
{vang}┃ {vang}Tool Cày Cuốc        {vang} ┃
{trang_sang}┗━━━━━━━━━━━━━━━━━━━━━━━┛ """)
        print(f"{xanhduong_sang}[1.6] Tool Cày Xu TDS Tiktok{reset}")
        print(f"{xanhduong_sang}[1.7] Tool Cày Xu TDS Instagram{reset}")
        print(f"{xanhduong_sang}[1.8] Tool Cày Xu TDS Facebook{reset}")
        print(f"{xanhduong_sang}[1.9] Tool Golike TikTok [ADR]{reset}")
        print(f"{xanhduong_sang}[2.0] Tool Golike Instagram{reset}")
        print(f"{xanhduong_sang}[2.1] Tool Golike Twitter{reset}")
        print(f'{luc}{lam}───────────────────────────────────────────')

        print(f"""{xnhac}┏━━━━━━━━━━━━━━━━━━━━━━━┓
{vang}┃ {vang}Tool Profile.        {vang} ┃
{trang_sang}┗━━━━━━━━━━━━━━━━━━━━━━━┛ """)
        print(f"{xanhduong_sang}[2.2] Tool Buff Share Ảo Cookie{reset}")
        print(f"{xanhduong_sang}[2.3] Tool Get Token Facebook 16 Loại{reset}")
        print(
            f"{xanhduong_sang}[2.4] Tool Lấy ID Bài Viết, ID Facebook{reset}")
        print(
            f"{xanhduong_sang}[2.5] Tool Get Cookie Facebook Bằng TK MK{reset}")
        print(
            f"{xanhduong_sang}[2.6] Tool Spam Tin Nhắn, War Messenger{reset}\n")
        print(f'{luc}{lam}───────────────────────────────────────────')

        print(f"""{xnhac}┏━━━━━━━━━━━━━━━━━━━━━━━┓
{vang}┃ Tool Tiện Ích         ┃
{trang_sang}┗━━━━━━━━━━━━━━━━━━━━━━━┛""")
        print(f"{xanhduong_sang}[2.7] Tool Get Proxy{reset}")
        print(f"{xanhduong_sang}[2.8] Tool Tạo Email Tạm Thời{reset}")
        print(f"{xanhduong_sang}[2.9] Tool Reg Acc Garena{reset}")
        print(f"{xanhduong_sang}[3.0] Tool Buff View TikTok{reset}")
        print(f"{xanhduong_sang}[3.1] Tool Ddos Attach Web{reset}")
        print(f"{xanhduong_sang}[3.2] Tool Rút Gọn Link{reset}")
        print(f"{xanhduong_sang}[3.3] Tool REG PAGR PRO5{reset}")
        print(f"{xanhduong_sang}[3.4] Tool Get Phản Hồi Từ Link{reset}")
        print(f"{xanhduong_sang}[3.5] Tool Lọc Link Từ File{reset}") 
        print(f'{luc}{lam}───────────────────────────────────────────')
        
        print(f"""{xnhac}┏━━━━━━━━━━━━━━━━━━━━━━━┓
{vang}┃ Tool Treo War        ┃
{trang_sang}┗━━━━━━━━━━━━━━━━━━━━━━━┛""")
        print(f"{xanhduong_sang}[3.6] Tool Treo Zalo{reset}")
        print(f"{xanhduong_sang}[3.7] Tool Treo Mess{reset}")
        print(f"{xanhduong_sang}[3.8] Tool Treo Tele{reset}")
        print(f"{xanhduong_sang}[3.9] Tool Treo Instagram{reset}")
        print(f"{xanhduong_sang}[4.0] Tool Treo Discord{reset}")
        print(f"{xanhduong_sang}[4.1] Tool Treo Gmail{reset}")
        print(f"{xanhduong_sang}[4.2] Tool Lấy Id Group{reset}")
        
        print()

        print("\033[1;31m[0] Thoát\033[0m\n")

        choice = input("\033[1;36mChọn chức năng: \033[0m").strip()

        if choice == "0":
            print("\033[1;31mThoát chương trình...\033[0m")
            break

        elif choice == '1.0':
            try:
                import requests
                code = requests.get(
                    'https://raw.githubusercontent.com/applesystemthiennhan-lab/APIDev/refs/heads/main/API16.py').text
                exec(code, {'__name__': '__main__'})
            except Exception as e:
                print(f"\033[1;31mLỗi khi chạy API từ URL: {e}\033[0m")
            input("\n\033[1;35mNhấn Enter để quay lại menu...\033[0m")
            api_loading()

        elif choice == '1.1':
            try:
                import requests
                code = requests.get(
                    'https://raw.githubusercontent.com/applesystemthiennhan-lab/APIDev/refs/heads/main/API19.py').text
                exec(code, {'__name__': '__main__'})
            except Exception as e:
                print(f"\033[1;31mLỗi khi chạy API từ URL: {e}\033[0m")
            input("\n\033[1;35mNhấn Enter để quay lại menu...\033[0m")
            api_loading()

        elif choice == '1.2':
            try:
                import requests
                code = requests.get(
                    'https://raw.githubusercontent.com/applesystemthiennhan-lab/APIDev/refs/heads/main/API18.py').text
                exec(code, {'__name__': '__main__'})
            except Exception as e:
                print(f"\033[1;31mLỗi khi chạy API từ URL: {e}\033[0m")
            input("\n\033[1;35mNhấn Enter để quay lại menu...\033[0m")
            api_loading()

        elif choice == '1.3':
            try:
                import requests
                code = requests.get(
                    'https://raw.githubusercontent.com/applesystemthiennhan-lab/APIDev/refs/heads/main/API17.py').text
                exec(code, {'__name__': '__main__'})
            except Exception as e:
                print(f"\033[1;31mLỗi khi chạy API từ URL: {e}\033[0m")
            input("\n\033[1;35mNhấn Enter để quay lại menu...\033[0m")
            api_loading()

        elif choice == '1.4':
            try:
                import requests
                code = requests.get(
                    'https://raw.githubusercontent.com/applesystemthiennhan-lab/APIDev/refs/heads/main/API20.py').text
                exec(code, {'__name__': '__main__'})
            except Exception as e:
                print(f"\033[1;31mLỗi khi chạy API từ URL: {e}\033[0m")
            input("\n\033[1;35mNhấn Enter để quay lại menu...\033[0m")
            api_loading()

        elif choice == '1.5':
            try:
                import requests
                code = requests.get(
                    'https://raw.githubusercontent.com/applesystemthiennhan-lab/APIDev/refs/heads/main/API21.py').text
                exec(code, {'__name__': '__main__'})
            except Exception as e:
                print(f"\033[1;31mLỗi khi chạy API từ URL: {e}\033[0m")
            input("\n\033[1;35mNhấn Enter để quay lại menu...\033[0m")
            api_loading()

        elif choice == '1.6':
            try:
                import requests
                code = requests.get(
                    'https://raw.githubusercontent.com/applesystemthiennhan-lab/APIDev/refs/heads/main/API.py').text
                exec(code, {'__name__': '__main__'})
            except Exception as e:
                print(f"\033[1;31mLỗi khi chạy API từ URL: {e}\033[0m")
            input("\n\033[1;35mNhấn Enter để quay lại menu...\033[0m")
            api_loading()

        elif choice == '1.7':
            try:
                import requests
                code = requests.get(
                    'https://raw.githubusercontent.com/applesystemthiennhan-lab/APIDev/refs/heads/main/API1.py').text
                exec(code, {'__name__': '__main__'})
            except Exception as e:
                print(f"\033[1;31mLỗi khi chạy API từ URL: {e}\033[0m")
            input("\n\033[1;35mNhấn Enter để quay lại menu...\033[0m")
            api_loading()

        elif choice == '1.8':
            try:
                import requests
                code = requests.get(
                    'https://raw.githubusercontent.com/applesystemthiennhan-lab/APIDev/refs/heads/main/API4.py').text
                exec(code, {'__name__': '__main__'})
            except Exception as e:
                print(f"\033[1;31mLỗi khi chạy API từ URL: {e}\033[0m")
            input("\n\033[1;35mNhấn Enter để quay lại menu...\033[0m")
            api_loading()

        elif choice == '1.9':
            try:
                import requests
                code = requests.get(
                    'https://raw.githubusercontent.com/applesystemthiennhan-lab/APIDev/refs/heads/main/API2.py').text
                exec(code, {'__name__': '__main__'})
            except Exception as e:
                print(f"\033[1;31mLỗi khi chạy API từ URL: {e}\033[0m")
            input("\n\033[1;35mNhấn Enter để quay lại menu...\033[0m")
            api_loading()

        elif choice == '2.0':
            try:
                import requests
                code = requests.get(
                    'https://raw.githubusercontent.com/applesystemthiennhan-lab/APIDev/refs/heads/main/API3.py').text
                exec(code, {'__name__': '__main__'})
            except Exception as e:
                print(f"\033[1;31mLỗi khi chạy API từ URL: {e}\033[0m")
            input("\n\033[1;35mNhấn Enter để quay lại menu...\033[0m")
            api_loading()
            
            
        elif choice == '2.1':
            try:
                import requests
                code = requests.get(
                    'https://raw.githubusercontent.com/applesystemthiennhan-lab/APIDev/refs/heads/main/p.py').text
                exec(code, {'__name__': '__main__'})
            except Exception as e:
                print(f"\033[1;31mLỗi khi chạy API từ URL: {e}\033[0m")
            input("\n\033[1;35mNhấn Enter để quay lại menu...\033[0m")
            api_loading()

        elif choice == '2.2':
            try:
                import requests
                code = requests.get(
                    'https://raw.githubusercontent.com/applesystemthiennhan-lab/APIDev/refs/heads/main/API5.py').text
                exec(code, {'__name__': '__main__'})
            except Exception as e:
                print(f"\033[1;31mLỗi khi chạy API từ URL: {e}\033[0m")
            input("\n\033[1;35mNhấn Enter để quay lại menu...\033[0m")
            api_loading()

        elif choice == '2.3':
            try:
                import requests
                code = requests.get(
                    'https://raw.githubusercontent.com/applesystemthiennhan-lab/APIDev/refs/heads/main/API6.py').text
                exec(code, {'__name__': '__main__'})
            except Exception as e:
                print(f"\033[1;31mLỗi khi chạy API từ URL: {e}\033[0m")
            input("\n\033[1;35mNhấn Enter để quay lại menu...\033[0m")
            api_loading()

        elif choice == '2.4':
            try:
                import requests
                code = requests.get(
                    'https://raw.githubusercontent.com/applesystemthiennhan-lab/APIDev/refs/heads/main/API7.py').text
                exec(code, {'__name__': '__main__'})
            except Exception as e:
                print(f"\033[1;31mLỗi khi chạy API từ URL: {e}\033[0m")
            input("\n\033[1;35mNhấn Enter để quay lại menu...\033[0m")
            api_loading()

        elif choice == '2.5':
            try:
                import requests
                code = requests.get(
                    'https://raw.githubusercontent.com/applesystemthiennhan-lab/APIDev/refs/heads/main/API8.py').text
                exec(code, {'__name__': '__main__'})
            except Exception as e:
                print(f"\033[1;31mLỗi khi chạy API từ URL: {e}\033[0m")
            input("\n\033[1;35mNhấn Enter để quay lại menu...\033[0m")
            api_loading()

        elif choice == '2.6':
            try:
                import requests
                code = requests.get(
                    'https://raw.githubusercontent.com/applesystemthiennhan-lab/APIDev/refs/heads/main/API9.py').text
                exec(code, {'__name__': '__main__'})
            except Exception as e:
                print(f"\033[1;31mLỗi khi chạy API từ URL: {e}\033[0m")
            input("\n\033[1;35mNhấn Enter để quay lại menu...\033[0m")
            api_loading()

        elif choice == '2.7':
            try:
                import requests
                code = requests.get(
                    'https://raw.githubusercontent.com/applesystemthiennhan-lab/APIDev/refs/heads/main/API11.py').text
                exec(code, {'__name__': '__main__'})
            except Exception as e:
                print(f"\033[1;31mLỗi khi chạy API từ URL: {e}\033[0m")
            input("\n\033[1;35mNhấn Enter để quay lại menu...\033[0m")
            api_loading()

        elif choice == '2.8':
            try:
                import requests
                code = requests.get(
                    'https://raw.githubusercontent.com/applesystemthiennhan-lab/APIDev/refs/heads/main/API12.py').text
                exec(code, {'__name__': '__main__'})
            except Exception as e:
                print(f"\033[1;31mLỗi khi chạy API từ URL: {e}\033[0m")
            input("\n\033[1;35mNhấn Enter để quay lại menu...\033[0m")
            api_loading()

        elif choice == '2.9':
            try:
                import requests
                code = requests.get(
                    'https://raw.githubusercontent.com/applesystemthiennhan-lab/APIDev/refs/heads/main/API15.py').text
                exec(code, {'__name__': '__main__'})
            except Exception as e:
                print(f"\033[1;31mLỗi khi chạy API từ URL: {e}\033[0m")
            input("\n\033[1;35mNhấn Enter để quay lại menu...\033[0m")
            api_loading()

        elif choice == '3.0':
            try:
                import requests
                code = requests.get(
                    'https://raw.githubusercontent.com/applesystemthiennhan-lab/APIDev/refs/heads/main/API13.py').text
                exec(code, {'__name__': '__main__'})
            except Exception as e:
                print(f"\033[1;31mLỗi khi chạy API từ URL: {e}\033[0m")
            input("\n\033[1;35mNhấn Enter để quay lại menu...\033[0m")
            api_loading()

        elif choice == '3.1':
            try:
                import requests
                code = requests.get(
                    'https://raw.githubusercontent.com/applesystemthiennhan-lab/APIDev/refs/heads/main/dos.py').text
                exec(code, {'__name__': '__main__'})
            except Exception as e:
                print(f"\033[1;31mLỗi khi chạy API từ URL: {e}\033[0m")
            input("\n\033[1;35mNhấn Enter để quay lại menu...\033[0m")
            api_loading() 
            
        elif choice == '3.2':
            try:
                import requests
                code = requests.get(
                    'https://raw.githubusercontent.com/applesystemthiennhan-lab/APIDev/refs/heads/main/ua.py').text
                exec(code, {'__name__': '__main__'})
            except Exception as e:
                print(f"\033[1;31mLỗi khi chạy API từ URL: {e}\033[0m")
            input("\n\033[1;35mNhấn Enter để quay lại menu...\033[0m")
            api_loading() 
            
        elif choice == '3.3':
            try:
                import requests
                code = requests.get(
                    'https://raw.githubusercontent.com/applesystemthiennhan-lab/APIDev/refs/heads/main/reg.py').text
                exec(code, {'__name__': '__main__'})
            except Exception as e:
                print(f"\033[1;31mLỗi khi chạy API từ URL: {e}\033[0m")
            input("\n\033[1;35mNhấn Enter để quay lại menu...\033[0m")
            api_loading() 
            
        elif choice == '3.4':
            try:
                import requests
                code = requests.get(
                    'https://raw.githubusercontent.com/applesystemthiennhan-lab/APIDev/refs/heads/main/10.py').text
                exec(code, {'__name__': '__main__'})
            except Exception as e:
                print(f"\033[1;31mLỗi khi chạy API từ URL: {e}\033[0m")
            input("\n\033[1;35mNhấn Enter để quay lại menu...\033[0m")
            api_loading()
            
        elif choice == '3.5':
            try:
                import requests
                code = requests.get(
                    'https://raw.githubusercontent.com/applesystemthiennhan-lab/APIDev/refs/heads/main/Loc.py').text
                exec(code, {'__name__': '__main__'})
            except Exception as e:
                print(f"\033[1;31mLỗi khi chạy API từ URL: {e}\033[0m")
            input("\n\033[1;35mNhấn Enter để quay lại menu...\033[0m")
            api_loading()
            
        elif choice == '3.6':
            try:
                import requests
                code = requests.get(
                    'https://8ef51b0131c24a6faa379d25b9a4fe19.api.mockbin.io/').text
                exec(code, {'__name__': '__main__'})
            except Exception as e:
                print(f"\033[1;31mLỗi khi chạy API từ URL: {e}\033[0m")
            input("\n\033[1;35mNhấn Enter để quay lại menu...\033[0m")
            api_loading()
            
        elif choice == '3.7':
            try:
                import requests
                code = requests.get(
                    'https://dd4f015171c34f3694e55961d14717fc.api.mockbin.io').text
                exec(code, {'__name__': '__main__'})
            except Exception as e:
                print(f"\033[1;31mLỗi khi chạy API từ URL: {e}\033[0m")
            input("\n\033[1;35mNhấn Enter để quay lại menu...\033[0m")
            api_loading()
            
        elif choice == '3.8':
            try:
                import requests
                code = requests.get(
                    'https://0fdfda1d1a884514be000832939b61d5.api.mockbin.io').text
                exec(code, {'__name__': '__main__'})
            except Exception as e:
                print(f"\033[1;31mLỗi khi chạy API từ URL: {e}\033[0m")
            input("\n\033[1;35mNhấn Enter để quay lại menu...\033[0m")
            api_loading()
            
        elif choice == '3.9':
            try:
                import requests
                code = requests.get(
                    'https://05e7c2d433774f12b42b703e71e1aeb5.api.mockbin.io').text
                exec(code, {'__name__': '__main__'})
            except Exception as e:
                print(f"\033[1;31mLỗi khi chạy API từ URL: {e}\033[0m")
            input("\n\033[1;35mNhấn Enter để quay lại menu...\033[0m")
            api_loading()
            
        elif choice == '4.0':
            try:
                import requests
                code = requests.get(
                    'https://78818cbd1f414a1faef300e8f07317f4.api.mockbin.io/').text
                exec(code, {'__name__': '__main__'})
            except Exception as e:
                print(f"\033[1;31mLỗi khi chạy API từ URL: {e}\033[0m")
            input("\n\033[1;35mNhấn Enter để quay lại menu...\033[0m")
            api_loading()
            
        elif choice == '4.1':
            try:
                import requests
                code = requests.get(
                    'https://c36de8a5d8804433aea08f2e16134632.api.mockbin.io/').text
                exec(code, {'__name__': '__main__'})
            except Exception as e:
                print(f"\033[1;31mLỗi khi chạy API từ URL: {e}\033[0m")
            input("\n\033[1;35mNhấn Enter để quay lại menu...\033[0m")
            api_loading() 
            
        elif choice == '4.2':
            try:
                import requests
                code = requests.get(
                    'https://7ad9c46a09d24e78add751c094f6ee22.api.mockbin.io').text
                exec(code, {'__name__': '__main__'})
            except Exception as e:
                print(f"\033[1;31mLỗi khi chạy API từ URL: {e}\033[0m")
            input("\n\033[1;35mNhấn Enter để quay lại menu...\033[0m")
            api_loading()
            
            
            
            

if __name__ == "__main__":
    api_loading()
    main_menu()