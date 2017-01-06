# coding=utf-8
import httplib,urllib,re, time
from bs4 import BeautifulSoup

#連線前準備，GW位置
host = '10.10.1.223'
#排除網站阻擋
user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
headers = { 'User-Agent' : user_agent}
#連線控制與URL
http_connect = httplib.HTTPConnection(host, 80, timeout=10)


def http_get(data):
	#列出來源頁面
	#print '<a href="'+sub+'" target="_blank">'+host+sub+'</a>'
	#print "<br>"
	#print sub	
	#print (sub,headers)
	http_connect.request('GET', sub, '', headers)	
	#準備收取內容
	http_data = http_connect.getresponse()
	#Read page source html
	data = http_data.read()
	http_connect.close()
	#print data
	return data
	
	
def http_post(data):
	#列出來源頁面
	#print '<a href="'+sub+'" target="_blank">'+host+sub+'</a>'
	#print "<br>"
	#request(method, url, body, headers)
	#print (host,sub,params,headers)	
	# http_data = urllib.urlopen(sub, params)
	http_connect.request('POST', sub, params, headers)	
	# 準備收取內容
	http_data = http_connect.getresponse()
	# Read page source html
	data = http_data.read()
	#print data
	#return data
	http_connect.close()
	
# sub = '/goform/LoginForm'
login_url = '/goform/LoginForm'
login_pass = 'username=octtel&password=12841302'
telnet_url = '/goform/LoginAccountForm'
# telnet_on = 'FORM_INDEX=0&K12_0=octtel&K13_0=**********&CPK13_0=**********&HK1046_0=0&K1046_0=1&K373_0=asdfasdfsadfsadfsadfa&K374_0=**********&CPK374_0=**********&HK1129_0=0&K1129_0=1&K259_0=80&HK607_0=0&K607_0=1&K1067_0=443&K115_0=60&HK626_0=0&K626_0=1&HK627_0=0&K627_0=1&HK812_0=0&K812_0=1'
# telnet_off = 'FORM_INDEX=0&K12_0=octtel&K13_0=**********&CPK13_0=**********&HK1046_0=0&K1046_0=1&K373_0=asdfasdfsadfsadfsadfa&K374_0=**********&CPK374_0=**********&HK1129_0=0&K1129_0=1&K259_0=80&HK607_0=0&K607_0=1&K1067_0=443&K115_0=60&HK626_0=0&K626_0=1&HK627_0=0&HK812_0=0&K812_0=1'

telnet_on = 'FORM_INDEX=0&HK627_0=0&K627_0=1'
telnet_off = 'FORM_INDEX=0&HK627_0=0'
login_account_url = '/LoginAccountForm.asp'
save_restart_url = '/goform/ConfigBackupLoadForm'
save_restart = 'FORM_INDEX=0&K48_0=1&K20_0=1&Config=ID_Reboot'
data = '123'

#login
sub = login_url
params = login_pass
login_page = http_post(data)
time.sleep(1)

#telnet_on
# sub = telnet_url
# params = telnet_on
# telnet_page = http_post(data)

#telnet_off
# sub = telnet_url
# params = telnet_off
# telnet_page = http_post(data)

#check_telnet
sub = login_account_url
telnet_page = http_get(data)
#print telnet_page
SRC_soup = BeautifulSoup(telnet_page, "html.parser")
soup_out = SRC_soup.find(id='telnet_service')
#<input checked="" class="INPUT_rightPlus8" name="K627_0" type="checkbox" value="1"> Enable Telnet Service </input></input></td> </tr> </tbody>
#<input class="INPUT_rightPlus8" name="K627_0" type="checkbox" value="1"> Enable Telnet Service </input></input></td> </tr> </tbody>
print soup_out
# checked = re.compile(u'checked')
# checked = 'checked'
#無法檢查checkbox！！！！！！
for tag in soup_out.find_all(True):
	print (tag._class)
	# if tag.name == "checked":
		# print "telnet enabledOOOOOOOOOOOOOO"
	# else:
		# print "telnet disabledXXXXXXXXXXXX"