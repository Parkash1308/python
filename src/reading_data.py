import pandas as pd
#Reading the data from csv file
def main_1():
    print("Reading data from csv file\n")


    csv_path="C:\\Users\\User\\Downloads\\demo\\my_model\\data\\shows.csv"
    data=pd.read_csv(csv_path)
    print(data.head(10))
#Reading data from dictionary

def main__2():
    print("\n\nReading data from dictionary\n")
    my_data ={
        'name':["Pehlaj" ,"Parkash","Nizam","Hismat","Suneel"],
        'age':[20,22,23,25,24],
        'program':["MBBS", "CS","CS","CS","BBA"]
    }
    myData=pd.DataFrame(my_data)
    print(myData)
if "__name__= __main__":
    print("\n=============Welcome to my model============\n")
    main_1()
    main__2()
