import argparse
from utils import *
from bs4 import BeautifulSoup
from time import time


def get_args():
    parser = argparse.ArgumentParser(description='Crawler for Usenix Security.')
    parser.add_argument('crash_dir', help='path to the directory containing crash reports')
    parser.add_argument('-u', '--url', type=str, help='url that contains the accepted papers')
    parser.add_argument('-k', '--keyword', nargs='+', help='keyword list for report filtering')
    parser.add_argument('-o', '--out_dir', type=str, help='out dir to save the results')
    parser.add_argument('-s', '--stat', action='store_true', help='flag to stat the conference')
    parser.add_argument('-S', '--save', action='store_true', help='flag to save the results')

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


def download_pdf(pdf_url, title, out_dir):
    pass


if __name__ == '__main__':
    t0 = time()
    args = get_args()
    out_dir = args.out_dir or os.path.dirname(__file__)

    usenix_sec_accepted_url = 'https://www.usenix.org/conference/usenixsecurity23/summer-accepted-papers'
    accepted_papers = get_accepted_papers(usenix_sec_accepted_url)
    i = 0
    for title in accepted_papers:
        i += 1
        print('[%d] %s: %s'%(i, title, accepted_papers[title]))
    print('Done! Cost %.2f seconds'%(time()-t0))