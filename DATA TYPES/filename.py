original_list = [2,3,4,5,6,7,8,8,2,4,2,5,6,0]

duplicate_list = original_list.copy()

for i in range(3):
    duplicate_list.remove(2)

print('List 1:' , original_list)
print('List 2:' , duplicate_list)

