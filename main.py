import json
import re
import requests
import os
from bs4 import BeautifulSoup
import datetime

laravel_session = os.environ["COOKIE"]
SEND_KEY = os.environ["SEND_KEY"]

UA = "Mozilla/5.0 (iPhone; CPU iPhone OS 15_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.18(0x18001234) NetType/WIFI Language/zh_CN"
loginUrl = "https://service.jiangsugqt.org/youth/lesson"
confirmUrl = "https://service.jiangsugqt.org/youth/lesson/confirm"
session = requests.session()
userinfo = {}

params = {
"s": "/youth/lesson",
"form": "inglemessage",
"isappinstalled": "0"
}
headers = {
'User-Agent': UA,
'Cookie': "laravel_session=" + laravel_session  # 抓包获取
}

def to_wechat(session):
    """
    学习完成后通过server酱发送至微信，附带学习成绩报告的链接
    :param session:
    :return:
    """
    data = {
        'title': '青年大学习已完成',
        'desp': 'https://service.jiangsugqt.org/youth/report'
    }
    server_chan = "https://sctapi.ftqq.com/{}.send".format(SEND_KEY)
    resp = session.get(server_chan, headers=headers, params=data)
    print('Server酱:', resp.text)

# GET
getRes = session.get(url=loginUrl, headers=headers, params=params)
if '抱歉，出错了' in getRes.text:
    raise Exception("GET 错误")

userinfo['token'] = re.findall(r'var token ?= ?"(.*?)"', getRes.text)[0]
userinfo['lesson_id'] = re.findall(r"'lesson_id':(.*)", getRes.text)[0]
tmp = BeautifulSoup(getRes.text, 'html.parser').select(".confirm-user-info p")
for i in tmp:
    item = BeautifulSoup(str(i), 'html.parser').get_text()
    userinfo[item[:4]] = item[5:]

# POST
params = {
"_token": userinfo.get('token'),
"lesson_id": userinfo.get('lesson_id')
}
res = json.loads(session.post(url=confirmUrl, params=params).text)

print(f"返回结果:{res}")
if res["status"] == 1 and res["message"] == "操作成功":
    print("青年大学习已完成")
    # github action 中会泄露个人隐私信息
    # print(f"您的信息:{userinfo}")
    if datetime.datetime.now().weekday() == 0:
        to_wechat(session)
else:
    raise Exception("POST 错误")
