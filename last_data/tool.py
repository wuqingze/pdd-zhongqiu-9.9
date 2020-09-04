#!/usr/bin/env python
# -*- coding: utf-8 -*- 

dpsf  = open('dps', 'r', encoding='utf-8')
# dpsf = open('dps','r',encoding='utf8')
img_urlsf = open('img_urls')
namesf = open('names')
opsf = open('ops')
urlsf = open('urls')
wbcsf = open('wbcs')

dpsl = []
img_urlsl = []
namesl = []
opsl = []
urlsl = []
wbcsl = []

for line in dpsf:
    dpsl.append(line.strip())
for line in img_urlsf:
    img_urlsl.append(line.strip())
for line in namesf:
    namesl.append(line.strip())
for line in opsf:
    opsl.append(line.strip())
for line in urlsf:
    urlsl.append(line.strip())
for line in wbcsf:
    wbcsl.append(line.strip())
for i in range(0, 104):
    print(namesl[i].strip(), '|', opsl[i], '￥', '|', dpsl[i], '￥', '|', wbcsl[i], '|', '[商品图片](', img_urlsl[i], ')', '|', '[商品地址](', urlsl[i], ')|')
