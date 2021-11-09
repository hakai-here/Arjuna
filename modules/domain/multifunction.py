import socket 
import requests
from data.data import HEADERS

apihack = "https://api.hackertarget.com/{}/?q={}"

def apihk(opt,x):

    if not x: return
    if x.split(".")[0].isnumeric(): x = socket.gethostbyname(x)
    else: pass
    req = requests.get(apihack.format(opt,x),stream=True,headers=HEADERS)
    for res in req.iter_lines():
        print(f"\t{res.decode('utf-8')}")
    return