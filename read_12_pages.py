# coding=utf-8
from bs4 import BeautifulSoup
#from HTMLParser import HTMLParser
import httplib
#加入base page
print '<base href="http://www.123kubo.com/" target="_blank">'

host = 'www.123kubo.com'
#排除網站阻擋
user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
headers = { 'User-Agent' : user_agent}
#連線
http_connect = httplib.HTTPConnection(host, 80, timeout=10)


def collect_links(data):
#find links from src page
	for div in data:
		links = div.findAll('a')
		for a in links:
			#print "http://"+host + a['href']
			http_connect.request('GET', a['href'], '', headers)
			http_data = http_connect.getresponse()
			hd_raw = http_data.read()
			hd_soup = BeautifulSoup(hd_raw, "html.parser")
			#搜尋所有<div class="vpl"
			hd_links = hd_soup.find_all('div', class_='vpl')
			#all links			
			if len(hd_links) <= 1:
				#如果沒有先鋒片源，則跳過搜尋
				print "No XFplay source"
				print "<br>"
			else:
				#找第2個class=vpl，因第一個vpl是flv片源，第2個才是先鋒片源
				links2 = hd_links[1].findAll('a')
			#列出第1個連接，通常是最清楚或最新的連結
			#print links2[0]
			#print 'http://'+host +str(links2[0])
			#如果array是空的，就是沒有片子
			if len(links2) <= 0:
				print "No file"
				print "<br>"
			else:
				print links2[0]
				print "<br>"


#URL = raw_input("請輸入123kubo.com網址:")

for page in range(1,13):
	sub = '/vod-search-id-1-cid--area-%E6%AD%90%E7%BE%8E-tag--year-2016-wd--actor--order-vod_hits_month%20desc-p-'+str(page)+'.html'
	#列出來源頁面
	print '<a href="'+sub+'" target="_blank">'+host+sub+'</a>'
	print "<br>"
	http_connect.request('GET', sub, '', headers)
	#準備收取內容
	http_data = http_connect.getresponse()
	#Read page source html
	data = http_data.read()
	#print data
	
	#準備讓soup介入處理
	soup = BeautifulSoup(data, "html.parser")
	#找尋該頁所有影片子頁
	#搜尋字串為:<p class="t">
	#print soup.find_all("p", class_="t")
	data = soup.find_all('p', class_='t')
	linkgrep = collect_links(data)