# -*- coding: gbk -*-

import urllib.request
import json

url1 = 'http://m.weather.com.cn/data3/city.xml'
#conternt1 = repr(urllib.request.urlopen(url1).read().decode('utf-8'))#repr() 函数将对象转化为供解释器读取的形式。返回一个对象的 string 格式。
conternt1 = urllib.request.urlopen(url1).read().decode('utf-8')
#print(json.loads(urllib.request.urlopen(url1).read()))
#print(type(repr(conternt1)))data = json.loads(content)
provinces = conternt1.split(',')
#print('\n\n',urllib.request.urlopen(url1).read().decode('utf-8'))
#print('\n',provinces)
result = 'city = {\n'
url = 'http://m.weather.com.cn/data3/city%s.xml'
for p in provinces:
    #print('\n\n',p)
    p_code = p.split('|')[0]
    #print('\n\n',p_code)
    url2 = url % p_code
    #print('\n\n url2',url2)
    content2 = urllib.request.urlopen(url2).read().decode('utf-8')
    cities = content2.split(',')
    #print('\n cities \n',url2)
    for c in cities:
        #print('\n c: \n',c)
        c_code = c.split('|')[0]
        url3 = url % c_code
        content3 = urllib.request.urlopen(url3).read().decode('utf-8')
        districts = content3.split(',')
        #print('\n content3: \n',districts)
        for d in districts:
            #print('\n\n',d)
            d_pair = d.split('|')
            #print('\nd_pair \n',d_pair)
            d_code = d_pair[0]
            name = d_pair[1]
            url4 = url % d_code
            content4 = urllib.request.urlopen(url4).read().decode('utf-8')
            code = content4.split('|')[1]
            line = "   '%s':  '%s',\n" % (name, code)
            result += line
            print(name+ ':' + code)
         
result += '}'
with open('C:/Users/Administrator/Desktop/python/day01/city2.py','w') as f:
    f.write(result)
    
