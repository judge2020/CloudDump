# parses out.json
import json

prices = json.loads(open('out.json').read())

#
# MARKDOWN
#
with open('out.md', 'w') as outmd:
    outmd.write('|TLD|price (USD)|')
    outmd.write("\n")
    outmd.write('|---|---|')
    for tld in prices:
        outmd.write("\n")
        outmd.write(f"|{tld[0]}|{tld[1]}|")
    outmd.write("\n")

#
# TEXT
#

with open('out.txt', 'w') as outmd:
    for tld in prices:
        outmd.write(f"{tld[0]}:{tld[1]}")
        outmd.write("\n")
