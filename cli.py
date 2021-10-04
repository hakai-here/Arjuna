from getpass import getuser,getpass
from os import system,name
from data.data import flush,TB, printlinkedin
from module.archive import archive_call
from module.crawl import init_crawl
from module.hackertrget import apihk,apibanner, iplookup, phone
from module.hunter import search_domain
from module.username import linkedin, run
from module.whois import whois_module
from socket import gethostbyname
from module.seccheck import indicator
import re
from time import sleep
from module.subdomain import main as sub
import json




Bld = "\033[1m"
G = '\033[92m'  
Y = '\033[93m'  
B = '\033[36m'  
R = '\033[91m' 
W = '\033[0m'
L = "\033[90m"
w = "\033[47m"
WT = "\033[37m"

menu_list = {
    '1':'dns',
    '2':'zone',
    '3':'geoip',
    '4':'shareddns',
    '5':'analytics',
    '6':'subnetcalc',
    '7':'reverseip',
    '8':'reversedns',
    '10':'whois',
    '9':'banner',
    '11':'subdomain',
    '12':'headers',
    '13':'crawl',
    '14':'user',
    '15':'number',
    '16':'linkedin',
    '17':'archive',
    '18':'email'
}

dom_all = [
    'dns',
    'geoip',
    'zone',
    'shareddns',
    'analytics',
    'subnetcalc',
    'whois',
    'banner',
    'headers',
    'crawl',
    'archive'
]

z=False

menu = f"""
             {w}\033[30m Do\Combain number(s) [TARGET] or type exit to exit {W}

        {Y} 1{W} {G}DNS Lookup      {W}  {WT}To determine Mail,DNS servers and SPF records{W}
        {Y} 2{W} {G}Zone Transfer   {W}  {WT}Zone Transfer Test to get domains{W}
        {Y} 3{W} {G}GeoIp Lookup    {W}  {WT}Discover the location of a domain {W}
        {Y} 4{W} {G}Shared Dns      {W}  {WT}Find Shared DNS Servers{W}
        {Y} 5{W} {G}Analytics ID    {W}  {WT}To Find Google Analytics ID {W}
        {Y} 6{W} {G}Subnet Lookup   {W}  {WT}To determine properties of a network subnet {W}    
        {Y} 7{W} {G}Reverse Dns     {W}  {WT}Reverse DNS Lookup to get server detials {W}
        {Y} 8{W} {G}Reverse Ip      {W}  {WT}To reverse an IP to Find corresponding domain  {W} 
        {Y} 9{W} {G}Banner Grabber  {W}  {WT}Discover network services by simply querying   {W} 
        {Y}10{W} {G}Whois Lookup    {W}  {WT}Whois Lookup to find registered owners{W}
        {Y}11{W} {G}Subdomain Enum  {W}  {WT}To Find All subdomains associated with The domain{W}
        {Y}12{W} {G}Headers Check   {W}  {WT}To Check Security Headers   {W} 
        {Y}13{W} {G}Crawl Web       {W}  {WT}Extract Links From Page {W} 
        {Y}14{W} {G}User Recon      {W}  {WT}Search For Username in web{W}
        {Y}15{W} {G}Number Recon    {W}  {WT}Seprate Countrycode and Number with Underscore{W}
        {Y}16{W} {G}Linkdein Recon  {W}  {WT}Using Google Dorking to Find Linkedin Profile{W}
        {Y}17{W} {G}Archive Crawl   {W}  {WT}Crawling The Archive Web of given domain  {W}
        {Y}18{W} {G}Email finder    {W}  {WT}Find Email of employees(mostly) of given domain {W}
        
"""

logo =f''' 
{G}
╭━━━╮╭╮╱╭╮╱╱╱╱╱╱╭╮╱╱/╱╱╱╱/╭━━━╮╱╱╱╱╱╭━╮╱╱╱╱╱╱╱╱╱╱╱╭━━━━╮╱╱╱╱╭╮╭╮╱╭━━┳╮
┃╭━╮┣╯╰┳╯╰╮╱╱╱╱╱┃┃╱╱/╱╱╱╱/┃╭━╮┃╱╱╱╱╱┃╭╯╱╱╱╱╱╱╱╱╱╱╱┃╭╮╭╮┃╱╱╱╱┃┃┃┃╱╰┫┣╯╰╮
┃┃╱┃┣╮╭┻╮╭╋━━┳━━┫┃╭╮/╱╱╱╱/┃╰━━┳╮╭┳━┳╯╰┳━━┳━━┳━━╮╱╱╰╯┃┃┣┻━┳━━┫┃┃┃╭╮┃┣╮╭╯
┃╰━╯┃┃┃╱┃┃┃╭╮┃╭━┫╰╯╯/╭━━╮/╰━━╮┃┃┃┃╭┻╮╭┫╭╮┃╭━┫┃━┫╭━━╮┃┃┃╭╮┃╭╮┃┃┃╰╯╯┃┃┃┃
┃╭━╮┃┃╰╮┃╰┫╭╮┃╰━┫╭╮╮/╰━━╯/┃╰━╯┃╰╯┃┃╱┃┃┃╭╮┃╰━┫┃━┫╰━━╯┃┃┃╰╯┃╰╯┃╰┫╭╮┳┫┣┫╰╮
╰╯╱╰╯╰━╯╰━┻╯╰┻━━┻╯╰╯/╱╱╱╱/╰━━━┻━━┻╯╱╰╯╰╯╰┻━━┻━━╯╱╱╱╱╰╯╰━━┻━━┻━┻╯╰┻━━┻━╯
             Dev's - Version  Alpha Binary Testing 
{W}'''


username = getuser()

def ipv4(x):
  return gethostbyname(x)

def init_module():
    cleard()
    print(logo)
    getpass("Enter >")
    cleard()
    print(menu)
    global z
    while True:
        get_input = input(G+Bld+f"[{username}@Analyzer]$ "+W)
        if 'showall' in get_input:
            z = True
        else:
            z = False
        get_input = get_input.split()
        balancer(get_input)

def all_lister(x,y):
    if (str(x) == 'domain'):
        for i in dom_all:
            run_init(i,y)


def formaturl(url):
    if not re.match('(?:http|ftp|https)://', url):
        return 'https://{}'.format(url)
    return url

def cleard():
  if(name == 'posix'):
      system("clear")
  else:
      system("cls")

def tuner(x,y):
    if x.isnumeric():
        run_init(menu_list[x],y)
    else:
        run_init(x,y)

def list_show(x):
    if(str(x).lower() == "headers"):
        print(TB)

def balancer(inp_values):
    try:
        if (inp_values[0].lower() == "do"):
            tuner(inp_values[1],inp_values[2])
        elif(inp_values[0].lower() == "all"):
            all_lister(inp_values[1],inp_values[2])
        elif(inp_values[0].lower() == "combain"):
            pass
        elif(inp_values[0].lower() == "menu"):
            print(menu)
        elif(inp_values[0].lower() == "exit"):
            exit(0)
        elif(inp_values[0].lower() == "clear" or inp_values[0].lower() == 'screen'):
            cleard()
        elif(inp_values[0].lower() == "flush"):
            flush()
        elif(inp_values[0].lower() == "list"):
            list_show(inp_values[1])
        elif(inp_values[0].lower() == "help"):
            pass
        else:
            pass
        
    except IndexError:
        print("\n Missing Value or Command")

def real(x):
  if x.lower() == "show":
    return True
  else:
    return False

def run_init(x,y):
    print(f"{Y}{Bld}[module {x} running ] {W}")
    if(str(x) == 'dns'):
        apihk('dnslookup',y)

    elif(str(x) == 'zone'):
        apihk('zonetransfer',y)

    elif(str(x) == 'geoip'):
        iplookup(y)

    elif(str(x) == 'shareddns'):
        apihk('findshareddns',y)

    elif(str(x) == "analyticID"):
        apihk('analyticslookup',y)

    elif(str(x) == 'subnetcalc'):
        apihk('subnetcalc',y)

    elif(str(x) == 'reverseip'):
        apihk('reverseiplookup',y)

    elif(str(x) == 'reversedns'):
        apihk('reversedns',y)

    elif(str(x) == 'whois'):
        whois_module(y)
    
    elif(str(x) == 'banner'):
        apibanner(ipv4(y))
    
    elif(str(x) == 'subdomain'):
        sub(y)

    elif(str(x) == 'headers'):
        indicator(formaturl(y),z)

    elif(str(x) == 'crawl'):
        init_crawl(y)

    elif(str(x) == 'user'):
        run(username=y)
    
    elif(str(x) == 'number'):
        phone(tobesplited=y)

    elif(str(x) == 'linkedin'):
        linkedin(y)
        y=y.split('.')
        linkedin(y[0])
        printlinkedin()
    
    elif(str(x) == 'archive'):
        archive_call(domain=y)
    
    elif(str(x) == 'email'):
        search_domain(y)

    else:
        print("\n Error")
    

if __name__ == "__main__":
    try:
        init_module()
    except KeyboardInterrupt:
        exit("\n Exiting")