#!/usr/bin/python3

from getpass import getpass
import whois 
from prettytable import PrettyTable
import datetime


def registar_address(w):
    if w.registrar_url:
        return w.registrar_url
    elif w.whois_server:
        return w.whois_server

def date_format(x):
    if type(x) == datetime.datetime:
        r = x.strftime("%d")+"/"+x.strftime("%m")+"/"+x.strftime("%Y")
        return r
    else:
        list2=[]
        for i in x:
            r = i.strftime("%d")+"/"+i.strftime("%m")+"/"+i.strftime("%Y")
            list2.append(r)
        return list2
def org(w):
    if w.org:
        return w.org
    elif w.organization:
        return w.organization



def s_m(x,t,value):
    if (x != None):
        if type(x) == str:
            t.add_row([value,x])
        else:
            t.add_row([value+"s",'-------'])
            i = 1
            for y in x:
                t.add_row([str(i)+".",y])
                i+=1
            t.add_row(["","-------"])
            t.add_row(["",""])
    else:
        return

def whois_module(domain):

    w = whois.whois(domain)
    
    t = PrettyTable(["Options ","Information"])
    s_m(w.domain_name,t,"Domain name")
    t.add_row(["Organization",org(w)])
    s_m(w.registrar,t,"Registrar")
    t.add_row(["Registrar_url",registar_address(w)])
    s_m(w.emails,t,"Email")
    cdate=date_format(w.creation_date)
    s_m(cdate,t,"creation date")
    cdate=date_format(w.updated_date)
    s_m(cdate,t,"Updated date")
    cdate=date_format(w.expiration_date)
    s_m(cdate,t,"Expiration Date")
    s_m(w.name_servers,t,"Name Server")
    s_m(w.country,t,"Country")
    s_m(w.city,t,"City")
    s_m(w.state,t,"State")
    s_m(w.zipcode,t,"Zipcode")
    print(t)
