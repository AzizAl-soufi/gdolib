import re , hashlib , requests , uuid , json , urllib , random , string , time , instaloader
from user_agent import generate_user_agent

class info_IG:


    def followers(user: str) -> str:
        s = instaloader.Instaloader()
        info = instaloader.Profile.from_username(s.context, user)
        try:
            followers = info.followers()
            return str(followers)

        except:
            return False

    def following(user: str) -> str:
        s = instaloader.Instaloader()
        profile = instaloader.Profile.from_username(s.context, user)
        try:
            following = info.followees()
            return str(following)

        except:
            return False

    def posts(user: str) -> str:
        url = f'https://www.instagram.com/{user}/?__a=1'
        headers = {
            "content-type": "application/json",
            "User-agent": str(generate_user_agent())}
        res = requests.get(url=url, headers=headers).json()
        try:
            posts = res['graphql']['user']['edge_owner_to_timeline_media']['count']
            return posts

        except:
            return False

    def id(user: str) -> str:
    	url = "https://i.instagram.com/api/v1/users/lookup/"
    	headers = {'Host': 'i.instagram.com',
                'Connection':'keep-alive',
                'X-IG-Connection-Type': 'WIFI',
                'X-IG-Capabilities': '3Ro=',
                'Accept-Language': 'en-US',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'User-Agent': 'Instagram 9.7.0 Android (28/9; 420dpi; 1080x2131; samsung; SM-A505F; a50; exynos9610; en_US)',
                'Accept-Encoding': 'gzip, deflatet'}
    	data = 'signed_body=acd10e3607b478b845184ff7af8d796aec14425d5f00276567ea0876b1ff2630.%7B%22_csrftoken%22%3A%22rZj5Y3kci0OWbO8AMUi0mWwcBnUgnJDY%22%2C%22q%22%3A%22'+str(user)+'%22%2C%22_uid%22%3A%226758469524%22%2C%22guid%22%3A%22a475d908-a663-4895-ac60-c0ab0853d6df%22%2C%22device_id%22%3A%22android-1a9898fad127fa2a%22%2C%22_uuid%22%3A%22a475d908-a663-4895-ac60-c0ab0853d6df%22%7D&ig_sig_key_version=4' ;      	res = requests.post(url,headers=headers,data=data).json()
    	try:
    		id = res['user']['pk']
    		return id
    	
    	except KeyError:
    		return False

    def name(user: str) -> str:
    	url = "https://i.instagram.com/api/v1/users/lookup/"
    	headers = {'Host': 'i.instagram.com',
                'Connection':'keep-alive',
                'X-IG-Connection-Type': 'WIFI',
                'X-IG-Capabilities': '3Ro=',
                'Accept-Language': 'en-US',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'User-Agent': 'Instagram 9.7.0 Android (28/9; 420dpi; 1080x2131; samsung; SM-A505F; a50; exynos9610; en_US)',
                'Accept-Encoding': 'gzip, deflatet'}
    	data = 'signed_body=acd10e3607b478b845184ff7af8d796aec14425d5f00276567ea0876b1ff2630.%7B%22_csrftoken%22%3A%22rZj5Y3kci0OWbO8AMUi0mWwcBnUgnJDY%22%2C%22q%22%3A%22'+str(user)+'%22%2C%22_uid%22%3A%226758469524%22%2C%22guid%22%3A%22a475d908-a663-4895-ac60-c0ab0853d6df%22%2C%22device_id%22%3A%22android-1a9898fad127fa2a%22%2C%22_uuid%22%3A%22a475d908-a663-4895-ac60-c0ab0853d6df%22%7D&ig_sig_key_version=4' ;      	res = requests.post(url,headers=headers,data=data).json()
    	try:
    		id = res['user']['full_name']
    		return id
    	
    	except KeyError:
    		return False
    
    
    def profile(user: str) -> str:
    	url = "https://i.instagram.com/api/v1/users/lookup/"
    	headers = {'Host': 'i.instagram.com',
                'Connection':'keep-alive',
                'X-IG-Connection-Type': 'WIFI',
                'X-IG-Capabilities': '3Ro=',
                'Accept-Language': 'en-US',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'User-Agent': 'Instagram 9.7.0 Android (28/9; 420dpi; 1080x2131; samsung; SM-A505F; a50; exynos9610; en_US)',
                'Accept-Encoding': 'gzip, deflatet'}
    	data = 'signed_body=acd10e3607b478b845184ff7af8d796aec14425d5f00276567ea0876b1ff2630.%7B%22_csrftoken%22%3A%22rZj5Y3kci0OWbO8AMUi0mWwcBnUgnJDY%22%2C%22q%22%3A%22'+str(user)+'%22%2C%22_uid%22%3A%226758469524%22%2C%22guid%22%3A%22a475d908-a663-4895-ac60-c0ab0853d6df%22%2C%22device_id%22%3A%22android-1a9898fad127fa2a%22%2C%22_uuid%22%3A%22a475d908-a663-4895-ac60-c0ab0853d6df%22%7D&ig_sig_key_version=4' ;      	res = requests.post(url,headers=headers,data=data).json()
    	try:
    		profile = res['user']['profile_pic_url']
    		return profile
    	
    	except KeyError:
    		return False

    def date(user: str) -> str:
        url = "https://i.instagram.com/api/v1/users/lookup/"
        headers = {'Host': 'i.instagram.com',
                'Connection':'keep-alive',
                'X-IG-Connection-Type': 'WIFI',
                'X-IG-Capabilities': '3Ro=',
                'Accept-Language': 'en-US',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'User-Agent': 'Instagram 9.7.0 Android (28/9; 420dpi; 1080x2131; samsung; SM-A505F; a50; exynos9610; en_US)',
                'Accept-Encoding': 'gzip, deflatet'}
        data = 'signed_body=acd10e3607b478b845184ff7af8d796aec14425d5f00276567ea0876b1ff2630.%7B%22_csrftoken%22%3A%22rZj5Y3kci0OWbO8AMUi0mWwcBnUgnJDY%22%2C%22q%22%3A%22'+user+'%22%2C%22_uid%22%3A%226758469524%22%2C%22guid%22%3A%22a475d908-a663-4895-ac60-c0ab0853d6df%22%2C%22device_id%22%3A%22android-1a9898fad127fa2a%22%2C%22_uuid%22%3A%22a475d908-a663-4895-ac60-c0ab0853d6df%22%7D&ig_sig_key_version=4' ;             res = requests.post(url,headers=headers,data=data).json()
        try:
        	pk = res['user']['pk']
        	get = "https://o7aa.pythonanywhere.com/?id="+str(pk)
        	head = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9,ar;q=0.8',
            'Connection': 'keep-alive',
            'Host': 'o7aa.pythonanywhere.com',
            'User-Agent': str(generate_user_agent())}
        	res = requests.get(get, headers=head).json()
        	return str(res["data"])

        except:
        	return False

    def bio(user: str) -> str:
        s = instaloader.Instaloader()
        info = instaloader.Profile.from_username(s.context, user)
        try:
            bio = info.biography
            return str(bio)

        except:
            return False

    def private(user: str) -> str:
        url = "https://i.instagram.com/api/v1/users/lookup/"
        headers = {'Host': 'i.instagram.com',
                'Connection':'keep-alive',
                'X-IG-Connection-Type': 'WIFI',
                'X-IG-Capabilities': '3Ro=',
                'Accept-Language': 'en-US',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'User-Agent': 'Instagram 9.7.0 Android (28/9; 420dpi; 1080x2131; samsung; SM-A505F; a50; exynos9610; en_US)',
                'Accept-Encoding': 'gzip, deflatet'}
        data = 'signed_body=acd10e3607b478b845184ff7af8d796aec14425d5f00276567ea0876b1ff2630.%7B%22_csrftoken%22%3A%22rZj5Y3kci0OWbO8AMUi0mWwcBnUgnJDY%22%2C%22q%22%3A%22'+user+'%22%2C%22_uid%22%3A%226758469524%22%2C%22guid%22%3A%22a475d908-a663-4895-ac60-c0ab0853d6df%22%2C%22device_id%22%3A%22android-1a9898fad127fa2a%22%2C%22_uuid%22%3A%22a475d908-a663-4895-ac60-c0ab0853d6df%22%7D&ig_sig_key_version=4' ;             res = requests.post(url,headers=headers,data=data).json()
        try:
            private = str(res['graphql']['user']['is_private'])
            return private

        except:
            return False

    
    def domin(user: str) -> str:
    	url = "https://i.instagram.com/api/v1/users/lookup/"
    	headers = {'Host': 'i.instagram.com',
                'Connection':'keep-alive',
                'X-IG-Connection-Type': 'WIFI',
                'X-IG-Capabilities': '3Ro=',
                'Accept-Language': 'en-US',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'User-Agent': 'Instagram 9.7.0 Android (28/9; 420dpi; 1080x2131; samsung; SM-A505F; a50; exynos9610; en_US)',
                'Accept-Encoding': 'gzip, deflatet'}
    	data = 'signed_body=acd10e3607b478b845184ff7af8d796aec14425d5f00276567ea0876b1ff2630.%7B%22_csrftoken%22%3A%22rZj5Y3kci0OWbO8AMUi0mWwcBnUgnJDY%22%2C%22q%22%3A%22'+str(user)+'%22%2C%22_uid%22%3A%226758469524%22%2C%22guid%22%3A%22a475d908-a663-4895-ac60-c0ab0853d6df%22%2C%22device_id%22%3A%22android-1a9898fad127fa2a%22%2C%22_uuid%22%3A%22a475d908-a663-4895-ac60-c0ab0853d6df%22%7D&ig_sig_key_version=4' ;      	res = requests.post(url,headers=headers,data=data).json()
    	try:
    		domin = res['obfuscated_email']
    		return domin
    	
    	except KeyError:
    		return False
    
    def Server_IG():
        vers = '136.0.0.34.124'
        virs = '208061712'
        de = {
            'one_plus_7': {'app_version': vers ,'android_version': '29' ,'android_release': '10.0' ,'dpi': '420dpi'
                           ,'resolution': '1080x2340' ,'manufacturer': 'OnePlus' ,'device': 'GM1903'
                           ,'model': 'OnePlus7' ,'cpu': 'qcom' ,'version_code': virs},
            'one_plus_3': {'app_version': vers ,'android_version': '28' ,'android_release': '9.0' ,'dpi': '420dpi'
                           ,'resolution': '1080x1920' ,'manufacturer': 'OnePlus' ,'device': 'ONEPLUS A3003'
                           ,'model': 'OnePlus3' ,'cpu': 'qcom' ,'version_code': virs},
            'samsung_galaxy_s7': {'app_version': vers ,'android_version': '26' ,'android_release': '8.0'
                                  ,'dpi': '640dpi' ,'resolution': '1440x2560' ,'manufacturer': 'samsung'
                                  ,'device': 'SM-G930F' ,'model': 'herolte' ,'cpu': 'samsungexynos8890'
                                  ,'version_code': virs},
            'huawei_mate_9_pro': {'app_version': vers ,'android_version': '24' ,'android_release': '7.0'
                                  ,'dpi': '640dpi' ,'resolution': '1440x2560' ,'manufacturer': 'HUAWEI'
                                  ,'device': 'LON-L29' ,'model': 'HWLON' ,'cpu': 'hi3660' ,'version_code': virs},
            'samsung_galaxy_s9_plus': {'app_version': vers ,'android_version': '28' ,'android_release': '9.0'
                                       ,'dpi': '640dpi' ,'resolution': '1440x2560' ,'manufacturer': 'samsung'
                                       ,'device': 'SM-G965F' ,'model': 'star2qltecs' ,'cpu': 'samsungexynos9810'
                                       ,'version_code': virs},
            'one_plus_3t': {'app_version': vers ,'android_version': '26' ,'android_release': '8.0' ,'dpi': '380dpi'
                            ,'resolution': '1080x1920' ,'manufacturer': 'OnePlus' ,'device': 'ONEPLUS A3010'
                            ,'model': 'OnePlus3T' ,'cpu': 'qcom' ,'version_code': virs},
            'lg_g5': {'app_version': vers ,'android_version': '23' ,'android_release': '6.0.1' ,'dpi': '640dpi'
                      ,'resolution': '1440x2392' ,'manufacturer': 'LGE/lge' ,'device': 'RS988' ,'model': 'h1'
                      ,'cpu': 'h1' ,'version_code': virs},
            'zte_axon_7': {'app_version': vers ,'android_version': '23' ,'android_release': '6.0.1' ,'dpi': '640dpi'
                           ,'resolution': '1440x2560' ,'manufacturer': 'ZTE' ,'device': 'ZTE A2017U'
                           ,'model': 'ailsa_ii' ,'cpu': 'qcom' ,'version_code': virs},
            'samsung_galaxy_s7_edge': {'app_version': vers ,'android_version': '23' ,'android_release': '6.0.1'
                                       ,'dpi': '640dpi' ,'resolution': '1440x2560' ,'manufacturer': 'samsung'
                                       ,'device': 'SM-G935' ,'model': 'hero2lte' ,'cpu': 'samsungexynos8890'
                                       ,'version_code': virs} ,}
        davic = random.choice(list(de.keys()))
        versions = de[davic]['app_version']
        androids = de[davic]['android_version']
        endroids = de[davic]['android_release']
        phonas = de[davic]['dpi']
        phones = de[davic]['resolution']
        manufa = de[davic]['manufacturer']
        devicees = de[davic]['device']
        modelas = de[davic]['model']
        apicup = de[davic]['cpu']
        versiones = de[davic]['version_code']
        massage = 'Instagram {} Android ({}/{}; {}; {}; {}; {}; {}; {}; en_US; {})'.format(str(versions) ,str(androids)
                                                                                           ,str(endroids) ,str(phonas)
                                                                                           ,str(phones) ,str(manufa)
                                                                                           ,str(devicees) ,str(modelas)
                                                                                           ,str(apicup) ,str(versiones))
        return massage


# -------------------------[CoDe BY GDØ]------------------------
# -------------------------[CoDe BY GDØ]------------------------
# -------------------------[CoDe BY GDØ]------------------------

class session_IG:
    
    def login(session: str) -> str:
        url = "https://i.instagram.com/api/v1/accounts/current_user/?edit=true"
        headers = {
            'X-IG-Connection-Type': 'WIFI',
            'X-IG-Capabilities': '3brTBw==',
            'User-Agent': str(info_IG.Server_IG()),
            'Accept-Language': 'en-US',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Accept-Encoding': 'gzip, deflate',
            'Host': 'i.instagram.com',
            'Connection': 'keep-alive',
            'Accept': '*/*'}
        cookies = {"sessionid": str(session)}
        res = requests.get(url, headers=headers, cookies=cookies).json()
        if str('message') in res:
            return {'status': 'error', 'login': 'error_session'}

        else:
            username = res['user']['username']
            id = res['user']['pk']
            full_name = res['user']['full_name']
            profile = res['user']['profile_pic_url']
            private = res['user']['is_private']
            date = info_IG.date(username)
            return {'status':'Success','username':str(username),'id':str(id),'name':str(full_name),'date':str(date),'private':str(private),'profile':str(profile),'sessionid':str(session)}

    def get_sessionid(username: str, password: str) -> str:
   
        url = "https://www.instagram.com/accounts/login/ajax/"
        tok = requests.Session().get("https://www.instagram.com/", headers={"user-agent": str(generate_user_agent())}).text
        token = re.findall(r"\"csrf_token\"\:\"(.*?)\"", str(tok))[0]
        headers = {
	    'accept': '*/*',
	    'accept-encoding': 'gzip, deflate, br',
	    'accept-language': 'en-US,en;q=0.9',
	    'content-length': '272',
	    'content-type': 'application/x-www-form-urlencoded',
	    'cookie': f'ig_did=F839D900-5ECC-4392-BCAD-5CBD51FB9228; mid=YChlyQALAAHp2POOp2lK_-ciAGlM; ig_nrcb=1; csrftoken={token}; ds_user_id=45872034997; shbid=6144; shbts=1614374582.8963153',
	    'origin': 'https://www.instagram.com',
	    'referer': 'https://www.instagram.com/accounts/login/',
	    'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
	    'sec-ch-ua-mobile': '?0',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-origin',
	    'user-agent': str(info_IG.Server_IG()),
	    'x-csrftoken': str(token),
	    'x-ig-app-id': '936619743392459',
	    'x-ig-www-claim': '0',
	    'x-instagram-ajax': '790551e77c76',
	    'x-requested-with': 'XMLHttpRequest'}
        data = {
	    "username": str(username),
	    "enc_password": f"#PWD_INSTAGRAM_BROWSER:0:&:{password}",
	    "queryParams": {},
	    "optIntoOneTap":False}
        res =requests.post(url,headers=headers,data=data)
        
        if res.json()['authenticated']==True:
            cookie = res.cookies.get_dict()
            cookies = ";".join([v + "=" + cookie[v] for v in cookie])
            sessionid = cookie['sessionid']
            userid = res.json()['userId']
            date = requests.get(f"https://o7aa.pythonanywhere.com/?id={userid}").json()['data']
            massage = {
                'status': 'Success',
                'sessionid': str(sessionid),}
            return massage

        elif ("checkpoint_url") in res.text:
            return {'status': 'error', 'login': 'checkpoint'}

        else:
            return {'status': 'error', 'login': 'error.username_or_password'}

    def follow(session: str, user: str) -> str:
        tok = requests.Session().get("https://www.instagram.com/", headers={"user-agent": str(generate_user_agent())}).text
        toke = re.findall(r"\"csrf_token\"\:\"(.*?)\"", str(tok))[0]
        url = "https://www.instagram.com/web/friendships/" + str(info_IG.id(user)) + "/follow/"
        headers = {
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
            'content-length': '0',
            'content-type': 'application/x-www-form-urlencoded',
            'cookie': 'mid=YfHAnwALAAFCLfUn6sJVurIEyEfr; ig_did=DF84157E-69D8-46D5-B090-33F4741C808C; ig_nrcb=1; csrftoken=hbqh3XgJPV7Rbvr7dgcKiHQnUtX887Pv; ds_user_id=53352662133; sessionid=' + str(session) + '; rur="CLN\05453352662133\0541684424578:01f726c10813bcb9113b0f4dcf1be24a5278c0fed11c90001622f46b9b5fdf7010e66eda"',
            'origin': 'https://www.instagram.com',
            'referer': 'https://www.instagram.com/' + str(user) + '/',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': str(generate_user_agent()),
            'x-asbd-id': '198387',
            'x-csrftoken': str(toke),
            'x-ig-app-id': '936619743392459',
            'x-ig-www-claim': 'hmac.AR3ftyvn6nRl6sa3ptTW-Vz0nWdjaRGWCLkc_dmTa7Pg4Ag3',
            'x-instagram-ajax': '808d16d2325b',
            'x-requested-with': 'XMLHttpRequest', }
        res = requests.post(url, headers=headers).text
        if str('{"result":"following","status":"ok"}') in res:
            message = {'status': 'Success', 'following': 'true', 'userneme': str(user)}
            return message

        elif str("message") in res:
            return {'status': 'checkpoint', 'following': 'false', 'username': str(user)}
        else:
            return {'status': 'error', 'following': 'false', 'username': str(user)}

    def like(session: str, id: str) -> str:
        url = f'https://www.instagram.com/web/likes/{id}/like/'
        tok = requests.Session().get("https://www.instagram.com/", headers={"user-agent": str(generate_user_agent())}).text
        toke = re.findall(r"\"csrf_token\"\:\"(.*?)\"", str(tok))[0]
        headers = {
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
            'content-length': '0',
            'content-type': 'application/x-www-form-urlencoded',
            'cookie': 'mid=YfHAnwALAAFCLfUn6sJVurIEyEfr; ig_did=DF84157E-69D8-46D5-B090-33F4741C808C; ig_nrcb=1; shbid="19368\05452914264168\0541682536774:01f7c91f0322a7914c4967e12bcfa34c11317752f470517e402d83ba56c43dd701276cd8"; shbts="1651000774\05452914264168\0541682536774:01f704008a362d517796cf36108b67ea9ace8dbfcadcd2a319c9f940d90aa3647ebd9dbe"; csrftoken=hbqh3XgJPV7Rbvr7dgcKiHQnUtX887Pv; ds_user_id=53352662133;; sessionid=' + str(session) + '; rur="CLN\05452914264168\0541682560907:01f70b26a7341573483af51f1be279a94d451a4ebb66ffdf3419bec3f98f6850794bf7f7"',
            'origin': 'https://www.instagram.com',
            'referer': 'https://www.instagram.com/p/' + str(id),
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': str(generate_user_agent()),
            'x-asbd-id': '198387',
            'x-csrftoken': str(toke),
            'x-ig-app-id': '936619743392459',
            'x-ig-www-claim': 'hmac.AR1uQ-iX4kPv3S7OgVlHqdoy-l9MiEpOXeiyxpZdbvWKxKgA',
            'x-instagram-ajax': '20e2a5e214f4',
            'x-requested-with': 'XMLHttpRequest', }
        res = requests.post(url, headers=headers).text
        if ('status: "ok"') in res:
            return {'status': 'Success', 'like': 'true'}

        elif str("message") in res:
            return {'status': 'checkpoint', 'like': 'false'}

        else:
            return {'status': 'error', 'like': 'false'}

    def comment(session: str, id: str, text: str,link: str) -> str:
        li = link.split('p/')[1].split('/')[0]
        url = f"https://www.instagram.com/web/comments/{id}/add/"
        tok = requests.Session().get("https://www.instagram.com/", headers={"user-agent": str(generate_user_agent())}).text
        toke = re.findall(r"\"csrf_token\"\:\"(.*?)\"", str(tok))[0]
        data = {
            "comment_text": str(text),
            "replied_to_comment_id": "", }
        headers = {
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'content-length': '37',
            'content-type': 'application/x-www-form-urlencoded',
            'cookie': f'ig_did=3228C28C-878C-4032-B1BA-805CA7DCDE80; mid=YCMNFgALAAGTkjQS4zQTJ887fFG5; ig_nrcb=1; csrftoken={toke}; ds_user_id=46015777379; sessionid={session}; rur=RVA',
            'origin': 'https://www.instagram.com',
            "referer": f"https://www.instagram.com/p/{li}/comments/",
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': str(generate_user_agent()),
            'x-csrftoken': str(toke),
            'x-ig-app-id': "1217981644879628",
            'x-ig-www-claim': 'hmac.AR2Ba9nmJROdSoghzs45qrHKC88BhLBeE0C1g5XLvznnHULt',
            'x-instagram-ajax': '0edc1000e5e7',
            'x-requested-with': 'XMLHttpRequest', }
        res = requests.post(url, data=data, headers=headers).text
        if ('status: "ok"') in res:
            return {'status': 'Success', 'comment': 'true'}

        elif str("message") in res:
            return {'status': 'checkpoint', 'comment': 'false'}

        else:
            return {'status': 'error', 'comment': 'false'}


class login_IG:

    def __init__(self, username, password):
        self.username = username
        self.password = password


    def instagram(self):
        self.url = "https://www.instagram.com/accounts/login/ajax/"
        tok = requests.Session().get("https://www.instagram.com/", headers={"user-agent": str(generate_user_agent())}).text
        token = re.findall(r"\"csrf_token\"\:\"(.*?)\"", str(tok))[0]
        headers = {
	    'accept': '*/*',
	    'accept-encoding': 'gzip, deflate, br',
	    'accept-language': 'en-US,en;q=0.9',
	    'content-length': '272',
	    'content-type': 'application/x-www-form-urlencoded',
	    'cookie': f'ig_did=F839D900-5ECC-4392-BCAD-5CBD51FB9228; mid=YChlyQALAAHp2POOp2lK_-ciAGlM; ig_nrcb=1; csrftoken={token}; ds_user_id=45872034997; shbid=6144; shbts=1614374582.8963153',
	    'origin': 'https://www.instagram.com',
	    'referer': 'https://www.instagram.com/accounts/login/',
	    'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
	    'sec-ch-ua-mobile': '?0',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-origin',
	    'user-agent': str(info_IG.Server_IG()),
	    'x-csrftoken': str(token),
	    'x-ig-app-id': '936619743392459',
	    'x-ig-www-claim': '0',
	    'x-instagram-ajax': '790551e77c76',
	    'x-requested-with': 'XMLHttpRequest'}
        data = {
	    "username": str(self.username),
	    "enc_password": f"#PWD_INSTAGRAM_BROWSER:0:&:{self.password}",
	    "queryParams": {},
	    "optIntoOneTap":False}
        res =requests.post(self.url,headers=headers,data=data)
        if ('checkpoint_url') in str(res.text):
        	return {'status': 'checkpoint'}
 
        elif res.json()['authenticated']==True:
            cookie = res.cookies.get_dict()          
            cookies = ";".join([v + "=" + cookie[v] for v in cookie])
            sessionid = cookie['sessionid']
            try:
                following = info_IG.following(self.username)
                followers = ibfo_IG.followers(self.username)
            except:
                following = False 
                followers = False
            userid = res.json()['userId']
            date = requests.get(f"https://o7aa.pythonanywhere.com/?id={userid}").json()['data']
            massage = {
                'status': 'Success',
                'userid': str(userid),
                'following':str(following),
                'followers':str(followers),
                'date': str(date),
                'sessionid': str(sessionid),
                'cookies': str(cookies)}
            return massage

        else:
            return {'status': 'error'}


class create_IG():
	   def __init__(self) -> None:
	       self.hosturl = "https://www.instagram.com/"
	       self.createurl = "https://www.instagram.com/accounts/web_create_ajax/attempt/"
	       self.ageurl = "https://www.instagram.com/web/consent/check_age_eligibility/"
	       self.sendurl = "https://i.instagram.com/api/v1/accounts/send_verify_email/"
	       self.checkcodeurl = "https://i.instagram.com/api/v1/accounts/check_confirmation_code/"
	       self.createacc = "https://www.instagram.com/accounts/web_create_ajax/"
	       self.session = requests.Session()
	       self.session.headers = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36', 'Referer': self.hosturl}
	       self.session.proxies = {'http': requests.get("https://gimmeproxy.com/api/getProxy").json()['curl']}
	       self.password = "GDOTools"+str(random.randint(0,30))
	       self.name = "GDØ Tools ."
	       self.register()
	   def register(self):
	       	self.reqB = self.session.get(self.hosturl)
	       	self.session.headers.update({'X-CSRFToken': self.reqB.cookies['csrftoken']})
	       	self.mail = self.getmail()
	       	self.mailss = self.mail[1]
	       	self.maile = self.mail[0]
	       	self.user = "GDO_0"+''.join(random.choice(string.digits)for i in range(5))
	       	self.data = {'enc_password':'#PWD_INSTAGRAM_BROWSER:0:&:'+self.password,'email':self.maile,'username':self.user,'first_name':self.name,'client_id':'','seamless_login_enabled':'1','opt_into_one_tap':'false',}
	       	self.reg1 = self.session.post(url=self.createurl,headers=self.session.headers,data=self.data,allow_redirects=True)
	       	if(self.reg1.json()['status'] == 'ok'):
	       		pass
	       	else:
	       		return {'status':'error'}
	       	self.data2 = {'day':'1','month':'1','year':'1995',}
	       	self.reqA = self.session.post(url=self.ageurl,headers=self.session.headers,data=self.data2,allow_redirects=True)
	       	if(self.reqA.json()['status'] == 'ok'):pass
	       	else:
	       	   return {'status':'error'}
	       	self.sendcode = self.session.post(url=self.sendurl,headers=self.session.headers,data={'device_id': '','email': self.maile},allow_redirects=True)
	       	if(self.sendcode.json()['status'] == 'ok'):pass
	       	else:
	       	   return {'status':'error'}
	       	while 1:
	       	   self.inbox = self.getindox(self.mailss)
	       	   if "Instagram" in self.inbox:
	       	       code = self.inbox.split(" is")[0]
	       	       break     
	       	   else:
	       	       time.sleep(10)
	       	       continue
	       	self.confirmation = self.session.post(url=self.checkcodeurl,headers=self.session.headers,data={'code': code,'device_id': '','email': self.maile})
	       	if self.confirmation.json()['status'] == "ok":
	       	   signup_code = self.confirmation.json()['signup_code']
	       	   self.create = self.session.post(
                url=self.createacc,
                data={
                'enc_password': '#PWD_INSTAGRAM_BROWSER:0:&:'+self.password,
                'email': self.maile,
                'username': self.user,
                'first_name': self.name,
                'month': '1','day': '1',
                'year': '1995',
                'client_id': '',
                'seamless_login_enabled': '1',
                'tos_version': 'row',
                'force_sign_up_code': signup_code})
	       	   if '"account_created": false' in self.create.text:
	       	   	return {'status':'error'}
	       	   else:
	       	       return {'status':'Success','username':str(self.user),'password':str(self.password)}
	       	else:
	       	   return {'status':'error'}
	   def getmail(self):
	       	self.rem = requests.get("https://10minutemail.net/address.api.php")
	       	return self.rem.json()['mail_get_mail'],self.rem.cookies['PHPSESSID']
	   def getindox(self,sessionid):
	       	self.rei = requests.get("https://10minutemail.net/address.api.php",cookies={"PHPSESSID":sessionid})
	       	return self.rei.json()['mail_list'][0]['subject']
	   def user_generator(self):
	       	return ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(12))


# -------------------------[CoDe BY GDØ]------------------------
# -------------------------[CoDe BY GDØ]------------------------
# -------------------------[CoDe BY GDØ]------------------------