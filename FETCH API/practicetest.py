#1 use Api to fetch and display data
import requests
res = requests.get("https://randomuser.me/api/")
result = res.json()
print(result["results"][0]["gender"])

#2 create a list of 10 elements and find max number
li = [2,3,45,67,89,47,23,75,45,23]
li2 = 0
for i in li:
    if (i>li2):
        li2 = i
     
print(li2)