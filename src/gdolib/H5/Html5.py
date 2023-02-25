import os
import time
import webbrowser
import requests


"""

Programed language used: html, css, python

type code help()

~ folow us in Telegram : @gdolib, @gdo_0.

"""


def help():
	codes="""codes of library /help
	
_______________________________________________________________

h1, h2, h3, h4, h5, h6 --> have(text,style,name,id,__class__)
_______________________________________________________________

img(src,text,id,style,name',alt,__class__)

a(text,target,id,name,href,style,__class__)
_______________________________________________________________

input(name,id,text,style,placeholder,__class__)

button(name,id,text,style,__class__)

textarea(name,id,style,text,placeholder,__class__)

br() --> used for spacing
_______________________________________________________________

line, DTH, html_start/end, head_start/end, body_start/end --> just add

line(count)
_______________________________________________________________

title(text)

style(id,__class__,styles)
_______________________________________________________________

html_add(code) --> Add codes to written codes

html_free(code) --> Write all the codes on without any additions

get_source_code_form(url) --> get source code form by url
_______________________________________________________________

run?

H5.run(port) without port or with

example :

H5.run(port=8888)

or

H5.run()

or 

H5.run(auto_open=True)

_______________________________________________________________
	"""
	for i in codes.splitlines():
		print(i)
		time.sleep(0.01)


file1 = open("H5.html",'w')
file1.write('')


def run(port=None,auto_open=''):
	if not port:
		print('\033[1;31mRunnig By \033[1;32mGDO\033[0;37m ')
		print('[port] http://127.0.0.1:8000/H5.html')
		if auto_open == True:
			webbrowser.open('http://127.0.0.1:8000/H5.html')
		os.system('python3 -m http.server 8000')
		
	else:
		print('\033[1;31mHosted By \033[1;32mTrackCobra\033[0;37m ')
		print(f'[port] http://127.0.0.1:{port}/H5.html')
		if auto_open == True:
			webbrowser.open(f'http://127.0.0.1:{port}/H5.html')
		os.system(f'python3 -m http.server {port}')


def DTH():
	file = open('H5.html','a')
	file.write('<!DOCTYPE Html>')
	file.close()


def html_start():
	file = open('H5.html','a')
	file.write('<html>')
	file.close()


def html_end():
	file = open('H5.html','a')
	file.write('</html>')
	file.close()


def head_start():
	file = open('H5.html','a')
	file.write('<head>')
	file.close()


def head_end():
	file = open('H5.html','a')
	file.write('</head>')
	file.close()


def title(text='gdolib'):
	file = open('H5.html','a')
	file.write(f'<title>{text}</title>')
	file.close()


def style(__class__=None,id=None,styles=None):
	file = open('H5.html','a')
	file.write('<style>')
	file.close()
	if not __class__:
		name=None
	else:
		file = open('H5.html','a')
		file.write(f'.{__class__}'+'{'+styles+'}')
		file.close()

	if not id:
		name=None
	else:
		file = open('H5.html','a')
		file.write(f'#{id}'+'{'+styles+'}')
		file.close()

	file = open('H5.html','a')
	file.write(f'</style>')
	file.close()


def body_start():
	file = open('H5.html','a')
	file.write('<body>')
	file.close()


def body_end():
	file = open('H5.html','a')
	file.write('</body>')
	file.close()


def html_free(code):
	file = open('H5.html','w')
	file.write(f"""{code}""")
	file.close()


def html_add(code):
	file = open('H5.html','a')
	file.write(f"""{code}""")
	file.close()


def br():
	file = open('H5.html','a')
	file.write('<br></br>')
	file.close()


def line(count=0):
	file = open('H5.html','a')
	file.write('\n' * count)
	file.close()


def button(name=None,id=None,text=None,style=None,__class__=None):
	file = open('H5.html','a')
	file.write('<button ')
	file.close()
	if not name:
		none=None
	else:
		file = open('H5.html','a')
		file.write(f'name="{name}" ')
		file.close()

	if not id:
		none=None
	else:
		file = open('H5.html','a')
		file.write(f'id="{id}" ')
		file.close()

	if not __class__:
		none=None
	else:
		file = open('H5.html','a')
		file.write(f'class="{__class__}" ')
		file.close()

	if not style:
		none=None
	else:
		file = open('H5.html','a')
		file.write(f'style="{style}" ')
		file.close()

	if not text:
		none=None
	else:
		file = open('H5.html','a')
		file.write(f'>{text}')
		file.close()

	file = open('H5.html','a')
	file.write('</button>')
	file.close()


def input(name=None,id=None,text=None,style=None,placeholder=None,__class__=None):
	file = open('H5.html','a')
	file.write('<input ')
	file.close()
	if not name:
		none=None
	else:
		file = open('H5.html','a')
		file.write(f'name="{name}" ')
		file.close()

	if not id:
		none=None
	else:
		file = open('H5.html','a')
		file.write(f'id="{id}" ')
		file.close()

	if not __class__:
		none=None
	else:
		file = open('H5.html','a')
		file.write(f'class="{__class__}" ')
		file.close()

	if not style:
		none=None
	else:
		file = open('H5.html','a')
		file.write(f'style="{style}" ')
		file.close()

	if not placeholder:
		none=None
	else:
		file = open('H5.html','a')
		file.write(f'placeholder="{placeholder}"')
		file.close()

	if not text:
		none=None
	else:
		file = open('H5.html','a')
		file.write(f'>{text}')
		file.close()

	file = open('H5.html','a')
	file.write('</input>')
	file.close()


def textarea(name=None,id=None,style=None,text=None,placeholder=None,__class__=None):
	file = open('H5.html','a')
	file.write('<textarea ')
	file.close()
	if not name:
		none=None
	else:
		file = open('H5.html','a')
		file.write(f'name="{name}" ')
		file.close()

	if not id:
		none=None
	else:
		file = open('H5.html','a')
		file.write(f'id="{id}" ')
		file.close()

	if not __class__:
		none=None
	else:
		file = open('H5.html','a')
		file.write(f'class="{__class__}" ')
		file.close()

	if not style:
		none=None
	else:
		file = open('H5.html','a')
		file.write(f'style="{style}" ')
		file.close()

	if not placeholder:
		none=None
	else:
		file = open('H5.html','a')
		file.write(f'placeholder="{placeholder}"')
		file.close()

	if not text:
		none=None
	else:
		file = open('H5.html','a')
		file.write(f'>{text}')
		file.close()

	file = open('H5.html','a')
	file.write('</textarea>')
	file.close()


def a(text=None,target=None,id=None,name=None,href=None,style=None,__class__=None):
	file = open('H5.html','a')
	file.write('<a ')
	file.close()
	if not name:
		none=None
	else:
		file = open('H5.html','a')
		file.write(f'name="{name}" ')
		file.close()

	if not target:
		none=None
	else:
		file = open('H5.html','a')
		file.write(f'target="{target}" ')
		file.close()

	if not id:
		none=None
	else:
		file = open('H5.html','a')
		file.write(f'id="{id}" ')
		file.close()

	if not __class__:
		none=None
	else:
		file = open('H5.html','a')
		file.write(f'class="{__class__}" ')
		file.close()

	if not href:
		none=None
	else:
		file = open('H5.html','a')
		file.write(f'href="{href}" ')
		file.close()

	if not style:
		none=None
	else:
		file = open('H5.html','a')
		file.write(f'style="{style}" ')
		file.close()

	if not text:
		none=None
	else:
		file = open('H5.html','a')
		file.write(f'>{text}')
		file.close()

	file = open('H5.html','a')
	file.write('</a>')
	file.close()


def img(src=None,text=None,id=None,style=None,name=None,alt=None,__class__=None):
	file = open('H5.html','a')
	file.write('<img ')
	file.close()
	if not name:
		none=None
	else:
		file = open('H5.html','a')
		file.write(f'name="{name}" ')
		file.close()

	if not src:
		none=None
	else:
		file = open('H5.html','a')
		file.write(f'src="{src}" ')
		file.close()

	if not id:
		none=None
	else:
		file = open('H5.html','a')
		file.write(f'id="{id}" ')
		file.close()

	if not __class__:
		none=None
	else:
		file = open('H5.html','a')
		file.write(f'class="{__class__}" ')
		file.close()

	if not alt:
		none=None
	else:
		file = open('H5.html','a')
		file.write(f'alt="{alt}" ')
		file.close()

	if not style:
		none=None
	else:
		file = open('H5.html','a')
		file.write(f'style="{style}" ')
		file.close()

	if not text:
		none=None
	else:
		file = open('H5.html','a')
		file.write(f'>{text}')
		file.close()

	file = open('H5.html','a')
	file.write('>')
	file.close()



def h1(name=None,id=None,text=None,style=None,__class__=None):
	file = open('H5.html','a')
	file.write('<h1 ')
	file.close()
	if not name:
		none=None
	else:
		file = open('H5.html','a')
		file.write(f'name="{name}" ')
		file.close()

	if not id:
		none=None
	else:
		file = open('H5.html','a')
		file.write(f'id="{id}" ')
		file.close()

	if not __class__:
		none=None
	else:
		file = open('H5.html','a')
		file.write(f'class="{__class__}" ')
		file.close()

	if not style:
		none=None
	else:
		file = open('H5.html','a')
		file.write(f'style="{style}" ')
		file.close()

	if not text:
		none=None
	else:
		file = open('H5.html','a')
		file.write(f'>{text}')
		file.close()
	file = open('H5.html','a')
	file.write('</h1>')
	file.close()


def h2(name=None,id=None,text=None,style=None,__class__=None):
	file = open('H5.html','a')
	file.write('<h2 ')
	file.close()
	if not name:
		none=None
	else:
		file = open('H5.html','a')
		file.write(f'name="{name}" ')
		file.close()

	if not id:
		none=None
	else:
		file = open('H5.html','a')
		file.write(f'id="{id}" ')
		file.close()

	if not __class__:
		none=None
	else:
		file = open('H5.html','a')
		file.write(f'class="{__class__}" ')
		file.close()

	if not style:
		none=None
	else:
		file = open('H5.html','a')
		file.write(f'style="{style}" ')
		file.close()

	if not text:
		none=None
	else:
		file = open('H5.html','a')
		file.write(f'>{text}')
		file.close()
	file = open('H5.html','a')
	file.write('</h2>')
	file.close()


def h3(name=None,id=None,text=None,style=None,__class__=None):
	file = open('H5.html','a')
	file.write('<h3 ')
	file.close()

	if not name:
		none=None
	else:
		file = open('H5.html','a')
		file.write(f'name="{name}" ')
		file.close()

	if not id:
		none=None
	else:
		file = open('H5.html','a')
		file.write(f'id="{id}" ')
		file.close()

	if not __class__:
		none=None
	else:
		file = open('H5.html','a')
		file.write(f'class="{__class__}" ')
		file.close()

	if not style:
		none=None
	else:
		file = open('H5.html','a')
		file.write(f'style="{style}" ')
		file.close()

	if not text:
		none=None
	else:
		file = open('H5.html','a')
		file.write(f'>{text}')
		file.close()
	file = open('H5.html','a')
	file.write('</h3>')
	file.close()


def h4(name=None,id=None,text=None,style=None,__class__=None):
	file = open('H5.html','a')
	file.write('<h4 ')
	file.close()

	if not name:
		none=None
	else:
		file = open('H5.html','a')
		file.write(f'name="{name}" ')
		file.close()

	if not id:
		none=None
	else:
		file = open('H5.html','a')
		file.write(f'id="{id}" ')
		file.close()

	if not __class__:
		none=None
	else:
		file = open('H5.html','a')
		file.write(f'class="{__class__}" ')
		file.close()

	if not style:
		none=None
	else:
		file = open('H5.html','a')
		file.write(f'style="{style}" ')
		file.close()

	if not text:
		none=None
	else:
		file = open('H5.html','a')
		file.write(f'>{text}')
		file.close()

	file = open('H5.html','a')
	file.write('</h4')
	file.close()


def h5(name=None,id=None,text=None,style=None,__class__=None):
	file = open('H5.html','a')
	file.write('<h5 ')
	file.close()
	if not name:
		none=None
	else:
		file = open('H5.html','a')
		file.write(f'name="{name}" ')
		file.close()

	if not id:
		none=None
	else:
		file = open('H5.html','a')
		file.write(f'id="{id}" ')
		file.close()

	if not __class__:
		none=None
	else:
		file = open('H5.html','a')
		file.write(f'class="{__class__}" ')
		file.close()

	if not style:
		none=None
	else:
		file = open('H5.html','a')
		file.write(f'style="{style}" ')
		file.close()

	if not text:
		none=None
	else:
		file = open('H5.html','a')
		file.write(f'>{text}')
		file.close()

	file = open('H5.html','a')
	file.write('</h5>')
	file.close()


def h6(name=None,id=None,text=None,style=None,__class__=None):
	file = open('H5.html','a')
	file.write('<h6 ')
	file.close()
	if not name:
		none=None
	else:
		file = open('H5.html','a')
		file.write(f'name="{name}" ')
		file.close()

	if not id:
		none=None
	else:
		file = open('H5.html','a')
		file.write(f'id="{id}" ')
		file.close()

	if not __class__:
		none=None
	else:
		file = open('H5.html','a')
		file.write(f'class="{__class__}" ')
		file.close()

	if not style:
		none=None
	else:
		file = open('H5.html','a')
		file.write(f'style="{style}" ')
		file.close()

	if not text:
		none=None
	else:
		file = open('H5.html','a')
		file.write(f'>{text}')
		file.close()

	file = open('H5.html','a')
	file.write('</h6>')
	file.close()


def get_source_code_form(url=None):
	if not url:
		raise ValueError('argument "url" required')
	if 'http' in url:
		code = requests.get(url).text
		file = open('H5.html','w')
		file.write(str(code))
		file.close()
	else:
		print(' Not Found http/https !!?') 
