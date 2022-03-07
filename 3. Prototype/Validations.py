import re


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


def type_check_int(value):
    if isinstance(value, int):
        return True
    else:
        return False


def type_check_float(value):
    if isinstance(value, float):
        return True
    else:
        return False


def type_check_string(value):
    if isinstance(value, string):
        return True
    else:
        return False


def type_check_boolean(value):
    if isinstance(value, bool):
        return True
    else:
        return False


def type_check_currency(value):  # float to 2 d.p.
    if isinstance(value, float):
        # check 2 d.p.
        pass
    else:
        return False

# Type checks needed for: string, int, float, boolean, currency (float to 2 d.p.)
# Format check needed for date:
    # dd slash mm slash yyyy
    # first digit in dd can only be 0, 1, 2, 3 (if month != 02)
    # second digit in dd can be any
    # first digit in mm is 0 or 1
    # second digit is any
    # any digits in yyyy


def type_check_date(value):
    date_pattern = r"[0-3][0-9][/][0-1][0-9][/][1-2][0-9][0-9][0-9]"
    valid_dd_pattern = [0, 1]
    if re.match(value, date_pattern):
        # proceed to further checks
        if value[0] == "3":  # if day is 30 or 31
            if value[1] not in valid_dd_pattern:
                return False

        pass
    else:
        return False



sample = {"a":1, "b":2}
print(str(sample))
print(len(sample))
print(type(sample))
print(isinstance(sample, dict))
print(type(1))
print(type(True))

print(9 in range(0, 9+1))
