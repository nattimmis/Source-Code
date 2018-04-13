import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cluster import KMeans
#import sqlite3
#conn = sqlite3.connect('test.db')
# if conn = True:
# 	print("Datbase Loaded")
# cursor = conn.execute(["SELECT name,age,days,room-type,people from datas"])
#the code is built in a demo-prototype way and can be connected to sqlite databases altering the code properties on number of columns and its values<>

data = "data.csv"
read = pd.read_csv(data)
#aim of the code to predict which room-type the customer will choose based on his age,people and days

le = LabelEncoder()
read["room-type"] = le.fit_transform(read["room-type"])
#read.head(2)

t = {"Age":pd.Series(read["Age"]),"people":pd.Series(read["people"]),"days":pd.Series(read["days"])}
train_data = pd.DataFrame(t)
x = train_data.values
y = read["room-type"].values
#x[3:6]

#customers segmented using unsupervised learning
model = KMeans(n_clusters=3)
model.fit(x)
print("customer clustered model using unsupervised method:",model.labels_)

#predictive machine learning
class_model = KNeighborsClassifier(n_neighbors=1)
class_model.fit(x,y)
age = int(input("Enter The Age of the person"))
days = int(input("Enter the number of days"))
people = int(input("Enter the number of people along"))

output = class_model.predict([[age,days,people]])
output = np.squeeze(output,axis=0)
output = int(output)
# print(output)

if output == 1:
    print("The customer will prefer Premium room-type")
elif output == 2:
    print("The customer will prefer Ultra room-type")
else:
    print("The customer will prefer Ordinary room-type")