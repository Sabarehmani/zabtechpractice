import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6])

# Find even numbers
even_mask = arr % 2 == 0
even_numbers = arr[even_mask]

# Find odd numbers
odd_mask = arr % 2 != 0
odd_numbers = arr[odd_mask]

print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)




#ANOTHER METHOD
li = [1,2,3,4,56,7,8,9]
for i in li:
    if(i%2==0):
        print("Even:" ,i)
    elif(i%2!=0):
        print("odd:" ,i)