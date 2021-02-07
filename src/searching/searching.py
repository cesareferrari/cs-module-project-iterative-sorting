def linear_search(arr, target):

    # return the index
    for i in range(0, len(arr)):
        if arr[i] == target:
            return i

    # return the value instead, this also works
    # for value in arr:
    #     if value == target:
    #         return target

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    if len(arr == 0:)
        return -1 # array empty

    low = 0
    high = len(arr) - 1

    while low <= high:
        middle = (low + right) // 2
    # go to the middle

    # ask if the middle is less than or greater than our target
    ## if less, eliminate the right hand side
        if target < arr[middle]:
            high = middle - 1
        elif target > arr[middle]:
            low = middle + 1
        else:
            return middle

    # adjust the low or high accordingly

    return -1  # not found
