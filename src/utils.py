import requests
import os
from fake_useragent import UserAgent

UA = UserAgent()
# You need to set http_proxy and https_proxy in environment with export
PROXIES = {'http': 'http://localhost:7890', 'https': 'http://localhost:7890'}


def check_dir(d):
    if os.path.isdir(d):
        return True
    else:
        try:
            os.makedirs(d)
            return True
        except:
            return False


def request_get(url):
    random_header = {'User-Agent': UA.random}
    return requests.get(url=url, headers=random_header, proxies=PROXIES)