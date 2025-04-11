def add(numbers):
    if not numbers:
        return 0
    
    delimiter = ','
    number_part = numbers
    ## Handle custom delimiter
    if numbers.startswith("//"):
        delimiter_line, number_part = numbers.split("\n", 1)
        delimiter = delimiter_line[2:]

    number_part = number_part.replace('\n', delimiter)
    string_number_list = number_part.split(delimiter)
    number_list = [int(num) for num in string_number_list]

    return sum(number_list)
    
if __name__ == "__main__":
    input_string = input('Enter a string:')
    result = add(input_string)
    print(f"Output is: {result}")