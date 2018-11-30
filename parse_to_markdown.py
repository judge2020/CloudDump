# parses out.json
import json

tlds = []

for line in open('out.json').readlines():
    if len(line) <= 1:
        continue
    outjson = json.loads(line)["result"]
    for result in outjson:
        tld = result["name"].split(".")[1]
        registration = result["fees"]["registration_fee"]
        # redemption = result["fees"]["redemption_fee"]
        tlds.append((tld, registration))

tlds.sort()
#
# MARKDOWN
#
with open('out.md', 'w') as outmd:
    outmd.write('|TLD|price (USD)|')
    outmd.write("\n")
    outmd.write('|---|---|')
    for tld in tlds:
        outmd.write("\n")
        outmd.write(f"|{tld[0]}|{tld[1]}|")

#
# TEXT
#

with open('out.txt', 'w') as outmd:
    for tld in tlds:
        outmd.write(f"{tld[0]}:{tld[1]}")
        outmd.write("\n")
