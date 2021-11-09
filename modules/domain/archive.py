from urllib.parse import urlparse
import requests
import json

from data.data import HEADERS, flush
from modules.domain.crawler import printv, record, sorter

arurls = {
1:"https://web.archive.org/cdx/search/cdx?url=*.{name}/*&output=json&collapse=urlkey",
2:"http://web.archive.org/cdx/search/cdx?url={name}&output=json"
}

listed =set()

def archive_call(domain):
    print("Nemo Look through the archive files we might get something intresting .(it running take a break)")
    for i in [1,2]:
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
    flush()
    