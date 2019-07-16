# STRETCH: implement Linear Search				
def linear_search(arr, target):
  
  # TO-DO: add missing code
  for i in range(0, len(arr)):
    if arr[i] == target:
      return i
  return -1


# STRETCH: write an iterative implementation of Binary Search 
def binary_search(arr, target):

  if len(arr) == 0:
    return -1 # array empty
    
  low = 0
  high = len(arr)-1

  middle = (high + low) // 2

  # TO-DO: add missing code

  while high != middle and low != middle:
    if arr[middle] == target:
      return middle
    elif arr[middle] > target:
      print(f"should be setting high ({high}) to middle ({middle})")
      high = middle
    elif arr[middle] < target:
      print(f"Should be setting low ({low}) to middle ({middle})")
      low = middle

    middle = (high + low) // 2
    print(f"High: {high}, Low: {low}, Middle: {middle}")

  return -1


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
