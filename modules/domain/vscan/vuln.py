import requests


def ClickJacking(url):
    page=requests.get(url)
    headers=page.headers
    if not "X-Frame-Options" in headers:
            print(" Vulnerable\t: Clickjacking Injection ")
    else:
        print("' Not found\t: Clickjacking Injection  ")


def HostHeader(url):
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)  Chrome/93.0.4577.63 Safari/537.36",
        'Host': 'http://evil.com'}
        
    response = requests.get(url, headers=headers)
    if 'evil.com' in response.headers:
        print(" Vulnerable\t: Host Header Injection ")
    else:
        print(" Not found\t: Host Header Injection ")