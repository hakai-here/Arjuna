import prettytable
import requests
from prettytable import PrettyTable
HEADERS = {'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
           'Accept-Language' : 'en-US,en;q=0.5',
           'Accept-Encoding' : 'gzip, deflate',
           'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)  Chrome/93.0.4577.63 Safari/537.36"
          }


G = '\033[92m\033[1m'  
Y = '\033[93m' 
E = '\033[0m'  

def gitusers(x):
    print(f'{G}▰▰▰▰▰▰▰▰▰▰▰▰▰▰ Users ▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰ {E}')
    baseurl = "https://api.github.com/search/users?q={}"
    req = requests.get(baseurl.format(x),headers=HEADERS,timeout=60).json()
    if req['total_count'] == 0:
        print(" No result found ")
    else:
        k = req['items']
        for i in k:
            print(Y+"*"*40+E)
            L,R = res(i['type'])
            print(L,end="")
            print(f"User  : {i['login']}")
            print(f"Url   : {i['html_url']}")
            print(f"Type  : {i['type']}")
            print(f"Admin : {i['site_admin']}",end="")
            print(R)

def gitrepo(x):
    print(f'{G}▰▰▰▰▰▰▰▰▰▰▰▰ Repositories ▰▰▰▰▰▰▰▰▰▰▰▰ {E}')
    baseurl = "https://api.github.com/search/repositories?q={}"
    req = requests.get(baseurl.format(x),headers=HEADERS,timeout=60).json()
    if req['total_count'] == 0:
        print(" No result found ")
    else:
        k = req['items']
        for i in k:
            L,R = res(i['owner']['type'])
            print(Y+"*"*40+E)
            print(L,end="")
            print("Owner Detials:\n")
            print(f"User       : {i['owner']['login']}")
            print(f"Url        : {i['owner']['html_url']}")
            print(f"Type       : {i['owner']['type']}")
            print(f"Admin      : {i['owner']['site_admin']}")
            print("\nRepository detials:\n")
            print(f"Id         : {i['id']}")
            print(f"Repo Name  : {i['name']}")
            print(f"Repo Link  : {i['html_url']}")
            print(f"Breif      : {i['description']}")
            print(f"isForked   : {i['fork']}")
            print(f"Created at : {i['created_at']}")
            print(f"Updated at : {i['updated_at']}")
            print(f"Pushed at  : {i['pushed_at']}")
            print(f"Language   : {i['language']}")
            print(f"Visibility : {i['visibility']}")
            print(f"Branch     : {i['default_branch']}")
            print(R)


def res(x):
    if x in ['Organization']:
        return G,E
    else:
        return "",""

    
def init_github(domain):
    x = domain.split(".")
    gitusers(x[0])
    gitrepo(x[0 ])



