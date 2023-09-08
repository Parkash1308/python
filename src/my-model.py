import numpy
from sklearn.metrics import r2_score
numpy.random.seed(2)
x=numpy.random.normal(3,1,100)
y=numpy.random.normal(150,40,100)/x

# Traning data
train_x=x[:80]
train_y=y[:80]
#Testing data
test_x=x[80:]
test_y=y[80:]

mymodel=numpy.poly1d(numpy.polyfit(train_x,train_y,4))

def main():
    isTure=True
    while isTure:
        print("\n================WELCOME===================\n")
        print("This model estimate that how much money a buying customer will\n"
            "         spend regarding the time he/she stays at shop\n ")
        try:
            time= int(input("Enter the time in min >>=== "))
            print(mymodel(time))
            choice =input("Do you want to test again ? Y/N ==>> ")
            if choice =="Y":
                isTure=True
            elif choice =="N":
                isTure=False
            else:
                isTure=False
                print("Invalid input")
        except ValueError:
            print("Invalid input")

if "__name__= __main__":
    main()

