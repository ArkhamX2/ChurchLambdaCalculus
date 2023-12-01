def QuickSort(unsortedList):
    if len(unsortedList) <= 1:
        return unsortedList
    elem = unsortedList[0]
    left = list(filter(lambda x : x<elem, unsortedList))
    center = [i for i in unsortedList if i == elem]
    right = list(filter(lambda x : x>elem, unsortedList))

    return QuickSort(left) + center + QuickSort(right)