def  least_positive_index(arr):
    smallest_positive = float('inf')  # Initialize with positive infinity
    last_occurrence_index = -1

    for i in range(len(arr)):
        if arr[i] > 0 and arr[i] <= smallest_positive:
            smallest_positive = arr[i]
            last_occurrence_index = i

    return last_occurrence_index