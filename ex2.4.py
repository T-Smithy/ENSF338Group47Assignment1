import sys
import requests
import json
import timeit
import matplotlib.pyplot as plt

sys.setrecursionlimit(20000)
def func1(arr, low, high):
    if low < high:
        if high - low + 1 <= 10: 
            for i in range(low + 1, high + 1):
                key = arr[i]
                j = i - 1
                while j >= low and arr[j] > key:
                    arr[j + 1] = arr[j]
                    j = j - 1
                arr[j + 1] = key
        else:
            pi = func2(arr, low, high)
            func1(arr, low, pi-1)
            func1(arr, pi + 1, high)

def func2(array, start, end):
    mid = (start + end) // 2
    if array[start] > array[mid]:
        array[start], array[mid] = array[mid], array[start]
    if array[mid] > array[end]:
        array[mid], array[end] = array[end], array[mid]
        if array[start] > array[mid]:
            array[start], array[mid] = array[mid], array[start]
    p = array[mid]
    low = start + 1
    high = end
    while True:
        while low <= high and array[high] >= p:
            high = high - 1
        while low <= high and array[low] <= p:
            low = low + 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break
    array[start], array[high] = array[high], array[start]
    return high

def main():
    url = 'https://raw.githubusercontent.com/ldklab/ensf338w23/main/assignments/assignment2/ex2.json'
    data = json.loads(requests.get(url).text)

    timings = []
    for arr in data:
        n = len(arr)
        elapsed_time = timeit.timeit(lambda: func1(arr, 0, n-1), number=1)
        timings.append(elapsed_time)
    
    plt.plot(timings)
    plt.title('Timing Results')
    plt.xlabel('Inputs')
    plt.ylabel('Time taken(s)')
    plt.show()

if __name__ == "__main__":
    main()