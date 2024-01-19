def least_positive_index(arr):
    if not arr:  # Check if the list is empty
        return -1

    smallest_pos = float('inf')  # Initialize with positive infinity
    smallest_pos_index = -1  # Initialize index to -1 (not found)

    for i in range(len(arr)):
        if arr[i] > 0 and arr[i] < smallest_pos:
            smallest_pos = arr[i]
            smallest_pos_index = i

    if smallest_pos_index == -1:
        return -(len(arr) + 1)  # Return -(length of array + 1) if only negative integers are present
    else:
        return smallest_pos_index