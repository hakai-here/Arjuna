from bs4.builder import TreeBuilder
import requests
import threading
from bs4 import BeautifulSoup
url="https://searx.be/search?q={}&categories=general&pageno={}&language=en-US"
from data.data import HEADERS
links=set()
wlinks=set()
def searchx(target,num):
    try:
        req=requests.get(url=url.format(target,num),headers=HEADERS)
        if req.status_code != 404:
            soup = BeautifulSoup(req.content,'html.parser')
            for link in soup.find_all('a'):
                l = link.get('href')
                if l in ['/','/about','/donate','/preferences','/stats','mailto:contact[at]searx.be','https://searx.space','https://searxng.github.io/searxng','https://github.com/searxng/searxng','https://github.com/searxng/searxng/issues']: pass
                else:
                    if 'web.archive.org' in l:
                        wlinks.add(l)
                    else:
                        links.add(l)

        else:
            return
    except:
        pass


def init_searx(target):
    thread=[]

    for i in range(100):
        t = threading.Thread(target=searchx , args=[target,i])
        t.daemon = True
        thread.append(t)

    for i in range(100):
        thread[i].start()

    for i in range(100):
        thread[i].join()
    
    with open (f'{target}.search.txt','a') as f:
        f.write(" Links : \n")
        for i in links:
            f.write(i+'\n')
        
        for i in wlinks:
            f.write(i+'\n')
    print(f" The run is been successful and the data is been stored in {target}.search.txt ")