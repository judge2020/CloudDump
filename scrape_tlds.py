import requests
from bs4 import BeautifulSoup

tld_text = requests.get('https://www.cloudflare.com/tld-policies/').text

soup = BeautifulSoup(tld_text, features="html.parser")
table = soup.find_all("table", class_="table-light")[0]

tlds = []

for item in table.descendants:
    if item.name == "tr":
        tlds.append(item.contents[1].string)

with open('tlds.txt', 'w')as outfile:
    for tld in tlds:
        if tld is None:
            continue
        outfile.write(tld)
        outfile.write("\n")
