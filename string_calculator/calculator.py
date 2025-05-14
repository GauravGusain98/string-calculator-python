def add(numbers):
    if not numbers:
        return -1

    delimiter = ','

    try:
        delimiter, number_part = find_delimiter(numbers)
        number_list = get_numbers_list(delimiter, number_part)

        if delimiter.lower() == 'o':
            number_list = find_odd_numbers_list(number_list)

        is_negative_present, negatives = is_negative_present_in_list(number_list)

        if not is_negative_present:
            return sum(number_list)
    except Exception:
        return -1

    exception_message = f"negative numbers not allowed {','.join(negatives)}"
    raise Exception(exception_message)

def find_delimiter(numbers):
    delimiter = ','
    number_part = numbers

    if numbers.startswith("//"):
        delimiter_line, number_part = numbers.split("\n", 1)
        delimiter = delimiter_line[2:]

    return delimiter, number_part

def get_numbers_list(delimiter, number_part):
    number_part = number_part.replace('\n', delimiter)
    string_number_list = number_part.split(delimiter)
    number_list = [int(num) for num in string_number_list]

    return number_list

def is_negative_present_in_list(number_list):
    negatives = []

    for num in number_list:
        if num < 0:
            negatives.append(str(num))

    if negatives:
        return True, negatives

    return False, negatives

def find_odd_numbers_list(numbers_list):
    odd_number_list = []
    for number in numbers_list:
        if number % 2 != 0:
            odd_number_list.append(number)

    return odd_number_list


if __name__ == "__main__":
    input_string = input('Enter the string with positive numbers in correct format:')
    result = add(input_string)
    if result == -1:
        print('Invalid Input')
    else:
        print(f"Output is: {result}")