#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import requests
import json

def trans_wbcs(wbc):
    if None == wbc or '' == wbc.strip():
        return ''

    if '万' in wbc:
        t = wbc.split('万')
        return int(float(t[0])*10000)
    else:
        return int(float(wbc))


class Commodity:
    def __init__(self):
        self.name = ''
        self.original_price = ''
        self.discount_price = ''
        self.url = ''
        self.img_url = ''
        self.wanted_buy_cnt = ''

#    def __str__(self):
#        return '(Commodity: %s, %s, %s, %s, %s)' % (self.name, self.original_price, self.discount_price, self.wanted_buy_cnt,
#                self.img_url, self.url)
                    
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

url = 'https://mobile.yangkeduo.com/luxury_spike.html?_wv=41729&_wvx=10&id=143534&subject_id=&type=47&refer_share_id=7w3gqdrutsr1ns1g068xepflpmn6hilo&refer_share_uid=4935443353500&refer_share_uin=RNORJ7PISN75P3PEBVM4LI2SHY_GEXDA&refer_share_channel=copy_link'

response = requests.get(url, headers=headers)
json_str = response.content.decode().split('\n')[35][31:-61]
json_str = '{"props"' + json_str[6:]
json_str += '}'
list = json.loads(json_str)['props']['store']['list']
for obj in list:
    if obj['store'].get('imgData', None):
        try:
            imgData = obj['store'].get('imgData')[0]
            imgUrl = imgData['imgUrl']
            url = imgData['url']
            name = imgData['name'] 
            response = requests.get(url, headers=headers)
            html = response.content.decode().split('\n')[23]
            i = html.find('￥')
            pstr = html[i:i+50]
            oi = pstr.find("<span>")
            oj = pstr.find("</span")
            di = pstr.find("-->")
            dj = pstr.find("</del")
            dprice = pstr[oi+6:oj]
            oprice = pstr[di+3:dj]
            ti = html.find("人想买")
            ts = html[ti-30:ti] 
            bstr = ts[ts.find("等")+1:] 
            bcnt = bstr.split("<!-- -->")[1]
            selli = html.find("共")
            sellj = html.find("件")
            sellstr = html[selli+1:sellj]
            sellcnt = sellstr.split("<!-- -->")[1]
            print('|' , name, '|' , sellcnt, '|', oprice, '￥ |', dprice, '￥ |', trans_wbcs(bcnt), '| [商品图片](', imgUrl, ')| [商品地址](', url, ')|')
        except:
            pass
