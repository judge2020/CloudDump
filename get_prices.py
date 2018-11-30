import requests

import secrets

sld = "pleasenoban2011"

tlds = []
with open('tlds.txt') as _tlds:
    _tlds = _tlds.readlines()
    for tld in _tlds:
        tld = tld.strip("\n")
        tlds.append(f"{sld}.{tld}")

headers = {}

with open('headers.txt') as headersfile:
    _headers = headersfile.readlines()
    for header in _headers:
        header = header.strip("\n")
        name, value = header.split(": ")
        if name in ["Connection", "Host", 'Content-Length', "Accept-Encoding"]:
            continue
        headers[name] = value

b = requests.post(f"https://dash.cloudflare.com/api/v4/accounts/{secrets.account_id}/registrar/domains",
                  json={'id': tlds}, headers=headers)

print(b.text)
if "icaan_fee" in b.text:
    # success
    with open('out.json', 'a') as file:
        file.write(b.text)
    print("Written output to out.json: do not commit this file!")
else:
    print("failed!")
    print(b.status_code)
