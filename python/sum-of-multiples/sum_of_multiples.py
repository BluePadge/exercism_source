def sum_of_multiples(limit, multiples):
    sum = 0
    for i in range(limit):
        for value in multiples:
            if i % value == 0:
                sum += i
                break
    return sum

