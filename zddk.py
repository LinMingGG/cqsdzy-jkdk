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
        'User-Agent': 'Mozilla/5.0 (Linux; Android 11; M2102J2SC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.96 Mobile Safari/537.36',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,ru;q=0.6,zh-TW;q=0.5'
}

#获取verilf 这是一个测试
login_url='http://ykm.cqsdzy.com/h5/clockin/index?type=qw&uuid='+uuid
request=requests.get(url=login_url,headers=login_header)
login_data=request.text#登陆成功后返回的信息
time.sleep(1)
print(login_data)

login_data2=json.loads(request.text)
print(login_data2)

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
                                   



