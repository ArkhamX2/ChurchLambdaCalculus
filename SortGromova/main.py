import os
import time


def ReadFile(fname):
    fhandle = open(fname)
    f = fhandle.read()
    fhandle.close()
    return f


def WriteFile(fname, time, sorted):
    with open(fname, 'w', encoding = 'utf-8') as fres:
        fres.write(str('Время: \n'))
        fres.write(str(str(time) + '\n'))
        fres.write(str('Отсортирован: \n'))
        fres.write(' '.join([str(i) for i in sorted]))


def BubleSort(unsorted):
    for i in range(0, len(unsorted) - 1):
        for j in range(len(unsorted) - i - 1):
            if unsorted[j] > unsorted[j + 1]:
                unsorted[j],unsorted[j+1] = unsorted[j+1], unsorted[j]
    return unsorted


fdir = os.path.abspath(os.path.dirname(__file__))
print(fdir)
fname = os.path.join(fdir, 'inputlab1.txt')
start = time.perf_counter()

list = [int(i) for i in ReadFile(fname).split(' ')]

sorted = BubleSort(list.copy())
end = time.perf_counter()

print("Неотсортированная последовательность: ", list)
print("Отсортированная последовательность: ", sorted)

WriteFile('reslab1.txt', end - start, sorted)


