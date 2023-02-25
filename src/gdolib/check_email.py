import os, random
import requests, user_agent, json, uuid, re, mechanize
from user_agent import generate_user_agent

# -------------------------[CoDe BY GDØ]------------------------
# -------------------------[CoDe BY GDØ]------------------------
# -------------------------[CoDe BY GDØ]------------------------

class check_email:

    def gmail(email: str) -> str:
        url = 'https://android.clients.google.com/setup/checkavail'
        headers = {
            'Content-Length': '98',
            'Content-Type': 'text/plain; charset=UTF-8',
            'Host': 'android.clients.google.com',
            'Connection': 'Keep-Alive',
            'user-agent': 'GoogleLoginService/1.3(m0 JSS15J)', }
        data = json.dumps({
            'username': str(email),
            'version': '3',
            'firstName': 'GDO_0',
            'lastName': 'GDOTools'})
        res = requests.post(url, data=data, headers=headers)
        if res.json()['status'] == 'SUCCESS':
            return {'status': 'Success', 'email': True}

        else:
            return {'status': 'error', 'email': False}

    def hotmail(email: str) -> str:
        url = "https://odc.officeapps.live.com/odc/emailhrd/getidp?hm=0&emailAddress=" + str(email) + "&_=1604288577990"
        headers = {
            "Accept": "*/*",
            "Content-Type": "application/x-www-form-urlencoded",
            "User-Agent": str(generate_user_agent()),
            "Connection": "close",
            "Host": "odc.officeapps.live.com",
            "Accept-Encoding": "gzip, deflate",
            "Referer": "https://odc.officeapps.live.com/odc/v2.0/hrd?rs=ar-sa&Ver=16&app=23&p=6&hm=0",
            "Accept-Language": "ar,en-US;q=0.9,en;q=0.8",
            "canary": "BCfKjqOECfmW44Z3Ca7vFrgp9j3V8GQHKh6NnEESrE13SEY/4jyexVZ4Yi8CjAmQtj2uPFZjPt1jjwp8O5MXQ5GelodAON4Jo11skSWTQRzz6nMVUHqa8t1kVadhXFeFk5AsckPKs8yXhk7k4Sdb5jUSpgjQtU2Ydt1wgf3HEwB1VQr+iShzRD0R6C0zHNwmHRnIatjfk0QJpOFHl2zH3uGtioL4SSusd2CO8l4XcCClKmeHJS8U3uyIMJQ8L+tb:2:3c",
            "uaid": "d06e1498e7ed4def9078bd46883f187b",
            "Cookie": "xid=d491738a-bb3d-4bd6-b6ba-f22f032d6e67&&RD00155D6F8815&354"}
        res = requests.post(url, data="", headers=headers).text
        if ("Neither") in res:
            return {'status': 'Success', 'email': True}

        else:
            return {'status': 'error', 'email': False}

    def outlook(email: str) -> str:
        url = "https://odc.officeapps.live.com/odc/emailhrd/getidp?hm=0&emailAddress=" + str(email) + "&_=1604288577990"
        headers = {
            "Accept": "*/*",
            "Content-Type": "application/x-www-form-urlencoded",
            "User-Agent": str(generate_user_agent()),
            "Connection": "close",
            "Host": "odc.officeapps.live.com",
            "Accept-Encoding": "gzip, deflate",
            "Referer": "https://odc.officeapps.live.com/odc/v2.0/hrd?rs=ar-sa&Ver=16&app=23&p=6&hm=0",
            "Accept-Language": "ar,en-US;q=0.9,en;q=0.8",
            "canary": "BCfKjqOECfmW44Z3Ca7vFrgp9j3V8GQHKh6NnEESrE13SEY/4jyexVZ4Yi8CjAmQtj2uPFZjPt1jjwp8O5MXQ5GelodAON4Jo11skSWTQRzz6nMVUHqa8t1kVadhXFeFk5AsckPKs8yXhk7k4Sdb5jUSpgjQtU2Ydt1wgf3HEwB1VQr+iShzRD0R6C0zHNwmHRnIatjfk0QJpOFHl2zH3uGtioL4SSusd2CO8l4XcCClKmeHJS8U3uyIMJQ8L+tb:2:3c",
            "uaid": "d06e1498e7ed4def9078bd46883f187b",
            "Cookie": "xid=d491738a-bb3d-4bd6-b6ba-f22f032d6e67&&RD00155D6F8815&354"}
        res = requests.post(url, data="", headers=headers).text
        if ("Neither") in res:
            return {'status': 'Success', 'email': True}

        else:
            return {'status': 'error', 'email': False}

    def mailru(email: str) -> str:
        url = "https://account.mail.ru/api/v1/user/exists"
        headers = {"User-Agent": str(generate_user_agent())}
        data = {'email': str(email)}
        res = requests.post(url, data=data, headers=headers)
        if res.json()['body']['exists'] == False:
            return {'status': 'Success', 'email': True}

        else:
            return {'status': 'error', 'email': False}

    def yahoo(email: str) -> str:
        email = str(email)
        email = email.split('@')[0]
        res = requests.get('https://login.yahoo.com/').text
        crumb = res.split('crumb" value="')[1].split('"')[0]
        acumb = res.split('acrumb" value="')[1].split('"')[0]
        url = "https://login.yahoo.com/account/module/create?validateField=userId"
        headers =  {'accept':'*/*',
		'accept-encoding':'gzip, deflate, br',
		'accept-language':'ar,en-US;q=0.9,en;q=0.8',
		'content-length':'8005',
		'content-type':'application/x-www-form-urlencoded; charset=UTF-8',
		'cookie':'PH=l=en-JO; cmp=t=1649967133&j=0; OTH=v=1&d=eyJraWQiOiIwMTY0MGY5MDNhMjRlMWMxZjA5N2ViZGEyZDA5YjE5NmM5ZGUzZWQ5IiwiYWxnIjoiUlMyNTYifQ.eyJjdSI6eyJndWlkIjoiUVM0Uk1FNVM1NTdEQlg2TTdOVFFRUTdHTlUiLCJwZXJzaXN0ZW50Ijp0cnVlLCJzaWQiOiJERWI2ZmRZN1BwQVUifX0.qS4v0LTtpXd4vhydwS6vpL9MANSOMDMZEYWffFSxshbnuwRCzeUzJbwM2p7nPMwYV96yEFCkM0B8Lo--XHoBQvQszdP_-M-HuzLttwUwkzkqDpZyo6Lzm5bAnbh6B3P-kTcNBHlCoSg9N-SExB0OrppOO2gONQqoR25mLHXhhnY; A1=d=AQABBB409GECEJnQ0nfMctyiH6Cq-PmrCeMFEgEABgLQWWIzY2Jcb2UB_eMBAAcIHjT0YfmrCeMID9DBO57ZmNoDBDj1XbSi9wkBBwoB3w&S=AQAAAjb2LJb55ay2ij3P5hQhTG8; A3=d=AQABBB409GECEJnQ0nfMctyiH6Cq-PmrCeMFEgEABgLQWWIzY2Jcb2UB_eMBAAcIHjT0YfmrCeMID9DBO57ZmNoDBDj1XbSi9wkBBwoB3w&S=AQAAAjb2LJb55ay2ij3P5hQhTG8; B=e62dbv5gv8d0u&b=4&d=6ZQJIRhtYFgpJyr7JyZD&s=1a&i=0ME7ntmY2gMEOPVdtKL3; GUC=AQEABgJiWdBjM0Id8gRd; FS=v=1&d=Sloq608oHDIvM2JuXcI4Gn9LK3_mICxQM3wH9IpTUuhixjO_VCNu~A; F=d=Gd70Kyk9vQ--; A1S=d=AQABBB409GECEJnQ0nfMctyiH6Cq-PmrCeMFEgEABgLQWWIzY2Jcb2UB_eMBAAcIHjT0YfmrCeMID9DBO57ZmNoDBDj1XbSi9wkBBwoB3w&S=AQAAAjb2LJb55ay2ij3P5hQhTG8&j=WORLD; AS=v=1&s=eroBY4Ev&d=A6303cef0|ZEYbW7L.2Srumj5bsSgNr6pHG9L7ftgk69kaOYpxhyconhETRftIvklmxO04_jnsTCAHWevCxf54nzHLDeXQYBVGkIH2LDMksIJ0iyvJP5i3gtL6j3zmgAXcFB16OfkxHB8pdR6xTYrWMAjw83DZOVDP01nUIgsVN67BRTBeAVyFm2TcM7zOAU4p3BRMjIxZnbs3W5up1zdPk6xoLrSutyCuIIW39lD9bf5jT2QM184mqYK_LEn4WZwqHIV1TyUJdBGp4.wcLzYAnTCWuHb2sYCfOw_GIQa9yYXkpf0lBSB._KpZHInUKarEmJILgtr.Qc4psV4H4aqUmftoG51WPnfBVJ4p.WM6QN8EjxFbz3ElX85AuY9KBfkBCfLMmd9abH1ad6Z7SKRRgddMzWqztRGoiKjvy9Yr_g47x5xy8TriwECyywopXIJl3BlLLR4kOW4vY21qxqW5BkxJtCAewQ0ty5n1iehZ6wg4cojgbKFlFwHyEe9Wp08oedMG94MHkxUtcW7YQbq_jm_Nw8FxhaTK65Ft3cwmIq_CE6qd9ZMgLL9B4NJtFqwBuXL3O848MSA2_b2a5khKLuKLGGHkMNpgl1OCxnwqhWQzlQa8KyJ5lJ7Wswp38Vvw95oAEGJSYQeb.uXvxZ61Oo6jTrAFoHUtMaD0Kh9QmBZjsAjoZ9OB5IxP9NIsY_WRLaB60fLMnTKx5YtaRUEImyx1N58o5OtBD65RlX8WbzwfhykQh61E90SPqBNMVcv3KUyAf4QQ2uDxUjQO0RR347MbnGbJ00YXrwnySDF3JC4LN8jEy0VtKkFaOSeGsKgJaBGSRzuv383Wcu1pEs0JWlBNBN7JWVdRJc9PJ1QDQH972XWuOZKTbA--~A',
		'origin':'https://login.yahoo.com',
		'referer':'https://login.yahoo.com/account/create?.intl=ca&.lang=en-CA&src=ym&activity=mail-direct&pspid=159600001&.done=https%3A%2F%2Fmail.yahoo.com%2Fd%3F.intl%3Dca%26.lang%3Den-CA&specId=yidregsimplified&done=https%3A%2F%2Fmail.yahoo.com%2Fd%3F.intl%3Dca%26.lang%3Den-CA',
		'sec-ch-ua':'".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
		'sec-ch-ua-mobile':'?0',
		'sec-ch-ua-platform':'"Windows"',
		'sec-fetch-dest':'empty',
		'sec-fetch-mode':'cors',
		'sec-fetch-site':'same-origin',
		'user-agent':str(generate_user_agent),
		'x-requested-with':'XMLHttpRequest',}
        data = {'validateField':'userId',
		'browser-fp-data':'{"language":"ar","colorDepth":24,"deviceMemory":4,"pixelRatio":1,"hardwareConcurrency":4,"timezoneOffset":-180,"timezone":"Asia/Riyadh","sessionStorage":1,"localStorage":1,"indexedDb":1,"openDatabase":1,"cpuClass":"unknown","platform":"Win32","doNotTrack":"unknown","plugins":{"count":5,"hash":"2c14024bf8584c3f7f63f24ea490e812"},"canvas":"canvas winding:yes~canvas","webgl":1,"webglVendorAndRenderer":"Google Inc. (Intel)~ANGLE (Intel, Intel(R) HD Graphics 4600 Direct3D11 vs_5_0 ps_5_0, D3D11)","adBlock":0,"hasLiedLanguages":0,"hasLiedResolution":0,"hasLiedOs":0,"hasLiedBrowser":0,"touchSupport":{"points":0,"event":0,"start":0},"fonts":{"count":48,"hash":"62d5bbf307ed9e959ad3d5ad6ccd3951"},"audio":"124.04347527516074","resolution":{"w":"1366","h":"768"},"availableResolution":{"w":"728","h":"1366"},"ts":{"serve":1661107587619,"render":1661107585090}}',
		'specId':'yidregsimplified','cacheStored':'',
		'crumb':str(crumb),'acrumb':str(acumb),
		'done':'https://mail.yahoo.com/d?.intl=ca&.lang=en-CA','googleIdToken':'',
		'authCode':'','attrSetIndex':'0','multiDomain':'',
		'tos0':'oath_freereg|xa|en-JO',
		'firstName':'GDO','lastName':'Tools',
		'userid-domain':'yahoo','userId':str(email),'password':'@GDOTools','birthYear':'','signup:':'',}
        resp = requests.post(url,headers=headers,data=data).text
        if "userId" in resp:return {'status': 'error', 'email': False}
        else:return {'status': 'Success', 'email': True}

    def aol(email: str) -> str:
        email = str(email)
        email = email.split('@')[0]
        url = 'https://login.aol.com/account/module/create?validateField=yid'
        headers = {
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
            'content-length': '18023',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'cookie': 'A1=d=AQABBGBeeWICEBR5epkCARe46kFw6ViOQ_AFEgEBAQGvemKDYgAAAAAA_eMAAA&S=AQAAAp3JQ6CyW2qRJcMsBzHGVvU; A3=d=AQABBGBeeWICEBR5epkCARe46kFw6ViOQ_AFEgEBAQGvemKDYgAAAAAA_eMAAA&S=AQAAAp3JQ6CyW2qRJcMsBzHGVvU; A1S=d=AQABBGBeeWICEBR5epkCARe46kFw6ViOQ_AFEgEBAQGvemKDYgAAAAAA_eMAAA&S=AQAAAp3JQ6CyW2qRJcMsBzHGVvU&j=WORLD; GUC=AQEBAQFieq9ig0IfzwR5; rxx=2bkczirpbih.2q6rpdsb&v=1; AS=v=1&s=JYNxcuAB&d=A627ab0eb|5n7NNlX.2Tqja_1ZC6lprFtAflUVdSswdgLRxIPQFqE9yPLfNXNQGllEgjcaz2MSyNOF0HA9XirM0hGhPu6hRyuyv6NS5uzzU2MRaRQf.1YBAQ8FypG1m_xQXAtuSInDrAwsMOptRW4zfkTgorDT4mTAhLg6RTvtz.RlGfCdtaQ4BBDOfp7jAYaYk.VJlzoY75HEqitjywIRo5cxa2LE6o5SUyxNOi7S_X3k_SPXAVdV.Pie3M8oZSqscWmfYaFDf586bpqdXlRbtd9NfqqCnsm39F_qAPBPvWHWieu4eZ4Guhk.MRMp7Daew_rlTFks0DO5LZYOCyO3RrW3LO3QaHRTvTBTaXP4RsdfXTOXPejofBwqmWSbUlACa4xD1EKndabLWQmEoy1AEUMoSbwgJMxI_j7xuQHqBgjCanjm8A6GOXCZKM44DjwdQdaMnR6GrHEfBfKds9z.7gjHKBoZ2jkWj7Hk7hPMzDGRBkqU.TWCGZRumYVYV8blYxEIS.H9qySKbh3SBBI8MIgkMqBNciHX3QnqQrc_CuA1uBOx7GHKgnI7pemzJnVMGwyYsAGU4UQRwAVGcDrHZH76hH..grS5ceMIZJSVt6nAcvYiTMElRUgLqk4RORTkyF9XbLMB9_U2I_ZVaERHP3X7j7f77RdHq2UlR68eZ_G5RY6ZrgfwFvy1Ptrd9WdFYaab69sfGI8SVXk2dtdR5udVorhaBdtoNxJ5PIy0Ue_qMPhxcsw4VzSExlyyNSaF0SFoSH5fK8kFVQ0IIBIWO_d0ik6d9azkHxffaa7MJpjYfsHmHpERb2hEkyr7uJzTQTf0H8NBfQdcQD8P9ja69DD7Ahdacge_a9D4QGaLgMvQi481iZMNd5Dy46uoeco5T.slB_psK4WxbBJgP7p6hgyb_wkDzvUhd_3ym5sQe1cBySzHgXSMyzsEurBQZKaMHv9302Cj6iNUZ2jjtMkAVdsh~A|B627ab2cd|x0gk8rH.2TpbbztShpG57nIccQOKaEGxqulmFIimnSbIetxQBy35pQAyeLh0g4kZXfUcZ8gS0KtJhnntdd169n74ag_k2YnldeTcAixJ8Oe1U9eEwr4TEKjAn5ew0omTSMojewjLD76vbkEv.zZYyCrRxd5vfs3vmQxAV_f6Y0sOWtsUeIu3OvEzUyK.1trUfGvmn7d3hvyFbF.OTRqd._NMsXRn2QVZ.T5RjYrog5983WaKy_9x1YPoBUNH4QPKi0zZBP9iMgx8Tlsrxhn4zs9Zyr3IiqPFbxjEuBh4G78xoEv7z6_PrYOwB37XEbTdaaeXyPFsSGhZf4bQovQopXVbHe.9nbDzDYkfdXD6d9wmf6jvSEex9a9eEu8Z.14NuIQZJcy_c6_PP5H0eXQAWO6LOsW7CtqdeDlLd74M9jUU5yseMxzkN0HSawwGQ.HU.XZFjoOjowHAX1bsDGRuWObSamI1LdvanTCHZZ6TICNO8lT9GjBWDYK.h6.ojgs.tCAAXzYPMf6UOHvrjtlwaCmODGFlndZMASPIp9IyDMRT9gC52spPRpBQJZOpJUt8YDEY6zKB5r2SsHH.ssGgtrnS3tlCg6rx8k.wEakhoSpj2ezEMO4IAODDXV0paODum6McXkpaxliXReHLYdtXIM9t5smt_PeP92ttd69oDB.zVFsEms7tdF1SQWbmUF.4plddWEwfn6FNVdj7TpJvpTAxjaso_xliccUrnkpUGvH1IUv11w4Pok0k92JLzk2AXJ5Ak_5R51n2X_Oc88nJKif3EZK7ly7lgMXtWaURJx2Zj4.88SxdyHNtRzmHFvkAwmxtDmjgj5OCF7m38h.4TZuT3.D3c7uhs0XPEZARricsnApvw1dUBRY0E3vvSU.S_4zHPhWn7BHQz1nySvei.tQaogRmeBpFHvzS3QNKSWksRu1w7T8O2RDtnr7pzs5VzPifkiXOKw--~A',
            'origin': 'https://login.aol.com',
            'referer': 'https://login.aol.com/account/module/create?validateField=yid%5C',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': str(generate_user_agent()),
            'x-requested-with': 'XMLHttpRequest', }
        data = {
            'browser-fp-data': '{"language":"ar","colorDepth":24,"deviceMemory":4,"pixelRatio":1,"hardwareConcurrency":4,"timezoneOffset":-180,"timezone":"Asia/Riyadh","sessionStorage":1,"localStorage":1,"indexedDb":1,"openDatabase":1,"cpuClass":"unknown","platform":"Win32","doNotTrack":"unknown","plugins":{"count":5,"hash":"2c14024bf8584c3f7f63f24ea490e812"},"canvas":"canvas winding:yes~canvas","webgl":1,"webglVendorAndRenderer":"Google Inc. (Intel)~ANGLE (Intel, Intel(R) HD Graphics 4600 Direct3D11 vs_5_0 ps_5_0, D3D11)","adBlock":0,"hasLiedLanguages":0,"hasLiedResolution":0,"hasLiedOs":0,"hasLiedBrowser":0,"touchSupport":{"points":0,"event":0,"start":0},"fonts":{"count":48,"hash":"62d5bbf307ed9e959ad3d5ad6ccd3951"},"audio":"124.04347527516074","resolution":{"w":"1366","h":"768"},"availableResolution":{"w":"728","h":"1366"},"ts":{"serve":1652124464147,"render":1652124464497}}',
            'specId': 'yidReg',
            'crumb': 'YLO.LxuwQbD',
            'acrumb': 'JYNxcuAB',
            'done': 'https://www.aol.com',
            'tos0': 'oath_freereg|us|en-US',
            'yid': str(email),
            'password': '@GDOTools',
            'shortCountryCode': 'US'}
        res = requests.post(url, headers=headers, data=data).text
        if ('"yid"') in res:
            return {'status': 'error', 'email': False}

        else:
            return {'status': 'Success', 'email': True}

    
    def instagram(email: str) -> str:
    	url = 'https://www.instagram.com/accounts/web_create_ajax/attempt/'
    	headers = {'accept': '*/*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'ar,en-US;q=0.9,en;q=0.8,ar-SA;q=0.7',
                'content-length': '61',
                'content-type': 'application/x-www-form-urlencoded',
                'cookie': 'ig_cb=2; ig_did=BB52B198-B05A-424E-BA07-B15F3D4C3893; mid=YAlcaQALAAHzmX6nvD8dWMRVYFCO; shbid=15012; rur=PRN; shbts=1612894029.7666144; csrftoken=CPKow8myeXW9AuB3Lny0wNxx0EzoDQoI',
                'origin': 'https://www.instagram.com',
                'referer': 'https://www.instagram.com/accounts/emailsignup/',
                'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
                'sec-ch-ua-mobile': '?0',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': str(generate_user_agent()),
                'x-csrftoken': 'CPKow8myeXW9AuB3Lny0wNxx0EzoDQoI',
                'x-ig-app-id': '936619743392459',
                'x-ig-www-claim': 'hmac.AR0Plwj5om112fwzrrYnMNjMLPnyWfFFq1tG7MCcMv5_vN9M',
                'x-instagram-ajax': '72bda6b1d047',
                'x-requested-with': 'XMLHttpRequest'} 
    	data = {'email' : str(email),
                'username': str(email),
                'first_name': 'GDO',
                'opt_into_one_tap': 'false'}
    	req = requests.post(url, headers=headers, data=data).text
    	if "Another account is using the same email." in req:
    		return {'status':'Success','email':True}
    	else:
    		return {'status':'error','email':False}

    
    def insta(email: str) -> str:
    	url = "https://i.instagram.com/api/v1/users/lookup/"
    	headers = {
			        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
			        'Host': 'i.instagram.com',
			        'Connection': 'Keep-Alive',
			        'User-Agent': 'Instagram 6.12.1 Android (25/7.1.2; 160dpi; 383x680; LENOVO/Android-x86; 4242ED1; x86_64; android_x86_64; en_US)',
			        'Accept-Language': 'en-US',
			        'X-IG-Connection-Type': 'WIFI',
			        'X-IG-Capabilities': 'AQ==',}
    	data = 'signed_body=acd10e3607b478b845184ff7af8d796aec14425d5f00276567ea0876b1ff2630.%7B%22_csrftoken%22%3A%22rZj5Y3kci0OWbO8AMUi0mWwcBnUgnJDY%22%2C%22q%22%3A%22'+str(email)+'%22%2C%22_uid%22%3A%226758469524%22%2C%22guid%22%3A%22a475d908-a663-4895-ac60-c0ab0853d6df%22%2C%22device_id%22%3A%22android-1a9898fad127fa2a%22%2C%22_uuid%22%3A%22a475d908-a663-4895-ac60-c0ab0853d6df%22%7D&ig_sig_key_version=4'
    	res = requests.post(url, headers=headers, data=data).text
    	if '"status":"ok"' in res:
    		return {'status':'Success','email':True}
    	else:
    		return {'status':'error','email':False}


    def facebook(email: str) -> str:
        e = 'https://mbasic.facebook.com/login/identify/?ctx=recover&search_attempts=1&ars=facebook_login&alternate_search=1'
        e1 = 'https://mbasic.facebook.com/login/identify/?ctx=recover&c=%2Flogin%2F&search_attempts=1&ars=facebook_login&alternate_search=1&show_friend_search_filtered_list=0&birth_month_search=0&city_search=0'
        br = mechanize.Browser()
        br.set_handle_robots(False)
        br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
        br.addheaders = [('User-agent','Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2729.25 Safari/537.36')]
        br.open("https://mbasic.facebook.com/login/identify/?ctx=recover&search_attempts=0&ars=facebook_login&alternate_search=0&toggle_search_mode=1") 
        br._factory.is_html= True
        br.select_form(nr=0)
        br.form["email"] = email
        br.submit()
        res = br.geturl()
        if e in res or e1 in res:
            return {'status': 'error', 'email': False}

        else:
            return {'status': 'Success', 'email': True}

    def twiter(email: str) -> str:
        v = 'https://twitter.com/i/flow/password_reset?input_flow_data=%7B%22requested_variant%22%3A%22eyJwbGF0Zm9ybSI6IlJ3ZWIifQ%3D%3D%22%7D'
        head = {'user-agent': str(generate_user_agent())}
        req = requests.post(v, headers=head).cookies.get_dict()
        per = req['personalization_id']
        g_id = req['guest_id_marketing']
        g_ads = req['guest_id_ads']
        g_i = req['guest_id']
        url = f"https://twitter.com/i/api/i/users/email_available.json?email={email}"
        headers = {'accept': '*/*',
                   'accept-encoding': 'gzip, deflate, br',
                   'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
                   'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
                   'cookie': f'personalization_id={per}; guest_id_marketing={g_id}; guest_id_ads={g_ads}; guest_id={g_i}; ct0=49382582f7d8154eae4e5a0b51265894; _sl=1; gt=1542877580168249344; external_referer=padhuUp37zjgzgv1mFWxJ12Ozwit7owX|0|8e8t2xd8A2w%3D; _twitter_sess=BAh7CSIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNo%250ASGFzaHsABjoKQHVzZWR7ADoPY3JlYXRlZF9hdGwrCEkAKbqBAToMY3NyZl9p%250AZCIlMWI5MDZhMjgzYjJhY2JhNjIzZjUzNGQyNmE0MmI4NDU6B2lkIiVhOGNj%250AM2JiNGFhMjZlYjdhYjI2ZGQ1YmE4ZDZiZDBiZg%253D%253D--9eb344c9082b904ac770ed1170465202fad6cb18; att=1-AkCxZlbAOfhccMy18SL99HQSEWsxiWxOhcek7sAY; _ga=GA1.2.1018461544.1656685665; _gid=GA1.2.879109925.1656685665',
                   'referer': 'https://twitter.com/i/flow/signup',
                   'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
                   'sec-ch-ua-mobile': '?0',
                   'sec-ch-ua-platform': '"Windows"',
                   'sec-fetch-dest': 'empty',
                   'sec-fetch-mode': 'cors',
                   'sec-fetch-site': 'same-origin',
                   'user-agent': str(generate_user_agent()),
                   'x-csrf-token': '49382582f7d8154eae4e5a0b51265894',
                   'x-guest-token': '1542877580168249344',
                   'x-twitter-active-user': 'yes',
                   'x-twitter-client-language': 'en', }
        data = {'email': str(email)}
        res = requests.get(url, headers=headers, data=data).json()
        if res['taken'] == True:
            return {'status': 'Success', 'email': True}

        else:
            return {'status': 'error', 'email': False}

    def tik(email: str) -> str:
        url = "https://api2-t2.musical.ly/aweme/v1/passport/find-password-via-email/?version_code=7.6.0&language=ar&app_name=musical_ly&vid=43647C38-9344-40A3-AD8E-29F6C7B987E4&app_version=7.6.0&is_my_cn=0&channel=App%20Store&mcc_mnc=&device_id=6999590732555060741&tz_offset=10800&account_region=&sys_region=SA&aid=1233&screen_width=1242&openudid=a0594f8115e0a1a51e1a31490aeef9afc2409ff4&os_api=18&ac=WIFI&os_version=12.5.4&app_language=ar&tz_name=Asia/Riyadh&device_platform=iphone&build_number=76001&iid=7021194671750481669&device_type=iPhone7,1&idfa=20DB6089-D1C6-49EF-8943-9C310C8F1B5D&mas=002ed4fcfe1207217efade4142d0b05e0c845e118f07206205d6a8&as=a11664d78a2e110bd08018&ts=16347494182"
        headers = {
            'Host': 'api2-t2.musical.ly',
            'Cookie': 'store-country-code=sa; store-idc=alisg; install_id=7021194671750481669; odin_tt=7b67a77e780e497b1c89d483072f567580c860fe622a9ad519c8af998a287f424ed5f97297928981fa70ca6e8cb2648ebc46af23c9c9588a540567c77f877d307588080b16d8b92d3c3f875da9cd2291; ttreq=1$ee9fd401f276e956ba82d3ffd7392ffa6829472d',
            'Accept': '*/*',
            'Content-Type': 'application/x-www-form-urlencoded',
            'User-Agent': str(generate_user_agent()),
            'Accept-Language': 'ar-SA;q=1',
            'Content-Length': '25',
            'Connection': 'close'}
        data = {"email": email}
        req = requests.post(url, headers=headers, data=data)
        if "Sent successfully" in req.text:
            return {'status': 'Success', 'email': True}

        else:
            return {'status': 'error', 'email': False}
    
    
    def tiktok(email: str) -> str:
        url = "https://api16-normal-c-alisg.tiktokv.com/passport/email/send_code/?residence=AE&device_id=6923575826752275974&os_version=14.3&app_id=1233&iid=6951746276598204161&app_name=musical_ly&pass-route=1&vendor_id=EF3C1478-2AFC-4B8E-8030-C608120AECF9&locale=ar&pass-region=1&ac=WIFI&sys_region=US&ssmix=a&version_code=17.2.0&vid=EF3C1478-2AFC-4B8E-8030-C608120AECF9&channel=App%20Store&op_region=AE&os_api=18&idfa=00000000-0000-0000-0000-000000000000&install_id=6951746276598204161&idfv=EF3C1478-2AFC-4B8E-8030-C608120AECF9&device_platform=iphone&device_type=iPhone9%2C4&openudid=3ce553bec09070081e5a698d3a14a988f3642ac4&account_region=&tz_name=Asia%2FDubai&tz_offset=14400&app_language=ar&carrier_region=AE&current_region=AE&aid=1233&mcc_mnc=42402&screen_width=1242&uoo=1&content_language=&language=ar&cdid=FBF67CFE-39E1-4556-A3EB-624A20A434E1&build_number=172025&app_version=17.2.0&resolution=1242%2A2208"
        headers = {
       'Host':'api16-normal-c-alisg.tiktokv.com', 
	   'Connection':'close', 
	   'Content-Length':'76', 
	   'Cookie':'sessionid=b0b2ed352b9394eefc29754dfe80926c', 
       'x-Tt-Token':'2c593820065f9a47b9bf51281eda9604-1.0.0', 
	   'Content-Type':'application/x-www-form-urlencoded', 
	   'x-tt-passport-csrf-token':'b0b2ed352b9394eefc29754dfe80926c', 
       'sdk-version':'2', 
	   'passport-sdk-version':'5.12.1'}
        data = {
        'account_sdk_source':'app', 
	    'email':str(email), 
	    'mix_mode':'1', 
	    'type':'31'}
        req = requests.post(url, headers=headers, data=data)
        if '"message":"success"' in req.text:
            return {'status': 'Success', 'email': True}

        else:
            return {'status': 'error', 'email': False}



    def epicgames(email: str) -> str:
        url = "https://accounts.launcher-website-prod07.ol.epicgames.com/launcher/sendFriendRequest"
        data = f"inputEmail={email}&tab=connections"
        headers = {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'fr-FR,fr;q=0.9',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'DNT': '1',
            'Host': 'accounts.launcher-website-prod07.ol.epicgames.com',
            'Origin': 'https://accounts.launcher-website-prod07.ol.epicgames.com',
            'Pragma': 'no-cache',
            'Referer': 'https://accounts.launcher-website-prod07.ol.epicgames.com/launcher/addFriends',
            'sec-ch-ua-mobile': '?0',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': str(generate_user_agent()), }
        req = requests.post(url, headers=headers, data=data)
        if ("fieldValidationError") in req.cookies:
            return {'status': 'Success', 'email': True}

        else:
            return {'status': 'error', 'email': False}

    def godaddy(email: str) -> str:
        url = f"https://sso.godaddy.com/v1/api/idp/recovery/password/?username={email}&app=dashboard.api"
        headers = {
            'User-Agent': str(generate_user_agent()),
            'Pragma': 'no-cache',
            'Accept': '*/*', }
        req = requests.post(url, headers=headers)
        if ("account_email") in req.cookies:
            return {'status': 'Success', 'email': True}

        else:
            return {'status': 'error', 'email': False}

    def gap(email: str) -> str:
        url = "https://secure-www.gap.com/my-account/xapi/v2/create-account/verify-email"
        data = {'emailAddress': f'{email}'}
        headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.5',
            'Connection': 'keep-alive',
            'Host': 'secure-www.gap.com',
            'Origin': 'https://secure-www.gap.com',
            'Referer': 'https://secure-www.gap.com/my-account/sign-in',
            'User-Agent': str(generate_user_agent()), }
        req = requests.post(url, headers=headers, data=data)
        if ("isEmailRegistered:false") in req.cookies:
            return {'status': 'Success', 'email': True}

        else:
            return {'status': 'error', 'email': False}

    def noon(email: str) -> str:
        url = "https://login.noon.com/_svc/customer-v1/auth/reset_password"
        headers = {
            'User-Agent': str(generate_user_agent()),
            'Pragma': 'no-cache',
            'Accept': '*/*',
            'origin': 'https://login.noon.com',
            'referer': 'https://login.noon.com/uae-en/reset', }
        data = {'email': str(email), }
        req = requests.post(url, headers=headers, data=data)
        if ("ok") in req.cookies:
            return {'status': 'Success', 'email': True}

        else:
            return {'status': 'error', 'email': False}

    def sendgrid(email: str) -> str:
        url = f"https://api.sendgrid.com/v3/public/signup/username/{email}"
        headers = {
            'User-Agent': str(generate_user_agent()),
            'Pragma': 'no-cache',
            'Accept': '*/*', }
        req = requests.post(url, headers=headers)
        if ("Contains:204") in req.cookies:
            return {'status': 'Success', 'email': True}

        else:
            return {'status': 'error', 'email': False}
        

class more:
    
    
    def check_proxy(proxy: str) -> str:
        try:
            proxies = {'https': f'http://{proxy}'}
            res = requests.get('https://ipinfo.io/', proxies=proxies).json()
            country = res["country"]
            city = res["city"]
            return {'status': 'Success', 'country': str(country), 'city': str(city), 'proxy': True}
        except:
            return {'status': 'error', 'proxy': False}
            
    
    def check_card(cc: str, mm: str, yy: str, cvc: str) -> str:
        card = str(f"{cc}|{mm}|{yy}|{cvc}")
        url = "https://checker.visatk.com/ccn1/alien07.php"
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
            'Connection': 'keep-alive',
            'Content-Length': '57',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Cookie': '__gads=ID=42ac6c196f03a9b4-2279e5ef3fcd001d:T=1645035753:RT=1645035753:S=ALNI_MZL7kDSE4lwgNP0MHtSLy_PyyPW3w; PHPSESSID=tdsh3u2p5niangsvip3gvvbc12',
            'Host': 'checker.visatk.com',
            'Origin': 'https://checker.visatk.com',
            'Referer': 'https://checker.visatk.com/ccn1/',
            'sec-ch-ua': '"Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': str(generate_user_agent)}
        data = {
            'ajax': '1',
            'do': 'check',
            'cclist': card}
        req = requests.post(url, headers=headers, data=data).text
        if '"error":0' in req:
            many = req.split("[Charge :<font color=green>")[1].split("</font>] [BIN:")[0]
            message = {'status': 'Success', 'many': str(many), 'Card': str(card)}
            return message

        else:
            return {'status':'error'}


# -------------------------[CoDe BY GDØ]------------------------
# -------------------------[CoDe BY GDØ]------------------------
# -------------------------[CoDe BY GDØ]------------------------