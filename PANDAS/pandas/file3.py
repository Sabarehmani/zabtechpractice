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

#step 5:Fill missing values 
df['marks'] = df['marks'].fillna(df['marks'].mean())
df['grade'] = df['grade'].fillna('B')

#step 6: Add a new column : "status"
df['status'] = ['pass' if m >= 75 else 'fail' for m in df['marks']]

# step 7: Show cleaned and updated data
print("/n cleaned and updated data:")
print(df)