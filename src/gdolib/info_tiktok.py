import requests , json , secrets
from .gdo_drow import *
class info_tik:

    def get_sessionid(username: str, password: str) -> str:
        url = 'https://api2.musical.ly/passport/user/login/?mix_mode=1&username=1&email=&mobile=&account=&password=hg&captcha=&ts=&app_type=normal&app_language=en&manifest_version_code=2018073102&_rticket=1633593458298&iid=7011916372695598854&channel=googleplay&language=en&fp=&device_type=SM-G955F&resolution=1440*2792&openudid=91cac57ba8ef12b6&update_version_code=2018073102&sys_region=AS&os_api=28&is_my_cn=0&timezone_name=Asia/Muscat&dpi=560&carrier_region=OM&ac=wifi&device_id=6785177577851504133&mcc_mnc=42203&timezone_offset=14400&os_version=9&version_code=800&carrier_region_v2=422&app_name=musical_ly&version_name=8.0.0&device_brand=samsung&ssmix=a&build_number=8.0.0&device_platform=android&region=US&aid=&as=&cp=Qm&mas='
        headers = \
            {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
            'cookie': 'csrftoken=' + str(secrets.token_hex(8) * 2) + '; sessionid=' + str(secrets.token_hex(8) * 2) + ';',
            'User-Agent': 'Connectionzucom.zhiliaoapp.musically/2018073102 (Linux; U; Android 9; en_AS; SM-G955F; Build/PPR1.180610.011; Cronet/58.0.2991.0)z',
            'Host': 'api2.musical.ly', 'Connection': 'keep-alive'}
        data = {"email": str(username), "password": str(password)}
        res = requests.post(url, headers=headers, data=data)
        if ("user_id") in res.text:
            sessionid = str(res.json()['data']['session_key'])
            message = {
                'status': 'Succese',
                'sessionid': str(sessionid)}
            return message

        elif ("Incorrect account or password") in res.text:
            return {'status': 'error.username_or_password'}
        else:
            return {'status': 'error'}

    def name(user: str) -> str:
        url = 'https://m.tiktok.com/api/user/detail/?aid=1988&app_name=tiktok_web&device_platform=web_mobile&device_id=7074866456449713670&region=IQ&priority_region=IQ&os=android&referer=&cookie_enabled=true&screen_width=393&screen_height=873&browser_language=ar-EG&browser_platform=Linux+aarch64&browser_name=Mozilla&browser_version=5.0+(Linux;+Android+11;+M2103K19G)+AppleWebKit/537.36+(KHTML,+like+Gecko)+Chrome/99.0.4844.66+Mobile+Safari/537.36&browser_online=true&verifyFp=verify_l0wf3oa3_tprFK83t_Q0pW_4EH0_BU4w_42nV9RgFBTIH&app_language=ar&timezone_name=Asia/Baghdad&is_page_visible=true&focus_state=true&is_fullscreen=false&history_len=2&battery_info={}&uniqueId=' + user + '&msToken=4M1DZ-8b03tXs9pqv4iVHGoa9RXRgOB11HjiL7cvs8Sit3X4JTzxsy1FUbmomfk1U3kiown_BdR8lyO_nyxhL6EgNXwVolAz4Qg50PD5imlyx5VhnUkEAeOvU6Gs4ejKs2ODHR8=&X-Bogus=DFSzswSOxhhANtVzSRkg-KW5ZE/N&_signature=_02B4Z6wo0000142Tr2wAAIDC54h1kUWPxv-Nk6vAAIFYd8'
        headers = {
            'User-Agent': str(gdo_drow.get_user_agent()),
            'Accept': 'application/json, text/plain, */*',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
            'Content-Type': 'application/json',
            'Cookie': 'passport_csrf_token=458c72cf0594545b4d8e79bf3caded25; passport_csrf_token_default=458c72cf0594545b4d8e79bf3caded25; passport_auth_status=251fd84db2fafd555a135e73908379b5,; passport_auth_status_ss=251fd84db2fafd555a135e73908379b5,; sid_guard=9eac4270bbe6804badac8696654b064e|1648687327|5184000|Mon,+30-May-2022+00:42:07+GMT; uid_tt=6d8a5958360a534b628ae820fa7a2bdd67e9902f9494fceebe98cd9950759557; uid_tt_ss=6d8a5958360a534b628ae820fa7a2bdd67e9902f9494fceebe98cd9950759557; sid_tt=9eac4270bbe6804badac8696654b064e; sessionid=9eac4270bbe6804badac8696654b064e; sessionid_ss=9eac4270bbe6804badac8696654b064e; sid_ucp_v1=1.0.0-KDQ4MDZkODM4NzQ0MDE1YzNlYjlkOGJjYWMxZDhlYTk3OTY4MWUzYTEKHwiBiLn0lpPUrWEQ3_GTkgYYswsgDDCfpu2KBjgIQBIQAxoGbWFsaXZhIiA5ZWFjNDI3MGJiZTY4MDRiYWRhYzg2OTY2NTRiMDY0ZQ; ssid_ucp_v1=1.0.0-KDQ4MDZkODM4NzQ0MDE1YzNlYjlkOGJjYWMxZDhlYTk3OTY4MWUzYTEKHwiBiLn0lpPUrWEQ3_GTkgYYswsgDDCfpu2KBjgIQBIQAxoGbWFsaXZhIiA5ZWFjNDI3MGJiZTY4MDRiYWRhYzg2OTY2NTRiMDY0ZQ; store-idc=alisg; store-country-code=iq; tt-target-idc=alisg; tt_csrf_token=TOzZoC0p-lXaXuL7lq6ynvJywC006F8ixc-A; _abck=093D884478C406B48D6E8F4696FBC348~-1~YAAQBLR7XL8RDiOAAQAABiCpMgf/mTykvtzUPdMKxO5b9PAf4oFOTanUbEbor2OmIngPpyC6Gzf66YjbaUUGpIPpBJ6ZwPhpCdVw4jctEx+wSCOttDZjMU65rD6zxWbtErf36ZnocPLoCiwN5pagDq/K3e/s5O4bpPtO5xf8le7+yGLPsEHjMwGneEj6YSGYSE9QauyY6FvziUVCTSNQiuEUC8Soy+kufKxVEpwwzN5Zo1KV1q1rw4rtClwvCDo4CEi8icykPZfjta2PKf2zax/B4euHxWX5mzFP7HmPFsmBK8UQvmAM++ZUF7AY52kH1Polr7cB9ziWZAuRcLRO4UIKu35+cMb4xjJH3bAWXZXX5DaFoi55crdz3h9RBRzmCDTB5LPPiIN/RDA=~-1~-1~-1; ak_bmsc=3B8069AEE7E00870B984D180ECFFBD5D~000000000000000000000000000000~YAAQBLR7XMARDiOAAQAABiCpMg9auExniSBpZbCVcLzVPFqefIbpGImTcAxDH2gABB5UwaA2MVjucEhh3S7gz30SLbwpNUNrz1kgII1USn5iNT3nlqfwkJVlcGM/1WSVAAT4ZgMH9JJsS//Ev2hNH0Ux3RbCPvS+5d88mwT/lNKfrvgYT1zmm+1gb21gQNNIgnt3RSvR26eNTW80k36v2qJi1mLyiQVZYD3rRi94vlyWRGASfWooBznWg99OujqaSU2DXh2EuyupYmhBBkiOFvQFkvapmgdgfcIRy9HQJROh4YzV3aFuxOWpi+5a0DxdYE5kuh4dcEjOL7RDIukoWWNvcjLhX2ViXpIsA2NyFLbWTPq5nQFOArd4a+KagglgXyHAIX41UAg=; bm_sz=C6365C417EF2307C8B0C15C7E15B62F5~YAAQBLR7XMERDiOAAQAABiCpMg8IGWK7o/apYJdjwsv1/wjLItPslFiabm8NbHoZlZ73XiI+aRFhHtVd+ptrlGm0b5jJM63YDiGi+4Rb/IXFoZMyZmtm2If31jRMKd0p8jcPat/qubsjnRKFdRKSBqnJymUgVOb/A6SlOBhOfAqCXRJ0AvRBWce3f55YpiqDr50KCJS77E5dDyowvlOcXIbULbqO5MbYMj93Nl8DptG025NLLhevbIltxsVtU9Mr0OTE1ewY8MNOwZFKRM+0lZ1fvuQUJBFNTlqHwa6hbs3BXkc=~3552578~4408887; odin_tt=27b8d72a704b3dd1b987f6309bb1afbde567eb6d8f4108cc0c01daf7b00cc85a6461560b71a5592eb54b6776088e5a22971675b58ccfc9405aea62e1bf507156cec903e457da0accc7dbf02dfdef9cb7; ttwid=1|Y3Nv6hZ_tt-KrXdOWRCHJUZNBnvJt9gACwthXSzp5uY|1650117421|a5d1e6984719ca946c7088a118f5c09ca9468056b9430fd38b2ef693aaeb1eee; cmpl_token=AgQQAPOnF-RMpbFlvj7mvJ04-F-i-0ZR_4csYMA9cQ; bm_mi=7444CFE66808C67F62BCEBB880BD4DB7~UHV9BJZPF2NZr3P4g421EuBTucUNYIexr523/VwvKCGfGzEAfA1abHo8HYcKocxP+laN76JpUglyrLWY/Gkgc2BxZA4J3kAdwnBbz96YgaPRpe2m9+BRU2xTO6kc/ycqlm+3zUicVNfb+BftRwhtikPp+l3bSk4GNtW1kKVJI3DTB2YzhM9BMwiYMTvpxW9tSed75nLNZDJuCY/wP2hwfbmR0+UrKlZggDnPvsfpv8k=; msToken=1gt3-BZ_WjAoOKJxJh77qZAJR0tGKOAx_iKHEG75TaFCWXltux0CfvXETy1S5uFizHuw9DcSWYsip8dnS1EpGdK7gG_7XVOBSU_F7yzjFdB6V9UyhBONnTMqvHgGsO9wY4IXWO0=; bm_sv=EC714A2F6623FDD508362A22220189F7~uPx5OKNtLIB/jt8DLjlHUsoWWA2xFWVI1T6e4HQN01YlW2sITk6VB9L8uvYfK6KWeeNGzPqsa+fnnxgvUnSNA5aYfYIDBepRuxD1J8oSmfnY8CDJOt+09fr3PnZLd+cAvxrBKSE1nAEhvdeNGnN0fTu4h4erxMOH27501pU0E8g=',
            'Origin': 'https://www.tiktok.com',
            'Referer': 'https://www.tiktok.com/'}
        data = {'uniqueld': str(user)}
        try:
            res = requests.get(url, headers=headers, data=data).content
            info = json.loads(res)
            name = info['userInfo']['user']['nickname']
            return {'name': str(name)}
        except:
            return False

    def id(user: str) -> str:
        url = 'https://m.tiktok.com/api/user/detail/?aid=1988&app_name=tiktok_web&device_platform=web_mobile&device_id=7074866456449713670&region=IQ&priority_region=IQ&os=android&referer=&cookie_enabled=true&screen_width=393&screen_height=873&browser_language=ar-EG&browser_platform=Linux+aarch64&browser_name=Mozilla&browser_version=5.0+(Linux;+Android+11;+M2103K19G)+AppleWebKit/537.36+(KHTML,+like+Gecko)+Chrome/99.0.4844.66+Mobile+Safari/537.36&browser_online=true&verifyFp=verify_l0wf3oa3_tprFK83t_Q0pW_4EH0_BU4w_42nV9RgFBTIH&app_language=ar&timezone_name=Asia/Baghdad&is_page_visible=true&focus_state=true&is_fullscreen=false&history_len=2&battery_info={}&uniqueId=' + user + '&msToken=4M1DZ-8b03tXs9pqv4iVHGoa9RXRgOB11HjiL7cvs8Sit3X4JTzxsy1FUbmomfk1U3kiown_BdR8lyO_nyxhL6EgNXwVolAz4Qg50PD5imlyx5VhnUkEAeOvU6Gs4ejKs2ODHR8=&X-Bogus=DFSzswSOxhhANtVzSRkg-KW5ZE/N&_signature=_02B4Z6wo0000142Tr2wAAIDC54h1kUWPxv-Nk6vAAIFYd8'
        headers = {
            'User-Agent': str(gdo_drow.get_user_agent()),
            'Accept': 'application/json, text/plain, */*',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
            'Content-Type': 'application/json',
            'Cookie': 'passport_csrf_token=458c72cf0594545b4d8e79bf3caded25; passport_csrf_token_default=458c72cf0594545b4d8e79bf3caded25; passport_auth_status=251fd84db2fafd555a135e73908379b5,; passport_auth_status_ss=251fd84db2fafd555a135e73908379b5,; sid_guard=9eac4270bbe6804badac8696654b064e|1648687327|5184000|Mon,+30-May-2022+00:42:07+GMT; uid_tt=6d8a5958360a534b628ae820fa7a2bdd67e9902f9494fceebe98cd9950759557; uid_tt_ss=6d8a5958360a534b628ae820fa7a2bdd67e9902f9494fceebe98cd9950759557; sid_tt=9eac4270bbe6804badac8696654b064e; sessionid=9eac4270bbe6804badac8696654b064e; sessionid_ss=9eac4270bbe6804badac8696654b064e; sid_ucp_v1=1.0.0-KDQ4MDZkODM4NzQ0MDE1YzNlYjlkOGJjYWMxZDhlYTk3OTY4MWUzYTEKHwiBiLn0lpPUrWEQ3_GTkgYYswsgDDCfpu2KBjgIQBIQAxoGbWFsaXZhIiA5ZWFjNDI3MGJiZTY4MDRiYWRhYzg2OTY2NTRiMDY0ZQ; ssid_ucp_v1=1.0.0-KDQ4MDZkODM4NzQ0MDE1YzNlYjlkOGJjYWMxZDhlYTk3OTY4MWUzYTEKHwiBiLn0lpPUrWEQ3_GTkgYYswsgDDCfpu2KBjgIQBIQAxoGbWFsaXZhIiA5ZWFjNDI3MGJiZTY4MDRiYWRhYzg2OTY2NTRiMDY0ZQ; store-idc=alisg; store-country-code=iq; tt-target-idc=alisg; tt_csrf_token=TOzZoC0p-lXaXuL7lq6ynvJywC006F8ixc-A; _abck=093D884478C406B48D6E8F4696FBC348~-1~YAAQBLR7XL8RDiOAAQAABiCpMgf/mTykvtzUPdMKxO5b9PAf4oFOTanUbEbor2OmIngPpyC6Gzf66YjbaUUGpIPpBJ6ZwPhpCdVw4jctEx+wSCOttDZjMU65rD6zxWbtErf36ZnocPLoCiwN5pagDq/K3e/s5O4bpPtO5xf8le7+yGLPsEHjMwGneEj6YSGYSE9QauyY6FvziUVCTSNQiuEUC8Soy+kufKxVEpwwzN5Zo1KV1q1rw4rtClwvCDo4CEi8icykPZfjta2PKf2zax/B4euHxWX5mzFP7HmPFsmBK8UQvmAM++ZUF7AY52kH1Polr7cB9ziWZAuRcLRO4UIKu35+cMb4xjJH3bAWXZXX5DaFoi55crdz3h9RBRzmCDTB5LPPiIN/RDA=~-1~-1~-1; ak_bmsc=3B8069AEE7E00870B984D180ECFFBD5D~000000000000000000000000000000~YAAQBLR7XMARDiOAAQAABiCpMg9auExniSBpZbCVcLzVPFqefIbpGImTcAxDH2gABB5UwaA2MVjucEhh3S7gz30SLbwpNUNrz1kgII1USn5iNT3nlqfwkJVlcGM/1WSVAAT4ZgMH9JJsS//Ev2hNH0Ux3RbCPvS+5d88mwT/lNKfrvgYT1zmm+1gb21gQNNIgnt3RSvR26eNTW80k36v2qJi1mLyiQVZYD3rRi94vlyWRGASfWooBznWg99OujqaSU2DXh2EuyupYmhBBkiOFvQFkvapmgdgfcIRy9HQJROh4YzV3aFuxOWpi+5a0DxdYE5kuh4dcEjOL7RDIukoWWNvcjLhX2ViXpIsA2NyFLbWTPq5nQFOArd4a+KagglgXyHAIX41UAg=; bm_sz=C6365C417EF2307C8B0C15C7E15B62F5~YAAQBLR7XMERDiOAAQAABiCpMg8IGWK7o/apYJdjwsv1/wjLItPslFiabm8NbHoZlZ73XiI+aRFhHtVd+ptrlGm0b5jJM63YDiGi+4Rb/IXFoZMyZmtm2If31jRMKd0p8jcPat/qubsjnRKFdRKSBqnJymUgVOb/A6SlOBhOfAqCXRJ0AvRBWce3f55YpiqDr50KCJS77E5dDyowvlOcXIbULbqO5MbYMj93Nl8DptG025NLLhevbIltxsVtU9Mr0OTE1ewY8MNOwZFKRM+0lZ1fvuQUJBFNTlqHwa6hbs3BXkc=~3552578~4408887; odin_tt=27b8d72a704b3dd1b987f6309bb1afbde567eb6d8f4108cc0c01daf7b00cc85a6461560b71a5592eb54b6776088e5a22971675b58ccfc9405aea62e1bf507156cec903e457da0accc7dbf02dfdef9cb7; ttwid=1|Y3Nv6hZ_tt-KrXdOWRCHJUZNBnvJt9gACwthXSzp5uY|1650117421|a5d1e6984719ca946c7088a118f5c09ca9468056b9430fd38b2ef693aaeb1eee; cmpl_token=AgQQAPOnF-RMpbFlvj7mvJ04-F-i-0ZR_4csYMA9cQ; bm_mi=7444CFE66808C67F62BCEBB880BD4DB7~UHV9BJZPF2NZr3P4g421EuBTucUNYIexr523/VwvKCGfGzEAfA1abHo8HYcKocxP+laN76JpUglyrLWY/Gkgc2BxZA4J3kAdwnBbz96YgaPRpe2m9+BRU2xTO6kc/ycqlm+3zUicVNfb+BftRwhtikPp+l3bSk4GNtW1kKVJI3DTB2YzhM9BMwiYMTvpxW9tSed75nLNZDJuCY/wP2hwfbmR0+UrKlZggDnPvsfpv8k=; msToken=1gt3-BZ_WjAoOKJxJh77qZAJR0tGKOAx_iKHEG75TaFCWXltux0CfvXETy1S5uFizHuw9DcSWYsip8dnS1EpGdK7gG_7XVOBSU_F7yzjFdB6V9UyhBONnTMqvHgGsO9wY4IXWO0=; bm_sv=EC714A2F6623FDD508362A22220189F7~uPx5OKNtLIB/jt8DLjlHUsoWWA2xFWVI1T6e4HQN01YlW2sITk6VB9L8uvYfK6KWeeNGzPqsa+fnnxgvUnSNA5aYfYIDBepRuxD1J8oSmfnY8CDJOt+09fr3PnZLd+cAvxrBKSE1nAEhvdeNGnN0fTu4h4erxMOH27501pU0E8g=',
            'Origin': 'https://www.tiktok.com',
            'Referer': 'https://www.tiktok.com/'}
        data = {'uniqueld': str(user)}
        try:
            res = requests.get(url, headers=headers, data=data).content
            info = json.loads(res)
            id = info['userInfo']['user']['id']
            return {'id': str(id)}
        except:
            return False

    def followers(user: str) -> str:
        url = 'https://m.tiktok.com/api/user/detail/?aid=1988&app_name=tiktok_web&device_platform=web_mobile&device_id=7074866456449713670&region=IQ&priority_region=IQ&os=android&referer=&cookie_enabled=true&screen_width=393&screen_height=873&browser_language=ar-EG&browser_platform=Linux+aarch64&browser_name=Mozilla&browser_version=5.0+(Linux;+Android+11;+M2103K19G)+AppleWebKit/537.36+(KHTML,+like+Gecko)+Chrome/99.0.4844.66+Mobile+Safari/537.36&browser_online=true&verifyFp=verify_l0wf3oa3_tprFK83t_Q0pW_4EH0_BU4w_42nV9RgFBTIH&app_language=ar&timezone_name=Asia/Baghdad&is_page_visible=true&focus_state=true&is_fullscreen=false&history_len=2&battery_info={}&uniqueId=' + str(
            user) + '&msToken=4M1DZ-8b03tXs9pqv4iVHGoa9RXRgOB11HjiL7cvs8Sit3X4JTzxsy1FUbmomfk1U3kiown_BdR8lyO_nyxhL6EgNXwVolAz4Qg50PD5imlyx5VhnUkEAeOvU6Gs4ejKs2ODHR8=&X-Bogus=DFSzswSOxhhANtVzSRkg-KW5ZE/N&_signature=_02B4Z6wo0000142Tr2wAAIDC54h1kUWPxv-Nk6vAAIFYd8'
        headers = {
            'User-Agent': str(gdo_drow.get_user_agent()),
            'Accept': 'application/json, text/plain, */*',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
            'Content-Type': 'application/json',
            'Cookie': 'passport_csrf_token=458c72cf0594545b4d8e79bf3caded25; passport_csrf_token_default=458c72cf0594545b4d8e79bf3caded25; passport_auth_status=251fd84db2fafd555a135e73908379b5,; passport_auth_status_ss=251fd84db2fafd555a135e73908379b5,; sid_guard=9eac4270bbe6804badac8696654b064e|1648687327|5184000|Mon,+30-May-2022+00:42:07+GMT; uid_tt=6d8a5958360a534b628ae820fa7a2bdd67e9902f9494fceebe98cd9950759557; uid_tt_ss=6d8a5958360a534b628ae820fa7a2bdd67e9902f9494fceebe98cd9950759557; sid_tt=9eac4270bbe6804badac8696654b064e; sessionid=9eac4270bbe6804badac8696654b064e; sessionid_ss=9eac4270bbe6804badac8696654b064e; sid_ucp_v1=1.0.0-KDQ4MDZkODM4NzQ0MDE1YzNlYjlkOGJjYWMxZDhlYTk3OTY4MWUzYTEKHwiBiLn0lpPUrWEQ3_GTkgYYswsgDDCfpu2KBjgIQBIQAxoGbWFsaXZhIiA5ZWFjNDI3MGJiZTY4MDRiYWRhYzg2OTY2NTRiMDY0ZQ; ssid_ucp_v1=1.0.0-KDQ4MDZkODM4NzQ0MDE1YzNlYjlkOGJjYWMxZDhlYTk3OTY4MWUzYTEKHwiBiLn0lpPUrWEQ3_GTkgYYswsgDDCfpu2KBjgIQBIQAxoGbWFsaXZhIiA5ZWFjNDI3MGJiZTY4MDRiYWRhYzg2OTY2NTRiMDY0ZQ; store-idc=alisg; store-country-code=iq; tt-target-idc=alisg; tt_csrf_token=TOzZoC0p-lXaXuL7lq6ynvJywC006F8ixc-A; _abck=093D884478C406B48D6E8F4696FBC348~-1~YAAQBLR7XL8RDiOAAQAABiCpMgf/mTykvtzUPdMKxO5b9PAf4oFOTanUbEbor2OmIngPpyC6Gzf66YjbaUUGpIPpBJ6ZwPhpCdVw4jctEx+wSCOttDZjMU65rD6zxWbtErf36ZnocPLoCiwN5pagDq/K3e/s5O4bpPtO5xf8le7+yGLPsEHjMwGneEj6YSGYSE9QauyY6FvziUVCTSNQiuEUC8Soy+kufKxVEpwwzN5Zo1KV1q1rw4rtClwvCDo4CEi8icykPZfjta2PKf2zax/B4euHxWX5mzFP7HmPFsmBK8UQvmAM++ZUF7AY52kH1Polr7cB9ziWZAuRcLRO4UIKu35+cMb4xjJH3bAWXZXX5DaFoi55crdz3h9RBRzmCDTB5LPPiIN/RDA=~-1~-1~-1; ak_bmsc=3B8069AEE7E00870B984D180ECFFBD5D~000000000000000000000000000000~YAAQBLR7XMARDiOAAQAABiCpMg9auExniSBpZbCVcLzVPFqefIbpGImTcAxDH2gABB5UwaA2MVjucEhh3S7gz30SLbwpNUNrz1kgII1USn5iNT3nlqfwkJVlcGM/1WSVAAT4ZgMH9JJsS//Ev2hNH0Ux3RbCPvS+5d88mwT/lNKfrvgYT1zmm+1gb21gQNNIgnt3RSvR26eNTW80k36v2qJi1mLyiQVZYD3rRi94vlyWRGASfWooBznWg99OujqaSU2DXh2EuyupYmhBBkiOFvQFkvapmgdgfcIRy9HQJROh4YzV3aFuxOWpi+5a0DxdYE5kuh4dcEjOL7RDIukoWWNvcjLhX2ViXpIsA2NyFLbWTPq5nQFOArd4a+KagglgXyHAIX41UAg=; bm_sz=C6365C417EF2307C8B0C15C7E15B62F5~YAAQBLR7XMERDiOAAQAABiCpMg8IGWK7o/apYJdjwsv1/wjLItPslFiabm8NbHoZlZ73XiI+aRFhHtVd+ptrlGm0b5jJM63YDiGi+4Rb/IXFoZMyZmtm2If31jRMKd0p8jcPat/qubsjnRKFdRKSBqnJymUgVOb/A6SlOBhOfAqCXRJ0AvRBWce3f55YpiqDr50KCJS77E5dDyowvlOcXIbULbqO5MbYMj93Nl8DptG025NLLhevbIltxsVtU9Mr0OTE1ewY8MNOwZFKRM+0lZ1fvuQUJBFNTlqHwa6hbs3BXkc=~3552578~4408887; odin_tt=27b8d72a704b3dd1b987f6309bb1afbde567eb6d8f4108cc0c01daf7b00cc85a6461560b71a5592eb54b6776088e5a22971675b58ccfc9405aea62e1bf507156cec903e457da0accc7dbf02dfdef9cb7; ttwid=1|Y3Nv6hZ_tt-KrXdOWRCHJUZNBnvJt9gACwthXSzp5uY|1650117421|a5d1e6984719ca946c7088a118f5c09ca9468056b9430fd38b2ef693aaeb1eee; cmpl_token=AgQQAPOnF-RMpbFlvj7mvJ04-F-i-0ZR_4csYMA9cQ; bm_mi=7444CFE66808C67F62BCEBB880BD4DB7~UHV9BJZPF2NZr3P4g421EuBTucUNYIexr523/VwvKCGfGzEAfA1abHo8HYcKocxP+laN76JpUglyrLWY/Gkgc2BxZA4J3kAdwnBbz96YgaPRpe2m9+BRU2xTO6kc/ycqlm+3zUicVNfb+BftRwhtikPp+l3bSk4GNtW1kKVJI3DTB2YzhM9BMwiYMTvpxW9tSed75nLNZDJuCY/wP2hwfbmR0+UrKlZggDnPvsfpv8k=; msToken=1gt3-BZ_WjAoOKJxJh77qZAJR0tGKOAx_iKHEG75TaFCWXltux0CfvXETy1S5uFizHuw9DcSWYsip8dnS1EpGdK7gG_7XVOBSU_F7yzjFdB6V9UyhBONnTMqvHgGsO9wY4IXWO0=; bm_sv=EC714A2F6623FDD508362A22220189F7~uPx5OKNtLIB/jt8DLjlHUsoWWA2xFWVI1T6e4HQN01YlW2sITk6VB9L8uvYfK6KWeeNGzPqsa+fnnxgvUnSNA5aYfYIDBepRuxD1J8oSmfnY8CDJOt+09fr3PnZLd+cAvxrBKSE1nAEhvdeNGnN0fTu4h4erxMOH27501pU0E8g=',
            'Origin': 'https://www.tiktok.com',
            'Referer': 'https://www.tiktok.com/'}
        data = {'uniqueld': str(user)}
        try:
            res = requests.get(url, headers=headers, data=data).content
            info = json.loads(res)
            followers = info['userInfo']['stats']['followerCount']
            return {'followers': str(followers)}
        except:
            return False

    def following(user: str) -> str:
        url = 'https://m.tiktok.com/api/user/detail/?aid=1988&app_name=tiktok_web&device_platform=web_mobile&device_id=7074866456449713670&region=IQ&priority_region=IQ&os=android&referer=&cookie_enabled=true&screen_width=393&screen_height=873&browser_language=ar-EG&browser_platform=Linux+aarch64&browser_name=Mozilla&browser_version=5.0+(Linux;+Android+11;+M2103K19G)+AppleWebKit/537.36+(KHTML,+like+Gecko)+Chrome/99.0.4844.66+Mobile+Safari/537.36&browser_online=true&verifyFp=verify_l0wf3oa3_tprFK83t_Q0pW_4EH0_BU4w_42nV9RgFBTIH&app_language=ar&timezone_name=Asia/Baghdad&is_page_visible=true&focus_state=true&is_fullscreen=false&history_len=2&battery_info={}&uniqueId=' + str(
            user) + '&msToken=4M1DZ-8b03tXs9pqv4iVHGoa9RXRgOB11HjiL7cvs8Sit3X4JTzxsy1FUbmomfk1U3kiown_BdR8lyO_nyxhL6EgNXwVolAz4Qg50PD5imlyx5VhnUkEAeOvU6Gs4ejKs2ODHR8=&X-Bogus=DFSzswSOxhhANtVzSRkg-KW5ZE/N&_signature=_02B4Z6wo0000142Tr2wAAIDC54h1kUWPxv-Nk6vAAIFYd8'
        headers = {
            'User-Agent': str(gdo_drow.get_user_agent()),
            'Accept': 'application/json, text/plain, */*',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
            'Content-Type': 'application/json',
            'Cookie': 'passport_csrf_token=458c72cf0594545b4d8e79bf3caded25; passport_csrf_token_default=458c72cf0594545b4d8e79bf3caded25; passport_auth_status=251fd84db2fafd555a135e73908379b5,; passport_auth_status_ss=251fd84db2fafd555a135e73908379b5,; sid_guard=9eac4270bbe6804badac8696654b064e|1648687327|5184000|Mon,+30-May-2022+00:42:07+GMT; uid_tt=6d8a5958360a534b628ae820fa7a2bdd67e9902f9494fceebe98cd9950759557; uid_tt_ss=6d8a5958360a534b628ae820fa7a2bdd67e9902f9494fceebe98cd9950759557; sid_tt=9eac4270bbe6804badac8696654b064e; sessionid=9eac4270bbe6804badac8696654b064e; sessionid_ss=9eac4270bbe6804badac8696654b064e; sid_ucp_v1=1.0.0-KDQ4MDZkODM4NzQ0MDE1YzNlYjlkOGJjYWMxZDhlYTk3OTY4MWUzYTEKHwiBiLn0lpPUrWEQ3_GTkgYYswsgDDCfpu2KBjgIQBIQAxoGbWFsaXZhIiA5ZWFjNDI3MGJiZTY4MDRiYWRhYzg2OTY2NTRiMDY0ZQ; ssid_ucp_v1=1.0.0-KDQ4MDZkODM4NzQ0MDE1YzNlYjlkOGJjYWMxZDhlYTk3OTY4MWUzYTEKHwiBiLn0lpPUrWEQ3_GTkgYYswsgDDCfpu2KBjgIQBIQAxoGbWFsaXZhIiA5ZWFjNDI3MGJiZTY4MDRiYWRhYzg2OTY2NTRiMDY0ZQ; store-idc=alisg; store-country-code=iq; tt-target-idc=alisg; tt_csrf_token=TOzZoC0p-lXaXuL7lq6ynvJywC006F8ixc-A; _abck=093D884478C406B48D6E8F4696FBC348~-1~YAAQBLR7XL8RDiOAAQAABiCpMgf/mTykvtzUPdMKxO5b9PAf4oFOTanUbEbor2OmIngPpyC6Gzf66YjbaUUGpIPpBJ6ZwPhpCdVw4jctEx+wSCOttDZjMU65rD6zxWbtErf36ZnocPLoCiwN5pagDq/K3e/s5O4bpPtO5xf8le7+yGLPsEHjMwGneEj6YSGYSE9QauyY6FvziUVCTSNQiuEUC8Soy+kufKxVEpwwzN5Zo1KV1q1rw4rtClwvCDo4CEi8icykPZfjta2PKf2zax/B4euHxWX5mzFP7HmPFsmBK8UQvmAM++ZUF7AY52kH1Polr7cB9ziWZAuRcLRO4UIKu35+cMb4xjJH3bAWXZXX5DaFoi55crdz3h9RBRzmCDTB5LPPiIN/RDA=~-1~-1~-1; ak_bmsc=3B8069AEE7E00870B984D180ECFFBD5D~000000000000000000000000000000~YAAQBLR7XMARDiOAAQAABiCpMg9auExniSBpZbCVcLzVPFqefIbpGImTcAxDH2gABB5UwaA2MVjucEhh3S7gz30SLbwpNUNrz1kgII1USn5iNT3nlqfwkJVlcGM/1WSVAAT4ZgMH9JJsS//Ev2hNH0Ux3RbCPvS+5d88mwT/lNKfrvgYT1zmm+1gb21gQNNIgnt3RSvR26eNTW80k36v2qJi1mLyiQVZYD3rRi94vlyWRGASfWooBznWg99OujqaSU2DXh2EuyupYmhBBkiOFvQFkvapmgdgfcIRy9HQJROh4YzV3aFuxOWpi+5a0DxdYE5kuh4dcEjOL7RDIukoWWNvcjLhX2ViXpIsA2NyFLbWTPq5nQFOArd4a+KagglgXyHAIX41UAg=; bm_sz=C6365C417EF2307C8B0C15C7E15B62F5~YAAQBLR7XMERDiOAAQAABiCpMg8IGWK7o/apYJdjwsv1/wjLItPslFiabm8NbHoZlZ73XiI+aRFhHtVd+ptrlGm0b5jJM63YDiGi+4Rb/IXFoZMyZmtm2If31jRMKd0p8jcPat/qubsjnRKFdRKSBqnJymUgVOb/A6SlOBhOfAqCXRJ0AvRBWce3f55YpiqDr50KCJS77E5dDyowvlOcXIbULbqO5MbYMj93Nl8DptG025NLLhevbIltxsVtU9Mr0OTE1ewY8MNOwZFKRM+0lZ1fvuQUJBFNTlqHwa6hbs3BXkc=~3552578~4408887; odin_tt=27b8d72a704b3dd1b987f6309bb1afbde567eb6d8f4108cc0c01daf7b00cc85a6461560b71a5592eb54b6776088e5a22971675b58ccfc9405aea62e1bf507156cec903e457da0accc7dbf02dfdef9cb7; ttwid=1|Y3Nv6hZ_tt-KrXdOWRCHJUZNBnvJt9gACwthXSzp5uY|1650117421|a5d1e6984719ca946c7088a118f5c09ca9468056b9430fd38b2ef693aaeb1eee; cmpl_token=AgQQAPOnF-RMpbFlvj7mvJ04-F-i-0ZR_4csYMA9cQ; bm_mi=7444CFE66808C67F62BCEBB880BD4DB7~UHV9BJZPF2NZr3P4g421EuBTucUNYIexr523/VwvKCGfGzEAfA1abHo8HYcKocxP+laN76JpUglyrLWY/Gkgc2BxZA4J3kAdwnBbz96YgaPRpe2m9+BRU2xTO6kc/ycqlm+3zUicVNfb+BftRwhtikPp+l3bSk4GNtW1kKVJI3DTB2YzhM9BMwiYMTvpxW9tSed75nLNZDJuCY/wP2hwfbmR0+UrKlZggDnPvsfpv8k=; msToken=1gt3-BZ_WjAoOKJxJh77qZAJR0tGKOAx_iKHEG75TaFCWXltux0CfvXETy1S5uFizHuw9DcSWYsip8dnS1EpGdK7gG_7XVOBSU_F7yzjFdB6V9UyhBONnTMqvHgGsO9wY4IXWO0=; bm_sv=EC714A2F6623FDD508362A22220189F7~uPx5OKNtLIB/jt8DLjlHUsoWWA2xFWVI1T6e4HQN01YlW2sITk6VB9L8uvYfK6KWeeNGzPqsa+fnnxgvUnSNA5aYfYIDBepRuxD1J8oSmfnY8CDJOt+09fr3PnZLd+cAvxrBKSE1nAEhvdeNGnN0fTu4h4erxMOH27501pU0E8g=',
            'Origin': 'https://www.tiktok.com',
            'Referer': 'https://www.tiktok.com/'}
        data = {'uniqueld': str(user)}
        try:
            res = requests.get(url, headers=headers, data=data).content
            info = json.loads(res)
            following = info['userInfo']['stats']['followingCount']
            return {'following': str(following)}
        except:
            return False

    def videos(user: str) -> str:
        url = 'https://m.tiktok.com/api/user/detail/?aid=1988&app_name=tiktok_web&device_platform=web_mobile&device_id=7074866456449713670&region=IQ&priority_region=IQ&os=android&referer=&cookie_enabled=true&screen_width=393&screen_height=873&browser_language=ar-EG&browser_platform=Linux+aarch64&browser_name=Mozilla&browser_version=5.0+(Linux;+Android+11;+M2103K19G)+AppleWebKit/537.36+(KHTML,+like+Gecko)+Chrome/99.0.4844.66+Mobile+Safari/537.36&browser_online=true&verifyFp=verify_l0wf3oa3_tprFK83t_Q0pW_4EH0_BU4w_42nV9RgFBTIH&app_language=ar&timezone_name=Asia/Baghdad&is_page_visible=true&focus_state=true&is_fullscreen=false&history_len=2&battery_info={}&uniqueId=' + str(
            user) + '&msToken=4M1DZ-8b03tXs9pqv4iVHGoa9RXRgOB11HjiL7cvs8Sit3X4JTzxsy1FUbmomfk1U3kiown_BdR8lyO_nyxhL6EgNXwVolAz4Qg50PD5imlyx5VhnUkEAeOvU6Gs4ejKs2ODHR8=&X-Bogus=DFSzswSOxhhANtVzSRkg-KW5ZE/N&_signature=_02B4Z6wo0000142Tr2wAAIDC54h1kUWPxv-Nk6vAAIFYd8'
        headers = {
            'User-Agent': str(gdo_drow.get_user_agent()),
            'Accept': 'application/json, text/plain, */*',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
            'Content-Type': 'application/json',
            'Cookie': 'passport_csrf_token=458c72cf0594545b4d8e79bf3caded25; passport_csrf_token_default=458c72cf0594545b4d8e79bf3caded25; passport_auth_status=251fd84db2fafd555a135e73908379b5,; passport_auth_status_ss=251fd84db2fafd555a135e73908379b5,; sid_guard=9eac4270bbe6804badac8696654b064e|1648687327|5184000|Mon,+30-May-2022+00:42:07+GMT; uid_tt=6d8a5958360a534b628ae820fa7a2bdd67e9902f9494fceebe98cd9950759557; uid_tt_ss=6d8a5958360a534b628ae820fa7a2bdd67e9902f9494fceebe98cd9950759557; sid_tt=9eac4270bbe6804badac8696654b064e; sessionid=9eac4270bbe6804badac8696654b064e; sessionid_ss=9eac4270bbe6804badac8696654b064e; sid_ucp_v1=1.0.0-KDQ4MDZkODM4NzQ0MDE1YzNlYjlkOGJjYWMxZDhlYTk3OTY4MWUzYTEKHwiBiLn0lpPUrWEQ3_GTkgYYswsgDDCfpu2KBjgIQBIQAxoGbWFsaXZhIiA5ZWFjNDI3MGJiZTY4MDRiYWRhYzg2OTY2NTRiMDY0ZQ; ssid_ucp_v1=1.0.0-KDQ4MDZkODM4NzQ0MDE1YzNlYjlkOGJjYWMxZDhlYTk3OTY4MWUzYTEKHwiBiLn0lpPUrWEQ3_GTkgYYswsgDDCfpu2KBjgIQBIQAxoGbWFsaXZhIiA5ZWFjNDI3MGJiZTY4MDRiYWRhYzg2OTY2NTRiMDY0ZQ; store-idc=alisg; store-country-code=iq; tt-target-idc=alisg; tt_csrf_token=TOzZoC0p-lXaXuL7lq6ynvJywC006F8ixc-A; _abck=093D884478C406B48D6E8F4696FBC348~-1~YAAQBLR7XL8RDiOAAQAABiCpMgf/mTykvtzUPdMKxO5b9PAf4oFOTanUbEbor2OmIngPpyC6Gzf66YjbaUUGpIPpBJ6ZwPhpCdVw4jctEx+wSCOttDZjMU65rD6zxWbtErf36ZnocPLoCiwN5pagDq/K3e/s5O4bpPtO5xf8le7+yGLPsEHjMwGneEj6YSGYSE9QauyY6FvziUVCTSNQiuEUC8Soy+kufKxVEpwwzN5Zo1KV1q1rw4rtClwvCDo4CEi8icykPZfjta2PKf2zax/B4euHxWX5mzFP7HmPFsmBK8UQvmAM++ZUF7AY52kH1Polr7cB9ziWZAuRcLRO4UIKu35+cMb4xjJH3bAWXZXX5DaFoi55crdz3h9RBRzmCDTB5LPPiIN/RDA=~-1~-1~-1; ak_bmsc=3B8069AEE7E00870B984D180ECFFBD5D~000000000000000000000000000000~YAAQBLR7XMARDiOAAQAABiCpMg9auExniSBpZbCVcLzVPFqefIbpGImTcAxDH2gABB5UwaA2MVjucEhh3S7gz30SLbwpNUNrz1kgII1USn5iNT3nlqfwkJVlcGM/1WSVAAT4ZgMH9JJsS//Ev2hNH0Ux3RbCPvS+5d88mwT/lNKfrvgYT1zmm+1gb21gQNNIgnt3RSvR26eNTW80k36v2qJi1mLyiQVZYD3rRi94vlyWRGASfWooBznWg99OujqaSU2DXh2EuyupYmhBBkiOFvQFkvapmgdgfcIRy9HQJROh4YzV3aFuxOWpi+5a0DxdYE5kuh4dcEjOL7RDIukoWWNvcjLhX2ViXpIsA2NyFLbWTPq5nQFOArd4a+KagglgXyHAIX41UAg=; bm_sz=C6365C417EF2307C8B0C15C7E15B62F5~YAAQBLR7XMERDiOAAQAABiCpMg8IGWK7o/apYJdjwsv1/wjLItPslFiabm8NbHoZlZ73XiI+aRFhHtVd+ptrlGm0b5jJM63YDiGi+4Rb/IXFoZMyZmtm2If31jRMKd0p8jcPat/qubsjnRKFdRKSBqnJymUgVOb/A6SlOBhOfAqCXRJ0AvRBWce3f55YpiqDr50KCJS77E5dDyowvlOcXIbULbqO5MbYMj93Nl8DptG025NLLhevbIltxsVtU9Mr0OTE1ewY8MNOwZFKRM+0lZ1fvuQUJBFNTlqHwa6hbs3BXkc=~3552578~4408887; odin_tt=27b8d72a704b3dd1b987f6309bb1afbde567eb6d8f4108cc0c01daf7b00cc85a6461560b71a5592eb54b6776088e5a22971675b58ccfc9405aea62e1bf507156cec903e457da0accc7dbf02dfdef9cb7; ttwid=1|Y3Nv6hZ_tt-KrXdOWRCHJUZNBnvJt9gACwthXSzp5uY|1650117421|a5d1e6984719ca946c7088a118f5c09ca9468056b9430fd38b2ef693aaeb1eee; cmpl_token=AgQQAPOnF-RMpbFlvj7mvJ04-F-i-0ZR_4csYMA9cQ; bm_mi=7444CFE66808C67F62BCEBB880BD4DB7~UHV9BJZPF2NZr3P4g421EuBTucUNYIexr523/VwvKCGfGzEAfA1abHo8HYcKocxP+laN76JpUglyrLWY/Gkgc2BxZA4J3kAdwnBbz96YgaPRpe2m9+BRU2xTO6kc/ycqlm+3zUicVNfb+BftRwhtikPp+l3bSk4GNtW1kKVJI3DTB2YzhM9BMwiYMTvpxW9tSed75nLNZDJuCY/wP2hwfbmR0+UrKlZggDnPvsfpv8k=; msToken=1gt3-BZ_WjAoOKJxJh77qZAJR0tGKOAx_iKHEG75TaFCWXltux0CfvXETy1S5uFizHuw9DcSWYsip8dnS1EpGdK7gG_7XVOBSU_F7yzjFdB6V9UyhBONnTMqvHgGsO9wY4IXWO0=; bm_sv=EC714A2F6623FDD508362A22220189F7~uPx5OKNtLIB/jt8DLjlHUsoWWA2xFWVI1T6e4HQN01YlW2sITk6VB9L8uvYfK6KWeeNGzPqsa+fnnxgvUnSNA5aYfYIDBepRuxD1J8oSmfnY8CDJOt+09fr3PnZLd+cAvxrBKSE1nAEhvdeNGnN0fTu4h4erxMOH27501pU0E8g=',
            'Origin': 'https://www.tiktok.com',
            'Referer': 'https://www.tiktok.com/'}
        data = {'uniqueld': str(user)}
        try:
            res = requests.get(url, headers=headers, data=data).content
            info = json.loads(res)
            video = info['userInfo']['stats']['videoCount']
            return {'videos': str(video)}
        except:
            return False

    def heart(user: str) -> str:
        url = 'https://m.tiktok.com/api/user/detail/?aid=1988&app_name=tiktok_web&device_platform=web_mobile&device_id=7074866456449713670&region=IQ&priority_region=IQ&os=android&referer=&cookie_enabled=true&screen_width=393&screen_height=873&browser_language=ar-EG&browser_platform=Linux+aarch64&browser_name=Mozilla&browser_version=5.0+(Linux;+Android+11;+M2103K19G)+AppleWebKit/537.36+(KHTML,+like+Gecko)+Chrome/99.0.4844.66+Mobile+Safari/537.36&browser_online=true&verifyFp=verify_l0wf3oa3_tprFK83t_Q0pW_4EH0_BU4w_42nV9RgFBTIH&app_language=ar&timezone_name=Asia/Baghdad&is_page_visible=true&focus_state=true&is_fullscreen=false&history_len=2&battery_info={}&uniqueId=' + str(
            user) + '&msToken=4M1DZ-8b03tXs9pqv4iVHGoa9RXRgOB11HjiL7cvs8Sit3X4JTzxsy1FUbmomfk1U3kiown_BdR8lyO_nyxhL6EgNXwVolAz4Qg50PD5imlyx5VhnUkEAeOvU6Gs4ejKs2ODHR8=&X-Bogus=DFSzswSOxhhANtVzSRkg-KW5ZE/N&_signature=_02B4Z6wo0000142Tr2wAAIDC54h1kUWPxv-Nk6vAAIFYd8'
        headers = {
            'User-Agent': str(gdo_drow.get_user_agent()),
            'Accept': 'application/json, text/plain, */*',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
            'Content-Type': 'application/json',
            'Cookie': 'passport_csrf_token=458c72cf0594545b4d8e79bf3caded25; passport_csrf_token_default=458c72cf0594545b4d8e79bf3caded25; passport_auth_status=251fd84db2fafd555a135e73908379b5,; passport_auth_status_ss=251fd84db2fafd555a135e73908379b5,; sid_guard=9eac4270bbe6804badac8696654b064e|1648687327|5184000|Mon,+30-May-2022+00:42:07+GMT; uid_tt=6d8a5958360a534b628ae820fa7a2bdd67e9902f9494fceebe98cd9950759557; uid_tt_ss=6d8a5958360a534b628ae820fa7a2bdd67e9902f9494fceebe98cd9950759557; sid_tt=9eac4270bbe6804badac8696654b064e; sessionid=9eac4270bbe6804badac8696654b064e; sessionid_ss=9eac4270bbe6804badac8696654b064e; sid_ucp_v1=1.0.0-KDQ4MDZkODM4NzQ0MDE1YzNlYjlkOGJjYWMxZDhlYTk3OTY4MWUzYTEKHwiBiLn0lpPUrWEQ3_GTkgYYswsgDDCfpu2KBjgIQBIQAxoGbWFsaXZhIiA5ZWFjNDI3MGJiZTY4MDRiYWRhYzg2OTY2NTRiMDY0ZQ; ssid_ucp_v1=1.0.0-KDQ4MDZkODM4NzQ0MDE1YzNlYjlkOGJjYWMxZDhlYTk3OTY4MWUzYTEKHwiBiLn0lpPUrWEQ3_GTkgYYswsgDDCfpu2KBjgIQBIQAxoGbWFsaXZhIiA5ZWFjNDI3MGJiZTY4MDRiYWRhYzg2OTY2NTRiMDY0ZQ; store-idc=alisg; store-country-code=iq; tt-target-idc=alisg; tt_csrf_token=TOzZoC0p-lXaXuL7lq6ynvJywC006F8ixc-A; _abck=093D884478C406B48D6E8F4696FBC348~-1~YAAQBLR7XL8RDiOAAQAABiCpMgf/mTykvtzUPdMKxO5b9PAf4oFOTanUbEbor2OmIngPpyC6Gzf66YjbaUUGpIPpBJ6ZwPhpCdVw4jctEx+wSCOttDZjMU65rD6zxWbtErf36ZnocPLoCiwN5pagDq/K3e/s5O4bpPtO5xf8le7+yGLPsEHjMwGneEj6YSGYSE9QauyY6FvziUVCTSNQiuEUC8Soy+kufKxVEpwwzN5Zo1KV1q1rw4rtClwvCDo4CEi8icykPZfjta2PKf2zax/B4euHxWX5mzFP7HmPFsmBK8UQvmAM++ZUF7AY52kH1Polr7cB9ziWZAuRcLRO4UIKu35+cMb4xjJH3bAWXZXX5DaFoi55crdz3h9RBRzmCDTB5LPPiIN/RDA=~-1~-1~-1; ak_bmsc=3B8069AEE7E00870B984D180ECFFBD5D~000000000000000000000000000000~YAAQBLR7XMARDiOAAQAABiCpMg9auExniSBpZbCVcLzVPFqefIbpGImTcAxDH2gABB5UwaA2MVjucEhh3S7gz30SLbwpNUNrz1kgII1USn5iNT3nlqfwkJVlcGM/1WSVAAT4ZgMH9JJsS//Ev2hNH0Ux3RbCPvS+5d88mwT/lNKfrvgYT1zmm+1gb21gQNNIgnt3RSvR26eNTW80k36v2qJi1mLyiQVZYD3rRi94vlyWRGASfWooBznWg99OujqaSU2DXh2EuyupYmhBBkiOFvQFkvapmgdgfcIRy9HQJROh4YzV3aFuxOWpi+5a0DxdYE5kuh4dcEjOL7RDIukoWWNvcjLhX2ViXpIsA2NyFLbWTPq5nQFOArd4a+KagglgXyHAIX41UAg=; bm_sz=C6365C417EF2307C8B0C15C7E15B62F5~YAAQBLR7XMERDiOAAQAABiCpMg8IGWK7o/apYJdjwsv1/wjLItPslFiabm8NbHoZlZ73XiI+aRFhHtVd+ptrlGm0b5jJM63YDiGi+4Rb/IXFoZMyZmtm2If31jRMKd0p8jcPat/qubsjnRKFdRKSBqnJymUgVOb/A6SlOBhOfAqCXRJ0AvRBWce3f55YpiqDr50KCJS77E5dDyowvlOcXIbULbqO5MbYMj93Nl8DptG025NLLhevbIltxsVtU9Mr0OTE1ewY8MNOwZFKRM+0lZ1fvuQUJBFNTlqHwa6hbs3BXkc=~3552578~4408887; odin_tt=27b8d72a704b3dd1b987f6309bb1afbde567eb6d8f4108cc0c01daf7b00cc85a6461560b71a5592eb54b6776088e5a22971675b58ccfc9405aea62e1bf507156cec903e457da0accc7dbf02dfdef9cb7; ttwid=1|Y3Nv6hZ_tt-KrXdOWRCHJUZNBnvJt9gACwthXSzp5uY|1650117421|a5d1e6984719ca946c7088a118f5c09ca9468056b9430fd38b2ef693aaeb1eee; cmpl_token=AgQQAPOnF-RMpbFlvj7mvJ04-F-i-0ZR_4csYMA9cQ; bm_mi=7444CFE66808C67F62BCEBB880BD4DB7~UHV9BJZPF2NZr3P4g421EuBTucUNYIexr523/VwvKCGfGzEAfA1abHo8HYcKocxP+laN76JpUglyrLWY/Gkgc2BxZA4J3kAdwnBbz96YgaPRpe2m9+BRU2xTO6kc/ycqlm+3zUicVNfb+BftRwhtikPp+l3bSk4GNtW1kKVJI3DTB2YzhM9BMwiYMTvpxW9tSed75nLNZDJuCY/wP2hwfbmR0+UrKlZggDnPvsfpv8k=; msToken=1gt3-BZ_WjAoOKJxJh77qZAJR0tGKOAx_iKHEG75TaFCWXltux0CfvXETy1S5uFizHuw9DcSWYsip8dnS1EpGdK7gG_7XVOBSU_F7yzjFdB6V9UyhBONnTMqvHgGsO9wY4IXWO0=; bm_sv=EC714A2F6623FDD508362A22220189F7~uPx5OKNtLIB/jt8DLjlHUsoWWA2xFWVI1T6e4HQN01YlW2sITk6VB9L8uvYfK6KWeeNGzPqsa+fnnxgvUnSNA5aYfYIDBepRuxD1J8oSmfnY8CDJOt+09fr3PnZLd+cAvxrBKSE1nAEhvdeNGnN0fTu4h4erxMOH27501pU0E8g=',
            'Origin': 'https://www.tiktok.com',
            'Referer': 'https://www.tiktok.com/'}
        data = {'uniqueld': str(user)}
        try:
            res = requests.get(url, headers=headers, data=data).content
            info = json.loads(res)
            heart = info['userInfo']['stats']['heartCount']
            return {'heart': str(heart)}
        except:
            return False

# -------------------------[CoDe BY GDØ]------------------------
# -------------------------[CoDe BY GDØ]------------------------
# -------------------------[CoDe BY GDØ]------------------------