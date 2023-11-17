import numpy as np

print("Введите начало диапазона ")
a = float(input())
print("Введите конец диапазона ")
b = float(input())
print("Введите шаг ")
h = float(input())
function = "f(x) = x^4 + x^2 + x + 1"
print(function)
res = []

#for(int x = 0; x<=10;x+=h)

for x in np.arange(a,b+h,h):
    res.append(x**4 + x*2 + x + 1)
#print(res)
counter = 1

print('%-8s %-10s %-15s' % ("№", "x", "f(x)"))
for i in np.arange(a,b+h,h):
    print('%-8d %-10.2f %-15.2f' % (counter, i, res[counter-1]))
    #print("{0}".format(counter) + "{:10.2f}".format(i).ljust(10) + "{:18.3f}".format(res[counter-1]).ljust(16))
    counter += 1
