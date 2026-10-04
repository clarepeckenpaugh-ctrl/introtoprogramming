def recursive_inner_plus(input_list):
    for item in input_list:
        if isinstance(item, list):
            return recursive_inner_plus(item)

    result = []

    for number in input_list:
        result.append(number + 1)

    return result

input_list = [37, 38, 39, 40, [41, 42, 43, [44, 45]]]

answer = recursive_inner_plus(input_list)
print(answer)