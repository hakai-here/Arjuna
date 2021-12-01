import requests
from time import sleep
from extra.formatout import formatresult

from modules.domain.github import res


HEADERS = {'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
           'Accept-Language' : 'en-US,en;q=0.5',
           'Accept-Encoding' : 'gzip, deflate',
           'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)  Chrome/93.0.4577.63 Safari/537.36",
           'Content-Type': 'application/x-www-form-urlencoded',
           'charset':'UTF-8'
          }

logg = set()
def showw(x):
    logg.add(x)
    print(x)

animation = [
"▰▱▱▱▱▱▱▱▱▱▱▱▱▱▱ Active scan is on :)",
"▰▰▱▱▱▱▱▱▱▱▱▱▱▱▱ aCtive scan is on :)",
"▰▰▰▱▱▱▱▱▱▱▱▱▱▱▱ acTive scan is on :)",
"▰▰▰▰▱▱▱▱▱▱▱▱▱▱▱ actIve scan is on :)",
"▰▰▰▰▰▱▱▱▱▱▱▱▱▱▱ actiVe scan is on :)",
"▰▰▰▰▰▰▱▱▱▱▱▱▱▱▱ activE scan is on :)",
"▰▰▰▰▰▰▰▱▱▱▱▱▱▱▱ active Scan is on :)",
"▰▰▰▰▰▰▰▰▱▱▱▱▱▱▱ active sCan is on :)",
"▰▰▰▰▰▰▰▰▰▱▱▱▱▱▱ active scAn is on :)",
"▰▰▰▰▰▰▰▰▰▰▱▱▱▱▱ active scaN Is on :)",
"▰▰▰▰▰▰▰▰▰▰▰▱▱▱▱ active scan iS on :)",
"▰▰▰▰▰▰▰▰▰▰▰▰▱▱▱ active scan is On :)",
"▰▰▰▰▰▰▰▰▰▰▰▰▰▱▱ active scan is oN :)",
"▰▰▰▰▰▰▰▰▰▰▰▰▰▰▱ active scan is on ;)",
"▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰ active scan is on :>",
]

notcomplete = True

def loading():  
    i = 0
    while i<1100:
        print('',animation[i % len(animation)],"[approx : 2 min]", end='\r')
        sleep(.1)
        i += 1
    print(" ")


url = "https://pulsedive.com/api/analyze.php"

params = {
    "probe": "1",
    "pretty": "1",
     "key": "7f65bbd0ee69ddc2cd42fe63c0c6d2db92635657f58db5d1d5212f6084404401"
    }

param2 = {
  "pretty": "1",
  "key": "7f65bbd0ee69ddc2cd42fe63c0c6d2db92635657f58db5d1d5212f6084404401"
}


def postscan():
    req = requests.post(url,headers=HEADERS,params=params).json()
    return req['qid']

def getscan():
    requ  = requests.get(url,headers=HEADERS,params=param2).json()
    return requ

def init_activescan(domain):
    domain = domain.split(" ")
    params['value'] = domain[0]
    param2["qid"] = postscan()
    loading()
    getresult=getscan()
    forresult(getresult)
#############################################
def error_check(result):
    try:
        if result['error']:
            return True
    except KeyError:
        return False

def forresult(result):
    if error_check(result):return

    if result['status'] == 'done':
        formatresult(result)
    else:
        print("wait please")