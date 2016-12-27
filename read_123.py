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
#In data find links
	for div in data:
		links = div.findAll('a')
		for a in links:
			#print "http://"+host + a['href']
			http_connect.request('GET', a['href'], '', headers)
			http_data = http_connect.getresponse()
			hd_raw = http_data.read()
			hd_soup = BeautifulSoup(hd_raw, "html.parser")
			hd_links = hd_soup.find_all('div', class_='vpl')
			#all links
			#���2��vpl�A�]�Ĥ@�ӬOflv�A��2�Ӥ~�O���W����
			if len(hd_links) <= 1:
				print "No XFplay source"
				print "<br>"
			else:
				links2 = hd_links[1].findAll('a')
			#�C�X��1�ӳs���A�q�`�O�̲M���γ̷s���s��
			#print links2[0]
			#print 'http://'+host +str(links2[0])
			if len(links2) <= 0:
				print "No file"
				print "<br>"
			else:
				print links2[0]
				print "<br>"


for page in range(1,13):
	sub = '/vod-search-id-1-cid--area--tag--year-2016-wd--actor--order-vod_hits_month%20desc-p-'+str(page)+'.html'
	print sub
	print "<br>"
	http_connect.request('GET', sub, '', headers)
	#�������e
	http_data = http_connect.getresponse()
	data = http_data.read()
	#Read all data
	#print data
	soup = BeautifulSoup(data, "html.parser")

	#Find all:
	#<p class="t">
	#print soup.find_all("p", class_="t")
	data = soup.find_all('p', class_='t')
	bb = collect_links(data)