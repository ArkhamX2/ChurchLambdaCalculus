import os
import time

def readFile(filename):
    fileHandle = open(filename)
    file = fileHandle.read()
    fileHandle.close()
    return file

def writeResultToFile(fileName, timeScore, sortedArray, needList, writeMode):
    with open(fileName, writeMode, encoding='utf-8') as resultFile:
        resultFile.write('Sorted ' + str(len(sortedArray))+ ' elements in ' + str(timeScore) + ' seconds')
        resultFile.write('\n\n')
        if(needList):
            resultFile.write(' '.join([str(i) for i in sortedArray]))

def QuickSort(unsortedList):
    if len(unsortedList) <= 1:
        return unsortedList;
    elem = unsortedList[0]
    left = list(filter(lambda x : x<elem, unsortedList))
    center = [i for i in unsortedList if i == elem]
    right = list(filter(lambda x : x>elem, unsortedList))

    return QuickSort(left) + center + QuickSort(right)

fileDirectory = os.path.abspath(os.path.dirname("input.txt"))
filename = os.path.join(fileDirectory, r'input.txt')

start = time.perf_counter()
try:
    array = list(map(int,readFile(filename).split(' ')))
    answer = QuickSort(array.copy())
    end = time.perf_counter()
    writeResultToFile('result.txt', end - start, answer,False, 'w')

    for i in range(2,16):
        start = time.perf_counter()
        answer = QuickSort(array.copy()*i)
        end = time.perf_counter()
        writeResultToFile('result.txt',end-start, answer,False, 'a')
except:
    end = time.perf_counter()
    print("Файл содержит недопустимые символы!")
    writeResultToFile('result.txt', 0, [])


