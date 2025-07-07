import json as js

data = '''{
    "name":"Shifa",
    "age":20
}'''
a = js.loads(data)
print(type(a))
print(a["age"])

std={
     "name":"Shifa",
    "age":20
}
print(js.dumps(std))