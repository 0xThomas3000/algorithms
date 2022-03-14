arr = [2, 7, 9, 11, 20, 25, 27, 50, 51, 60]
target = 26

def bin_search(arr, target, start, end):
  mid = (start + end) // 2
  if (arr[mid] == target):
    return mid
  if (start == end):
    return -1
  if (arr[mid] > target):
    return bin_search(arr, target, start, mid - 1)
  if (arr[mid] < target):
    return bin_search(arr, target, mid + 1, end)

print(bin_search(arr, target, 0, len(arr) - 1))