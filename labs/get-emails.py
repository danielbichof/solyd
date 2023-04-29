import requests

EMAILS =  []

for i in range(36):
	response = requests.get(f"http://localhost:3000/rest/products/{i}/reviews")
	data = response.json()
	for review in data["data"]:
		email = review["author"]
		if email not in EMAILS:
			print(email)
			EMAILS.append(email)
