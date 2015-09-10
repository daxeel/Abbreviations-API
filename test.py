# from bs4 import BeautifulSoup
# import requests

# word = 'cs'

# URL = "http://fullforms.com/"+ word
# PAGE = requests.get(URL)
# HTML = PAGE.content
# soup = BeautifulSoup(HTML, "html.parser")

# all_trs = soup.find_all('table')[2].tbody.find_all('tr')

# for i in all_trs:
# 	all_tds = i.find_all('td')
# 	print all_tds[3].a['href']
# 	print '--------------'


# import urllib2
# import json

# response = urllib2.urlopen('http://fullform-daxeel.rhcloud.com/api/popular/cs')
# data = json.load(response)   

# print data['fullform']
# print data['meaning']

import urllib2
import json

response = urllib2.urlopen('http://fullform-daxeel.rhcloud.com/api/all/cs')
data = json.load(response)   

for each in data:
	print each['fullform']
	print each['meaning']
	print '-'*10