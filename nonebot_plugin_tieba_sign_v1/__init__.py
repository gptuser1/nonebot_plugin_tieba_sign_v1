from nonebot import on_command
from nonebot.matcher import Matcher
from nonebot.params import ArgPlainText, CommandArg
from nonebot.adapters.onebot.v11 import Message, MessageSegment, escape
import random
import time

import requests


tieba_ = on_command('贴吧', aliases={'tieba', '8u', 'bdtb'})


# 全局变量
headers = {
        'Cookie':'',#your baidu cookie
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'User-Agent': 'Dalvik/2.1.0(Linux;U;Android10;oppo Build/oppo a9s)',
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip',
        'Host': 'tieba.baidu.com',
    }
msg_basic = '(UTC)服务器时间：' + time.strftime("%Y年%m月%d日 %H:%M:%S")

#  获取贴吧列表
def get_like():
    params = {
        '_client_version': '6.5.8',
        'sign': '',#your sign
        'page_no': '1',
        'page_size': '100',
    }
    url = 'http://tieba.baidu.com/c/f/forum/like'
    res = requests.post(url, headers=headers, params=params)
    likes = res.json()['forum_list']['non-gconforum']
    return likes


#  登录账号获取tbs
def login():
    params = {
        'bdusstoken': '',#your bdusstoken
        '_client_version': '6.7.0',
        'sign': '',#your sign
        '_phone_imei': '000000000000000',
        '_client_type': '2',
    }
    url = 'http://c.tieba.baidu.com/c/s/login'
    res = requests.post(url, headers=headers, params=params)
    tbs = res.json()['anti']['tbs']
    return tbs


#  贴吧一键签到大师用的api, 找不到sign的算法，有待研究
def sign1(fid, kw, tbs, sign):
    params = {
        'fid': fid,
        'tbs': tbs,
        'sign': sign,
        'kw': kw,
    }
    url = 'http://c.tieba.baidu.com/c/c/forum/sign'
    res = requests.post(url, headers=headers, params=params)
    print(res.text)
    return


#  贴吧目前使用的api
def sign2(kw, tbs):
    signin_url = "https://tieba.baidu.com/sign/add"
    signin_data = {
        "ie": "utf-8",
        "kw": kw,
        "tbs": tbs,
    }
    res = requests.post(url=signin_url, data=signin_data, headers=headers)
    res.encoding = res.apparent_encoding
    status_code = res.json()['no']
    if status_code == 0:
        rank = res.json()['data']['uinfo']['user_sign_rank']
        msg_new = '亲爱的，{}吧签到成功啦，你是今天第{}个签到的噢'.format(kw, rank)
    elif status_code == 1101:
        msg_new = '亲爱的，{}吧已经签过啦(#^.^#)'.format(kw)
    else:
        msg_new = res.text + '亲爱的，出现了未知错误，o(╥﹏╥)o'
    return msg_new


def main(msg):
    likes = get_like()
    tbs = login()
    msg_echo = msg
    for like in likes:
        kw = like['name']
        msg_echo = msg_echo + sign2(msg_old=msg_echo, kw=kw, tbs=tbs)
        time.sleep(random.randint(1, 3))
    return msg_echo


@tieba_.handle()
async def _handle(matcher: Matcher, comd: Message = CommandArg()):
    if comd.extract_plain_text() and comd.extract_plain_text()[0]!='_':
        matcher.set_arg('comd', comd)


@tieba_.got('comd', prompt='你想干嘛？')
async def _(comd: str = ArgPlainText('comd')):
    if comd=='签到':
        await tieba_.send(msg_basic, at_sender=True)
        await tieba_.send('签到中...', at_sender=True)
        likes = get_like()
        tbs = login()
        for like in likes:
            kw = like['name']
            msg_echo = sign2(kw=kw, tbs=tbs)
            await tieba_.send(msg_echo, at_sender=True)
            time.sleep(random.randint(1, 3))
        await tieba_.send('签到完毕，请指示！', at_sender=True)
    elif comd[0]!='_':
        await tieba_.send('对不起做不到！', at_sender=True)
    else:
        await tieba_.reject_arg('comd',prompt='不能使用“_”作为查询前缀！请重新输入！')
