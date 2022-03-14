arr = [2, 7, 9, 11, 20, 25, 27, 50, 51, 60]
target = 25

def search(target, arr):
  left = 0
  right = len(arr) - 1
  while(left < right):
    mid = (left + right) // 2
    if (target == arr[mid]):
      return mid
    elif target > arr[mid]:
      left = mid + 1
    else:
      right = mid - 1
  return -1

print(search(target, arr))