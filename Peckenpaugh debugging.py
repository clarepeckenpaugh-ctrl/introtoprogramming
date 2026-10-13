#one_a 
def wrong_add_function(arg1, arg2):
    arg1_index = 0

    print(f"The correct answer is supposed to be: [2, 3, 4]")
    print(f"We are entering the while loop with arg1 = {arg1} and arg2 = {arg2}")

    while arg1_index < len(arg1):
        print(f"We are processing arg1 index {arg1_index}, whose value is {arg1[arg1_index]}.")

        arg_2_sum = 0

        for arg2_elements in arg2:
            print(f"The for loop is currently looking at {arg2_elements}, but the sum line uses the entire arg2 list: {arg2}.")
            arg_2_sum = sum([arg1[arg1_index] + i for i in arg2])
            print(f"The code is about to save {arg_2_sum}, but the correct value at index {arg1_index} should be {arg1[arg1_index] + arg2[arg1_index]}.")

        arg1[arg1_index] = arg_2_sum
        arg1_index += 1

    return arg1
    arg1 : list

arg1 = [1, 2, 3]
arg2 = [1, 1, 1]

wrong_add_function(arg1, arg2)  

#one_b
def correct_add_function(arg1, arg2):
    arg1_index = 0

    while arg1_index < len(arg1):
        arg_2_sum = 0
        arg_2_sum = arg1[arg1_index] + arg2[arg1_index]

        arg1[arg1_index] = arg_2_sum
        arg1_index += 1

    return arg1

correct_arg1 = [1, 2, 3]
correct_arg2 = [1, 1, 1]

print(correct_add_function(correct_arg1, correct_arg2))

#two_a
   # numeric section
def wrong_add_function(arg1, arg2): 
   if sum([type(i) == int for i in arg1]) == len(arg1) and \
      sum([type(i) == int for i in arg2]) == len(arg2):

      arg1_index = 0

      while arg1_index < len(arg1):
         arg_2_sum = arg1[arg1_index] + arg2[arg1_index]
         arg1[arg1_index] = arg_2_sum
         arg1_index += 1

      return arg1

#two_b

def exception_add_function(arg1, arg2):
    try:
        for index in range(len(arg1)):
            if type(arg1[index]) != type(arg1[0]):
                raise TypeError(1, index)

        for index in range(len(arg2)):
            if type(arg2[index]) != type(arg2[0]):
                raise TypeError(2, index)

        return wrong_add_function(arg1, arg2)

    except TypeError as error:
        argument_number = error.args[0]
        element_number = error.args[1]

        return f"Your input argument {argument_number} at element {element_number} is not of the expected type. Please change this and rerun."

arg_str_1 = ['1', '2', '3']
arg_str_2 = ['1', '1', 1]

print(exception_add_function(arg_str_1, arg_str_2))

# two_c

def wrong_add_function(arg1, arg2):

    # numeric section
    if sum([type(i) == int for i in arg1]) == len(arg1) and \
       sum([type(i) == int for i in arg2]) == len(arg2):

        arg1_index = 0

        while arg1_index < len(arg1):
            arg_2_sum = arg1[arg1_index] + arg2[arg1_index]
            arg1[arg1_index] = arg_2_sum
            arg1_index += 1

        return arg1

    # string section
    elif sum([type(i) == str for i in arg1]) == len(arg1) and \
         sum([type(i) == str for i in arg2]) == len(arg2):

        arg1_index = 0

        while arg1_index < len(arg1):
            arg_2_sum = ''

            for arg2_elements in arg2:
                arg_2_sum += arg2_elements

            arg1[arg1_index] = arg1[arg1_index] + str(arg_2_sum)
            arg1_index += 1

        return arg1


def correction_add_function(arg1, arg2):
    try:
        for index in range(len(arg1)):
            if type(arg1[index]) != type(arg1[0]):
                raise TypeError

        for index in range(len(arg2)):
            if type(arg2[index]) != type(arg2[0]):
                raise TypeError

        return wrong_add_function(arg1, arg2)

    except TypeError:
        corrected_arg1 = [str(item) for item in arg1]
        corrected_arg2 = [str(item) for item in arg2]

        return wrong_add_function(corrected_arg1, corrected_arg2)


arg_str_1 = ['1', '2', '3']
arg_str_2 = ['1', '1', 1]

print(correction_add_function(arg_str_1, arg_str_2))