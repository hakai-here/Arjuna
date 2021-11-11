
"""
respond
    search (in/for) ->search
    web/domain/ip -> web
    username    ->user
"""


from socket import gethostbyname
from extra.displaylist import Domain_menu, Main_menu
from extra.for_inp import formaturl, is_ip, stripurl, take
import requests
from modules.domain.archive import archive_call
from modules.domain.cms import detect
from modules.domain.crawler import init_crawl
from modules.domain.header import indicator
from modules.domain.ipmap import ip_map
from modules.domain.multifunction import apihk
from modules.domain.subdom import init_procress
from modules.domain.honeypot import init_hny
from modules.domain.iplookup import init_sh_scan, ip_init
from modules.domain.portscan import main as scanp
from modules.domain.vulnscan import init_vulnscan
from modules.domain.whois import whois_call
from modules.domain.dork import init_dorks


def proceed(k,x):
        k=k.lower()
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
        elif k in ["12","ipmap"]:
            ip_map(x)
        elif k in ["13","dork"]:
            init_dorks


