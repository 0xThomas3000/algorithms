
def swap(arr, pos1, pos2):
  get = arr[pos1], arr[pos2]
  arr[pos2], arr[pos1] = get 
  return arr

def quicksort(arr):
  quicksort1(arr, 0, len(arr)-1)

def quicksort1(arr, left, right):
  if (left >= right):
    return
  pivot = arr[(left+right)//2]
  index = partition(arr, left, right, pivot)
  quicksort1(arr, left, index-1)
  quicksort1(arr, index, right)

def partition(arr, left, right, pivot):
  while (left <= right):
    while (arr[left] < pivot):
      left += 1
    while (arr[right] > pivot):
      right -= 1
    if (left <= right):
      swap(arr, left, right)
      left += 1
      right -= 1
  return left

arr = [8, 7, 9, 12, 10]
quicksort(arr)
print(arr)