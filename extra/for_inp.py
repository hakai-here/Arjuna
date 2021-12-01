
import re
from os import system,name




def is_ip(address):
    return not address.split('.')[-1].isalpha()


def formaturl(url):
    if not re.match('(?:http|ftp|https)://', url):
        return 'https://{}'.format(url)
    return url



def screen_clear():
   if name == 'posix':
      system('clear')
   else:
      system('cls')