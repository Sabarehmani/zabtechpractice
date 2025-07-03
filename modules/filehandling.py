f = open("abc.txt","w")
f.write("Hello This is me Shifa Ahmed")

f = open("abc.txt","r")
f.write("I am very good girl")
for s in f:
     print(s)


f = open("abc.txt","r")
print(f.read())

import os
os.remove("abc.txt")




