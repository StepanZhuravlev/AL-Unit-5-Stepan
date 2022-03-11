# 1. Currency
# 2. ISBN
# 3. Email
# 4. Library Password

import re


def presence_check(value):
    """PRESENCE CHECK"""
    # len function doesn't work with numeric types -> convert int, float to str
    if isinstance(value, int) or isinstance(value, float):
        value = str(value)
    if len(value) == 0:
        return False
    else:
        return True


def lookup(value, appropriate_values):
    """LOOKUP"""
    if value in appropriate_values:
        return True
    else:
        return False
        
        
def length_check(value, max_length):
    """LENGTH CHECK"""
    if not isinstance(value, tuple) or not isinstance(value, list) or not isinstance(value, dict):  # if variable is not tuple, list, or dictionary, convert to string
        value = str(value)

    if len(value) > max_length:  # if longer than length (length check fail), return False
        return False
    else:  # else (length check pass), return True
        return True


def range_check(value, min_value, max_value):
    """RANGE CHECK"""
    if value in range(min_value, max_value+1):
        return False
    else:
        return True


# TYPE CHECK FUNCTIONS (combine into one?)


def type_check_int(value):
    """INT TYPE CHECK"""
    if isinstance(value, int):
        return True
    else:
        return False


def type_check_float(value):
    """FLOAT TYPE CHECK"""
    if isinstance(value, float):
        return True
    else:
        return False


def type_check_string(value):
    """STR TYPE CHECK"""
    if isinstance(value, string):
        return True
    else:
        return False


def type_check_boolean(value):
    """BOOL TYPE CHECK"""
    if isinstance(value, bool):
        return True
    else:
        return False


# FORMAT CHECK FUNCTIONS:


def format_check_currency(value):
    """CURRENCY FORMAT CHECK (float to 2 d.p.)"""
    # https://stackoverflow.com/questions/23307209/checking-if-input-is-a-float-and-has-exactly-2-numbers-after-the-decimal-point
    if isinstance(value, float):
        # if there is no decimal point, format the value
        # if contains dp:
            # if more than 2 after dp, return false
            # if 1 after dp, format and return True
            # if 2 after dp, return True
        pass
    else:
        return False


def format_check_date(value):
    """DATE FORMAT CHECK"""
    date_pattern = r"[0-9][0-9][/][0-9][0-9][/][0-9][0-9][0-9][0-9]"

    # remove?:
    # try multiple elif statements that return False, and one else statement at the end that returns True (if none of the else ifs get executed)
    # 1. First digit of dd = [0, 1, 2, 3]
    # 2. Second digit of dd = any, unless first digit = 3, then = [0, 1] ONLY
    # 3. First digit of mm = [0, 1]
    # 4. Second digit of mm: 1) if first digit = 0 then all but 0; 2) if first digit = 1 then ONLY [0, 1, 2]
    # 5. No checks for year as that's too complicated
    # 6. if mm = 02, then dd != 29-31
    #if re.match(value, date_pattern):  # first check: just check the "dd/mm/yyyy" pattern
    #   if value[0] not in ["0", "1", "2", "3"]:
    #       return False  # returns False because the first digit of dd can only be 0, 1, 2, or 3
    #    elif value[0] == "3":
    #        if value[1] not in ["0", "1"]:
    #            return False  # returns False because dd can't be equal to 32-39
    #    elif value[3] not in ["0", "1"]:
    #        return False  # returns False because first digit of mm must be 0 or 1
    #    elif value[3] == "0":
    #        if value[4] == "0":
    #            return False  # returns False because month can't be equal to 00
    #    elif value[3] == "1":
    #        if value[4] not in ["0", "1", "2"]:
    #            return False  # returns False because mm can't be equal to 13-19
    #    else:
    #        return True
    #else:  # return False immediately if the first check is failed
    #    return False

    # Doesn't check for invalid dates (e.g. 40/13/9000)
    if re.match(value, date_pattern):
        return True
    else:
        return False


def format_check_postcode(value):
    """POSTCODE FORMAT CHECK"""
    postcode_pattern_1 = r"[A-Z][A-Z][0-9][A-Z] [0-9][A-Z][A-Z]"  # [AA9A 9AA]
    postcode_pattern_2 = r"[A-Z][0-9][A-Z] [0-9][A-Z][A-Z]"  # [A9A 9AA]
    postcode_pattern_3 = r"[A-Z][0-9] [0-9][A-Z][A-Z]"  # [A9 9AA]
    postcode_pattern_4 = r"[A-Z][0-9][0-9] [0-9][A-Z][A-Z]"  # [A99 9AA]
    postcode_pattern_5 = r"[A-Z][A-Z][0-9] [0-9][A-Z][A-Z]"  # [AA9 9AA]
    postcode_pattern_6 = r"[A-Z][A-Z][0-9][0-9] [0-9][A-Z][A-Z]"  # [AA99 9AA]

    if re.match(value, postcode_pattern_1) or re.match(value, postcode_pattern_2) or re.match(value, postcode_pattern_3) or \
       re.match(value, postcode_pattern_4) or re.match(value, postcode_pattern_5) or re.match(value, postcode_pattern_6):
        return True
    else:
        return False


def format_check_lib_passwd(value):
    """PASSWORD FORMAT CHECK"""
    capital_letters = r"[A-Z]"
    small_letters = r"[a-z]"
    digits = r"[0-9]"
    special_symbols = r""  # - + = ! $ % ^ * ; :
    if re.match(value, capital_letters) and re.match(value, small_letters) and re.match(value, digits) and \
       re.match(value, special_symbols):
        return True
    else:
        return False


def format_check_isbn(value):
    """ISBN FORMAT CHECK"""
    pass


def format_check_email(value):
    """EMAIL FORMAT CHECK"""
    pass


sample = {"a": 1, "b": 2}
print(str(sample))
print(len(sample))
print(type(sample))
print(isinstance(sample, dict))
print(type(1))
print(type(True))
print(float(40))

print(9 in range(0, 9+1))
