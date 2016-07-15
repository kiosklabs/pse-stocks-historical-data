import os.path
import sys
import re
import csv

stocks = []
for i in range(1,6):
    fname = 'stocklist%s' % i
    with open(fname, 'r') as f:
        lines = f.read()
        regex = ur"<td><a href=\"#company\" onclick=\"cmDetail\(\'(\d+)\',\'(\d+)\'\);return false;\">(.*)\<\/a><\/td>"
        m = re.findall(regex, lines)
        for match in m:
            stocks.append(match)

print(stocks)

with open('finalstocks.csv','w') as out:
    csv_out=csv.writer(out)
    csv_out.writerow(['companyId','securityId', 'companyName'])
    for row in stocks:
        csv_out.writerow(row)