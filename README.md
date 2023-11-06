# conference-crawler
A carwler for cyber security conferences including the big 4 (SP, Usenix Security, NDSS, CCS) and some software conferences.


## Usage

### For Usenix Security
- Get the page link of technical sessions, like: https://www.usenix.org/conference/usenixsecurity23/technical-sessions
- Execute the `usenix_sec.py` in `src`:

```bash
cd src
pip install -r requirements.txt

python usenix_sec.py -u https://www.usenix.org/conference/usenixsecurity23/technical-sessions -o ../out/security23 -S

# python usenix_sec.py -h
usage: usenix_sec.py [-h] [-u URL] [-U SEASON_URL] [-k KEYWORD [KEYWORD ...]] [-o OUT_DIR] [-s] [-S] [-R RESUME_FROM]

Crawler for Usenix Security.

optional arguments:
  -h, --help            show this help message and exit
  -u URL, --url URL     technical session url that contains all accepted papers, recommended
  -U SEASON_URL, --season_url SEASON_URL
                        season url that contains the season accepted papers
  -k KEYWORD [KEYWORD ...], --keyword KEYWORD [KEYWORD ...]
                        keyword list for report filtering
  -o OUT_DIR, --out_dir OUT_DIR
                        out dir to save the results
  -s, --stat            flag to stat the conference
  -S, --save            flag to save the results
  -R RESUME_FROM, --resume_from RESUME_FROM
                        resume from the Nth pdf, where N >= 1.
```


### For Security and Privacy
- Get the page link of accepted papers, like: https://sp2023.ieee-security.org/program-papers.html
- Execute the `sp.py` in `src`:

```bash
cd src
# requirements are already satisfied
python sp.py -u https://sp2023.ieee-security.org/program-papers.html 0o ../out/sp23 -S
```


## TODOs

- [ ] Implementation for CCS and NDSS
- [ ] Implementation of arguments `-k` for keyword and `-s` for stat (stat the authors and authroities)
- [ ] Add more conference support
- [ ] Add more detailed log