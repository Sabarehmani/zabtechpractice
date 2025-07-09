import requests
response = requests.get("https://randomuser.me/api/")
print(response)
data = response.json()
print(data)

for results in data:
    print(data['name']["first"])