import argparse
import json
from utils import *
from bs4 import BeautifulSoup
from time import time


def get_args():
    parser = argparse.ArgumentParser(description='Crawler for Usenix Security.')
    parser.add_argument('-u', '--url', type=str, help='url that contains the accepted papers')
    parser.add_argument('-k', '--keyword', nargs='+', help='keyword list for report filtering')
    parser.add_argument('-o', '--out_dir', type=str, help='out dir to save the results')
    parser.add_argument('-s', '--stat', action='store_true', help='flag to stat the conference')
    parser.add_argument('-S', '--save', action='store_true', help='flag to save the results')
    parser.add_argument('-R', '--resume_from', type=int, help='resume from the Nth pdf, where N >= 1.')

    args = parser.parse_args()
    return args


def get_accepted_papers(accepted_url):
    usenix_sec_base = 'https://www.usenix.org'
    accepted_papers = {}
    r = request_get(accepted_url)
    soup = BeautifulSoup(r.text, 'html.parser')
    h2s = soup.find_all('h2')
    for h2 in h2s:
        try:
            href = h2.find('a').get('href')
            title = h2.text.strip()
        except:
            continue
        accepted_papers[title] = usenix_sec_base + href
    return accepted_papers

def get_pdf_url(paper_url):
    r = request_get(paper_url)
    soup = BeautifulSoup(r.text, 'html.parser')
    spans = soup.find_all('span', {'class': 'file'})
    try:
        pdf_url = spans[0].find('a').get('href')
    except:
        pdf_url = ''
    return pdf_url


if __name__ == '__main__':
    t0 = time()
    args = get_args()
    out_dir = args.out_dir or os.path.join(os.getcwd(), os.path.dirname(__file__), '../out')
    log_dir = os.path.join(os.getcwd(), os.path.dirname(__file__), '../log')
    check_dir(out_dir)
    check_dir(log_dir)
    
    accepted_papers_url = args.url
    # accepted_papers_url = 'https://www.usenix.org/conference/usenixsecurity23/summer-accepted-papers'
    
    accepted_papers = get_accepted_papers(accepted_papers_url)
    
    i = 0
    success_fn = os.path.join(log_dir, 'security_success.json')
    success_list = ck_load_list_from_json(success_fn)
    for title in accepted_papers:
        i += 1
        if args.resume_from and i < args.resume_from:
            print('[%d] skip until the resume_from point: %d'%(i, args.resume_from))
            continue
        if title in success_list:
            continue
        try:
            pdf_url = get_pdf_url(accepted_papers[title])
            print('[%d] %s: %s'%(i, title, pdf_url))
            if args.save == True:
                download_pdf(pdf_url, title, out_dir)
        except Exception as e:
            print('[X] paper: %s fail with exception: %s. continue.'%(title, e))
            continue
        success_list.append(title)
    
    with open(success_fn, 'w') as f:
        json.dump(success_list, f)
    print('[+] write log to %s'%success_fn)
            
    print('Done. %d/%d success! Cost %.2f seconds'%(len(success_list), len(accepted_papers), time()-t0))