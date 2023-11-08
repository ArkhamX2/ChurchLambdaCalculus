import numpy as np
def HandleOutput(inputParameters:[float],functionResult:[float]):
    leftBorder = inputParameters[0]
    rightBorder = inputParameters[1]
    step = inputParameters[2]
    print("{:5}".format("N")+"{:5}".format("x")+"{:5}".format("f(x)"))
    counter = 1
    for i in np.arange(leftBorder,rightBorder,step):
        print("{:0}".format(counter)+"{:7}".format(i)+"{:7}".format(functionResult[counter-1]))
        counter += 1
