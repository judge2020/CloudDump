import json

import requests

import secrets

sld = "pleasenoban2011"

tlds = []
with open('tlds.txt') as _tlds:
    _tlds = _tlds.readlines()
    for _tld in _tlds:
        _tld = _tld.strip("\n")
        tlds.append(f"{sld}.{_tld}")

# split list in half
_len_half = len(tlds) // 2
tlds_first_set = tlds[:len(tlds) // 2]
tlds_second_set = tlds[len(tlds) // 2:]

headers = {}

with open('headers.txt') as headersfile:
    _headers = headersfile.readlines()
    for header in _headers:
        header = header.strip("\n")
        name, value = header.split(": ")
        if name.lower() in ["connection", "host", 'content-Length', "accept-encoding", "accept"]:
            continue
        headers[name] = value

print(f"Obtaining the first {_len_half} domains...")
_prices_first = requests.post(f"https://dash.cloudflare.com/api/v4/accounts/{secrets.account_id}/registrar/domains",
                              json={'id': tlds_first_set}, headers=headers)
print(f"Status: {_prices_first.status_code}")

print(f"Obtaining the last {_len_half} domains...")

_prices_second = requests.post(f"https://dash.cloudflare.com/api/v4/accounts/{secrets.account_id}/registrar/domains",
                               json={'id': tlds_second_set}, headers=headers)
print(f"Status: {_prices_second.status_code}")

# the prices object is a list of tuples so we can support things like
# "redemption fee" (https://icannwiki.org/RGP) and ICANN fee in the future.

prices = []


def parse(cf_json):
    for _price_entry in cf_json["result"]:
        __name = _price_entry["name"].split(".")[1]
        __price = _price_entry["fees"]["registration_fee"]
        prices.append((__name, __price))


parse(_prices_first.json())
parse(_prices_second.json())

prices.sort()

open("out.json", 'w').write(json.dumps(prices))

print("Written output to out.json: do not commit this file!")
