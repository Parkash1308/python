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
def train_data():
    print("\nData training\n")
    r2=r2_score(train_y,mymodel(train_x))
    print(r2)
def test_data():
    print("\nData testing\n")
    r2=r2_score(test_y,mymodel(test_x))
    print(r2)
def main():
    print("\n================WELCOME===================\n")
    print("We splited the original data into two part\n")
    print("1) Training set contain 80% of original data ")
    print("2  Testing set contain 20 % of original data")
    train_data()
    test_data()

    print("\nWe are confident that our model fits testing as well as training ")



if "__name__= __main__":
    main()

