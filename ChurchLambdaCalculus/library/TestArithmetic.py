from ArithmeticEvaluator import *
from ArithmeticParser import *

input="5 + 4 + 2 / 2 * 10"
print(EvaluateEquation(Parse(input)))