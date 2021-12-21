from data.data import DRIVE_LINKS, EXTERNAL_LINKS, HANDLES_LINKS, HEADERS, IMG_SRC, MAIL_TO, NUMBERS, PDF, TINY_URLS, VISITED_LINKS, YOUTUBE_LINKS, flush
import requests
import threading
from urllib.parse import urlparse
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from time import sleep

counter = 0
counter2 = 0
domain =""

def valid(url):
    parsed = urlparse(url)
    if not parsed.netloc:
        url = domain+url
    return url


def sorter(sort_list,domm):

    for i in sort_list:
        if(domm in i and 'mailto' not in i and 'facebook' not in i and 'twitter' not in i  and 'instagram' not in i ):
            if('.png' in i or '.jpg' in i or '.jpeg' in i ):
                IMG_SRC.add(i)
            elif('.pdf' in i):
                PDF.add(i)
            else:    
                VISITED_LINKS.add(i)
    for i in sort_list:
        if('mailto' in i):
            MAIL_TO.add(i.strip('mailto:'))
    for i in sort_list:
        if('tel:' in i ):
            NUMBERS.add(i.strip('tel:'))
    for i in sort_list:
        if ('drive.google.com' in i):
            DRIVE_LINKS.add(i)
    for i in sort_list:
        if('twitter.com' in i or 'facebook.com' in i or 'instagram.com' in i ):
            HANDLES_LINKS.add(i)
    for i in sort_list:
        if ('tinyurl' in i):
            TINY_URLS.add(i)
    for i in sort_list:
        if ('youtube.com' in i):
            YOUTUBE_LINKS.add(i)
    for i in sort_list:
        if (domm not in i and 'mailto:' not in i and 'tel' not in i and  'drive.google.com' not in i and 'youtube.com' not in i and 'tinyurl' not in i and 'twitter' not in i and 'facebook' not in i and 'instagram' not in i and '#' not in i):
            EXTERNAL_LINKS.add(i)
 
def printv():
    if VISITED_LINKS:print("[*]Number Of Visitedlinks      : ",len(VISITED_LINKS)) 
    if DRIVE_LINKS:print("[*]Number Of Drivelinks        : ",len(DRIVE_LINKS))
    if IMG_SRC:print("[*]Number Of Imagelinks        : ",len(IMG_SRC))
    if YOUTUBE_LINKS:print("[*]Number Of Youtubelinks      : ",len(YOUTUBE_LINKS))
    if HANDLES_LINKS:print("[*]Number Of Social Handles    : ",len(HANDLES_LINKS))
    if EXTERNAL_LINKS:print("[*]Number Of Externallinks     : ",len(EXTERNAL_LINKS))
    if MAIL_TO:print("[*]Number Of collected mails   : ",len(MAIL_TO))
    if NUMBERS:print("[*]Number Of Phone numbers got : ",len(NUMBERS))
    if TINY_URLS:print("[*]Number Of Tinyurl's         : ",len(TINY_URLS))
    if PDF:print("[*]Number Of PDF links         : ",len(PDF))
       


def crawl(x):
    links = set()
    global counter2
    if x == None:
        k = list(VISITED_LINKS)
        if (counter2 < counter):
            x = k[counter2]
            counter2+=1    
    soup = BeautifulSoup("")
    try:         
        reqs = requests.get(x,headers=HEADERS,timeout=30).content
        soup = BeautifulSoup(reqs, 'html.parser')
        for link in soup.find_all('a'):
            links.add(link.get('href'))
        sorter(links,domain.netloc)
    except:
        pass

def record(x,y): #please optimise using for loop and format
    print(f"\n Your Run Has Been recored in as  {y}.txt ")
    with open(y+".txt",'wt') as f:
        if VISITED_LINKS:
            f.write("\n\n[*]Links :\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
            for i in VISITED_LINKS:
                f.write(i+"\n")
        if DRIVE_LINKS:
            f.write("\n[*]Drive links :\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
            for i in DRIVE_LINKS:
                f.write(i+"\n")
        if IMG_SRC:
            f.write("\n[*]Image Links :\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
            for i in IMG_SRC:
                f.write(i+"\n")
        if YOUTUBE_LINKS:
            f.write("\n[*]Youtube :\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
            for i in YOUTUBE_LINKS:
                f.write(i+"\n")
        if HANDLES_LINKS:
            f.write("\n[*]Handles and Social Media Connections :\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
            for i in HANDLES_LINKS:
                f.write(i+"\n")
        if EXTERNAL_LINKS:
            f.write("\n[*] External Links :\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
            for i in EXTERNAL_LINKS:
                f.write(i+"\n")
        if MAIL_TO:
            f.write('\n[*] Mail address :\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
            for i in MAIL_TO:
                f.write(i+"\n")
        if NUMBERS:
            f.write('\n[*] Phone Numbers :\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
            for i in NUMBERS:
                f.write(i+"\n")
        if TINY_URLS:
            f.write('\n[*] Tiny url :\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
            for i in TINY_URLS:
                f.write(i+"\n")
        if PDF:
            f.write('\n[*] Pdf :\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
            for i in PDF:
                f.write(i+"\n")

    


def init_crawl(x):
    print("'t1t5 ,Release the crawlers' .it running take a Long break")
    global counter,domain
    domain = urlparse(x)
    crawl(x)

    thread_value = list(VISITED_LINKS)
    counter = len(thread_value)
    thread = []

    for i in thread_value:
        t = threading.Thread(target=crawl , args=[None])
        t.daemon = True
        thread.append(t)

    for i in range(counter):
        thread[i].start()

    for i in range(counter):
        thread[i].join()
    printv()
    record(domain.netloc,domain.netloc+"_crawl")
    flush()