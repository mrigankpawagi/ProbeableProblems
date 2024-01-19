def least_positive_index(arr):
    if not arr:
        return None  # Return None if the array is empty

    least_integer = arr[0]
    least_index = 0

    for i in range(1, len(arr)):
        if arr[i] < least_integer:
            least_integer = arr[i]
            least_index = i

    return least_index