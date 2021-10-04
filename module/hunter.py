import json
import requests
from data.data import HEADERS,api_load

urls = [
    "https://api.hunter.io/v2/domain-search?domain={domain}&api_key={api}",
    "https://api.hunter.io/v2/email-finder?domain={domain}&first_name={firstname}&last_name={lastname}&api_key={api}",
    "https://api.hunter.io/v2/email-verifier?email={email}&api_key={api}"
]



def search_domain(domain):
    req = requests.get(urls[0].format(domain=domain,api=api_load('Hunter')),headers=HEADERS).json()
    data1 = req['data']
    print(f"Domain          : {data1['domain']} ")
    if data1['disposable']:  print(f"Disposable      : {data1['disposable']} ")
    if data1['organization']:print(f"organization    : {data1['organization']} ")
    if data1['country']:     print(f"Country         : {data1['country']} ")
    if data1['state']:       print(f"State           : {data1['state']} ")

    data = req['data']['emails']
    print('\nDetials of Email colected :\n```````````````````````````')
    for i in data:
        print(f"Surety       : {i['confidence']}% ")
        print(f"Name         : {i['first_name']} {i['last_name']}")
        if i['position']:      print(f"Position     : {i['position']}")
        if i['value']:         print(f"Email        : {i['value']}")
        if i['type']:          print(f"Type         : {i['type']} account")
        if i['seniority']:     print(f"Seniority    : {i['seniority']}")
        if i['department']:    print(f"Department   : {i['department']}")
        if i['twitter']:       print(f"Twitter      : {i['twitter']}")
        if i['phone_number']:  print(f"Phone        : {i['phone_number']}")
        if i['sources']:
            for k in i["sources"]:
                            print(f"Info Source  : {k['uri']}")
                            print(f"Val Source   : Validity is {k['still_on_page']} ")
                            print(f"Last seen on : {k['last_seen_on']}")
        print("\n")