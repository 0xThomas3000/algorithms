import sys

def swap(arr, pos1, pos2):
  get = arr[pos1], arr[pos2]
  arr[pos2], arr[pos1] = get 
  return arr

def bubbleSort(arr, n):
  haveSwap = False
  for i in range(n-1):
    haveSwap = False
    for j in range(n-i-1):
      if (arr[j] > arr[j+1]):
        swap(arr, j, j+1)
        haveSwap = True
    if(haveSwap == False):
      break

def printArray(arr, size):
  for i in range(size):
    print(arr[i])

arr = [64, 34, 25, 12, 22, 11, 90];
#n = sys.getsizeof(arr)//sys.getsizeof(arr[0])
n = len(arr)
bubbleSort(arr, n)
print("Sorted array: ", n)
printArray(arr, n)