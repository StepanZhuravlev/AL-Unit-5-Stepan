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
    date_pattern = r"[0-9][0-9][/][0-9][0-9][/][0-9][0-9][0-9][0-9]"
    # try multiple elif statements that return False, and one else statement at the end that returns True (if none of the else ifs get executed)
    # 1. First digit of dd = [0, 1, 2, 3]
    # 2. Second digit of dd = any, unless first digit = 3, then = [0, 1] ONLY
    # 3. First digit of mm = [0, 1]
    # 4. Second digit of mm: 1) if first digit = 0 then all but 0; 2) if first digit = 1 then ONLY [0, 1, 2]
    # 5. No checks for year as that's too complicated
    # 6. if mm = 02, then dd != 29-31

    if re.match(value, date_pattern):  # first check: just check the "dd/mm/yyyy" pattern
        if value[0] not in ["0", "1", "2", "3"]:
            return False  # returns False because the first digit of dd can only be 0, 1, 2, or 3
        elif value[0] == "3":
            if value[1] not in ["0", "1"]:
                return False  # returns False because dd can't be equal to 32-39
        elif value[3] not in ["0", "1"]:
            return False  # returns False because first digit of mm must be 0 or 1
        elif value[3] == "0":
            if value[4] == "0":
                return False  # returns False because month can't be equal to 00
        elif value[3] == "1":
            if value[4] not in ["0", "1", "2"]:
                return False  # returns False because mm can't be equal to 13-19
        else:
            return True
    else:  # return False immediately if the first check is failed
        return False



sample = {"a":1, "b":2}
print(str(sample))
print(len(sample))
print(type(sample))
print(isinstance(sample, dict))
print(type(1))
print(type(True))

print(9 in range(0, 9+1))
