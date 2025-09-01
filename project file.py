import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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
        
def Read_CSV():
    print("*"*80)
    print("\t\t\tDisplay COVID Status in DELHI")
    print("*"*80)
    df=pd.read_csv('C:\\Users\\Tushar Sharma\\OneDrive\\Documents\\covid.csv')
    print(df)

#FOR BAR GRAPH:)
def bar_chart():
    df = pd.read_csv('C:\\Users\\Tushar Sharma\\OneDrive\\Documents\\covid.csv')
    District = df["Districts"]
    Confirmed = df["Confirmed"]
    Recovered = df["Recovered"]
    Deaths = df["Deaths"]
    Active = df["Active"]
    plt.xlabel("Districts")

    choice = int(input("Now Enter your choice to display bar graph:"))
    while wish=='y' or wish=='Y':
        if  choice == 1:
            plt.ylabel("Confirmed Cases")
            plt.title("Districts Wise Confirmed Cases")
            plt.bar(District, Confirmed, color='r', width = 0.5)
            plt.show()
            bar_chart()
        elif  choice == 2:
            plt.ylabel("Recovered Cases")
            plt.title("Districts Wise Recovered Cases")
            plt.bar(District, Recovered, color='g', width = 0.5)
            plt.show()
            bar_chart()
        elif  choice == 3:
            plt.ylabel("Death Cases")
            plt.title("Districts Wise Death Cases")
            plt.bar(District, Deaths, color='b', width = 0.5)
            plt.show()
            bar_chart()
        elif  choice == 4:
            plt.ylabel("Active Cases")
            plt.title("Districts Wise Active Cases")
            plt.bar(District, Active, color='c', width = 0.5)
            plt.show()
            bar_chart()
        elif  choice == 5:
            plt.bar(District, Confirmed, color='r', width = 0.5, label = "Districts Wise Confirmed Cases")
            plt.bar(District, Recovered, color='g', width = 0.5, label = "Districts Wise Recovered Cases")
            plt.bar(District, Deaths, color='b', width = 0.5, label = "Districts Wise Death Cases")
            plt.bar(District, Active, color='c',width = 0.5, label = "Districts Wise Active Cases")
            plt.legend()
            plt.show()
            bar_chart()
        elif  choice == 6:
            D=np.arange(len(District))
            width=0.25
            plt.bar(D,Confirmed, width, color='b', label = "Districts Wise Confirmed Cases")
            plt.bar(D+0.25, Recovered, width, color='g', label = "Districts Wise Recovered Cases")
            plt.bar(D+0.50, Deaths, width, color='r', label = "Districts Wise Death Cases")
            plt.bar(D+0.75, Active ,width, color='c', label = "Districts Wise Active Cases")
            plt.legend()
            plt.show()
            bar_chart()
        elif choice == 7:
            break
            
    wish=input("Do u want to continue........") 

 #FOR LINE CHART:)

def line_chart():
    df = pd.read_csv('C:\\Users\\Tushar Sharma\\OneDrive\\Documents\\covid.csv')
  
    District=df["Districts"]
    Confirmed=df["Confirmed"]
    Recovered=df["Recovered"]
    Deaths=df["Deaths"]
    Active=df["Active"]
    plt.xlabel("Districts")
    wish=='y'
    choice = int(input("Enter the number representing your preferred line chart from the above choices: "))
    while True:
        if choice == 1:
            plt.ylabel("Confirmed Cases")
            plt.title("Districts Wise Confirmed Cases")
            plt.plot(District, Confirmed, color='b')
            plt.show()
            line_chart()
        elif choice == 2:
            plt.ylabel("Recovered Cases")
            plt.title("Districts Wise Recovered Cases")
            plt.plot(District, Recovered, color='g')
            plt.show()
            line_chart()
        elif choice == 3:
            plt.ylabel("Death Cases")
            plt.title("Districts Wise Death Cases")
            plt.plot(District, Deaths, color='r')
            plt.show()
            line_chart()
        elif choice == 4:
            plt.ylabel("Active Cases")
            plt.title("Districts Wise Active Cases")
            plt.plot(District, Active, color='c')
            plt.show()
            line_chart()
        elif choice == 5:
            plt.ylabel("Number of cases")
            plt.plot(District, Confirmed, color='b', label = "Districts Wise Confirmed Cases")
            plt.plot(District, Recovered, color='g', label = "Districts Wise Recovered Cases")
            plt.plot(District, Deaths, color='r', label = "Districts Wise Death Cases")
            plt.plot(District, Active, color='c', label = "Districts Wise Active Cases")
            plt.legend()
            plt.show()
            
        elif choice == 6:
            break
          
        wish=input("Do u want to continue........") 
        

  #scatter Graph    
def scatter_chart():
    df=pd.read_csv('Covid_data_kerala.csv')
    df['Districts'] = ['EKM','PTA','KTM','TSR','KKD','MPM','KLM','PKD','ALP','KNR','TVM','IDK','WYD','KGD']
    District = df["Districts"]
    Confirmed = df["Confirmed"]
    Recovered = df["Recovered"]
    Deaths = df["Deaths"]
    Active = df["Active"]
    
    SC=plt.gca()
    SC=plt.scatter(District, Confirmed, color="b", label="Districts Wise Confirmed Cases")
    SC=plt.scatter(District, Recovered, color="g", label="Districts Wise Recovered Cases")
    SC=plt.scatter(District, Deaths, color="r", label="Districts Wise Death Cases")
    SC=plt.scatter(District, Active, color="c", label="Districts Wise Active Cases")
    
    plt.xlabel("District")
    plt.title("Complete Scatter Chart")
    plt.legend()
    plt.show()
    



    

#main block for function calling

Main_Menu()

