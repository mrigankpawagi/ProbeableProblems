def reorder(data, num):
    if not data:
        return data

    smaller = [x for x in data if x < num]
    larger = [x for x in data if x >= num]

    return smaller + larger