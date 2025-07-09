import requests
respone = requests.get("https://jsonplaceholder.typicode.com/todos/")
# print(respone)
# print(respone.status_code)
data = respone.json()
print(data)
print(data[2]["title"])
print(data[25]["id"]) 

for result in data:
    print(result["id"] , result["title"])










