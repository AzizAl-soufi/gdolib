class order:

    def headers_ssl(info: str) -> str:
        try:
            return "headers = {}\n" + '\n'.join(str("headers['"+i.split(': ')[0]+"']='"+i.split(': ')[1]+"'").replace(" ", "") for i in info.splitlines())
        except IndexError:
            return False

    def headers(info: str) -> str:
        try:
            return {a.split(': ')[0]:a.split(': ')[1] for a in info.splitlines()}
        except IndexError:
            return False

    def headers_config(api: str) -> str:
        try:
            asp = "  HEADER " + '"' + api + '"'
            return asp
        except IndexError:
            return False

    def edit_domin_email(email: str, domin: str) -> str:
        try:
            email = str(email)
            email = str(email.split("@")[0]) + str(domin)
            return email
        except IndexError:
            return False

    def add_domin_user(user: str, domin: str) -> str:
        user = str(user)
        if "@" in user:
            user = user.split('@')[0]
            email = user + domin
            return email
        else:
            email = user + domin
            return email

    def del_domin_email(email: str) -> str:
        email = str(email)
        if "@" in email:
            azoz = email.split("@")[0]
            return azoz
        else:
            azoz = email
            return azoz

# -------------------------[CoDe BY GDØ]------------------------
# -------------------------[CoDe BY GDØ]------------------------
# -------------------------[CoDe BY GDØ]------------------------
