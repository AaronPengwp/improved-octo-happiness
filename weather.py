# -*- coding: gbk -*-

import urllib.request
import json
from city import city

cityname = input('��������ָ����е�������\n')
citycode = city.get(cityname)

if citycode:
    try:
        url = ('http://www.weather.com.cn/data/cityinfo/%s.html' % citycode)
        #print(url)
        content = urllib.request.urlopen(url).read()
        data = json.loads(content)
        result = data['weatherinfo']
        str_temp = ('%s\n%s ~ %s')%(
            result['weather'],result['temp1'],result['temp2'])
        print(str_temp)
    except:
        print('��ѯʧ��')
else:
    print('û�г����ó���')
