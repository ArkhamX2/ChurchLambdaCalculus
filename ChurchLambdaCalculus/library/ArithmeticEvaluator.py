operations = []

def EvaluateEquation(tokensInp):
    for i in range(len(tokensInp)):
        operations.append(tokensInp[i])
        curToken = operations[len(operations)-1]
        match curToken:
            case "-":
                operations.pop()
                operations.append(str(-1*float(operations.pop()) + float(operations.pop())))
                pass
            case "+":
                operations.pop()
                operations.append(str(float(operations.pop()) + float(operations.pop())))
                pass
            case "*":
                operations.pop()
                operations.append(str(float(operations.pop()) * float(operations.pop())))
                pass
            case "/":
                operations.pop()
                operations.append(str(1/float(operations.pop()) * float(operations.pop())))
                pass        
            case _:
                pass
    return float(operations.pop())