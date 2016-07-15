import os.path
import sys
import csv
import requests
import time
import json
from datetime import datetime

requestpath = 'http://edge.pse.com.ph/common/DisclosureCht.ax'

headers = {
    'Origin': 'http://edge.pse.com.ph'  , 
    'Accept-Encoding': 'gzip, deflate'  , 
    'Accept-Language': 'en-US,en;q=0.8'  , 
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'  , 
    'Content-Type': 'application/json'  , 
    'Accept': 'application/json, text/javascript, */*; q=0.01'  , 
    'Referer': 'http://edge.pse.com.ph/companyPage/stockData.do?cmpy_id=29&security_id=146'  , 
    'X-Requested-With': 'XMLHttpRequest'  , 
    'Connection': 'keep-alive'
    }

payload = {
    "cmpy_id":"164",
    "security_id":"249",
    "startDate":"07-15-2015",
    "endDate":"07-15-2016"
    }

with open('finalstocks.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    count = 0;
    for row in reader:
        if count < 234 and count > 240:
            count += 1
            continue
        companyFile = open('historicaldata/'+row['companyName']+'.csv', 'w')
        print(row['companyId'], row['securityId'], row['companyName'])
        
        payload['cmpy_id'] = row['companyId']
        payload['security_id'] = row['securityId']

        r = requests.post(requestpath, json=payload, headers=headers)
        hist_data = json.loads(r.content)
        hist_values = hist_data['chartData']

        companyHistFile = csv.writer(companyFile)
        companyHistFile.writerow(['Date', 'Value', 'Open', 'Close', 'High', 'Low']) 

        for item in hist_values: 
            print item

            date_object = datetime.strptime(item['CHART_DATE'],'%b %d, %Y 00:00:00')
            shortdate = date_object.strftime("%d/%m/%y")
            companyHistFile.writerow([shortdate, item['VALUE'], item['OPEN'], item['CLOSE'], item['HIGH'], item['LOW']]) 

        time.sleep(30)

