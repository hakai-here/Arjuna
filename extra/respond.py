

from socket import gethostbyname
from extra.for_inp import formaturl, is_ip
from modules.domain.activescan import init_activescan
from modules.domain.archive import archive_call
from modules.domain.integrated import detect
from modules.domain.crawler import init_crawl
from modules.domain.integrated import init_github
from modules.domain.header import indicator
from modules.domain.integrated import ip_map
from modules.domain.integrated import apihk
from modules.domain.integrated import init_searx
from modules.domain.integrated import init_procress
from modules.domain.integrated import init_hny
from modules.domain.integrated import init_sh_scan, ip_init
from modules.domain.integrated import main as scanp
from modules.domain.integrated import init_vulnscan
from modules.domain.whois import whois_call
from modules.domain.dork import init_dorks
from modules.domain.ohm import main as init_ohm
from modules.domain.password import nemopass as init_my
def init_proceed (k,x):
    k=k.lower()
    if k in ["all"]:
        for i in range (1,18):
            proceed(str(i), x)
    else:
        proceed(k,x)
def proceed(k,x):
        
        
        if k in ["1","locate"]:
            init_sh_scan(gethostbyname(x))
            ip_init(x)
        elif k in ["2","subdomain"]:
            init_procress(x)
        elif k in ["3","reversedns"]:
            if is_ip(x):
                apihk('reversedns',x)
            else:
                print(f"Given Target {x} is now an valid ip_address")
        elif k in ["4","cms"]:
            detect(x)
        elif k in ["5","portscan"]:
            scanp(x)
        elif k in ["6","vuln"]:
            init_vulnscan(x)
        elif k in ["7","header"]:
            indicator(x)
        elif k in ["8","crawl"]:
            init_crawl(formaturl(x))
        elif k in ["9","archive"]:
            archive_call(x)
        elif k in ["10","whois"]:
            whois_call(x)
        elif k in ["11","honeypot"]:
            init_hny(x)
        elif k in ["12","map"]:
            ip_map(x)
        elif k in ["13","dork","endpoint"]:
            init_dorks(x)
        elif k in ["14","github"]:
            init_github(x)
        elif k in ['15','risk','activescan']:
            init_activescan(x)
        elif k in ['16','csearch']:
            init_searx(x)
        elif k in ['18', 'ohcrawl']:
            init_ohm(x)
        elif k in ['17', 'ohm']:
            init_my(x)
