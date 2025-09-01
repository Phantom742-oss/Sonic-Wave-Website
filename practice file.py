'''name="tushar sharma"
print(name.upper())           #upper key
print(name.lower())
print(name.find("u"))
print(name.replace("tushar","Phantom"))
print("t" in name)'''

'''list=[]
for num in range (1,6):
    num = int(input("enter the number :"))
    list.append(num)
print("the list is :-",list)
greatest_number = max(list)
lowest_number = min(list)
print("the greatest number in the list is :",greatest_number)
print("the smallest number in the list is :",lowest_number)'''

'''name="tushar sharma"
print(name.upper())           #upper key
print(name.lower())
print(name.find("u"))
print(name.replace("tushar","Phantom"))
print("t" in name)'''

'''list=[]
for num in range (1,6):
    num = int(input("enter the number :"))
    list.append(num)
print("the list is :-",list)
greatest_number = max(list)
lowest_number = min(list)
print("the greatest number in the list is :",greatest_number)
print("the smallest number in the list is :",lowest_number)'''

'''num=int(input("enter the number:-"))
man=1
while (man<11):

    print("the number is :-",man*num)     # table by using while loop
    man=man+1'''

'''num=int(input("enter the number :-"))
num2=int(input("enter the number :-"))
def iron_man (num,num2):
    print(num+num2)

iron_man(num,num2)'''

'''list=[11,45,8,23,14,26,53,59,62]
list11=[11,45,8]
list22=[23,14,26]
list33=[53,59,62]

list11.sort(reverse=True)
list22.sort(reverse=True)
list33.sort(reverse=True)

print(list11)
print(list22)
print(list33)'''


'''sample_list=[11,45,8,23,14,26,53,59,62]
l=[]
l1=[]
for i in sample_list[0:3]:
    sample_list.remove(i)
    l.append(i)


for i in sample_list[0:3]:
    sample_list.remove(i)
    l1.append(i)

print(l)
print(l1)
print(sample_list)
l.reverse()
l1.reverse()
sample_list.reverse()
print("after reversing:",l)
print("after reversing:",l1)
print("after reversing:",sample_list)'''


'''student ={"ankit":89,"parul":67,"payal":96,"rahul":78}
highest=max(student.values())
print("the highest marks are :",highest)'''

'''student=["carry","a-23",[45,34,64,86,79],67.8]

student[0]="avinash"
student1=student
print(student1)'''

'''demo=[1,5,7,9,12,45,67,76]
sorted(demo)
print(demo)'''


'''List1 = [2,3,4,5,5,6,10]
print(List1[:3]+List1[:3])'''

'''List1=[2,3,4,5]
print(List1[len(List1)-1])'''



'''stRecord = ['Raman',"A-36",[56,98,99,72,69],78.9]
print(stRecord[2][4])'''


'''val=eval(input("enter the list:"))
val.sort()
s=len(val)
mid=s//2

m1, m2 = mid - 1,mid
med = (val[m1]+val[m2])/2

print(med)'''

'''num=int(input("enter the number"))
n=int(input("enter the number of multiples"))
print("multiple are")
for a in range (1,n+1):
    mult=num*a
print(num*a)'''

'''a=1
num=int(input("enter the table of the number : -"))
while(a<11):
    print(num,"x",a,"=",num*a)

    a=a+1'''

'''num=int(input("enter the table of the number : -"))
for i in range(1,11):
    print(num,"x",i,"=",num*i)'''


'''import pandas as pd 
data=["a1","b1","c1","d1","e1"]
s=pd.Series(data,index=[1001,1002,1003,1004,1005])
print(s[[1002,1003,1004]])'''

'''import pandas as pd
df1=pd.Series([[1,2,3],[4,5,6],[8,9,5]])
print(df1)'''



'''import pandas as pd

print(pd.options.display.max_rows) '''

'''import matplotlib.pyplot as plt
import numpy as np 

p = np.array([1,2,3,4])

print(p**2)'''


'''import pandas as pd
days=[31,28,31,30,31,30,31,31,30,31,30,31]
monthdays = pd.Series(days,index=range(1,13))
print(monthdays[3:0:-1])'''

'''list=[1,2,3,4,5,6,7,8,9]
print(list[3:0:-1])'''



'''import pandas as pd
d=[4,3,2,6,7,8,5,9]
s=pd.Series(d)
print(s)
print(s.index) 
print(s.index.name)
print(s.values)
print(s.dtypes)
print(s.shape)
print(s.nbytes)
print(s.ndim)
print(s.size)
print(s.hasnans)
print(s.empty)
print(s.name)'''







'''dict1 ={
     
    "name" : ["Tushar","Jai","Rahul","Sumit"],
    "number" : [395, 206, 256, 286],
    "Hobby" : ["Gun Fight","None","None","None"]

}

df = pd.DataFrame(dict1)
print(df)
print(df.index)
print(df.T)
print(df.size)
print(df.columns)
print(df.axes)
print(df.dtypes)
print(df.shape)
print(df.values)
print(df.empty)
print(df.ndim)'''

'''import pandas as pd 
d={"Population":[10927986,12691836,4631392,4328063],
   "Hospital":[189,208,149,157],
   "Schools":[7916,8508,7226,7617]
   }

p=pd.DataFrame(d,index=["Delhi","Mumbai","Kolkata","Chennai"])
#print(p)
#df=p[p.loc[:,"Hospital"]>200]
#print(df.loc[:,["Population","Hospital"]])
#print(p.ndim)
#print(p.loc[:,])

p["Density"] = [435,675,567,563]
p.loc["Bangalore"] = 4200
#del p["Density"]
#p.drop("Density",axis=1,inplace=True)
#p.drop("Bangalore",inplace=True)
#p=p.drop(["Bangalore"])
#p=p.rename(columns={"Population":"Total_Population"})
p.rename(columns={"Population":"Total_Population"},inplace=True)
#p=p.rename(index={"Delhi":"D","Mumbai":"M","Kolkata":"K","Chennai":"C"})
p.rename(index={"Delhi":"D","Mumbai":"M","Kolkata":"K","Chennai":"C"},inplace=True)

p.Total_Population["Bangalore"]= "4726"
#p.loc["K","Hospital"]=None
p["baap"] = p["Schools"]*0.1
print(p)'''


'''import pandas as pd
mon=['jan','feb','march','april','may','june','july','aug','sep','oct','nov','dec']
month=pd.Series(mon)
month.index.name="monthno"
print(month)'''


'''yes=["tushar","vikram","rolex","drkside"]
yes_2=[i.title() for i in yes]
print(yes_2)'''


'''import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
path="C:\\Users\\Tushar Sharma\\OneDrive\\Documents\\covid.csv"

def Main_Menu():
    
    while True:
        print("*"*80)
        print(" ")
        print("\t\t\t\tMain Menu for Data Visualization")
        print(" ")
        print("*"*80)
        print("1--> Fetch Data")
        print("2--> LINE GRAPH")
        print("3--> BAR GRAPH")
        print("4--> SCATTER GRAPH")
        print("5--> EXIT")
        ch=int(input("Enter your choice"))
        if ch==1:
               Read_CSV()
        elif ch==2:
            while True:
                print("\t\t\t LINE GRAPH Menu")
                print("    Press 1 to print the data for Confirmed cases as per Districts.")
                print("    Press 2 to print the data for Recovered cases as per Districts.")
                print("    Press 3 to print the data for Death cases as per Districts.")
                print("    Press 4 to print the data for Active cases as per Districts.")
                print("    Press 5 to print All data.")
                print("    Press 6 to EXIT")
                line_chart()

        elif ch==3:
            while True:
                print("\t\t\t BAR GRAPH Menu")
                print("    Press 1 to print the data for Confirmed cases as per Districts.")
                print("    Press 2 to print the data for Recovered cases as per Districts.")
                print("    Press 3 to print the data for Death cases as per Districts.")
                print("    Press 4 to print the data for Active cases as per Districts.")
                print("    Press 5 to print All data.")
                print("    Press 6 to EXIT")
                bar_chart()
            
            
        elif ch==4:
            while True:
                print("\t\t\t SCATTER GRAPH Menu")
                print("    Press 1 to print the data for Confirmed cases as per Districts.")
                print("    Press 2 to print the data for Recovered cases as per Districts.")
                print("    Press 3 to print the data for Death cases as per Districts.")
                print("    Press 4 to print the data for Active cases as per Districts.")
                print("    Press 5 to print All data.")
                print("    Press 6 to EXIT")                    
                scatter_chart()

        elif ch==5:
            break
            
            

#line chart
def line_chart():
    df=pd.read_csv("C:\\Users\\Tushar Sharma\\OneDrive\\Documents\\covid.csv")
    District=df["Districts"]
    Confirmed=df["Confirmed"]
    Recovered=df["Recovered"]
    Deaths=df["Deaths"]
    Active=df["Active"]
    #plt.xlabel("District")


    choice = int(input("Enter the number representing your preferred line chart from the above choices: "))
    while True:
        if choice == 1:
            plt.xlabel("Districts")
            plt.ylabel("Confirmed Cases")
            plt.title("Districts Wise Confirmed Cases")
            plt.plot(District, Confirmed, color='b')
            plt.show()
            line_chart()
        elif choice == 2:
            plt.xlabel('Districts')
            plt.ylabel("Recovered Cases")
            plt.title("Districts Wise Recovered Cases")
            plt.plot(District, Recovered, color='g')
            plt.show()
            line_chart()
        elif choice == 3:
            plt.xlabel('Districts')
            plt.ylabel("Death Cases")
            plt.title("Districts Wise Death Cases")
            plt.plot(District, Deaths, color='r')
            plt.show()
            line_chart()
        elif choice == 4:
            plt.xlabel('Districts')
            plt.ylabel("Active Cases")
            plt.title("Districts Wise Active Cases")
            plt.plot(District, Active, color='c')
            plt.show()
            line_chart()
        elif choice == 5:
            plt.title('Complete covid analaysis by line chart')
            plt.xlabel('Districts')
            plt.ylabel("Number of cases")
            plt.plot(District, Confirmed, color='b', label = "Districts Wise Confirmed Cases")
            plt.plot(District, Recovered, color='g', label = "Districts Wise Recovered Cases")
            plt.plot(District, Deaths, color='r', label = "Districts Wise Death Cases")
            plt.plot(District, Active, color='c', label = "Districts Wise Active Cases")
            plt.legend()
            plt.show()
            line_chart()
            
        elif choice == 6:
            Main_Menu()
#FOR BAR GRAPH:)
def bar_chart():
    df = pd.read_csv(path)
    District = df["Districts"]
    Confirmed = df["Confirmed"]
    Recovered = df["Recovered"]
    Deaths = df["Deaths"]
    Active = df["Active"]
    #plt.xlabel("Districts")

    choice = int(input("Now Enter your choice to display bar graph:"))
    while True:
        if  choice == 1:
            plt.ylabel("Confirmed Cases")
            plt.xlabel("Districts")
            plt.title("Districts Wise Confirmed Cases")
            plt.bar(District, Confirmed, color='r', width = 0.5)
            plt.show()
            bar_chart()
        elif  choice == 2:
            plt.ylabel("Recovered Cases")
            plt.xlabel("Districts")
            plt.title("Districts Wise Recovered Cases")
            plt.bar(District, Recovered, color='g', width = 0.5)
            plt.show()
            bar_chart()
        elif  choice == 3:
            plt.ylabel("Death Cases")
            plt.xlabel("Districts")
            plt.title("Districts Wise Death Cases")
            plt.bar(District, Deaths, color='b', width = 0.5)
            plt.show()
            bar_chart()
        elif  choice == 4:
            plt.ylabel("Active Cases")
            plt.xlabel("Districts")
            plt.title("Districts Wise Active Cases")
            plt.bar(District, Active, color='c', width = 0.5)
            plt.show()
            bar_chart()
        elif  choice == 5:
            D=np.arange(len(District))
            width=0.25
            plt.bar(D,Confirmed, width, color='b', label = "Districts Wise Confirmed Cases")
            plt.bar(D+0.25, Recovered, width, color='g', label = "Districts Wise Recovered Cases")
            plt.bar(D+0.50, Deaths, width, color='r', label = "Districts Wise Death Cases")
            plt.bar(D+0.75, Active ,width, color='c', label = "Districts Wise Active Cases")
            plt.xlabel("Districts")
            plt.ylabel("All Cases")
            plt.title('Complete covid analaysis by bar graph')
            plt.legend()
            plt.show()
            bar_chart()
        elif choice == 6:
            Main_Menu()
#scatter Graph    
def scatter_chart():
    df=pd.read_csv(path)
    District = df["Districts"]
    Confirmed = df["Confirmed"]
    Recovered = df["Recovered"]
    Deaths = df["Deaths"]
    Active = df["Active"]

    ch=int(input("Enter the number representing your preferred scatter chart from the above choices: "))
    while True:
        if ch==1:
            plt.scatter(District, Confirmed, color="b", label="Districts Wise Confirmed Cases")
            plt.xlabel('Districts')
            plt.ylabel('Confirmed')
            plt.title('District wise Confirmed cases')
            plt.legend()
            plt.show()
            scatter_chart()
        
        elif ch==2:
            plt.scatter(District, Recovered, color="g", label="Districts Wise Recovered Cases")
            plt.xlabel('Districts')
            plt.ylabel('Recovered')
            plt.title('District wise Recovered cases')
            plt.legend()
            plt.show()
            scatter_chart()

        elif ch==3:
            plt.scatter(District, Deaths, color="r", label="Districts Wise Death Cases")
            plt.xlabel('Districts')
            plt.ylabel('Death')
            plt.title('District wise death cases')
            plt.legend()
            plt.show()
            scatter_chart()

        elif ch==4:
            plt.scatter(District, Active, color="c", label="Districts Wise Active Cases")
            plt.xlabel('Districts')
            plt.ylabel('Active')
            plt.title('District wise Active cases')
            plt.legend()
            plt.show()
            scatter_chart()
        
        elif ch==5:
            plt.scatter(District, Confirmed, color="b", label="Districts Wise Confirmed Cases")
            plt.scatter(District, Recovered, color="g", label="Districts Wise Recovered Cases")
            plt.scatter(District, Deaths, color="r", label="Districts Wise Death Cases")
            plt.scatter(District, Active, color="c", label="Districts Wise Active Cases")
            plt.title('Complete covid analaysis by scatter graph')
            plt.xlabel('Districts')
            plt.ylabel("All Cases")
            plt.show()
            scatter_chart()

        elif ch==6:
            Main_Menu()    


def Read_CSV():
    print("*"*80)
    print("\t\t\tDisplay COVID Status in DELHI")
    print("*"*80)
    df=pd.read_csv(path)
    print(df)

Main_Menu()'''
