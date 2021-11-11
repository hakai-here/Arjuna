import requests 
from bs4 import BeautifulSoup
from time import sleep
from os import name

bold ="\033[1m"
green ="\033[92m"
end = "\033[0m"
red = "\033[91m"

'''
Problem occured and needed to be resolved  :
    google is blocking all request after 2 runs
    add more dorks if possible 

'''





url = "https://www.google.com/search?q={main}%20{side}&start=0&client=firefox-b-e"
header = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36" ,
    'referer':'https://www.google.com/'
    }
log_list=[
"inurl:admin",
"inurl:login",
"inurl:adminlogin",
"inurl:cplogin",
"inurl:weblogin",
"inurl:quicklogin",
"inurl:wp-admin",
"inurl:wp-login",
"inurl:portal",
"inurl:userportal",
"inurl:loginpanel",
"inurl:memberlogin",
"inurl:remote",
"inurl:dashboard",
"inurl:auth",
"inurl:exchange",
"inurl:ForgotPassword",
"inurl:test",
"inurl:config"]

filetypes=[
"filetype:doc",
"filetype:docx",
"filetype:xls",
"filetype:xlsx",
"filetype:ppt",
"filetype:pptx",
"filetype:mdb",
"filetype:pdf",
"filetype:sql",
"filetype:txt",
"filetype:rtf",
"filetype:csv",
"filetype:xml",
"filetype:conf",
"filetype:dat",
"filetype:ini",
"filetype:log",
"index%20of:id_rsa%20id_rsa.pub"
]

directory = [
'intitle:%22index%20of%22%20%22parent%20directory%22',
'intitle:%22index%20of%22%20%22DCIM%22',
'intitle:%22index%20of%22%20%22ftp%22',
'intitle:%22index%20of%22%20%22backup%22',
'intitle:%22index%20of%22%20%22mail%22',
'intitle:%22index%20of%22%20%22password%22',
'intitle:%22index%20of%22%20%22pub%22'
]

def init_main(domain,x):
    count=0
    gsite=f"site:{domain}"
    for i in x:
        baseurl=url.format(main=gsite,side=i)
        m = i.split(":")
        sleep(3)
        req=requests.get(baseurl,headers=header,timeout=20).content
        soup= BeautifulSoup(req,'html.parser')
        for link in soup.find_all('a'):
            k=str(link.get('href'))
            if "www.google.com/policies/terms/" in k or "support.google.com/websearch/answer/86640" in k:
                print(f"\t{red}{bold}Google is Blocking the request{end}")
                return
            else:
                if domain in k and "http" in k and "maps.google.com" not in k:
                    print("\t{}{}{}\t{}: {} ".format(bold,green,m[1],end,k))
                    count=1
    if count == 0:
            print(f"{bold}{green}\t None found {end}")

def identify():
    global bold,green,end,red
    if name == "nt":
        bold = ""
        green=""
        end=""
        red=""




def init_dorks(domain):
    identify()
    print(f"{bold}{green}Checking For admin page{end} :\n")
    init_main(domain,log_list)
    print(f"{bold}{green}Checking For Filetypes{end} : \n")
    init_main(domain,filetypes)
    print(f"{bold}{green}Checking for directory{end} : \n")
    init_main(domain,directory)

    
