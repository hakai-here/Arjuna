from socket import gethostbyname
from data.data import HEADERS, api_load
import requests

def init_hny(x):
    url = 'https://api.shodan.io/labs/honeyscore/{}?key={}'.format(gethostbyname(x),api_load("Shodan"))
    try:
        req = requests.get(url=url,headers=HEADERS).text
    except:
        req = None
        print("\n Unable to reach ")
    if "error" in req or "404" in req:
        print(f"\n Ip Not found ")
    elif req:
        prob = str(float(req)*10)
        print("Chance of Honeypot : {}%".format(req))
    else:
        print(f" Never gonna give you up, But now Nemo now need to ")