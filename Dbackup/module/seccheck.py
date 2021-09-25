from data.data import HEADERS
import requests
from prettytable import PrettyTable
from urllib.parse import urlparse
from socket import gethostbyname


G = '\033[92m'  
Y = '\033[93m' 
B = '\033[94m' 
R = '\033[91m'  
W = '\033[0m'  




def indicator(x):
    list1=[]
    list2=[]
    x = format(x)
    k = urlparse(x).netloc
    searchlist=["Date","Server","Content-Type","Cache-Control","X-TEC-API-VERSION","X-TEC-API-ROOT","X-TEC-API-ORIGIN","Transfer-Encoding","Pragma"]
    headerlist=["X-Frame-Options","Content-Security-Policy","X-XSS-Protection","X-Content-Type-Options","Strict-Transport-Security","P3P","X-Powered-By","X-Download-Options","Content-Disposition","Public-Key-Pins","Expect-CT","Cross-Origin-Resource-Policy","Cross-Origin-Opener-Policy","Access-Control-Allow-Origin","Access-Control-Allow-Credentials","Cross-Origin-Embedder-Policy","Feature-Policy","X-DNS-Prefetch-Control","Referrer-Policy","X-Permitted-Cross-Domain-Policies"]
    try:response=requests.get(x,params=None, headers=HEADERS, cookies=None, auth=None, timeout=None).headers
    except : print("{R} Unable To connect  {W}") ; return
    ip = gethostbyname(k)
    t = PrettyTable(["Raw Headers"," informations"])
    t.add_row([B+"IP",ip+W])
    for i in searchlist:
        if i in response:
            t.add_row([B+i,response[i]+W])
    print(t)
    for i in headerlist:
        if i in response:
            list1.append(i)

        else:
            list2.append(i)
    
    t = PrettyTable(['Headers', 'status'])
    for i in list1:
        k = G+i+W
        t.add_row([k,G+'✔'+W])

    for i in list2:
        k = R+i+W
        t.add_row([k,R+'✘'+W])

    print(t)

