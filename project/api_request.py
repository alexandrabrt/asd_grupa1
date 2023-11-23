import requests

url = "https://v6.exchangerate-api.com/v6/d01788f6764c212c4285d31a/latest/RON"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.json()['conversion_rates']['EUR'])
