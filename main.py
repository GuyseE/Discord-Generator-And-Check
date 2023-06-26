import os
from time import sleep
import requests
import random
import string
from colorama import Fore


os.system("cls")

print(f"{Fore.GREEN}[ {Fore.CYAN}\u00A7 {Fore.GREEN}] {Fore.LIGHTBLACK_EX}Discord checker and nitro by {Fore.RED}_Guyse_{Fore.LIGHTBLACK_EX}, by {Fore.RED}Pomosh=){Fore.LIGHTBLACK_EX} | Check my tg {Fore.RED}u my love:3 {Fore.GREEN}https://t.me/ahahahahahahahhaahahahahahahazxc")
print(f"{Fore.GREEN}[ {Fore.CYAN}\u00A7 {Fore.GREEN}] {Fore.LIGHTBLACK_EX}Sozdatel/creator in discord: {Fore.RED}_guyse_")
print(f"{Fore.GREEN}[ {Fore.CYAN}\u00A7 {Fore.GREEN}] {Fore.LIGHTBLACK_EX}Esli xotite chto-to novoe pishi v ds / If you want something new write on the discord : {Fore.RED}_guyse_")
amount = int(input(f"\n{Fore.RED}[ {Fore.YELLOW}> {Fore.RED}] {Fore.LIGHTBLACK_EX}How much do you need ?: {Fore.RED}"))
print(f"\n{Fore.RED}[ {Fore.YELLOW}? {Fore.RED}] {Fore.LIGHTBLACK_EX}Full ili je Classic?/Full nitro or classic?")
nitro = input(f"{Fore.CYAN}[ {Fore.YELLOW}> {Fore.CYAN}] {Fore.LIGHTBLACK_EX}Full codes or Classic codes {Fore.RED}(full or classic){Fore.LIGHTBLACK_EX}: {Fore.RED}")

if "full" in nitro or "classic" in nitro:
    pass
else:
    print(f"{Fore.RED}[ {Fore.RED}! {Fore.RED}] {Fore.LIGHTBLACK_EX}The answer should be {Fore.RED}boost(full) {Fore.LIGHTBLACK_EX}ili {Fore.RED}classic(basic)")
    exit()


checker = input(f"{Fore.CYAN}[ {Fore.YELLOW}> {Fore.CYAN}] {Fore.LIGHTBLACK_EX}Enable Checker? {Fore.RED}(yes or no){Fore.LIGHTBLACK_EX}: {Fore.RED}")

def scrape():
    scraped = 0
    f = open("proxies.txt", "a+")
    f.truncate(0)
    r = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=http&timeout=1500&ssl=da')
    proxies = []
    for proxy in r.text.split('\n'):
        proxy = proxy.strip()
        proxy = 'https://' + proxy
        if proxy:
            proxies.append(proxy)
    for p in proxies:
        scraped = scraped + 1 
        f.write((p)+"\n")
    f.close()
    print(f"{Fore.CYAN}[ {Fore.YELLOW}? {Fore.CYAN}] {Fore.LIGHTBLACK_EX}Scraped {Fore.WHITE}{scraped} {Fore.LIGHTBLACK_EX}proxies.")

if checker == "yes":
    scrapep = input(f"{Fore.YELLOW}[ {Fore.YELLOW}> {Fore.YELLOW}] {Fore.LIGHTBLACK_EX}Avtomaticheskaya ochistka proksi/Automatic proxy cleaning {Fore.RED}(yes or no){Fore.LIGHTBLACK_EX}: {Fore.RED}")
    print(f"\n{Fore.YELLOW}[ {Fore.YELLOW}? {Fore.YELLOW}] {Fore.LIGHTBLACK_EX}Yesli net, to kazhdaya proverka budet na sluchaynom proksi./If not, each check will be on a random proxy.")
    mult = input(f"{Fore.YELLOW}[ {Fore.YELLOW}> {Fore.YELLOW}] {Fore.LIGHTBLACK_EX}Mnozhestvennyye proverki proksi/Multiple proxy checks {Fore.RED}(yes or no){Fore.LIGHTBLACK_EX}: {Fore.RED}")
    if scrapep == "yes":
        scrape()
else:
    print(f"\n{Fore.CYAN}[ {Fore.YELLOW}? {Fore.CYAN}] {Fore.LIGHTBLACK_EX}Yesli eto pravda, pered kodom budet/If it is true before the code will be  {Fore.WHITE}discord.gift/")
    prefix = input(f"{Fore.CYAN}[ {Fore.YELLOW}> {Fore.CYAN}] {Fore.LIGHTBLACK_EX}Prefiks pered kodami/Prefix before the codes {Fore.WHITE}(yes or no){Fore.LIGHTBLACK_EX}: {Fore.WHITE}")
    if "yes" in prefix or "net" in prefix:
        pass
    else:
        print(f"{Fore.WHITE}[ {Fore.RED}! {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Otvet dolzhen byt'/The answer should be{Fore.WHITE}yes{Fore.LIGHTBLACK_EX}or {Fore.WHITE}net")
        exit()


print(f"\n{Fore.WHITE}[ {Fore.YELLOW}? {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Generating {Fore.WHITE}{amount}{Fore.LIGHTBLACK_EX} codes:3")
if checker != "yes":
    sleep(1)

fulla = amount
f = open("codes.txt", "w+", encoding="UTF-8")



def readproxies():
    try:
        p = open("proxies.txt", encoding="UTF-8")
    except FileNotFoundError:
        p = open("proxies.txt", "w+", encoding="UTF-8")
        print(f"{Fore.RED}[{Fore.RED} ! {Fore.RED}]{Fore.LIGHTBLACK_EX} Proksi ne naydeny v/No proxy found in {Fore.WHITE}proxies.txt!{Fore.WHITE}")
        raise SystemExit



    rproxy = p.read().split('\n')
    for i in rproxy:
        if i == "" or i == " ":
            index = rproxy.index(i)
            del rproxy[index]
    p.close()
    
    return rproxy
    
    
rproxy=readproxies()


if not rproxy:
        print(f"{Fore.RED}[{Fore.RED} ! {Fore.RED}]{Fore.LIGHTBLACK_EX} Proksi ne naydeny v/No proxy found in {Fore.WHITE}proxies.txt!{Fore.WHITE}")
        raise SystemExit


if checker != "yes":
    while amount > 0:
        amount = amount - 1
        if "boost" in nitro:
            code = ''.join([random.choice(string.ascii_letters + string.digits) for i in range(24)])
        else:
            code = ''.join([random.choice(string.ascii_letters + string.digits) for i in range(16)])
        if prefix == "yes":
            print(f"{Fore.WHITE}[ {Fore.GREEN}+ {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Generated code {Fore.WHITE}{code}")
            f.write(f"discord.gift/{code}\n")
        else:
            print(f"{Fore.WHITE}[ {Fore.GREEN}+ {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Generated code {Fore.WHITE}{code}")
            f.write(f"{code}\n")

else:
    while amount > 0:
        f = open(f"working-codes.txt","a", encoding="UTF-8")
        try:
            if not rproxy[0]:
                print(f"{Fore.RED}[ {Fore.RED}! {Fore.RED}] {Fore.LIGHTBLACK_EX}Vce proxie xyina{Fore.WHITE}")
                
            
                if scrapep == "yes":
                    print(f"{Fore.WHITE}[ {Fore.YELLOW}? {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Perezagruzka proksi...{Fore.WHITE}")
                    scrape()
                    rproxy=readproxies()
                else:
                    exit()

        except:
            print(f"{Fore.WHITE}[ {Fore.RED}! {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Vce proxie xyina/All proxies don't work{Fore.WHITE}")
            if scrapep == "yes":
                print(f"{Fore.WHITE}[ {Fore.YELLOW}? {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Perezagruzka proksi.../Reboot proxy...{Fore.WHITE}")
                scrape()
                rproxy=readproxies()
            else:
                exit()
        if mult == "yes":
            proxi = rproxy[0]
        else:
            proxi = random.choice(rproxy)
        proxies = {
            "https": proxi
        }
        amount = amount - 1
        if "boost" in nitro:
            code = ''.join([random.choice(string.ascii_letters + string.digits) for i in range(24)])
        else:
            code = ''.join([random.choice(string.ascii_letters + string.digits) for i in range(16)])
        try:
            url = requests.get(f"https://discordapp.com/api/v6/entitlements/gift-codes/{code}", proxies=proxies, timeout=3)
            if url.status_code == 200:
                print(f"{Fore.WHITE}[ {Fore.GREEN}+ {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Working Code {Fore.WHITE}{code}{Fore.WHITE}")
                f.write(f"\ndiscord.gift/{code}")
                f.close()
            elif url.status_code == 404:
                fulla = fulla - 1
                print(f"{Fore.WHITE}[ {Fore.RED}- {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Nevernui code!/Incorrect code {Fore.WHITE}{code}")
            elif url.status_code == 429:
                fulla = fulla - 1
                if mult == "yes":
                    print(f"{Fore.WHITE}[ {Fore.RED}- {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Proxy {Fore.WHITE}{proxi}{Fore.LIGHTBLACK_EX} ogranichen po skorosti! / Pereklyucheniye proksi/ Switching proxies")
                else:
                    print(f"{Fore.WHITE}[ {Fore.RED}- {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Proxy {Fore.WHITE}{proxi}{Fore.LIGHTBLACK_EX} ogranichen po skorosti!/Limited in speed! / Switching proxies.")
                index = rproxy.index(proxi)
                del rproxy[index]
            else:
                fulla = fulla - 1
                print(f"{Fore.WHITE}[ {Fore.RED}! {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Nevernaya oshibka!/Wrong mistake! | Status code {Fore.WHITE}{url.status_code}")
        except:
            index = rproxy.index(proxi)
            del rproxy[index]
            pw = open(f"proxies.txt","w", encoding="UTF-8")
            for i in rproxy:
                pw.write(i + "\n")
            pw.close()
            fulla = fulla - 1
            print(f"{Fore.WHITE}[ {Fore.RED}- {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Ne udalos' podklyuchit'sya k proksi/Failed to connect to proxy {Fore.WHITE}{proxi}{Fore.LIGHTBLACK_EX} | Udaleniye iz spiska!/Remove from the list!")

f.close()
print(f"{Fore.WHITE}[ {Fore.YELLOW}? {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Uspeshno sozdano/Successfully established {Fore.WHITE}{fulla} {Fore.LIGHTBLACK_EX}codes!{Fore.WHITE}")

input() 