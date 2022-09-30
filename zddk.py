import requests
import json
import time 
import os

# 配置开始
#user = os.environ["USER"]
#account = user.split( )[0] # 账号
#password = user.split( )[1] # 密码
#school_id = user.split( )[2] # 学校ID
#sign_gps = os.environ["SIGN_GPS"]  # 签到坐标（注意小数点取后6位）
#longitude = sign_gps.split(",")[0] # 经度
#latitude = sign_gps.split(",")[1] # 纬度
#SCKEY=os.environ["SCKEY"]
#address = os.environ["ADDRESS_NAME"]
#address_detail = os.environ["ADDRESS_DETAIL"]
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
login_url='http://ykm.cqsdzy.com/h5/clockin/index?type=qw&uuid=bf26aefa7f6c4c1098a0a72933253c85'
request=requests.get(url=login_url,headers=login_header)
login_data=request.text#登陆成功后返回的信息

#verilf=login_data['data']['verilf']

time.sleep(1)
print(login_data)















sign_url='http://ykm.cqsdzy.com/h5/clockin/add'
sign_data={ 
           'lngLat':'106.529942,29.588676',
          'uuid':'c42c8add9a7b4c119d73048ba6b6dafa',
          'ykmVerifyId':'c6bc7f0f6a3544e38e4c66e5c48a35ef',
          'homeStatus':'1'
    
   }
sign_request=requests.post(url=sign_url,data=sign_data,headers=login_header)
sign=json.loads(sign_request.text)
print(sign)
                                   



