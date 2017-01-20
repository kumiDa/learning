import requests
from bs4 import BeautifulSoup
import urllib2
import os

strs=[]


url=''#include the url for a particular product from the flipkart website
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1500.55 Safari/537.36'}

response = requests.get(url, headers=headers)

soup=BeautifulSoup(response.content,'html5lib')

calsses=['_3eAQiD','_1vC4OE _37U4_g','_3auQ3N _16fZeb','VGWI6T _3GXWnA']
foreHeads=['Product Name: ','The Selling Price: ','So called MRP: ','Percentage of Discount Offered: ']

for i in range(len(calsses)):
    tempStr=soup.find(['h1', 'div'], {'class': str(calsses[i])}).text
    txt=str(foreHeads[i])+tempStr.encode('ascii','ignore')
    strs.append(str(foreHeads[i])+tempStr.encode('ascii','ignore'))

print os.system('notify-send "{line1}" "{line2}"'.format(line1=strs[0],line2=strs[1]+'\n'+strs[2]+'\n'+strs[3]))

# to run the code continuously and get the notification from time to time
# run script as
#$watch -n <time interval> python flipTap.py
