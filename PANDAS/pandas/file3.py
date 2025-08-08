import pandas as pd
#step 1: Create a small datasheet (dataframe)
data = {
    "name" : ['Ali' , 'Sara' , 'Areeha' , 'Saba' , 'Shifa'],
    "marks" : [85, 56, 76, None, 88],
    "grade" : ['A' , 'A+' ,'B' , 'NONE' , '']
}

df = pd.DataFrame(data)

#step 2: Show the original data
print("original data:")
print(df)

#step 3: Show basic info
print("/n dataset info")
print(df.info())

#step 4: Show missing values
print("/n missing values:")
print(df.isnull().sum())

