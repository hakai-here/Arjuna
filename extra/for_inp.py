from prompt_toolkit import prompt
import re
import json
from os import system,name




def is_ip(address):
    return not address.split('.')[-1].isalpha()

def take(x):
    #return prompt(f"┌──[Nem0]{x}\n└──╼$ ")
    return prompt(f"{x}>> ")

def formaturl(url):
    if not re.match('(?:http|ftp|https)://', url):
        return 'https://{}'.format(url)
    return url

def stripurl(url):
    if re.match('(?:http|ftp|https)://', url):
        for i in ["https://","http://","ftp://"]:
           url=url.strip(i)
        return url
    return url

def screen_clear():
   if name == 'posix':
      system('clear')
   else:
      system('cls')