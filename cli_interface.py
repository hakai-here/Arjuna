#!/usr/bin/python3

from getpass import getpass
from sys import platform
import json
import re
from os import system
from time import sleep
from socket import gethostbyname
from data.data import flush
import module.hackertrget as apicall
from module.whois import whois_module
from module.subdomain import main as sub
from module.seccheck import indicator
from module.crawl import init_crawl, record
from module.username import run as usrname
from module.username import linkedin

G = '\033[92m'  
Y = '\033[93m'  
B = '\033[36m'  
R = '\033[91m' 
W = '\033[0m'
L = "\033[90m"
w = "\033[47m"
BLG = "\033[100m"
BB = "\033[104m"
WT= "\033[37m"


logo =f"""                                                                          
                                         WKX   NOddOW                 
                                       No;'.oO:.';,.,X                
                                      0,:ooo, 'ooooo;;0W              
                                     0,loooool'.;loool,;:k            
                                   WXd.':ooooool' .:oooo.c            
                                  K;.lK'  .,cooooc.';;c:.0            
                                 0'cd..;;:,  .';coo;'cl.l             
                                O.okkd.:co: l:.,;;,cl,..X             
                             W0k.'dkkko'0XOdK'lOkd:..;;'cN            
                         Wkc:;:ll:..ckk:cXXXX0odxoc;:xxl';W    NOxxdX 
                    WNWXl,:xkkkkkkkl.,kk,dXKdc;;cOKX0c;0WXW Nxo;.''.ll
                   K:'..;kkkkkkkkx:;, :kl.Ol.    xXXXXo.X Xl'.':xx'ON,
           WKXNW  l;d. lkkkkkkkkkkkxl,.lx.cKk.   .oOK0c.Ko;d;'kWx:0Wcd
           O .cclo''kl.:dokkkkkklkkkkkd,'..lox0xcOKkdodx;x;;xXXll0O;o     
            l';;lxk,'x:.;dolkkdx'ckkkkkko.'0         Wd;0llKKo:ckc;kW     ░█▀▀▀█ ░█▀▀▀█ ▀█▀ ░█▀▀█ ▀▀█▀▀  
            X,.cdkkk:..od,.;oko;'.ckkkkkkkl.;O       o.0;oxc:l' 'kW       ░█──░█ ─▀▀▀▄▄ ░█─ ░█▄▄█ ─░█──  
             d.:xkkkkxkx.:ko:;:cll..okkkkkkk: :X  NKO.:;':'.';:kW         ░█▄▄▄█ ░█▄▄▄█ ▄█▄ ░█─── ─░█── 
              O,.:xkkkkd;.'lxd,,:.;,.:kkkkkd.:,.lol..o..'  ;dK                        by :Saffcy_Bois  
                Xd,'cxkxllc:;..:';c.;.'xko,'occ0ddl  .;lk0N               
                  Nd. ..',;:::,;.;:.;do.. ,,:OXX0d;...0                     
                    N'    .       ..o  KXkkl:XXXXkloc'0               
                x''''.    0XOdc.    ;N     k.cO0lod'lW                
             Nd:.        ,X  Xd.    'X     O;,ooc:xK                  
     WWWNNNXXk..   .;ldkKXXd,     ;kW                                 
 WNNXK0OOOkkkkxd.   .';xkkk'     .OXW                                 
WX0OOkkkxxxxxxxx:'',;;;oxxd.  .      .;X                              
 NXK0OOkkkxxxxxxxxxxxxxxxxxoddkkk0KKKKKW                              
    WWNNXXKK000000O00000KKXXNNWW  
"""

menu = f"""
             {w}\033[30m Run\Combain number(s) [TARGET] or type exit to exit {W}

        {Y}01{W} {G}DNS_Lookup     {W}  {WT}Identify who is on domain{W}
        {Y}02{W} {G}GeoIp_Lookup   {W}  {WT}Discover the location of a domain {W}
        {Y}03{W} {G}Shared Dns     {W}  {WT}Find Shared DNS Servers{W}
        {Y}04{W} {G}Zone Transfer  {W}  {WT}Zone Transfer Test to get domains{W}
        {Y}05{W} {G}Reverse Dns    {W}  {WT}Reverse DNS Lookup to get server detias{W}
        {Y}06{W} {G}Whois Lookup   {W}  {WT}Whois Lookup to find registered owners{W}
        {Y}07{W} {G}Find Subdomains{W}  {WT}To Find All subdomains associated with The domain{W}
        {Y}08{W} {G}Analytics_ID   {W}  {WT}To Find Google Analytics ID {W}
        {Y}09{W} {G}Subnet Lookup  {W}  {WT}To determine properties of a network subnet {W}    
        {Y}10{W} {G}Reverse Ip     {W}  {WT}To reverse an IP to Find corresponding domain  {W} 
        {Y}11{W} {G}Banner Grabber {W}  {WT}Discover network services by simply querying   {W} 
        {Y}12{W} {G}Header Check   {W}  {WT}To Check Security Headers   {W} 
        {Y}13{W} {G}Crawl Web      {W}  {WT}Extract Links From Page {W} 
        {Y}14{W} {G}User Recon     {W}  {WT}Search For Username in web{W}
        {Y}15{W} {G}Number Recon   {W}  {WT}Seprate Countrycode and Number with Underscore{W}
        {Y}16{W} {G}Linkdein Recon {W}  {WT}Using Google Dorking to Find Linkedin Profile{W}
        
"""
def ipv4(x):
  return gethostbyname(x)

def formaturl(url):
    if not re.match('(?:http|ftp|https)://', url):
        print(f"{Y} No scheme found Defaulting to https://{W}")
        return 'https://{}'.format(url)
    return url

def man():
  print(f""" {G}
  run <module_number> [Target]
  combain <all the module numbers to combain> [Target]
  {W}""")

def clear():
  if platform == "linux" or platform == "linux2" or platform == "darwin":
      system("clear")
  elif platform == "win32":
      system('cls')


def init_check():
  clear()
  print(logo)
  sleep(0.3)
  #~~~json api check~~~~~

  f = open("api.json")
  data = json.load(f)
  for i in data['Virus_Total']:
    if 'Here_inside_this_double_quotes' in i["api"]:print(f"\n{Y}\t[-] Warning Required an api key from Virus_Total in api.json File {W}")
    else: print(f"\n{Y} No warnings found You are good to go{W}")
  getpass(f"\n{G}Press Ender to continue {W} ")
  clear()
  print(menu)
  
def run_init(x,y,z=1):
  print("-"*50,'\r')
  if x.lower() in('exit'): exit("\n Exiting ")
  elif x in ("01",'1'): apicall.apihk('dnslookup',y)
  elif x in ('4','04'): apicall.apihk('zonetransfer',y)
  elif x in ('2','02'): apicall.apihk('geoip',y)
  elif x in ('3','03'): apicall.apihk('findshareddns',y)
  elif x in ('5','05'): apicall.apihk('reversedns',y)
  elif x in ('6','06'): whois_module(y)
  elif x in ('7','07'): sub(domain=y)
  elif x in ('8','08'): apicall.apihk('analyticslookup',y)
  elif x in ('9','09'): apicall.apihk('subnetcalc',y)
  elif x in ('10'): apicall.apihk('reverseiplookup',y)
  elif x in ('11'): apicall.apibanner(ipv4(y))
  elif x in ('12'): indicator(formaturl(y))
  elif x in ('13'): init_crawl(formaturl(y)); record(y)
  elif x in ('14'): usrname(y)
  elif x in ('15'): apicall.phone(y)
  elif x in ('16'): linkedin(y)
  
  
  
  if(z == 0):
    getpass("\nEnter to clear Screen and Continue")
    clear()




def code_balancer(value):
  try:
    if value[0].lower() == "run":run_init(value[1],value[2],0)
    elif value[0].lower() == "combain":
      k = value[1]
      k=k.split(',')
      for i in k:
        run_init(i,value[2])
      getpass("\nEnter to clear Screen and Continue")
      clear()
    elif value[0].lower() == "menu": print(menu)
    elif value[0].lower() == "clear": clear()
    elif value[0].lower() == "exit": exit("\n Exiting ")
    elif value[0].lower() == "help": man()
    elif value[0].lower() == "flush": flush()
    else: pass
  except IndexError: print(f" {R}\n min 3 arguments requires in for {value[0]}() to work \n {W}")



def init_input():
  init_check()
  while True:
    get_input = input("~osipt~$ ")
    if "exec" in get_input:system(get_input.strip('exec'))
    else:get_input = get_input.split(" ")               # run module domain
    code_balancer(get_input)                       # combain run 1,2,3,4 domain
    





if __name__ == "__main__":
  try:init_input()
  except KeyboardInterrupt: exit("\n Exiting Due to Keybord Interrupt")