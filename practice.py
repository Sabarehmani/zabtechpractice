kitchen = ['spoon' , 'plates' , 'glasses' , 'bottles' , 'knifes' , 'pot']
kitchen.append('cooler')
print(kitchen)
kitchen.extend('refregerator')
print(kitchen)
kitchen.insert(3 ,'microwave')
print(kitchen)
kitchen.remove('plates')
print(kitchen)
popped = kitchen.pop(3)
print(popped)

#index
kitchen = ['spoon' , 'plates' , 'glasses' , 'bottles']
print(kitchen.index('glasses'))
print(kitchen.index('bottles'))

#count
figures = [1,2,2,3,4,2,5,6,7,8,2,9,2,0]
print(figures.count(2))

#sort
figures = [1,2,2,3,4,2,5,6,7,8,2,9,2,0]
figures.sort
print(figures)

#reverse
alphabets = [b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,e,t,h,j,i,k,l,s,d,f,g,b,n,m,h,s,a]
alphabets.sort()
print(alphabets)
alphabets.reverse()
print(alphabets)

#copy
list_A = [1,3,5,4,4,6,7,8,9,9]
rough_list = list_A.copy()
rough_list.sort()

rough_list.remove(4)
print(rough_list)









