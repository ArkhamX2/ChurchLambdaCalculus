import numpy as np

def LinearList(inputParameters:[float]):
    #result = np.array([0],dtype=float)
    leftBorder=inputParameters[0]
    rightBorder=inputParameters[1]
    step=inputParameters[2]
    parameterK=inputParameters[3]
    parameterM=inputParameters[4]
    result = []

    for x in np.arange(leftBorder,rightBorder,step):
        #np.append(result,LinearFunction([parameterK,x,parameterM])[0])
        result.append(LinearFunction([parameterK,x,parameterM]))

    return result



def LinearFunction(parameters:[float]):
    k = parameters[0]
    x = parameters[1]
    m = parameters[2]
    return k*x+m
    