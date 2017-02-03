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
// 找到 t class
// 在t class 抽出每個連結，但應該是每個t class抽出屬性href連結
$(document).ready(function() {
  var hrefs = new Array();
  var elements = $('.t > a');
  elements.each(function() {
    hrefs.push($(this).attr('href'))
  });
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
