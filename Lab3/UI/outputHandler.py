import numpy as np
def HandleOutputConsole(inputParameters:[float],functionResult:[float]):
    leftBorder = inputParameters[0]
    rightBorder = inputParameters[1]
    step = inputParameters[2]

    print("Результат работы программы:")
    print('%-8s %-10s %-15s' % ("№", "x", "f(x)"))
    counter = 1
    for i in np.arange(leftBorder,rightBorder+step,step):
        print("{:<9}".format(counter) + f"{'{:.2f}'.format(i).rstrip('0').rstrip('.'):<11}" + f"{'{:.3f}'.format(functionResult[counter-1]).rstrip('0').rstrip('.'):<15}")
        counter += 1

