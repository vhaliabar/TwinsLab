#!/usr/bin/env python3

import requests
import re
#import sys

#line = " some text [2223] IPO Price: 11.50$ Number Shares: 12,218,750 IPO Unit: 10$ another text and numbers ,.,."
#site_full = requests.get('https://sec.report/Document/0001193125-21-056708/d28906ds1a.htm')

#object = site_full.text
#object =
#print(object)
#y = urllib.requests.urlopen('https://sec.report/Document/0001193125-21-056708/d28906ds1a.htm')
#print(y.read)


from urllib.request import Request, urlopen

req = Request('https://sec.report/Document/0001193125-21-072571/', headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read().decode()
#print(webpage[500:1000])
pattern_shares = r'[s|S]hares \d+,\d+,\d+|\d+,\d+,\d+ [s|S]hares'
result_shares = re.findall(pattern_shares, webpage)
print("Found results with 'Number + Shares' : ", result_shares[:10])

print('-----------------------------------------------------------------------------', '\n')
pattern_IPO = r'(\$10.00)'
result_IPO = re.findall(pattern_IPO, webpage)
print("Result in 'IPO' - $10 : ", result_IPO[:10])

print('-----------------------------------------------------------------------------', '\n')
pattern_IPO_price = r'(\$\d+\.\d+|\d+\.\d+\$)'
result_IPO_price = re.findall(pattern_IPO_price, webpage)
print("Result in 'IPO price' : ", result_IPO_price[:10])
