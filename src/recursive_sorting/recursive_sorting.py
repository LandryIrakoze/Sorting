# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    for i in range(0, len(arrA)):
      if arrA[i] < arrB[i] or arrA[i] == arrB[i]:
        merged_arr[i*2] = arrA[i]
        merged_arr[i*2 + 1] = arrB[i]
      elif arrB[i] < arrA[i]:
        merged_arr[i*2] = arrB[i]
        merged_arr[i*2 + 1] = arrA[i]
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO

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
