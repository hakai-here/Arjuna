#!/usr/bin/python3

import argparse
import sys
import whois 
from prettytable import PrettyTable
import datetime

def parse_arg():
    parser = argparse.ArgumentParser(epilog="\t Example \r\n python3 "+sys.argv[0]+"-d example.com" )
    parser._optionals.title="Options :"
    parser.add_argument("-d","--domain",help="to set domain ")

    return parser.parse_args()

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
