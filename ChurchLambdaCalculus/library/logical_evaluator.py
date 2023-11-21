def EvaluateLogicalEquation(tokensInp):
    operations = []
    for i in range(len(tokensInp)):
        operations.append(tokensInp[i])
        curToken = operations[len(operations)-1]
        match curToken:
            case "¬":
                operations.pop()
                operations.append("NOT(" + str(operations.pop()) + ")")
                pass
            case "∧":
                operations.pop()
                operations.append("AND(" + str(operations.pop()) + ")(" + str(operations.pop()) + ")")
                pass
            case "∨":
                operations.pop()
                operations.append("OR(" + str(operations.pop()) + ")(" + str(operations.pop()) + ")")
                pass
            case "⊕":
                operations.pop()
                operations.append("XOR(" + str(operations.pop()) + ")(" + str(operations.pop()) + ")")
                pass 
            case "≡":
                operations.pop()
                operations.append("XNOR(" + str(operations.pop()) + ")(" + str(operations.pop()) + ")")
                pass       
            case _:
                operations.append("decodeBoolean("+str(operations.pop())+")")
                pass
    return "encodeBoolean(" + operations.pop() + ")"