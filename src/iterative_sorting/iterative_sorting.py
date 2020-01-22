# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 

        # TO-DO: swap

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
  def one_pass(arr):
    for i in range(0, len(arr)-1):
      left = arr[i]
      right = arr[i + 1]
      if right < left:
        arr[i] = right
        arr[i + 1] = left

  def check_sorted(arr):
    is_sorted = True
    for i in range(0, len(arr) - 1):
      left = arr[i]
      right = arr[i + 1]
      if right < left:
        is_sorted = False
    return is_sorted

  while check_sorted(arr) == False:
    one_pass(arr)

  check_sorted(arr)
  return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr