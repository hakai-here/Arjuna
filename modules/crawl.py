#!/usr/bin/python3

from data.data import DRIVE_LINKS, EXTERNAL_LINKS, HANDLES_LINKS, HEADERS, IMG_SRC, MAIL_TO, NUMBERS, TINY_URLS, VISITED_LINKS, YOUTUBE_LINKS
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


def sorter(sort_list):

    for i in sort_list:
        if(domain.netloc in i and 'mailto' not in i and 'facebook' not in i and 'twitter' not in i  and 'instagram' not in i ):
            if('.png' in i or '.jpg' in i or '.jpeg' in i ):
                IMG_SRC.add(i)
            else:    
                VISITED_LINKS.add(i)
        
    for i in sort_list:
        if('mailto' in i):
            print(i)
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
        if (domain.netloc not in i and 'mailto:' not in i and 'tel' not in i and  'drive.google.com' not in i and 'youtube.com' not in i and 'tinyurl' not in i and 'twitter' not in i and 'facebook' not in i and 'instagram' not in i and '#' not in i):
            EXTERNAL_LINKS.add(i)
 

def printv():
    if VISITED_LINKS:
        print("\n\n[*]Links :\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        for i in VISITED_LINKS:
            print(i)
    
    if DRIVE_LINKS:
        print("\n[*]Drive links :\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        for i in DRIVE_LINKS:
            print(i)

    if IMG_SRC:
        print("\n[*]Image Links :\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        for i in IMG_SRC:
            print(i)

    if YOUTUBE_LINKS:
        print("\n[*]Youtube :\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        for i in YOUTUBE_LINKS:
            print(i)

    if HANDLES_LINKS:
        print("\n[*]Handles and Social Media Connections :\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        for i in HANDLES_LINKS:
            print(i)

    if EXTERNAL_LINKS:
        print("\n[*] External Links :\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        for i in EXTERNAL_LINKS:
            print(i)
    
    if MAIL_TO:
        print('\n[*] Mail address :\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        for i in MAIL_TO:
            print(i)
    
    if NUMBERS:
        print('\n[*] Phone Numbers :\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        for i in NUMBERS:
            print(i)

    
    if TINY_URLS:
        print('\n[*] Mail address :\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        for i in TINY_URLS:
            print(i)



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
        reqs = requests.get(x,headers=HEADERS,timeout=250).content
        soup = BeautifulSoup(reqs, 'html.parser')
        
        for link in soup.find_all('a'):
            print(f"{link.get('href')}")
            links.add(link.get('href'))
        sorter(links)

    except:
        pass
   
  

    


def init_crawl(x):
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

