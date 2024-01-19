def reorder(numbers, num):
    smaller = [x for x in numbers if x < num]
    equal = [x for x in numbers if x == num]
    larger = [x for x in numbers if x > num]

    return smaller + equal + larger if equal else sorted(numbers)