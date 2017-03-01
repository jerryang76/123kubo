// ==UserScript==
// @name         123kubo美劇
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  try to take over the world!
// @author       You
// @match        http://www.123kubo.com/vod-search-id-2-*
// @include      http://www.123kubo.com/vod-search-id-2-*
// @grant        none
// ==/UserScript==
// 必須在美劇頁面才能使用:
// http://www.123kubo.com/vod-search-id-2-cid--area-%E6%AD%90%E7%BE%8E-tag--year--wd--actor--order-vod_hits_month%20desc.html
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
    //for(i = 0; i < hrefs.length; i++) {
    // 找到12個子頁的連結
    for(i = 0; i < 12; i++) {
        var each_subpage = httpGet(hrefs[i]);
        //console.log(each_subpage);
        //alert(each_subpage);
        //return each_subpage;
        // In .vmain class find child <p> contains xfplay
        // In this .vmain class get decendent .vpl class's direct decendent <a> with attribute of "href" value
        // $("p:contains("xfplay")")
        // $('html:contains("xfplay")')
        // 從div class="vmain"找到文字xfplay > class="vpl" > ul > li > a
        $(function() {
            //each_sublink = $('.vmain > html:contains("xfplay") .vpl > a.attr("href")');
            //each_sublink = $( "div.vpl > ul > li > a", each_subpage ).first().text();
            //正確文字版:
            //each_sublink = $( "div.vmain:contains('xfplay') > .vpl > ul > li > a", each_subpage ).text();
            //正確連結版:
            each_sublink = $( "div.vmain:contains('xfplay') > .vpl > ul > li > a", each_subpage );
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
    // return 沒發生?
    subpages = myFunction(hrefs);
    //alert(subpages[1]);
    // 用jquery拿子頁
    //$.get(hrefs[1], function(data, status){
    //    alert("Data: " + data + "\nStatus: " + status);
    //});
    // 回填母頁
    // 測試找到第1個狀態行
    //var test = $('div.listlf > ul > li > p').first().next().next().next().next().text();
    // 4 , 10, 16, 22, 28, 34, 40, 46, 52, 58, 64, 70(+6)
    //var test = $('div.listlf > ul > li > p:eq(4)').text();
    // 測試找到所有狀態行
    var test = [];
    test.append = $('div.listlf > ul > li > p:eq(4)').text();
    test.append = $('div.listlf > ul > li > p:eq(10)').text();
    test.append = $('div.listlf > ul > li > p:eq(16)').text();
    test.append = $('div.listlf > ul > li > p:eq(22)').text();
    test.append = $('div.listlf > ul > li > p:eq(28)').text();
    test.append = $('div.listlf > ul > li > p:eq(34)').text();
    test.append = $('div.listlf > ul > li > p:eq(40)').text();
    test.append = $('div.listlf > ul > li > p:eq(46)').text();
    test.append = $('div.listlf > ul > li > p:eq(52)').text();
    test.append = $('div.listlf > ul > li > p:eq(58)').text();
    test.append = $('div.listlf > ul > li > p:eq(64)').text();
    test.append = $('div.listlf > ul > li > p:eq(70)').text();
    //alert(test[2]);
    // 回填狀態:
    //$('div.listlf > ul > li > p').first().next().next().next().next().replaceWith(each_sublink);
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