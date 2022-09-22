import json
import re
import requests
import os
from bs4 import BeautifulSoup

laravelSession = os.getenv('cookie')
UA = "Mozilla/5.0 (iPhone; CPU iPhone OS 15_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.18(0x18001234) NetType/WIFI Language/zh_CN"
loginUrl = "https://service.jiangsugqt.org/youth/lesson"
confirmUrl = "https://service.jiangsugqt.org/youth/lesson/confirm"
session = requests.session()
userinfo = {}

# GET
params = {
    "s": "/youth/lesson",
    "form": "inglemessage",
    "isappinstalled": "0"
}
headers = {
    'User-Agent': UA,
    'Cookie': "laravelSession=" + laravelSession
}
getRes = session.get(url=loginUrl, headers=headers, params=params)

if '抱歉，出错了' in getRes.text:
    print(laravelSession)
    raise Exception("GET RE")


userinfo['token'] = re.findall(r'var token ?= ?"(.*?)"', getRes.text)[0]
userinfo['lesson_id'] = re.findall(r"'lesson_id':(.*)", getRes.text)[0]

temp = BeautifulSoup(getRes.text, 'html.parser').select(".confirm-user-info p")
for i in temp:
    item = BeautifulSoup(str(i), 'html.parser').get_text()
    userinfo[item[:4]] = item[5:]

params = {
    "_token": userinfo.get('token'),
    "lesson_id": userinfo.get('lesson_id')
}

# POST
res = json.loads(session.post(url=confirmUrl, params=params).text)

if res["status"] == 1 and res["message"] == "操作成功":
    print("江苏青年大学习已完成")
    print(f"您的信息:{userinfo}")
else:
    raise Exception("POST RE")
