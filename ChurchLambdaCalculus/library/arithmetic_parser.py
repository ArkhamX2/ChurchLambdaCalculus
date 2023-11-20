def ArithmeticParse(input):
    tokens=[]
    stack=[]
    parsed=[]
    tokens = input.split()
    for item in tokens:
        if (item == "("): stack.append(item)
        elif (item == ")"):
                while (len(stack) !=0 and stack[len(stack)-1] != "("):
                    parsed.append(stack.pop())
                stack.pop()
        elif (isOperator(item)):
            while (len(stack) !=0 and Priority(stack[len(stack)-1]) >= Priority (item)):
                parsed.append(stack.pop())
            stack.append(item)
        else:
            parsed.append(item)
    while (len(stack) != 0):
        parsed.append(stack.pop())
    return parsed

def Priority(c):
    match (c):
        case "^":
            return 5
        case "/":
            return 4
        case "*":
            return 2
        case "+":
            return 1
        case "-":
            return 1
        case _:
            return 0

def isOperator(c):
    if (c=="+" or c== "-" or c=="*" or c=="/" or c=="^"):
        return True
    else:
        return False
