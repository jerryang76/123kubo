# coding=utf-8
from bs4 import BeautifulSoup
#from HTMLParser import HTMLParser
import httplib, sys
#加入base page
#base_href = 'http://www.123kubo.com'
print '<base href="http://www.123kubo.com/" target="_blank">'

def help():
	print 'kubo_single <URL>'
	print 'example:'
	print 'kubo_single http://www.123kubo.com/vod-search-id-1-cid--area-%E6%AD%90%E7%BE%8E-tag--year-2015-wd--actor--order-vod_hits_month%20desc.html'
	sys.exit()

#連線前準備
host = 'www.123kubo.com'
#排除網站阻擋
user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
headers = { 'User-Agent' : user_agent}
#連線控制與URL
http_connect = httplib.HTTPConnection(host, 80, timeout=10)

#URL = raw_input("請輸入123kubo.com網址:")
if len(sys.argv) < 2:
	help()
sub = sys.argv[1]

def http_get(data):
	#列出來源頁面
	#print '<a href="'+sub+'" target="_blank">'+host+sub+'</a>'
	#print "<br>"
	#print sub
	http_connect.request('GET', sub, '', headers)	
	#準備收取內容
	http_data = http_connect.getresponse()
	#Read page source html
	data = http_data.read()
	#print data
	return data


#find links from src page
#搜尋字串為:<p class="t"> 
data = '123'
SRC_page = http_get(data)
#print "here:"+str(http_soup_out)
#print SRC_page
#準備讓soup介入處理
soup = BeautifulSoup(SRC_page, "html.parser")
#找尋該頁所有影片子頁
#print soup.find_all('p', class_='t')
soup_out = soup.find_all('p', class_='t')

for src in soup_out:
	src_links = src.findAll('a')	
	#linkgrep = collect_links(src_links)	
	#def collect_links(src_links):
	for a in src_links:		
		sub = a.get("href")
		#print a.get("href")
		#print sub
		DST_page = http_get(data)
		#print DST_page
		#http_connect.request('GET', a['href'], '', headers)
		#http_data = http_connect.getresponse()
		#hd_raw = http_data.read()
		hd_soup = BeautifulSoup(DST_page, "html.parser")
		#搜尋所有<div class="vpl"
		hd_links = hd_soup.find_all('div', class_='vpl')			
		#all links			
		if len(hd_links) <= 1:
			#如果沒有先鋒片源，則跳過搜尋
			print "No XFplay source"
			print "<br>"
			continue
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
			continue
		else:
			print links2[0]
			print "<br>"