from data.data import HEADERS
import requests
from prettytable import PrettyTable
from urllib.parse import urlparse
from socket import gethostbyname

from extra.for_inp import formaturl


G = '\033[92m'  
Y = '\033[93m' 
B = '\033[94m' 
R = '\033[91m'  
W = '\033[0m'  




def indicator(x):
    list1=[]
    list2=[]
    x = formaturl(x)
    k = urlparse(x).netloc
    searchlist=["Date","Server","Content-Type","Cache-Control","X-TEC-API-VERSION","X-TEC-API-ROOT","X-TEC-API-ORIGIN","Transfer-Encoding","Pragma"]
    headerlist=[
"Content-Type",  
"Date",           	              
"Server",          	                
"Set-Cookie",      	               
"Connection",      	                
"Content-Encoding",	                
"Vary",	                           
"Cache-Control",  	               
"Transfer-Encoding",  	               
"Expires",         	                
"Content-Length",	                   
"X-Powered-By",	                   
"Link",	                            
"Pragma",	                           
"Keep-Alive",      	               
"Last-Modified",  	                
"X-Content-Type-Options",	            
"CF-RAY",	                            
"ETag",	                            
"X-Frame-Options",     	            
"CF-Cache-Status",     	            
"Accept-Ranges",	                    
"Strict-Transport-Security",	        
"X-XSS-Protection",	               
"Expect-CT",	                        
"X-Cache",                            
"set-cookie",             	        
"Age",                                
"Upgrade",                 	        
"Content-Language",	                
"P3P",	                               
"Content-Security-Policy CSP",	        
"Via",                                
"Alt-Svc",	                            
"X-AspNet-Version",       	        
"Access-Control-Allow-Origin",      
"X-UA-Compatible",       	       
"Referrer-Policy",        	        
"Report-To",	                        
"NEL",                     	        
"X-Download-Options",     	        
"X-Permitted-Cross-Domain-Policies",	 
"X-Proxy-Cache",                   	
"Etag",	                           
"X-Cacheable",                     	
"X-Dc",	 
"X-Sorting-Hat-PodId",	                
"X-Shopify-Stage",	                    
"X-ShopId",	                        
"X-Sorting-Hat-ShopId",	            
"X-ShardId",	                        
"X-Alternate-Cache-Key",	            
"X-Cache-Hits",	                    
"X-Varnish",	                       
"X-Pass-Why",                     	
"X-Generator",	                        
"X-Cache-Group",	                    
"X-Powered-By-Plesk",                 	
"X-AspNetMvc-Version",            	
"X-Powered-CMS",	                   
"X-Served-By",                     	
"expires",                        	
"X-Amz-Cf-Pop",	                   
"X-Amz-Cf-Id",                      
"X-Drupal-Cache",                  	
"X-Xss-Protection",                	
"Server-Timing",	                   
"content-encoding",               	
"X-Timer",                         	
"X-Runtime",	                        
"X-ac",	                            
"Host-Header",                       
"Access-Control-Allow-Headers",	  
"X-hacker",                        	
"Access-Control-Allow-Methods",	 
"X-LiteSpeed-Cache",	 
"X-Turbo-Charged-By",              	
"strict-transport-security",	        
"etag",	                            
"X-Robots-Tag",                    	
"X-Seen-By",	 
"X-Wix-Request-Id",	                
"x-contextid", 
"X-Mod-Pagespeed",                   
"X-Cache-Status",	 
"Status",                          	
"X-Server-Cache",	                   
"x-ray",	                            
"Cache-control",                   	
"X-Cache-Enabled",	                    
"Access-Control-Allow-Credentials",	
"X-Server-Powered-By",                
"X-Adblock-Key",	                   
"X-Host",                          	
"X-Nginx-Cache-Status"            	
]
    try:response=requests.get(x,params=None, headers=HEADERS, cookies=None, auth=None, timeout=None).headers
    except : print("{R} Unable To connect  {W}") ; return
    ip = gethostbyname(k)
    t = PrettyTable(["Raw Headers"," informations"])
    t.add_row([B+"IP",ip+W])
    for i in searchlist:
        if i in response:
            t.add_row([B+i,response[i]+W])
    print(t)
    for i in headerlist:
        if i in response:
            list1.append(i)

        else:
            list2.append(i)
    
    t = PrettyTable(['Headers', 'status'])
    for i in list1:
        k = G+i+W
        t.add_row([k,G+'✔'+W])
    

    print(t)

