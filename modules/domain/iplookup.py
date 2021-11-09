import socket
from prompt_toolkit import prompt
import requests
import shodan
from prettytable import PrettyTable
from data.data import HEADERS,api_load
from treelib import Node, Tree


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
    print("Result's may be not accurate Probably of ISP's: Taken from two different sources \n")
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