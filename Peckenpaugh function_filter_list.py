[3, 7, 13, 17, 19, 23, 32, 37]
def filter_list(numbers, threshold):
    filtered_numbers = []

    for number in numbers:
        if number<= threshold:
            filtered_numbers.append(number)

    return filtered_numbers

example_numbers = [1, 3, 6, 32, 37]
example_threshold = 30

result = filter_list(example_numbers, example_threshold)
print(result)