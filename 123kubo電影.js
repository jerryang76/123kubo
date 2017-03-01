// ==UserScript==
// @name         123kubo電影
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  try to take over the world!
// @author       You
// @match        http://www.123kubo.com/vod-search-id-1-*
// @include      http://www.123kubo.com/vod-search-id-1-*
// @grant        none
// ==/UserScript==
// 必須在電影頁面才能使用:
// http://www.123kubo.com/vod-search-id-1-cid--area-%E6%AD%90%E7%BE%8E-tag--year--wd--actor--order-vod_hits_month%20desc.html
function httpGet(theUrl)
{
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "GET", theUrl, false ); // false for synchronous request
    //xmlHttp.setRequestHeader("User-Agent","Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36");
    xmlHttp.send( null );
    return xmlHttp.responseText;
}
function myFunction(hrefs) {
    var out = "";
    var i;
	var sublinks = new Array(0);
    for(i = 0; i < 12; i++) {
        var each_subpage = httpGet(hrefs[i]);
        //alert(each_subpage);
        //return each_subpage;
        // In .vmain class find child <p> contains xfplay
        // In this .vmain class get decendent .vpl class's direct decendent <a> with attribute of "href" value
        // $("p:contains("xfplay")")
        // $('html:contains("xfplay")')
        $(function() {
            each_sublink = $("div.vmain:contains('xfplay') > .vpl > ul > li > a:first", each_subpage );
            // If not found, return "no xfplay", else find class vpl's 1st link
            //alert(each_sublink);
			sublinks.push(each_sublink);
        });
    }
	return sublinks;
}
$(document).ready(function() {
    var hrefs = new Array(0);
    // 找到 t class
    // Class Selector
    // $('.classid')
    var elements = $('.t > a');
    // 在t class 抽出每個連結，但應該是每個t class抽出屬性href連結，存入href array
    elements.each(function() {
        hrefs.push($(this).attr('href'));
    });

    // http get所有子頁
    var subpages = new Array(0);
    subpages = myFunction(hrefs);
    $('div.listlf > ul > li > p:eq(4)').replaceWith(subpages[0]);
    $('div.listlf > ul > li > p:eq(9)').replaceWith(subpages[1]);
    $('div.listlf > ul > li > p:eq(14)').replaceWith(subpages[2]);
    $('div.listlf > ul > li > p:eq(19)').replaceWith(subpages[3]);
    $('div.listlf > ul > li > p:eq(24)').replaceWith(subpages[4]);
    $('div.listlf > ul > li > p:eq(29)').replaceWith(subpages[5]);
    $('div.listlf > ul > li > p:eq(34)').replaceWith(subpages[6]);
    $('div.listlf > ul > li > p:eq(39)').replaceWith(subpages[7]);
    $('div.listlf > ul > li > p:eq(44)').replaceWith(subpages[8]);
    $('div.listlf > ul > li > p:eq(49)').replaceWith(subpages[9]);
    $('div.listlf > ul > li > p:eq(54)').replaceWith(subpages[10]);
    $('div.listlf > ul > li > p:eq(59)').replaceWith(subpages[11]);
});