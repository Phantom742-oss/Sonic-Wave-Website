'''i = 1
while i <= 100:
    print(i)
    i = i + 1'''

'''num = int(input("enter the number : "))
n=int(input("enter the number of multiple"))
for i in range (1,n+1):             # table of any number you want
    totl=num*i
    print(num,"x",i,"=",totl)'''

'''val=[500]
val.insert(0,200)
print(val)'''

'''i=0
while(i<11):
    print("i love you my future wife")
    i=i+1'''










'''import pandas as pd
TS= pd.Series([1,2,3,4,5],index =["a","b","c","d","e"])
B = pd.Series([1000,2000,-1000,-5000,1000], index = ["a","b","c","d","e"])
df=pd.DataFrame(TS)
print(df)'''

'''import pandas as pd
series_A = pd.Series([11,22,33,44,55])
print(series_A)'''


import matplotlib.pyplot as plt
student=[450,200,123,164]
sports=["Chess","Carrom","Badminton","football"]
color=["red","blue","black","yellow"]
m=[0,0,0,0.1]
plt.pie(student,labels = sports,explode=m,colors=color)
plt.show()



'''import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("C:\\Users\\Tushar Sharma\\OneDrive\\INDIA POPULATION.csv")
state_data= df.head(5)
state_names = state_data['India / State/ Union Territory']
populations=state_data['Population - 2011']
total=(df.head(5))
State=(df.head(5))
c=['green','blue','yellow','orange','red']
plt.pie(populations,labels=state_names,colors=c,autopct="%.1f%%")
plt.title("2011 Population of India")
plt.legend(loc='lower left')
plt.show()'''





'''import pandas as pd

dict1 ={
     
    "name" : ["Tushar","Jai","Rahul","Sumit"],
    "number" : [395, 206, 256, 286],
    "Hobby" : ["Gun Fight","None","None","None"]

}

df = pd.DataFrame(dict1)
#print(df)


df.to_csv("guys_index_false_.csv")

#print(df.describe())

df.loc[0,'name'] = "Tushar"
#df.index =[0,1,2,3]
#print(df.head(2))
print(df.index)
print(df.T)
#print(df.sort_index(axis=0,ascending=False))
#print(df.loc[[0, 1]])
print(df.size)
print(df.columns)
print(df.axes)
print(df.dtypes)
print(df.shape)
print(df.values)
print(df.empty)
print(df.ndim)
'''

