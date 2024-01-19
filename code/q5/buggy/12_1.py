def reorder(lst, k):
    # Step 1: Create two lists to store numbers smaller and larger than k
    smaller_than_k = []
    larger_than_k = []

    # Step 2: Iterate through the given list and categorize numbers
    for num in lst:
        if num <= k:
            smaller_than_k.append(num)
        else:
            larger_than_k.append(num)

    # Step 3: Combine the two lists to get the final rearranged list
    rearranged_list = smaller_than_k + larger_than_k

    return rearranged_list