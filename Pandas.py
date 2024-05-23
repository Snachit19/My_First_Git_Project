import pandas as pd
#Dataframe is just like multi-dimentional matrix
data = {
    'Name': ["Tanmay", "Shaswat", "Neha", "Digvijay"],
    'Age' : [19,14,35,48],
    'Programming_experience' : ["Python and C/C++","No","No","Excel"]
} 
df = pd.DataFrame(data)
print(df)
Example = pd.read_csv("annual-enterprise-survey-2021-financial-year-provisional-csv.csv")
print(Example)
print(Example.columns)
example = Example[Example["Year"] < 2021]
example.to_csv('output.csv',index=False)
example_1 = pd.read_csv("output.csv")
print(example_1)
example_2 = Example.describe()
print(example_2)
print(Example.isnull())
print(len(Example))
len(Example.isnull())
print(Example.isnull().sum())