# STRETCH: implement Linear Search				
def linear_search(arr, target):
  
  # TO-DO: add missing code
  for i in range(0, len(arr)):
    if arr[i] == target:
      return i
  return -1


# STRETCH: write an iterative implementation of Binary Search 
# def binary_search(arr, target):

#   if len(arr) == 0:
#     return -1 # array empty
    
#   low = 0
#   high = len(arr)-1

#   # TO-DO: add missing code

#   return -1 # not found


# STRETCH: write a recursive implementation of Binary Search 
def binary_search_recursive(arr, target, low, high):
  
  middle = (low+high)//2

  if len(arr) == 0:
    return -1 # array empty

  if arr[middle] == target:
    return middle
  
  if arr[middle] > target:
    return binary_search_recursive(arr, target, low, middle)
  else:
    return binary_search_recursive(arr, target, middle, high)
  # TO-DO: add missing if/else statements, recursive calls
