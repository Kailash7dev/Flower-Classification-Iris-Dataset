def irisModel(petal_width,petal_length):

    petal_width = float(petal_width)
    petal_length = float(petal_length)

    if petal_width >=0.1 and petal_width <=0.7:
        if petal_length >=0.8 and petal_length <= 2.0:
            print("Flower is identified to be SETOSA")


    elif petal_width >=0.9 and petal_width <=1.6:
        if petal_length >=3.0 and petal_length <= 4.8:
            print("Flower is identified to be VERSICOLOR")


    elif petal_width >=1.7 and petal_width <=2.6:
        if petal_length >=4.9 and petal_length <= 7.0:
            print("Flower is identified to be VIRGINICA")


    else:
        print("Flower Doesnot belong to Iris family")

while True:
    print(irisModel(input("petal_width:"),input("petal_length")))
