import requests
import json
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


def ck_load_list_from_json(fn):
    if os.path.isfile(fn) == False:
        return []
    with open(fn, 'r') as f:
        d = json.load(f)
    return d


def request_get(url):
    random_header = {'User-Agent': UA.random}
    return requests.get(url=url, headers=random_header, proxies=PROXIES)


def download_pdf(pdf_url, title, out_dir):
    check_dir(out_dir)
    illegal_to_blank = [':', '/', '\\', '?', '<', '>', '|', '"']
    for ic in illegal_to_blank:
        save_title = title.replace(ic, '')
    save_fn = os.path.join(out_dir, save_title + '.pdf')
    
    # get bytes content of the pdf
    r = request_get(pdf_url)
    pdf_bytes = r.content
    with open(save_fn, 'wb') as f:
        f.write(pdf_bytes)
    print('[+] save pdf to %s'%save_fn)