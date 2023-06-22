import requests as re
from colorama import init, Fore, Back, Style

init()

def user_finder():
    urls_file = 'urls.txt'
    usernames = input("[+] Enter the username to search: ")

    with open(urls_file, 'r') as file:
        list_urls = file.read().splitlines()

    for url in list_urls:
        try:
            if "https://www.youtube.com" in url:
                url += f"/@{usernames}"
            full_url = f"{url}/{usernames}"
            response = re.get(full_url)

            if response.status_code == 200:
                print(Fore.GREEN + f"\n[+] {response.status_code} => {full_url}")
            
        except Exception as e:
            print(Fore.YELLOW + "[-] An exception occurred while trying to access the website:", str(e))

user_finder()