import pandas as pd

# Read File Content
with open('iris.data') as myFile:
    data = myFile.read()

# Make a List of the Data
data = data.split('\n')
myData = []

for i in data:
    myData.append(i.split(','))

df = pd.DataFrame(myData, columns=['Length', 'Width', 'Height', 'Density', 'Type'])
df.to_excel('data.xlsx', index=False)