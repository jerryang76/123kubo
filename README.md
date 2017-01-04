# 123kubo
file filter
Requires beautifulsoup4
Installation:
pip install beautifulsoup4

RUN:

python read_12_pages.py

Windows:

Download read_12_pages.exe

Execute result will display at Standard Output


If you want to make html file:

read_12_pages.exe > output.html



#kubo_single \<URL\>
P.S. URL must be in UTF-8 format, not big5 format.
Exmaple:

kubo_single http://www.123kubo.com/vod-search-id-1-cid--area-%E6%AD%90%E7%BE%8E-tag--year-2015-wd--actor--order-vod_hits_month%20desc.html

This Link format is wrong!!!!!                                                ↓↓↓↓

http://www.123kubo.com/vod-search-id-1-cid--tag--area-泰國-tag--year-2017-wd--actor--order-vod_hits_month%20desc.html
