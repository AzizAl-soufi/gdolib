import requests

class fake:
	
	def first_name():
		url = "https://randomuser.me/api?nat=US"
		res = requests.get(url).text
		first = res.split('first":"')[1].split('"')[0]
		return first
		
		
	def last_name():
		url = "https://randomuser.me/api?nat=US"
		res = requests.get(url).text
		last = res.split('last":"')[1].split('"')[0]
		return last
		
		
	def full_name():
		url = "https://randomuser.me/api?nat=US"
		res = requests.get(url).text
		first = res.split('first":"')[1].split('"')[0]
		last = res.split('last":"')[1].split('"')[0]
		full = f'{first} {last}'
		return last

			
	def username():
		url = "https://randomuser.me/api?nat=US"
		res = requests.get(url).text
		user = res.split('"username":"')[1].split('"')[0]
		return user

		
	def email():
		url = "https://randomuser.me/api?nat=US"
		res = requests.get(url).text
		email = res.split('"email":"')[1].split('"')[0]
		return email


	def city():
		url = "https://randomuser.me/api?nat=US"
		res = requests.get(url).text
		city = res.split('"city":"')[1].split('"')[0]
		return city
	
	
	def country():
		url = "https://randomuser.me/api?nat=US"
		res = requests.get(url).text
		country = res.split('"country":"')[1].split('"')[0]
		return country
		
	
	def phone():
		url = "https://randomuser.me/api?nat=US"
		res = requests.get(url).text
		phone = res.split('"phone":"')[1].split('"')[0]
		return phone
		
	
	def state():
		url = "https://randomuser.me/api?nat=US"
		res = requests.get(url).text
		state = res.split('"state":"')[1].split('"')[0]
		return state
		
	
	def user():
		url = "https://randomuser.me/api?nat=US"
		res = requests.get(url).text
		first = res.split('first":"')[1].split('"')[0]
		last = res.split('last":"')[1].split('"')[0]
		full = f'{first} {last}'
		user = res.split('"username":"')[1].split('"')[0]
		email = res.split('"email":"')[1].split('"')[0]
		city = res.split('"city":"')[1].split('"')[0]
		country = res.split('"country":"')[1].split('"')[0]
		state = res.split('"state":"')[1].split('"')[0]
		message = {
		'first_name':first,'last_name':last,
		'full_name':full,'username':user,
		'email':email,'city':city,
		'country':country,'state':state}
		return message