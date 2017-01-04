# coding=utf-8
from bs4 import BeautifulSoup
#from HTMLParser import HTMLParser
import httplib
#�[�Jbase page
print '<base href="http://www.123kubo.com/" target="_blank">'

host = 'www.123kubo.com'
#�ư���������
user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
headers = { 'User-Agent' : user_agent}
#�s�u
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
			#�j�M�Ҧ�<div class="vpl"
			hd_links = hd_soup.find_all('div', class_='vpl')
			#all links			
			if len(hd_links) <= 1:
				#�p�G�S�����W�����A�h���L�j�M
				print "No XFplay source"
				print "<br>"
			else:
				#���2��class=vpl�A�]�Ĥ@��vpl�Oflv�����A��2�Ӥ~�O���W����
				links2 = hd_links[1].findAll('a')
			#�C�X��1�ӳs���A�q�`�O�̲M���γ̷s���s��
			#print links2[0]
			#print 'http://'+host +str(links2[0])
			#�p�Garray�O�Ū��A�N�O�S�����l
			if len(links2) <= 0:
				print "No file"
				print "<br>"
			else:
				print links2[0]
				print "<br>"


#URL = raw_input("�п�J123kubo.com���}:")

for page in range(1,13):
	sub = '/vod-search-id-1-cid--area-%E6%AD%90%E7%BE%8E-tag--year-2016-wd--actor--order-vod_hits_month%20desc-p-'+str(page)+'.html'
	#�C�X�ӷ�����
	print '<a href="'+sub+'" target="_blank">'+host+sub+'</a>'
	print "<br>"
	http_connect.request('GET', sub, '', headers)
	#�ǳƦ������e
	http_data = http_connect.getresponse()
	#Read page source html
	data = http_data.read()
	#print data
	
	#�ǳ���soup���J�B�z
	soup = BeautifulSoup(data, "html.parser")
	#��M�ӭ��Ҧ��v���l��
	#�j�M�r�ꬰ:<p class="t">
	#print soup.find_all("p", class_="t")
	data = soup.find_all('p', class_='t')
	linkgrep = collect_links(data)