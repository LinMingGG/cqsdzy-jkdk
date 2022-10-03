import requests
import json
import time 
import os

# 配置开始
uuid = os.environ["UUID"]
sign_gps = os.environ["SIGN_GPS"]  # 签到坐标（注意小数点取后6位）
longitude = sign_gps.split(",")[0] # 经度
latitude = sign_gps.split(",")[1] # 纬度
   # 'Content-Length': '582',
login_header={
        'Host': 'ykm.cqsdzy.com',
        'Connection': 'Keep-Alive',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 11; M2102J2SC Build/RKQ1.200826.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 wxwork/4.0.16 ColorScheme/Light MicroMessenger/7.0.1 NetType/WIFI Language/zh Lang/zh',
        'Upgrade-Insecure-Requests': '1',
        'X-Requested-With': 'com.tencent.wework',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7'
}

#获取verilf 这是一个测试
#login_url='http://ykm.cqsdzy.com/h5/clockin/index?type=qw&uuid='+uuid
login_url='http://ykm.cqsdzy.com/h5/clockin/index?type=qw&uuid=d942899913fe40f9a496ad7daab9b05f'
request=requests.get(url=login_url,headers=login_header)
login_data=request.text#登陆成功后返回的信息
time.sleep(1)
print(login_data)



#测试1
#verify = login_data['ykmVerifyId']
#print(verify)


#打卡接口
sign_url='http://ykm.cqsdzy.com/h5/clockin/add'
sign_data={ 
           'lngLat': sign_gps,
          'uuid':uuid,
        #  'ykmVerifyId': verify,
          'homeStatus':'1'
    
   }
sign_request=requests.post(url=sign_url,data=sign_data,headers=login_header)
sign=json.loads(sign_request.text)
print(sign)

#测试2
pf=sign['msg']
print(pf)
                                   



