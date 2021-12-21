from os import name
from prettytable import PrettyTable

title='''
▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰
            {}
▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰
'''

nameList = {
    "a":"Address",
    "mx":"Mail Servers",
    "ns":"Name Servers",
    "txt":"Text Record",
    "soa":"Start of authority",
    "mname":'Primary Name Server',
    "rname":'Admin email address',
    "cname":"Canonical Name",
    "aaaa":'128–bit/IPv6 addresses',
    "port":"Open Ports",
    "protocol":"Protocols Used",
    "technology":"Technology",
    "hosttype":"Host Type"

}





def checktype(y,x,t):
    j=1
    if isinstance(x,list):
        t.add_row([nameList[y.lower()]," "])
        for i in x:
            t.add_row([f'*{j}',i])
            j+=1
    else:
        t.add_row([nameList[y.lower()],x])
    t.add_row(["",""])



def extractkey(x):
    key_val = set()
    for key,value in x.items():
        key_val.add(key)
    return key_val

def dotask(ww,value,i):
    t = PrettyTable(["Server Points","Information"])
    try:m = i['summary']['properties'] 
    except KeyError:pass
    try:n = i['summary']
    except KeyError:pass
    results("Name",i['indicator'],t)
    results("Risk",i['risk'],t)
    try:ww.add_row([i['indicator'],nameList['mx'],i['risk'],i['type']])
    except KeyError:pass
    t.add_row(["",""])
    try:results("ID",i['iid'],t)
    except KeyError:
        pass
    results("Domain ID",n['domainiid'],t)
    results("Domain",n['domain'],t)
    try:results("Status code",m['http']['++code'],t)
    except KeyError:
        pass
    try:results("Content type",m['http']['++content-type'],t)
    except KeyError:
        pass
    results("Type",i['type'],t)
    try:results("City",m['geo']['city'],t)
    except KeyError:
        pass
    results("Region",m['geo']['region'],t)
    results("Country",m['geo']['country'],t)
    results("Country Code",m['geo']['countrycode'],t)
    print(t)
    print("")

def results(name,val,t):
    try:
        t.add_row([name,val])
    except KeyError:
        pass

def formatresult(result):
        try:
        
            res = result['data']
            name = res['indicator']
            ww=PrettyTable(["Server indicator","Type of Server","Risk found","Related to"]) 
            ww.add_row([res['indicator'],"Target Domain",res['risk'],res['type']])
            ww.add_row(["","","",""])
            print(title.format("Mail Server Analysis"))  
            l = res['links']['Mail Servers']
            for i in l:
               dotask(ww,'mx',i)
            ww.add_row(["","","",""])
            l = res['links']['Name Servers']
            print(title.format("Name Server Analysis"))
            for i in l:
               dotask(ww,'ns',i)
               print("")
            l = res['properties']['dns']
            k = extractkey(l)
            print(title.format('Dns Records Analysis'))
            t = PrettyTable(["Dns Records ","Information"])
            for i in k:
                checktype(i,l[i],t)
            print(t) 
            print(title.format("Attributes Analysis"))
            t = PrettyTable(['Attributes',"Analysis Info"])
            k = extractkey(res['attributes'])
            l=res['attributes']
            for i in k:
                checktype(i,l[i],t)
            print(t)
            print(title.format("Primary Risk Analysis"))
            m = res['riskfactors']
            t1=PrettyTable(["risk",'Reason'])
            for i in m:
                t1.add_row([i['risk'],i['description']])
            print(t1)

            print(title.format("Summary of the scan"))
            print(ww)


        
        except IndexError:
            print("[+++++ Error occured during scan+++++++]")

def formatresult2():
    content=[]
    