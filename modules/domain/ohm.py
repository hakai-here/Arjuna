import requests
import argparse
from functools import partial
from multiprocessing import Pool
from bs4 import BeautifulSoup as bsoup




def google_search(query, page):
    base_url = 'https://www.google.com/search'
    headers  = { 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:71.0) Gecko/20100101 Firefox/71.0' }
    params   = { 'q': query, 'start': page * 10 }
    resp = requests.get(base_url, params=params, headers=headers)
    soup = bsoup(resp.text, 'html.parser')
    links  = soup.findAll('cite')
    result = []
    for link in links:
        result.append(link.text)
    return result


def search_result(q, engine, pages, processes, result):
    print('-' * 70)
    print(f'Searching for: {q} in {pages} page(s) of {engine} with {processes} processes')
    print('-' * 70)
    print()
    counter = 0
    for range in result:
        for r in range:
            print('[+] ' + r)
            counter += 1
    print()
    print('-' * 70)
    print(f'Number of urls: {counter}')
    print('-' * 70)


def main(options):
    
    if not options:
        query = input('[?] Enter the Search Query: ')
    else:
        query = options

    engine = "google"
    if engine.lower() == 'google':
        target = partial(google_search, query)

    pages= 7
    processes= 2

    with Pool(int(processes)) as p:
        result = p.map(target, range(int(pages)))

    search_result(query, engine, pages, processes, result)
