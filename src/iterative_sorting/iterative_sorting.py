# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
             



        # TO-DO: swap
        current = arr[cur_index]
        arr[cur_index] = arr[smallest_index]
        arr[smallest_index] = current




    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    num_changes = -1
    while num_changes != 0: #Keep going until you haven't had to change anything
        #reset num_changes to 0
        num_changes = 0

        for i in range(0, len(arr) - 1):
            if arr[i] > arr[i + 1]:
                num_changes += 1
                big = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = big


    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):
    
    final_array = []
    
    #check for empty array
    if len(arr) == 0:
        return []

    if min(arr) < 0:
        return "Error, negative numbers not allowed in Count Sort"
    
    #initialize count array
    count_array = [0] * (max(arr) + 1)
    
    for i in range(0, len(arr)):
        count_array[arr[i]] += 1
    
    print("initial count")
    print(count_array)
    # turn individual counts into running total
    for i in range(1, len(count_array)):
        count_array[i] += count_array[i-1]
    
    print("running total")
    print(count_array)
    counter = 0
    for i in range(0, len(count_array)):
        while counter < count_array[i]:
            final_array.append(i)
            counter += 1
    print("Final")
    print(final_array)

    return final_array

    count_sort([0, 1, 1, 3, 2, 5, 3])