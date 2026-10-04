def while_inner_plus(input_list):
    current_list = input_list
    found_nested_list = True

    while found_nested_list:
        found_nested_list = False

        for item in current_list:
            if isinstance(item, list):
                current_list = item
                found_nested_list = True
                break

    result = []

    for number in current_list:
        result.append(number + 1)

    return result

input_list = [37, 38, 39, 40, [41, 42, 43, [44, 45]]]

answer = while_inner_plus(input_list)
print(answer)