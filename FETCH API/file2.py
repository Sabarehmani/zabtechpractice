import requests
response = requests.get("https://randomuser.me/api/")
data = response.json()
result = data["results"]
name = result["0"]


for s in data:
    # print(result[0]["gender"])
    print(name["name"]["first"])
