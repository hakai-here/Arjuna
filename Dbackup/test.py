from data.data import HEADERS
import requests
from bs4 import BeautifulSoup


def linkedin(domain):
	urly = f'http://google.com/search?num=100&start=0&hl=en&meta=&q=site%3Alinkedin.com/in%20'+str(domain)
	req = requests.get(urly,headers=HEADERS,timeout=200).content
	soup = BeautifulSoup(req, 'html.parser')
	for link in soup.find_all('a'):
		if 'linkedin.com' in str(link.get('href')) and 'https://' in str(link.get('href')):
			print(link.get('href'))


linkedin('vitbhopal.ac.in')