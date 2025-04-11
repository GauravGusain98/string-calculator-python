def add(numbers):
    if not numbers:
        return 0
    
    delimiter = ','
    number_part = numbers
    number_part = number_part.replace('\n', delimiter)
    string_number_list = number_part.split(delimiter)
    number_list = [int(num) for num in string_number_list]

    return sum(number_list)
    
if __name__ == "__main__":
    input_string = input('Enter a string:')
    result = add(input_string)
    print(f"Output is: {result}")