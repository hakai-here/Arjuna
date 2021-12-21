from tabulate import tabulate
import re
import multiprocessing
import json
import urllib.parse as urlparse
import socket
import shodan
from data.data import HEADERS,api_load
from treelib import Tree
import socket
import os
import time
import threading
import sys
from queue import Queue
from datetime import datetime
from prettytable import PrettyTable
import requests
from modules.domain.vscan.sql import scan_sql_injection
from modules.domain.vscan.vuln import ClickJacking
from modules.domain.vscan.header import init_header
from extra.for_inp import formaturl
def catolog(x):
    m =""
    for i in x:
        m +=i
        m +=" "
    return m

def ver(i):
    try:
        return i['version']
    except KeyError:
        return "--"

def detect(domain):
    url="https://whatcms.org/API/Tech?key=1641c3b9f2b1c8676ceaba95d00f7cf2e3531830c5fa9a6cc5e2d922b2ed7165dcce66&url={url}".format(url=domain)
    cms_data = requests.get(url).json()
    cms_code = cms_data['result']
    if cms_code['code'] == 200:
        k = cms_data['results']
        t= PrettyTable(["Name","Categories","Version"])
        for i in k:
            t.add_row([ i['name'],catolog(i['categories']), ver(i) ])
        print(t)
    else:
        print("Error Occured")


G,E="",""
import requests
from prettytable import PrettyTable
HEADERS = {'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
           'Accept-Language' : 'en-US,en;q=0.5',
           'Accept-Encoding' : 'gzip, deflate',
           'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)  Chrome/93.0.4577.63 Safari/537.36"
          }

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
        print(f" Never gonna give you up, But now t1t5 now need to ")




iplookurl = "https://ipgeolocation.abstractapi.com/v1/?api_key={}&ip_address={}"
	
def ip_init(x):
    try:
        tree = Tree()
        url = iplookurl.format(api_load('Abstract'),socket.gethostbyname(x))
        req = requests.get(url,headers=HEADERS).json()
        tree.create_node(str(x),"main")
        if req['ip_address']:
            tree.create_node("Ip","ip",parent="main")
            tree.create_node(str(req['ip_address']),"ipaddress",parent="ip")
        if req['city']:	
            tree.create_node("City","city",parent="main")
            tree.create_node(str(req['city']),"cityy",parent="city")
        if req['region']:
            tree.create_node("Region","region",parent="main")
            tree.create_node(str(req['region']),"reg",parent="region")
        if req['postal_code']:
            tree.create_node("Postal Code","pc",parent="main")
            tree.create_node(str(req['postal_code']),"postal",parent="pc")
        if req['country']:
            tree.create_node("Country","cont",parent="main")
            tree.create_node(str(req['country']),"icon",parent="cont")
        if req['continent']:
            tree.create_node("Continent","conte",parent="main")
            tree.create_node(str(req['continent']),"contee",parent="conte")
        if req['longitude']:
            log = req["longitude"]
            tree.create_node("Logitude","log",parent="main")
            tree.create_node(str(req["longitude"]),"logi",parent="log")
        if req['latitude']:
            lat = req['latitude']
            tree.create_node("Latitude","lat",parent="main")
            tree.create_node(str(req["latitude"]),"lati",parent="lat")
        if log and lat:
            tree.create_node("Google Map","map",parent="main")
            k="https://maps.google.com/?q={lat},{log}".format(log=log,lat=lat)
            tree.create_node(k,"ma",parent="map")
        data2=req['security']
        tree.create_node("Security","sec",parent="main")
        if data2['is_vpn']:
            tree.create_node("Vpn_service","vpn",parent="sec")
            tree.create_node("Yes","choice",parent="vpn")
        else:
            tree.create_node("Vpn_service","vpn",parent="sec")
            tree.create_node("No","choice",parent="vpn")
        data2 = req['connection']
        tree.create_node("Connections","conn",parent="main")
        if data2['isp_name']:
            tree.create_node("Internet Serice Provider","isp",parent="conn")
            tree.create_node(str(data2['isp_name']),"is",parent="isp")
        if data2['organization_name']:
            tree.create_node("Organization name","org",parent="conn")
            tree.create_node(str(data2['organization_name']),"isb",parent="org")
        if data2['autonomous_system_number']:
            tree.create_node("Autonomous system number","asn",parent="conn")
            tree.create_node(str(data2['autonomous_system_number']),"an",parent="asn")
        if data2['autonomous_system_organization']:
            tree.create_node("Autonomous system organization","aso",parent="conn")
            tree.create_node(str(data2['autonomous_system_organization']),"as",parent="aso")
        if data2['connection_type']:
            tree.create_node("Connection type","ct",parent="conn")
            tree.create_node(str(data2['connection_type']),"cto",parent="ct")
        print("\n")
        tree.show()
      
    
    except socket.gaierror:
        print("[-]Invalid Url Found",x)
    
    except UnboundLocalError:
        print("[-]Error in referencing varibles from request ")

def init_sh_scan(IP):
    api = shodan.Shodan(api_load("Shodan"))
    try:    
        host = api.host(IP)
        print("[+]IP Address   :" + str(host['ip_str']))
        print("[+]Country      :" + str(host['country_name']))
        print("[+]City         :" + str(host['city']))
        print("[+]Organization :" + str(host['org']))
        print("[+]ISP          :" + str(host['isp']))
        print("[+]Open ports   :" + str(host['ports']))
    except:
        print("[-]Unable to access by shodan")





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



apihack = "https://api.hackertarget.com/{}/?q={}"

def apihk(opt,x):

    if not x: return
    if x.split(".")[0].isnumeric(): x = socket.gethostbyname(x)
    else: pass
    req = requests.get(apihack.format(opt,x),stream=True,headers=HEADERS)
    for res in req.iter_lines():
        print(f"\t{res.decode('utf-8')}")
    return








def main(target):
    socket.setdefaulttimeout(0.30)
    print_lock = threading.Lock()
    discovered_ports = []
    try:
        t_ip = socket.gethostbyname(target)
    except (UnboundLocalError, socket.gaierror):
        print("\n[-]Invalid format. Please use a correct IP or web address[-]\n")
        sys.exit()
    print("\n\tPort\t\tState")
    print("-" * 34)
    t1 = datetime.now()

    

    def portscan(port):

       s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
       
       try:
          conx = s.connect((t_ip, port))
          with print_lock:
             print("\t{}\t\topen".format(port))
             discovered_ports.append(str(port))
          conx.close()

       except (ConnectionRefusedError, AttributeError, OSError):
          pass

    def threader():
       while True:
          worker = q.get()
          portscan(worker)
          q.task_done()
      
    q = Queue()
    for x in range(200):
       t = threading.Thread(target = threader)
       t.daemon = True
       t.start()

    for worker in range(1, 10000):
       q.put(worker)

    q.join()

    t2 = datetime.now()
    total = t2 - t1
    print("\n","[duration {}] Portscan completed".format(str(total)),"\n")




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





is_windows = sys.platform.startswith('win')
G = '\033[92m' 
Y = '\033[93m'  
R = '\033[91m'  
W = '\033[0m'  
 


def parser_error(errmsg):     
    print(R + "Error: " + errmsg + W)
    sys.exit()

def store(z,y):
    x = z+".txt"

    with open(x,'wt') as f:
        for i in y:
            f.write(i+os.linesep)
    print(f' File Has Been Saved name of {x}')

def subdomain_sorting_key(hostname):
    parts = hostname.split('.')[::-1]
    if parts[-1] == 'www':
        return parts[:-1], 1
    return parts, 0

class enumratorBase(object):
    def __init__(self, base_url, engine_name, domain, subdomains=None, silent=False, verbose=True):
        subdomains = subdomains or []
        self.domain = urlparse.urlparse(domain).netloc
        self.session = requests.Session()
        self.subdomains = []
        self.timeout = 25
        self.base_url = base_url
        self.engine_name = engine_name
        self.silent = silent
        self.verbose = verbose
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.8',
            'Accept-Encoding': 'gzip',
        }
        self.print_  

    def print_(self, text):
        if not self.silent:
            print(text)
        return


    def send_req(self, query, page_no=1):

        url = self.base_url.format(query=query, page_no=page_no)
        try:
            resp = self.session.get(url, headers=self.headers, timeout=self.timeout)
        except Exception:
            resp = None
        return self.get_response(resp)

    def get_response(self, response):
        if response is None:
            return 0
        return response.text if hasattr(response, "text") else response.content

    def check_max_subdomains(self, count):
        if self.MAX_DOMAINS == 0:
            return False
        return count >= self.MAX_DOMAINS

    def check_max_pages(self, num):
        if self.MAX_PAGES == 0:
            return False
        return num >= self.MAX_PAGES


    def extract_domains(self, resp):        
        return

    def check_response_errors(self, resp):
        return True

    def generate_query(self):
        return

    def get_page(self, num):        
        return num + 10

    def enumerate(self, altquery=False):
        flag = True
        page_no = 0
        prev_links = []
        retries = 0
        while flag:
            query = self.generate_query()
            count = query.count(self.domain)  
            if self.check_max_subdomains(count):
                page_no = self.get_page(page_no)
            if self.check_max_pages(page_no):  
                return self.subdomains
            resp = self.send_req(query, page_no)
            if not self.check_response_errors(resp):
                return self.subdomains
            links = self.extract_domains(resp)
            if links == prev_links:
                retries += 1
                page_no = self.get_page(page_no)
                if retries >= 3:
                    return self.subdomains
            prev_links = links
        return self.subdomains

class enumratorBaseThreaded(multiprocessing.Process, enumratorBase):
    def __init__(self, base_url, engine_name, domain, subdomains=None, q=None, silent=False, verbose=True):
        subdomains = subdomains or []
        enumratorBase.__init__(self, base_url, engine_name, domain, subdomains, silent=silent, verbose=verbose)
        multiprocessing.Process.__init__(self)
        self.q = q
        return

    def run(self):
        domain_list = self.enumerate()
        for domain in domain_list:
            self.q.append(domain)

class Virustotal(enumratorBaseThreaded):
    def __init__(self, domain, subdomains=None, q=None, silent=False, verbose=True):
        subdomains = subdomains or []
        base_url = 'https://www.virustotal.com/api/v3/domains/{domain}/subdomains'
        self.engine_name = "Virustotal"
        if os.getenv("VT_APIKEY") is None:
            VT_APIKEY=api_load('Virus_Total')
            VT_APIKEY=VT_APIKEY.strip()
            if VT_APIKEY != "":
                os.environ["VT_APIKEY"]=(VT_APIKEY)
        else:
            VT_APIKEY = os.getenv("VT_APIKEY")
        os.environ["VT_APIKEY"]=(VT_APIKEY)
        self.apikey = os.getenv('VT_APIKEY', None)
        self.q = q
        super(Virustotal, self).__init__(base_url, self.engine_name, domain, subdomains, q=q, silent=silent, verbose=verbose)
        self.url = self.base_url.format(domain=self.domain)
        return

    def send_req(self, url):
        try:
            self.headers.update({'X-ApiKey':self.apikey})
            resp = self.session.get(url, headers=self.headers, timeout=self.timeout)
        except Exception as e:
            self.print_(e)
            resp = None
        return self.get_response(resp)

    def enumerate(self):
        if self.apikey:
            while self.url != '':
                resp = self.send_req(self.url)
                resp = json.loads(resp)
                if 'error' in resp:
                    self.print_(R + "Error Code: {}".format(resp['error']["code"]) +W)
                    self.print_(R + "Virus Total Server Message: {}".format(resp['error']["message"]) + W)
                    break
                if 'links' in resp and 'next' in resp['links']:
                    self.url = resp['links']['next']
                else:
                    self.url = ''
                self.extract_domains(resp)
        else:
            self.print_(R + "[!] Error: VirusTotal API key environment variable not found. Skipping" + W)
            self.print_(R + "[!] To get a VT APIKEY, register at https://www.virustotal.com/gui/join-us" +W)
        return self.subdomains

    def extract_domains(self, resp):
        try:
            for i in resp['data']:
                if i['type'] == 'domain':
                    subdomain = i['id']
                    if not subdomain.endswith(self.domain):
                        continue
                    if subdomain not in self.subdomains and subdomain != self.domain:
                        self.subdomains.append(subdomain.strip())
        except Exception:
            pass

class ThreatCrowd(enumratorBaseThreaded):
    def __init__(self, domain, subdomains=None, q=None, silent=False, verbose=True):
        subdomains = subdomains or []
        base_url = 'https://www.threatcrowd.org/searchApi/v2/domain/report/?domain={domain}'
        self.engine_name = "ThreatCrowd"
        self.q = q
        super(ThreatCrowd, self).__init__(base_url, self.engine_name, domain, subdomains, q=q, silent=silent, verbose=verbose)
        return

    def req(self, url):
        try:
            resp = self.session.get(url, headers=self.headers, timeout=self.timeout)
        except Exception:
            resp = None
        return self.get_response(resp)

    def enumerate(self):
        url = self.base_url.format(domain=self.domain)
        resp = self.req(url)
        self.extract_domains(resp)
        return self.subdomains

    def extract_domains(self, resp):
        try:
            links = json.loads(resp)['subdomains']
            for link in links:
                subdomain = link.strip()
                if not subdomain.endswith(self.domain):
                    continue
                if subdomain not in self.subdomains and subdomain != self.domain:
                    self.subdomains.append(subdomain.strip())
        except Exception as e:
            pass

class CrtSearch(enumratorBaseThreaded):
    def __init__(self, domain, subdomains=None, q=None, silent=False, verbose=True):
        subdomains = subdomains or []
        base_url = 'https://crt.sh/?q=%25.{domain}'
        self.engine_name = "SSL Certificates"
        self.q = q
        super(CrtSearch, self).__init__(base_url, self.engine_name, domain, subdomains, q=q, silent=silent, verbose=verbose)
        return

    def req(self, url):
        try:
            resp = self.session.get(url, headers=self.headers, timeout=self.timeout)
        except Exception:
            resp = None
        return self.get_response(resp)

    def enumerate(self):
        url = self.base_url.format(domain=self.domain)
        resp = self.req(url)
        if resp:
            self.extract_domains(resp)
        return self.subdomains

    def extract_domains(self, resp):
        link_regx = re.compile('<TD>(.*?)</TD>')
        try:
            links = link_regx.findall(resp)
            for link in links:
                link = link.strip()
                subdomains = []
                if '<BR>' in link:
                    subdomains = link.split('<BR>')
                else:
                    subdomains.append(link)
                for subdomain in subdomains:
                    if not subdomain.endswith(self.domain) or '*' in subdomain:
                        continue
                    if '@' in subdomain:
                        subdomain = subdomain[subdomain.find('@')+1:]
                    if subdomain not in self.subdomains and subdomain != self.domain:
                        self.subdomains.append(subdomain.strip())
        except Exception as e:
            print(e)
            pass

class PassiveDNS(enumratorBaseThreaded):
    def __init__(self, domain, subdomains=None, q=None, silent=False, verbose=True):
        subdomains = subdomains or []
        base_url = 'https://api.sublist3r.com/search.php?domain={domain}'
        self.engine_name = "PassiveDNS"
        self.q = q
        super(PassiveDNS, self).__init__(base_url, self.engine_name, domain, subdomains, q=q, silent=silent, verbose=verbose)
        return

    def req(self, url):
        try:
            resp = self.session.get(url, headers=self.headers, timeout=self.timeout)
        except Exception as e:
            resp = None
        return self.get_response(resp)

    def enumerate(self):
        url = self.base_url.format(domain=self.domain)
        resp = self.req(url)
        if not resp:
            return self.subdomains
        self.extract_domains(resp)
        return self.subdomains

    def extract_domains(self, resp):
        try:
            subdomains = json.loads(resp)
            for subdomain in subdomains:
                if subdomain not in self.subdomains and subdomain != self.domain:
                    self.subdomains.append(subdomain.strip())
        except Exception as e:
            pass

def init_procress(domain, threads=7000 ,silent=None):
    print(f"{G} Take a rest t1t5 is doing the work {W}")
    try:
        name = socket.gethostbyname(domain)
        engines= None
        search_list = set()
        if is_windows:
            subdomains_queue = list()
        else:
            subdomains_queue = multiprocessing.Manager().list()
        verbose = True
        domain_check = re.compile("^(http|https)?[a-zA-Z0-9]+([\-\.]{1}[a-zA-Z0-9]+)*\.[a-zA-Z]{2,}$")
        if not domain_check.match(domain):
            if not silent:
                print(R + "Error: Please enter a valid domain" + W)
            return []
        if not domain.startswith('http://') or not domain.startswith('https://'):
            domain = 'http://' + domain
        parsed_domain = urlparse.urlparse(domain)
        if not silent:
            pass 
        chosenEnums = [Virustotal, ThreatCrowd,CrtSearch, PassiveDNS]
        enums = [enum(domain, [], q=subdomains_queue, silent=silent, verbose=verbose) for enum in chosenEnums]
        for enum in enums:
            enum.start()
        for enum in enums:
            enum.join()
        subdomains = set(subdomains_queue)
        for subdomain in subdomains:
            search_list.add(subdomain)
        if subdomains:
            subdomains = sorted(subdomains, key=subdomain_sorting_key)
        print(Y + " Total Unique Subdomains Found: %s" % len(subdomains) + W)
        store(name,subdomains)      

    except KeyboardInterrupt:
        print("\n")
        time.sleep(5)
        exit(0)





def init_vulnscan(x):
    x = formaturl(x)
    ClickJacking(x)
    init_header(x)
    
    scan_sql_injection(str(formaturl(x)+"/"))

