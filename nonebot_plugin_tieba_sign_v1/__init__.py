from nonebot import on_command
from nonebot.matcher import Matcher
from nonebot.params import ArgPlainText, CommandArg
from nonebot.adapters.onebot.v11 import Message, MessageSegment, escape



tieba_ = on_command('贴吧', aliases={'tieba', '8u', 'bdtb'})


def sign_main():
    import random
    import time

    import requests

    # 全局变量
    headers = {
            'Cookie': 'BIDUPSID=65657D020ACE0DCB0F010337A3290262; PSTM=1589872111; rpln_guide=1; bdshare_firstime=1590802131786; __yjs_duid=1_dc508bb103c6efd8bd3bb4e1fd39fded1620310738569; MCITY=-%3A; H_WISE_SIDS=110085_127969_153067_176399_179349_184716_188741_189659_190620_191068_191247_194085_195343_195538_196425_196528_197242_197711_197892_197956_198258_199022_199313_199569_200434_201104_201538_201706_202058_202759_202905_202911_203195_203266_203361_203518_203525_203606_203886_204031_204255_204304_204536_204860_204914_204973_205087_205171_205218_205239_205408_205485_205690_205806_205831_205842_205909_206008_206058_206065_206099_206124_206251_206276_206284_206476_206515_206729_206870_206910_206927_207144_207234_207363_207497_207534_207540_207668_207893; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; BAIDUID=758F987032014F6594BFAECEC43447B6:SL=0:NR=10:FG=1; Hm_lvt_287705c8d9e2073d13275b18dbd746dc=1652709448,1652849143; H_PS_PSSID=31254_26350; BDUSS=nVoQmozdGF4V2VwRVZNSjNReFVMMzlXdzZOMG4tcDhoalhjc2tZUXV-V3RJS3hpRVFBQUFBJCQAAAAAAAAAAAEAAABPvFY6VG9reW~YvGhvdNivyMgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAK2ThGKtk4Ric; BDUSS_BFESS=nVoQmozdGF4V2VwRVZNSjNReFVMMzlXdzZOMG4tcDhoalhjc2tZUXV-V3RJS3hpRVFBQUFBJCQAAAAAAAAAAAEAAABPvFY6VG9reW~YvGhvdNivyMgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAK2ThGKtk4Ric; BAIDUID_BFESS=758F987032014F6594BFAECEC43447B6:SL=0:NR=10:FG=1; STOKEN=e15c856e849722aeafe4b29148fb3faffc6c5a20adf9edccd1054384ec0aa3a0; Hm_lvt_98b9d8c2fd6608d564bf2ac2ae642948=1652712944,1652759591,1652849142,1652857137; st_key_id=17; BAIDU_WISE_UID=wapp_1652857201065_450; USER_JUMP=-1; LONGID=978762831; Cuid=758F987032014F6594BFAECEC43447B6%3ASL%3D0%3ANR%3D10%3AFG%3D1; Appid=tieba; Appkey=appkey; DeviceType=20; Extension-Version=2.2; LCS-Header-Version=1; RT="z=1&dm=baidu.com&si=30u5mnqu673&ss=l3b8hylr&sl=7&tt=b35&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=5w8s&cl=d1ay"; Hm_lpvt_98b9d8c2fd6608d564bf2ac2ae642948=1652857805; ab_sr=1.0.1_Y2U3ZDNkYzcxNjVlZTUxYTczMzBhYjAyODhjNjg3ZDJkZDIwYzI2MWZjMGE2NGIxMjc2OGUwN2Y2ZTY1MjMwY2JkZjFjNjM1MTUxMmY1ZjFlMTM5MDIwMTVkMmZkNjg4YmQ5OGI2N2I4YTBkZmJiMzk0N2MwMTEwY2RhZDAzNTU2Mjc2MTBkNGIwNmE1NTkzMzZmNGI1NDUyZjlhY2U3YzZhZTg3ZjY2ZGZhOGMxOWY5NjRiYjRiYjQ2MGY1NDBk; st_data=117588af9a6cc7083d5b4cb7b6d4ba1a5f26327cb9980c0b9a6d3e46d4f16d1536fbfdb3c7b550a1280cb4e4d44d290f5f0ae034dcefa86e66c7823b08d406a01906fe805b7ed4bf65c6acbb28a18d7db36992b27f5af766aa02a510f72cb1f1; st_sign=2a5b129c; showCardBeforeSign=1',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'User-Agent': 'Dalvik/2.1.0(Linux;U;Android10;SEA-AL10 Build/HUAWEISEA-AL10)',
            'Connection': 'Keep-Alive',
            'Accept-Encoding': 'gzip',
            'Host': 'tieba.baidu.com',
        }
    message = '服务器时间：' + time.strftime("%Y年%m月%d日 %H:%M:%S")
    #  获取贴吧列表
    def get_like():
        params = {
            '_client_version': '6.5.8',
            'sign': '2a85df953f60b5c2dc5b997face66d7c',
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
            'bdusstoken': 'Dc3QXlzaXhvczVrZVJiaFhIZHRxdWRoV2FxcnhHM2VWencxMFR3U1ZSQ3BDcUJpRUFBQUFBJCQAAAAAAAAAAAEAAABPvFY6VG9reW~YvGhvdNivyMgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKl9eGKpfXhiM',
            '_client_version': '6.7.0',
            'sign': 'cbc0a2b987019a0e5617c7b511a59f6f',
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
        global message
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
            message = message + '亲爱的，{}吧签到成功啦，你是今天第{}个签到的噢'.format(kw, rank)
        elif status_code == 1101:
            message = message + '亲爱的，{}吧已经签过啦(#^.^#)'.format(kw)
        else:
            message = message + res.text + '亲爱的，出现了未知错误，o(╥﹏╥)o'
        return


    def main():
        likes = get_like()
        tbs = login()
        for like in likes:
            kw = like['name']
            sign2(kw=kw, tbs=tbs)
            time.sleep(random.randint(1, 3))
        return

    return message



@tieba_.handle()
async def _handle(matcher: Matcher, comd: Message = CommandArg()):
    if comd.extract_plain_text() and comd.extract_plain_text()[0]!='_':
        matcher.set_arg('comd', comd)


@tieba_.got('comd', prompt='你想干嘛？')
async def _(comd: str = ArgPlainText('comd')):
    if comd=='签到':
        await tieba_.send('签到中...', at_sender=True)
        msg=sign_main()
        await tieba_.send(msg, at_sender=True)
    elif comd[0]!='_':
        await tieba_.send('对不起做不到！', at_sender=True)
        #await tieba_.send('签到中...', at_sender=True)
        #await tieba_.send(MessageSegment.image(file=f'http://zh.wttr.in/{escape(city)}.png', cache=False), at_sender=True)
    else:
        await tieba_.reject_arg('comd',prompt='不能使用“_”作为查询前缀！请重新输入！')
