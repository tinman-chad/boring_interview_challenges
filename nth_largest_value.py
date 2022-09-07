#given an array of integers sorted smallest to largest find the Nth largest

def nth_largest(arr, k):
    for i in range(k-1):
        arr.remove(max(arr))
    return max(arr)