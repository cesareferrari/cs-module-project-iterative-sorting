def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(cur_index + 1, len(arr)):
            # compare all these values to the value at cur_index
            # find the smallest
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]
    return arr





def bubble_sort(arr):
    # initialize the swapped flag to True so loop can start.
    # "swapped" keeps track of when values are swapped.
    # When swapped is False, the list is sorted and the loop is exited
    swapped = True

    # keep looping through the list while swapped is true
    # if there are swapped value, it means the list is not sorted
    # it's sorted when there are no more swapped values
    while swapped is True:
        # when False, exit the loop
        # turn it to False here, so there is a way to exit the loop
        # it can be turned to True again if there is a swap below
        # in that case it will keep looping
        swapped = False 

        # length of list - 1 (because the last
        # element doesn't have a right element to swap with)
        for i in range(0, len(arr) - 1): 
            if arr[i] > arr[i + 1]:
                # do the swapping by reassigning the variables to each other
                # in parallel
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                # there is a swap, so turn the flag True and keep looping
                swapped = True

    return arr

'''
STRETCH: implement the Count Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    counts = [0] * (maximum + 1)

    for value in arr:
        counts[value] += 1

    j = 0
    for i in range(0, len(counts)):
        while counts[i] > 0:
            arr[j] = i
            j += 1
            count[i] -= 1

    return arr
