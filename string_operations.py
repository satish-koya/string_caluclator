class NegativeNumberException(Exception):
    """Custom exception for negative numbers."""
    pass

def add_numbers(list_of_numbers):
    try:
        sum_of_numbers = 0
        if len(list_of_numbers) > 0:
            for i in list_of_numbers:
                sum_of_numbers += int(i)
        return sum_of_numbers

    except NegativeNumberException as e:
        print(f"Exception in add_numbers: {e}")
        return 0  # Return 0 if exception is caught


def string_addition(numbers_string):
    try:
        if isinstance(numbers_string,str):
            split_each_num = numbers_string.split(",")
            return add_numbers(split_each_num)
        else:
            print("Please Provide Numbers , separated string")
            return 0
    except Exception as e:
        print("Exception string_addition :" + str(e))
        return None
