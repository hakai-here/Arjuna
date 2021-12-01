from prettytable import PrettyTable
import requests
from data.data import HEADERS
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
        t= PrettyTable(["Name","Id","Categories","Version"])
        for i in k:
            t.add_row([ i['name'],i['id'],catolog(i['categories']), ver(i) ])

        print(t)
    else:
        print("Error Occured")