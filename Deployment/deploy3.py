import requests
base_url = 'http://127.0.0.1:8007/lr?x1='

x1 = str(input("Enter the value of x1: "))
x2 = str(input("Enter the value of x2: "))

url = base_url+x1+"&x2="+x2

r = requests.get(url)

if r.status_code == 200:
	r = r.json()
	print("Prediction:",r)
