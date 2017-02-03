// ==UserScript==
// @name         New Userscript
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  try to take over the world!
// @author       You
// @match        http://www.123kubo.com/vod-search-id-1-*
// @grant        none
// ==/UserScript==
// 必須在電影頁面才能使用:
// http://www.123kubo.com/vod-search-id-1-cid--area-%E6%AD%90%E7%BE%8E-tag--year--wd--actor--order-vod_hits_month%20desc.html
function httpGet(theUrl)
{
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "GET", theUrl, false ); // false for synchronous request
    xmlHttp.setRequestHeader("User-Agent","Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36");
    xmlHttp.send( null );
    return xmlHttp.responseText;
}

$(document).ready(function() {
  var hrefs = new Array();
  // 找到 t class
  var elements = $('.t > a');
  // 在t class 抽出每個連結，但應該是每個t class抽出屬性href連結，存入href array
  elements.each(function() {
    hrefs.push($(this).attr('href'))
  });
  // 來個第一頁
  var subpage = httpGet(hrefs[0]);
  alert(subpage);
  
  $('body').append('<input type="button" value="開所有子頁" id="CP">')
  $("#CP").css("position", "fixed").css("top", 0).css("left", 0);
  $('#CP').click(function(){
    $.each(hrefs, function(index, value) {
      setTimeout(function(){
       window.open(value, '_blank');
      },1000);
    });
  });
});
