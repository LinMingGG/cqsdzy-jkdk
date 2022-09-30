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
   
login_header={
        'Content-Type': 'application/x-www-form-urlencoded',
        'Content-Length': '227',
        'Host': 'ykm.cqsdzy.com',
        'Connection': 'Keep-Alive',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 11; M2102J2SC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.96 Mobile Safari/537.36',

}
login_url='http://ykm.cqsdzy.com/h5/clockin/index?type=qw&uuid=bf26aefa7f6c4c1098a0a72933253c85'
request=requests.get(url=login_url,headers=login_header)
login_data=json.loads(request.text)#登陆成功后返回的信息
#token=login_data['data']['token']
time.sleep(1)

print(login_data)















#sign_url='https://api.xixunyun.com/signin_rsa?token='+token+'&from=app&version=4.9.9&platform=android&entrance_year=0&graduate_year=0 '
#sign_data={'address':address_detail,#签到地址
#           'address_name':address,#签到地点名称
#           'change_sign_resource':'0',
 #          'comment':'',
#           'latitude':"PcsiE2OsHB5/8tdtamFezKcg9jYp4lKOryX8mG68mE32nVFwh1BNzaJgDIaUK0QOnz7iGDgOcyGMwbB85zJT7wf3Dczy5O9z3/mTBOH9zOFhxKhUSUqlpKdfG5+ZV8UJF6evTcYci5YPIpqGI6uifnQmyB/X86bcNGqe1f2i0WU=",
 #          'longitude':"fS0dMPGfCMjpBmLZgJKV6GXjlC/PD8ZaVlsxSsXopLOPkctgbRuNfGThWBXdjuOY0ESvvWg+l6oYrhMsiHvrTrpJKyy95bMhDW83SNbLrvHQcvdlo5I+ApSYTBNRxvRHqDlSOifwRUdweCBKgrSs26YLP0JWZPwAK54uwNruN3U=",
#           'remark':'0',
    
 #   }
#sign_request=requests.post(url=sign_url,data=sign_data,headers=login_header)
#sign=json.loads(sign_request.text)
#print(sign)
                                   



