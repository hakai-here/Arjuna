import json


G = '\033[92m'  
Y = '\033[93m'  
B = '\033[36m'  
R = '\033[91m' 
W = '\033[0m'
L = "\033[90m"
w = "\033[47m"
BLG = "\033[100m"
BB = "\033[104m"
WT= "\033[37m"
Bld = "\033[1m"

HEADERS = {'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
           'Accept-Language' : 'en-US,en;q=0.5',
           'Accept-Encoding' : 'gzip, deflate',
           'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)  Chrome/93.0.4577.63 Safari/537.36"
          }

VISITED_LINKS = set()
DRIVE_LINKS = set()
IMG_SRC = set()
YOUTUBE_LINKS = set()
HANDLES_LINKS = set()
MAIL_TO = set()
TINY_URLS =set()
NUMBERS = set()
LINKEDIN_URLS = set()
EXTERNAL_LINKS= set()
PDF =set()

def api_load(x):
    f = open('api.json',)
    data = json.load(f)
    for i in data[x]:
        return i["api"]

def flush():
    VISITED_LINKS.clear()
    DRIVE_LINKS.clear()
    IMG_SRC.clear()
    YOUTUBE_LINKS.clear()
    HANDLES_LINKS.clear()
    MAIL_TO.clear()
    TINY_URLS.clear()
    NUMBERS.clear()
    EXTERNAL_LINKS.clear()
    LINKEDIN_URLS.clear()
    PDF.clear()

def printlinkedin():
    for i in LINKEDIN_URLS:
        print(i)

    flush()

TB =f'''
{G}

\t\tThe Following are the Headers we Use check 


\tContent-Type                      \t:\t Denotes the type of media
\tDate                              \t:\t Date and Time from the response
\tServer                  	      \t:\t Information about the Server Software
\tSet-Cookie              	      \t:\t Assigns cookies from Server to Client
\tConnection              	      \t:\t Controls network connection
\tContent-Encoding           	      \t:\t Specifies compression type   
\tVary                    	      \t:\t Details how to determine if cache can be used rather than a new response from server       
\tCache-Control           	      \t:\t Details caching options in requests and responses                                          
\tTransfer-Encoding       	      \t:\t Encoding to be used for transfer of data                                                   
\tExpires	Specifies                 \t:\t when the response becomes "stale"                                                          
\tContent-Length             	      \t:\t Size of resource in number of bytes                                                        
\tX-Powered-By            	      \t:\t Hosting and Backend Server Frameworks may use this.                                        
\tLink                    	      \t:\t Serialising one or more links in HTTP headers                                              
\tPragma                  	      \t:\t Related to caching, may be implemented in different ways.                                  
\tKeep-Alive              	      \t:\t Specifies how long a persistent connection stays open                                      
\tLast-Modified           	      \t:\t Last modification date of resource. Used for caching.                                      
\tX-Content-Type-Options  	      \t:\t Disables MIME Sniffing and forces browser to use type shown in Content-Type
\tCF-RAY                  	      \t:\t A hashed value encoding information about the data center and the request. 
\tETag                    	      \t:\t Cache Validation Tag. Also used for tracking users with cookies disabled. 
\tX-Frame-Options         	      \t:\t Specifies whether browser should show page in an iFrame  
\tCF-Cache-Status	                  \t:\t CloudFlare header shows whether a resource is cached 
\tAccept-Ranges	                  \t:\t Advertise its support of partial requests   
\tStrict-Transport-Security	      \t:\t Force communication to use HTTS (not HTTP)
\tX-XSS-Protection	              \t:\t Enables Cross Site Scripting (XSS) filtering  
\tExpect-CT               	      \t:\t Reporting and enforcement of Certificate Transparency.
\tX-Cache                 	      \t:\t Used by CDN's to specify whether resource in CDN cache matches server resource 
\tset-cookie              	      \t:\t Assigns cookies from Server to Client
\tAge	                              \t:\t Time in seconds resource has been in proxy cache                                           
\tUpgrade                 	      \t:\t One way to switch from HTTP to HTTPS                  
\tContent-Language        	      \t:\t Describes the language(s) intended for the document
\tP3P                     	      \t:\t Privacy Protocol that was not widely adopted 
\tContent-Security-Policy CSP       \t:\t Controls which resources the client can load for the page                                  
\tVia	                              \t:\t Added by proxies. Can be used for both forward and reverse proxies (requests & responses)
\tAlt-Svc                 	      \t:\t List other ways to access service
\tX-AspNet-Version        	      \t:\t Specifies the version of ASP.NET being used 
\tAccess-Control-Allow-Origin	      \t:\t Details whether the response can be shared.
\tX-UA-Compatible	                  \t:\t Compatiability header for old versions of Microsoft Internet Explorer (IE) and Edge 
\tReferrer-Policy             	  \t:\t Rules which referrer information sent in the referrer header is incorporated with requests 
\tReport-To                   	  \t:\t Header used for adding troubleshooting information??
\tNEL                            	  \t:\t An option for developers to set network error reporting.
\tX-Download-Options          	  \t:\t Specific to IE8. Stops downloads opening directly in browser. 
\tX-Permitted-Cross-Domain-Policies \t:\t Allows PDF and Flash to conduct cross-domain request
\tX-Proxy-Cache               	  \t:\t Enable caching in NGINX reverse proxy                                                      
\tEtag	                          \t:\t Used for HTTP Cache validation and conditional requests using If-Match and If-None-Match   
\tX-Request-Id                   	  \t:\t Unique request ID that associates HTTP requests between a client and a server.             
\tX-Cacheable                 	  \t:\t Non-standard header related to caching, use can vary between different proxy & cdn networks
\tX-Sorting-Hat-PodId	              \t:\t Shopify Related                                                                            
\tX-Shopify-Stage             	  \t:\t Shopify Related                                                                            
\tX-ShopId	                      \t:\t Shopify Related                                                                            
\tX-Sorting-Hat-ShopId        	  \t:\t Shopify Related                                                                            
\tX-ShardId	                      \t:\t Shopify Related                                                                            
\tX-Alternate-Cache-Key	          \t:\t Shopify Related                                                                            
\tX-Cache-Hits                	  \t:\t Data successfully located in cache memory                                                  
\tX-Varnish	                      \t:\t ID of the current request and the ID of the request that populated the Varnish cache       
\tX-Pass-Why	                      \t:\t provides reason for a 'MISS' result in the x-cache                                         
\tX-Generator                 	  \t:\t exposes information/meta data about the site such as version of software                   
\tX-Cache-Group	                  \t:\t Tags the clients about the cache-group to which they belong                                
\tX-Powered-By-Plesk          	  \t:\t Plesk Hosting Software                                                                     
\tX-AspNetMvc-Version	              \t:\t Shows the version of the framework                                                           
\tX-Powered-CMS	                  \t:\t Exposes name and version of CMS                                                            
\tX-Served-By	                      \t:\t Caching related                                                                            
\texpires	                          \t:\t Contains the date/time after which the response object is considered stale                 
\tX-Amz-Cf-Pop	                  \t:\t Amazon CloudFront                                                                          
\tX-Amz-Cf-Id                 	  \t:\t Amazon CloudFront ID (CloudFront requires this information for debugging.)                 
\tX-Drupal-Cache              	  \t:\t Indicates if request was served from Drupal Cache (Hit or Miss)                            
\tX-Xss-Protection	              \t:\t Internet explorer header compatibility filter for blocking XSS                             
\tServer-Timing	                  \t:\t Conveys information for the request-response cycle                                         
\tcontent-encoding            	  \t:\t Header specifying compression (gzip / compress / deflates etc)                             
\tX-Timer                     	  \t:\t A "Fastly" header end to end request timing information                                     
\tX-Runtime	                      \t:\t reveals time application takes to serve a request                                          
\tX-ac	                          \t:\t WordPress.com related                                                                      
\tHost-Header                    	  \t:\t Maybe same as "Host" header?                                                              
\tAccess-Control-Allow-Headers	  \t:\t To indicate which HTTP headers can be used during the actual request                                               
\tX-hacker	                      \t:\t Recruitment 'ad' by automattic.com                                                         
\tAccess-Control-Allow-Methods	  \t:\t specifies the methods when accessing the resource in response to a preflight request.      
\tX-LiteSpeed-Cache	              \t:\t Specify the usage of LSCaches (build in feature of LiteSpeed server products)              
\tX-Turbo-Charged-By	              \t:\t Added when clouflare is used                                                               
\tstrict-transport-security	      \t:\t HSTS informs browser to use HTTPS not HTTP                                                 
\tetag	                          \t:\t Identifies object (and version) for caching purposes                                       
\tX-Robots-Tag	                  \t:\t Allows you to choose content search engines can crawl on the site                          
\tX-Wix-Request-Id            	  \t:\t Wix hosting request ID                                                                     
\tX-Mod-Pagespeed	Module            \t:\t for apache (and nginx) to increase performance                                             
\tX-Cache-Status                    \t:\t Status of caches                                                                           
\tStatus	                          \t:\t Non-standard HTTP response status (Status 200 OK)                                         
\tX-Server-Cache              	  \t:\t Non-standard caching related                                                               
\tx-ray	                          \t:\t CloudFlare Releated                                                                        
\tCache-control	                  \t:\t Specifies requests and responses caching mechanisms                                        
\tX-Cache-Enabled             	  \t:\t Cache Enabled (True / False)                                                               
\tAccess-Control-Allow-Credentials  \t:\t Header tells browser whether to expose the response to frontend JavaScript                 
\tX-Server-Powered-By	              \t:\t Exposes server side software                                                               
\tX-Adblock-Key	                  \t:\t Sites use this to bypass ad blocker plugins                                                
\tX-Host	                          \t:\t Non-standard host header                                                                   
\tX-Nginx-Cache-Status	          \t:\t Nginx Caching Header  
{W}
'''