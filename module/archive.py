from urllib.parse import urlparse
import requests
import json

from module.crawl import printv, record, sorter


HEADERS = {'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
           'Accept-Language' : 'en-US,en;q=0.5',
           'Accept-Encoding' : 'gzip, deflate',
           'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)  Chrome/93.0.4577.63 Safari/537.36"
          }

arurls = {
1:"https://web.archive.org/cdx/search/cdx?url=*.{name}/*&output=json&collapse=urlkey",
2:"https://www.virustotal.com/vtapi/v2/domain/report?apikey={name}",
3:"http://web.archive.org/cdx/search/cdx?url={name}&output=json",
4:"http://index.commoncrawl.org/CC-MAIN-2018-22-index?url={wildcard}{name}/*&output=json"
}

listed =set()

def archive_call(domain):
    for i in [1,3]:
        dom = urlparse(domain)
        url = arurls[i].format(name=domain)
        response = requests.get(url,headers=HEADERS,timeout=100)
        jsondata = json.loads(response.text)
        for i in jsondata:
            if i == jsondata[0]:
                pass 
            else :
                listed.add(i[2])
        
        sorter(listed,domm=dom.netloc)
    printv()
    record(domain,domain+"_archive")
    