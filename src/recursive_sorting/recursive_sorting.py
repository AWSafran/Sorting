# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    print("Attempting to merge:")
    print(arrA)
    print(arrB)
    elements = len( arrA ) + len( arrB )
    merged_arr = []
    # TO-DO
    i = 0
    j = 0
    for k in range(0, elements):
        if i == len(arrA):
            merged_arr.extend(arrB[j:])
            break
        elif j == len(arrB):
            merged_arr.extend(arrA[i:])
            break
        elif arrA[i] < arrB[j]:
            print(f"appending {arrA[i]}")
            merged_arr.append(arrA[i])
            i += 1
        else:
            print(f"appending {arrB[j]}")
            merged_arr.append(arrB[j])
            j += 1
        

    print(merged_arr)
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if len(arr) <= 1:
        return arr
    else:
        return merge(merge_sort(arr[:len(arr) // 2]), merge_sort(arr[len(arr) // 2 :]))

    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
