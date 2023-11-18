def HandleParameterConsole(parameterName:str,defaultValue:float = 0):
    try:
        parameter = float(input(f"Введите параметр {parameterName}: "))
    except:
        print(f"Некорректно введён параметр {parameterName}! Будет установлено значение по умолчанию - {defaultValue}")
        parameter = defaultValue
    return parameter

def CheckParameters(parameters:[float]):
    isInputCorrect = ""
    if parameters[0]>parameters[1]:
        isInputCorrect +="Параметр a должен быть меньше или равен параметра b.\n"
    if parameters[2]<=0:
        isInputCorrect += "Параметр h должен быть больше или равен 0.\n"
    return isInputCorrect
    
def HandleInputConsole():
    while True:
        leftBorder = HandleParameterConsole("a",0)
        rightBorder = HandleParameterConsole("b",10)
        step = HandleParameterConsole("h",1)
        parameterK = HandleParameterConsole("k",1)
        parameterM = HandleParameterConsole("b",0)
        parameters = [leftBorder,rightBorder,step,parameterK,parameterM]
        check = CheckParameters(parameters)
        if check != "":
            print(check)
            print("Попробуйте ещё раз.\n")
        else:
            return parameters
