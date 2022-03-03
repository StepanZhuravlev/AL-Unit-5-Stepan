def presence_check(value):
    # len function doesn't work with numeric types -> convert int, float to str
    if isinstance(value, int) or isinstance(value, float):
        value = str(value)
    if len(value) == 0:
        return False
    else:
        return True


def lookup(value, appropriate_values):
    if value in appropriate_values:
        return True
    else:
        return False
        
        
def length_check(value, max_length):
    if not isinstance(value, tuple) or not isinstance(value, list) or not isinstance(value, dict):  # if variable is not tuple, list, or dictionary, convert to string
        value = str(value)

    if len(value) > max_length:  # if longer than length (length check fail), return False
        return False
    else:  # else (length check pass), return True
        return True


def format_check(value, regex):
    pass


def range_check(value, min_value, max_value):
    """Checks if an integer's value is within the range"""
    if value in range(min_value, max_value+1):
        return False
    else:
        return True

# Type checks needed for: string, int, float, boolean, currency (float to 2 d.p.)
# Format check needed for date:
    # 00 slash 00 slash 0000, where 0 is a digit
    # first digit in dd can only be 0, 1, 2, 3 (if month != 02
    # second


sample = {"a":1, "b":2}
print(str(sample))
print(len(sample))
print(type(sample))
print(isinstance(sample, dict))

print(9 in range(0, 9+1))
