def HandleParameter(parameterName:str,defaultValue:float = 0):
    try:
        parameter = float(input(f"Введите параметр {parameterName}: "))
    except:
        print(f"Некорректно введён параметр {parameterName}! Будет установлено значение по умолчанию - {defaultValue}")
        parameter = defaultValue
    return parameter

def CheckParameters(parameters:[float]):
    isInputCorrect = True
    if parameters[0]>parameters[1]:
        print("Параметр a должен быть меньше или равен параметра b.\n")
        isInputCorrect = False
    if parameters[2]<=0:
        print("Параметр h должен быть больше или равен 0.\n")
        isInputCorrect = False
    return isInputCorrect
    
def HandleInput():
    while True:
        leftBorder = HandleParameter("a",0)
        rightBorder = HandleParameter("b",10)
        step = HandleParameter("h",1)
        parameterK = HandleParameter("k",1)
        parameterM = HandleParameter("b",0)
        parameters = [leftBorder,rightBorder,step,parameterK,parameterM]
        if CheckParameters(parameters) == False:
            print("Попробуйте ещё раз.\n")
        else:
            return parameters

