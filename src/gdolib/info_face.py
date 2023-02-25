import requests , uuid

class info_face:

    def get_id_for_url(url: str) -> str:
        url = str(url)
        try:
            res = requests.get(url).text
            if ('userID":"') in res:
                uid = res.split('userID":"')[1]
                id = uid.split('",')[0]
                return {'status' :'true' ,'userID' :str(id)}
            else:
                return {'status' :'false' ,'userID' :None}

        except:
            return False


    def get_token_id(email: str, password: str) -> str:
        url = "https://b-graph.facebook.com/auth/login"
        headers = {
            "authorization": "OAuth 200424423651082|2a9918c6bcd75b94cefcbb5635c6ad16",
            "user-agent": "Dalvik/2.1.0 (Linux; U; Android 10; BLA-L29 Build/HUAWEIBLA-L29S) [FBAN/MessengerLite;FBAV/305.0.0.7.106;FBPN/com.facebook.mlite;FBLC/ar_PS;FBBV/372376702;FBCR/Ooredoo;FBMF/HUAWEI;FBBD/HUAWEI;FBDV/BLA-L29;FBSV/10;FBCA/arm64-v8a:null;FBDM/{density=3.0,width=1080,height=2040};]"}
        data = f"email={email}&password={password}&credentials_type=password&error_detail_type=button_with_disabled&format=json&device_id={uuid.uuid4()}&generate_session_cookies=1&generate_analytics_claim=1&generate_machine_id=1&method=POST"
        res = requests.post(url, data=data, headers=headers ,verify=False, timeout=15).json()
        if list(res)[0] == "session_key":
            message = {
                'status' :'Success',
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

    def name(id: str, token: str) -> str:
        id = str(id);token = str(token)
        try:
            res = requests.get('https://graph.facebook.com/%s?access_token=%s ' %(id ,token)).json()
            name = (res['name'])
            return name
        except:
            return False


    def first_name(id: str, token: str) -> str:
        id = str(id);token = str(token)
        try:
            res = requests.get('https://graph.facebook.com/%s?access_token=%s ' %(id ,token)).json()
            name = (res['first_name'])
            return name
        except:
            return False

    def last_name(id: str, token: str) -> str:
        id = str(id);token = str(token)
        try:
            res = requests.get('https://graph.facebook.com/%s?access_token=%s ' %(id ,token)).json()
            name = (res['last_name'])
            return name
        except:
            return False

    def username(id: str, token: str) -> str:
        id = str(id);token = str(token)
        try:
            res = requests.get('https://graph.facebook.com/%s?access_token=%s ' %(id ,token)).json()
            name = (res['username'])
            return name
        except:
            return False

    def email(id: str, token: str) -> str:
        id = str(id);token = str(token)
        try:
            res = requests.get('https://graph.facebook.com/%s?access_token=%s ' %(id ,token)).json()
            name = (res['email'])
            return name
        except:
            return False


    def phone(id: str, token: str) -> str:
        id = str(id);token = str(token)
        try:
            res = requests.get('https://graph.facebook.com/%s?access_token=%s ' %(id ,token)).json()
            name = (res['mobile_phone'])
            return name
        except:
            return False

    def birthday(id: str, token: str) -> str:
        id = str(id);token = str(token)
        try:
            res = requests.get('https://graph.facebook.com/%s?access_token=%s ' %(id ,token)).json()
            name = (res['birthday'])
            return name
        except:
            return False


    def gender(id: str, token: str) -> str:
        id = str(id);token = str(token)
        try:
            res = requests.get('https://graph.facebook.com/%s?access_token=%s ' %(id ,token)).json()
            name = (res['gender'])
            return name
        except:
            return False


    def link(id: str, token: str) -> str:
        id = str(id);token = str(token)
        try:
            res = requests.get('https://graph.facebook.com/%s?access_token=%s ' %(id ,token)).json()
            name = (res['link'])
            return name
        except:
            return False

    def status(id: str, token: str) -> str:
        id = str(id);token = str(token)
        try:
            res = requests.get('https://graph.facebook.com/%s?access_token=%s ' %(id ,token)).json()
            name = (res['relationship_status'])
            return name
        except:
            return False


    def bio(id: str, token: str) -> str:
        id = str(id);token = str(token)
        try:
            res = requests.get('https://graph.facebook.com/%s?access_token=%s ' %(id ,token)).json()
            name = (res['about'])
            return name
        except:
            return False


    def hometown(id: str, token: str) -> str:
        id = str(id);token = str(token)
        try:
            res = requests.get('https://graph.facebook.com/%s?access_token=%s ' %(id ,token)).json()
            name = (res['hometown']['name'])
            return name
        except:
            return False


    def location(id: str, token: str) -> str:
        id = str(id);token = str(token)
        try:
            res = requests.get('https://graph.facebook.com/%s?access_token=%s ' %(id ,token)).json()
            name = (res['location']['name'])
            return name
        except:
            return False


    def timezone(id: str, token: str) -> str:
        id = str(id);token = str(token)
        try:
            res = requests.get('https://graph.facebook.com/%s?access_token=%s ' %(id ,token)).json()
            name = (res['timezone'])
            return name
        except:
            return False


    def updated_time(id: str, token: str) -> str:
        id = str(id);token = str(token)
        try:
            res = requests.get('https://graph.facebook.com/%s?access_token=%s ' %(id ,token)).json()
            name = (res['updated_time'])
            return name
        except:
            return False


    def friends(id: str, token: str) -> str:
        id = str(id);token = str(token)
        try:
            res = requests.get('https://graph.facebook.com/%s/friends?limit=50000&access_token=%s ' %(id, token)).json()
            friends = []
            for i in res['data']:
                friends.append(i['id'])

            return str(len(friends))
        except:
            return False


    def followers(id: str, token: str) -> str:
        id = str(id);token = str(token)
        try:
            res = requests.get('https://graph.facebook.com/%s/subscribers?access_token=%s ' %(id, token)).json()
            followers = res['summary']['total_count']
            return followers
        except:
            return False

# -------------------------[CoDe BY GDØ]------------------------
# -------------------------[CoDe BY GDØ]------------------------
# -------------------------[CoDe BY GDØ-------------------------