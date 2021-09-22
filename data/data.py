from requests.sessions import SessionRedirectMixin


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
EXTERNAL_LINKS= set()
