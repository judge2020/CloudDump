#### CloudDump

Dumps Cloudflare to get the price of all of their TLD's.


https://github.com/judge2020/Actual-Domain-Prices

##### Setup

Requirements:

* pipenv
* python ~3.7
* Cloudflare account with registrar enabled

1. run `python scrape_tlds.py` to get all of the TLDs Cloudflare currently supports
2. copy .env.example to .env and fill out relevant information
3. go to the CF dashboard and MITM a request
4. copy the headers (including cookie) to a file called `headers.txt`, in the format of `name: value`
5. run `python get_prices.py`

NOTE: You should split up the `tls.txt` list before running get_prices. Cloudflare sometimes dies with a gateway timeout if you query too many TLDs, so run it twice with different TLDs each time.

##### INFO

This project will likely not be maintained, but PR's are welcomed.


