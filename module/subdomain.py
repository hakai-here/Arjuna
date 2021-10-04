#!/usr/bin/python3

import re
import sys
import os
import time
import multiprocessing
import threading
import socket
import json
import requests
import urllib.parse as urlparse
import urllib.parse as urllib
from data.data import api_load

is_windows = sys.platform.startswith('win')
G = '\033[92m' 
Y = '\033[93m'  
B = '\033[94m'  
R = '\033[91m'  
W = '\033[0m'  
M = "\033[35m" 
L = "\033[33m"
K = "\033[31m"



def parser_error(errmsg):     
    print(R + "Error: " + errmsg + W)
    sys.exit()

def store(z,y):
    x = z+".txt"
    with open(x,'wt') as f:
        for i in y:
            f.write(i+os.linesep)
    print(f'File Has Been Saved name of {x}')

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
            self.print_(R + "[!] set VT_APIKEY to your virus total API key using:   export VT_APIKEY=Your_VT_API_KEY_VALUE" + W)
            self.print_(B + "[!] To get a VT APIKEY, register at https://www.virustotal.com/gui/join-us" +W)
        return self.subdomains

    def extract_domains(self, resp):
        try:
            for i in resp['data']:
                if i['type'] == 'domain':
                    subdomain = i['id']
                    if not subdomain.endswith(self.domain):
                        continue
                    if subdomain not in self.subdomains and subdomain != self.domain:
                        if self.verbose:
                            self.print_("%s%s%s" % (R, subdomain, W))
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
                    if self.verbose:
                        self.print_("%s%s%s" % (R, subdomain, W))
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
                        if self.verbose:
                            self.print_("%s%s%s" % (Y, subdomain, W))
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
                    if self.verbose:
                        self.print_("%s%s%s" % (B, subdomain, W))
                    self.subdomains.append(subdomain.strip())
        except Exception as e:
            pass

def main(domain, threads=7000 ,silent=None):
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
            pass #print(G + " Enumerating subdomains now for %s" % parsed_domain.netloc + W)
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


