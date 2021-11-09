import requests
from data.data import HEADERS


def ip_map(domain):
    domin = 'https://dnsdumpster.com/static/map/{}.png'.format(domain)
    req = requests.get(domin,headers=HEADERS,timeout=60)

    if req.status_code == 200:
        name = domain+'.png'
        with open(name,"wb") as f:
            f.write(req.content)
            print(f"{name} DNS Map image is saved Locally")
    else:
        print("\n Not able to find a map")
