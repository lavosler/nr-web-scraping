from datetime import datetime
from bs4 import BeautifulSoup
import requests
import pandas as pd
import csv
from html.parser import HTMLParser

datestr = datetime.now().strftime("%m-%d-%Y")
f = open('C:/Users/laurenv/Documents/Python/Lashley_Land-'+datestr+'.csv', 'w', newline="")
writer = csv.writer(f)

header = ["Address", "Price", "Name", "Info Row", "Land Type", "Link"]
writer.writerow(header)

page = 1
while True: 
    url = f"https://lashleyland.com/nebraska-farms-for-sale/page/{page}/"
    page = page + 1
    result = requests.get (url)
    doc = BeautifulSoup(result.content, "html.parser")
#url = "https://lashleyland.com/nebraska-farms-for-sale/"
    properties = doc.select('.property-item')
    if not len(properties):
        break
    for p in properties:
        row = []
        row.append(p.select('.property-address')[0].string)
        row.append(p.select('.price.hide-on-list .item-price')[0].string)
        row.append(p.select('.info-row .property-title')[0].string)
        inforesults = p.select('.info-row.amenities span')
        nl = ""
        infostr = ""
        for info in inforesults:
            infostr = infostr + nl + info.string
            nl = "|"
        row.append(infostr)
        row.append(p.select('.info-row.amenities p')[2].string)
        # landresults = p.select('.info-row.amenities p')
        # infoland = ""
        # for i in landresults:
        #     infoland = infoland + nl + i.string
        #     nl = "|"
        # row.append(infoland)
        row.append(p.select('.phone a[href]')[0]['href'])
        writer.writerow(row)

f.close()
