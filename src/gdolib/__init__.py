import os
try:
    import requests , user_agent , names , uuid , urllib , hashlib , mechanize , instaloader
except ModuleNotFoundError:
    os.system('pip install requests')
    os.system('pip install user_agent')
    os.system('pip install names')
    os.system('pip install uuid')
    os.system('pip install mechanize')
    os.system('pip install instaloader')

from .gdo_drow import gdo_drow
from .check_email import check_email, more
from .gdo_order import gdo_order
from .IG import info_IG , session_IG , login_IG , create_IG
from .info_face import info_face
from .info_tiktok import info_tik
from .login import login