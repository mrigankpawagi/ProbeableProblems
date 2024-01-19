def reorder(lst, num):
    smaller = [i for i in lst if i < num]
    larger = [i for i in lst if i >= num]
    return smaller + larger