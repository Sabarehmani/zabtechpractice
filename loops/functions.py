def program() :
    print("code")
    
program()

def SayMyName(name) :
    print("My Name is" , name)
SayMyName("SABA")
SayMyName("SHIFA")
SayMyName("AREEHA")

def subjects(a , b) :
    print("his favourite subject is", a , "her favourite subject is" , b)
subjects("English" , "Mathematics")

def Addition(a , b) :
    print(a + b)
Addition(23 , 56)

def Subtraction(c , d) :
    print(c - d)
Subtraction(45 , 89)

def Multiplication(c , d) :
    print(c * d)
Multiplication(36 , 48)

def Division(c , d) :
    print(c / d)
Division(45 , 5)

def add (a , b) :
    return 70

result = add(20 , 20)
print(result)


def fun(*b) :
    for value in b:
        print(value*6)
fun(2,3,4,5,6,7,8,9)



tup = (1,2,3,4,5,6,7,8,9)
print(tup[5])
print(tup[7])
print(type(tup))

