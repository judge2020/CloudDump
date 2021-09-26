Looks like this doesn't work anymore. Unfortunate.

#### CloudDump

Dumps Cloudflare to get the price of all of their TLD's.


https://github.com/judge2020/Actual-Domain-Prices

##### Setup

Requirements:

* pipenv (or manually install the dependencies in [Pipfile](Pipfile))
* python ~3.7
* Cloudflare account

1. copy .env.example to .env and fill out relevant information
2. go to the CF dashboard and MITM a request
3. copy the headers (including cookie) to a file called `headers.txt`, in the format of `name: value`
4. run `scrape_tlds.py` to get all of the TLDs Cloudflare currently supports
5. run `get_prices.py`
6. run `export_prices.py`


The relevant files are `out.md` and `out.txt`.

##### INFO

This project will likely not be maintained, but PR's are welcomed.


