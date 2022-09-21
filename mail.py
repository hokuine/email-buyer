import requests, json, threading, ctypes; from colorama import Fore
lock = threading.Lock(); config = json.load(open("config.json")); thread_count = config["Threads"]; apikey = config["API_Key"]; amount = config["Amount_at_once"]; type = config["type"]
class data: mails = 0; retry = 0
def buy_mails():
    while True:
        url = requests.get(f"https://api.hotmailbox.me/mail/buy?apikey={apikey}&mailcode={type}&quantity={amount}").json(); ctypes.windll.kernel32.SetConsoleTitleW(f"Mails Bought {data.mails} | Retries {data.retry}")
        try:
            for emailpass in url["Data"]["Emails"]:
                email = emailpass["Email"]; password = emailpass["Password"]
                with open("mails.txt", 'a') as f:
                    print(f"{Fore.GREEN}[!] Bought {type} Mail\n Data:{data.mails} - {email} | {password}"); lock.acquire(); lock.release(); data.mails+= 1; f.write(f"{email}|{password}\n")
        except KeyError as e: print(f"{data.retry}x retry - Error: {e}"); data.retry += 1; pass
for x in range(thread_count): threading.Thread(target=buy_mails).start()