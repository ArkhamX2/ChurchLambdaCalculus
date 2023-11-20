def EvaluateArithmeticEquation(tokensInp):
    operations = []
    for i in range(len(tokensInp)):
        operations.append(tokensInp[i])
        curToken = operations[len(operations)-1]
        match curToken:
            case "-":
                operations.pop()
                second = str(operations.pop())
                first = str(operations.pop())
                operations.append("SIGNED_SUBTRACT(" + first + ")(" + second + ")")
                pass
            case "+":
                operations.pop()
                operations.append("SIGNED_ADD(" + str(operations.pop()) + ")(" + str(operations.pop()) + ")")
                pass
            case "*":
                operations.pop()
                operations.append("SIGNED_MULTIPLY(" + str(operations.pop()) + ")(" + str(operations.pop()) + ")")
                pass
            case "/":
                operations.pop()
                second = str(operations.pop())
                first = str(operations.pop())
                operations.append("SIGNED_DIVIDE(" + first + ")(" + second + ")")
                pass        
            case _:
                operations.append("decodeSigned("+str(operations.pop())+")")
                pass
    return "encodeSigned(" + operations.pop() + ")"