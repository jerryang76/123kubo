# coding=utf-8
from bs4 import BeautifulSoup
#from HTMLParser import HTMLParser
import httplib, sys, re
#�[�Jbase page
#base_href = 'http://www.123kubo.com'
print '<base href="http://www.123kubo.com/" target="_blank">'

def help():
	print 'kubo_single <URL>'
	print 'example:'
	print 'kubo_single http://www.123kubo.com/vod-search-id-1-cid--area-%E6%AD%90%E7%BE%8E-tag--year-2015-wd--actor--order-vod_hits_month%20desc.html'
	sys.exit()

#�s�u�e�ǳ�
host = 'www.123kubo.com'
#�ư���������
user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
headers = { 'User-Agent' : user_agent}
#�s�u����PURL
http_connect = httplib.HTTPConnection(host, 80, timeout=10)

#URL = raw_input("�п�J123kubo.com���}:")
if len(sys.argv) < 2:
	help()
sub = sys.argv[1]

def http_get(data):
	#�C�X�ӷ�����
	#print '<a href="'+sub+'" target="_blank">'+host+sub+'</a>'
	#print "<br>"
	#print sub
	http_connect.request('GET', sub, '', headers)	
	#�ǳƦ������e
	http_data = http_connect.getresponse()
	#Read page source html
	data = http_data.read()
	#print data
	return data


#find links from src page
#�j�M�r�ꬰ:<p class="t"> 
data = '123'
SRC_page = http_get(data)
#print "here:"+str(http_soup_out)
#print SRC_page
#�ǳ���soup���J�B�z
SRC_soup = BeautifulSoup(SRC_page, "html.parser")
#��M�ӭ��Ҧ��v���l��
#print SRC_soup.find_all('p', class_='t')
soup_out = SRC_soup.find_all('p', class_='t')
#�j�M�r��ɥ����n��X��UTF-8
xfplay = re.compile(u'xfplay')
#xfplay = 'xfplay'
#�B�z�l�������s��
for src in soup_out:
	#��D�����Ҧ��s��
	src_links = src.findAll('a')
	#��Ҧ��ݭn���N���i���A�j
	p = src.find('a')
	p1 = p.find_next('p')
	p2 = p1.find_next('p')
	p3 = p2.find_next('p')
	p4 = p3.find_next('p')
	#�߰ݥD�����s�����l��
	for a in src_links:		
		sub = a.get("href")
		#print a.get("href")
		#print sub
		#http get �l��
		DST_page = http_get(data)
		#print DST_page
		DST_soup = BeautifulSoup(DST_page, "html.parser")
		#�j�M�Ҧ�<div class="vmain"
		DST_vmain = DST_soup.find_all('div', class_='vmain')
		#DST_vmain���G��utf-8�s�X!!!�A�ݭnunicode
		#print DST_vmain
		#print
		
		#�ˬd�l���O�_��xfplay
		DST_xfp_check = DST_soup.find(text=xfplay)
		if DST_xfp_check is None:
			print "<b>No xfplay</b>"
			DST_link = 'No xfplay'
			p4.replace_with(DST_link)
			#�N�t�[�^<p>
			p4.Tag.insert(0,'p')
			#continue #�^��for
		
		
		#���ifor�j�M�s�����e�A�������T�{vmain�̭��O�_�t��xfplay
		#�ѦҴ��խ���:
		#http://www.123kubo.com/vod-search-id-1-cid--area-%E6%AD%90%E7%BE%8E-tag--year-2016-wd--actor--order-vod_hits_month%20desc-p-3.html
		#���{/���P�J��(�̭��S��xfplay�s��)
		#�٨S��!!!!!
		#�q vmain ���� xfplay
		#�q�t��xfplay��vmain���A��<div class="vpl"
		#�q vpl ����
		for sector in DST_vmain:	
			#print sector
			#�u���Find�A���M���׬Oarray�A�L�kcheck for none
			DST_check = sector.find(text=xfplay)
			#print sector.find(text=xfplay)
			if  DST_check is None:
				# print "<b>No xfplay</b>"
				continue #�^��for
			else:			
				#�p��xfplay�A�hvpl�̲�1�ӳs���N�O���Tlink
				#sector�Ounicode
				# print sector
				# print
				# print
				DST_vpl = sector.find_next('div', class_='vpl')				
				# print DST_vpl
				#print DST_vpl.find_all('a')
				DST_link = DST_vpl.find_next('a')
				#�̫ᵲ�G!!!
				print DST_link
				p4.replace_with(DST_link)
print SRC_soup