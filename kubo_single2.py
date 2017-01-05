# coding=utf-8
from bs4 import BeautifulSoup
#from HTMLParser import HTMLParser
import httplib, sys, re
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
SRC_soup = BeautifulSoup(SRC_page, "html.parser")
#找尋該頁所有影片子頁
#print SRC_soup.find_all('p', class_='t')
soup_out = SRC_soup.find_all('p', class_='t')
#搜尋字串時必須要轉碼成UTF-8
xfplay = re.compile(u'xfplay')
#xfplay = 'xfplay'
#處理子頁中的連結
for src in soup_out:
	#找主頁中所有連結
	src_links = src.findAll('a')	
	#詢問主頁中連結的子頁
	for a in src_links:		
		sub = a.get("href")
		#print a.get("href")
		#print sub
		#http get 子頁
		DST_page = http_get(data)
		#print DST_page
		DST_soup = BeautifulSoup(DST_page, "html.parser")
		#搜尋所有<div class="vmain"
		DST_vmain = DST_soup.find_all('div', class_='vmain')
		#DST_vmain結果為utf-8編碼!!!，需要unicode
		#print DST_vmain
		#print
		
		#檢查子頁是否有xfplay
		DST_xfp_check = DST_soup.find(text=xfplay)
		if DST_xfp_check is None:
			print "<b>No xfplay</b>"
			continue #回到for
		
		
		#跳進for搜尋連結之前，必須先確認vmain裡面是否含有xfplay
		#參考測試頁面:
		#http://www.123kubo.com/vod-search-id-1-cid--area-%E6%AD%90%E7%BE%8E-tag--year-2016-wd--actor--order-vod_hits_month%20desc-p-3.html
		#降臨/異星入境(裡面沒有xfplay連結)
		#還沒做!!!!!
		#從 vmain 中找 xfplay
		#從含有xfplay的vmain中，找<div class="vpl"
		#從 vpl 中找
		for sector in DST_vmain:	
			#print sector
			#只能用Find，不然答案是array，無法check for none
			DST_check = sector.find(text=xfplay)
			#print sector.find(text=xfplay)
			if  DST_check is None:
				# print "<b>No xfplay</b>"
				continue #回到for
			else:			
				#如有xfplay，則vpl裡第1個連結就是正確link
				#sector是unicode
				# print sector
				# print
				# print
				DST_vpl = sector.find_next('div', class_='vpl')				
				# print DST_vpl
				#print DST_vpl.find_all('a')
				DST_link = DST_vpl.find_next('a')
				#最後結果!!!
				print DST_link
