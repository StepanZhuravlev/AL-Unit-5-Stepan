# IMPORTANT:
# re.match(pattern, string, flags=0)
# If zero or more characters at the beginning of string match the regular expression pattern, return a corresponding match object.
# Return None if the string does not match the pattern; note that this is different from a zero-length match.

# re.search(pattern, string, flags=0)
# Scan through string looking for the first location where the regular expression pattern produces a match, and return a corresponding match object.
# Return None if no position in the string matches the pattern; note that this is different from finding a zero-length match at some point in the string.

# re.findall(pattern, string, flags=0)
# Returns a list of all substrings that match a pattern.

# . matches any character
# ^ASDF - should start with ASDF
# ASDF$ - should end with ASDF
# \s - whitespace character

import re
import decimal
from tkinter import *

# BASIC VALIDATIONS


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


# TYPE CHECK FUNCTIONS


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
    if isinstance(value, str):
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


def format_check_currency(value):  # Doesn't use RegEx, debugged
    """CURRENCY FORMAT CHECK (float to 2 d.p.)"""
    # count dp
    # if 0 or 1 - format to 2 and return True, store formatted value in database
    # if 2 - return True
    # if more than 2 return False and error
    decimal_places = abs(decimal.Decimal(value).as_tuple().exponent)
    value = float(value)
    if decimal_places < 2:
        value = "{:.2f}".format(value)  # the formatted value needs to be put into the database
        return True, value
    if decimal_places == 2:
        return True, value
    if decimal_places > 2:
        return False


def format_check_date(value):  # FIXED
    """DATE FORMAT CHECK"""
    date_pattern = r"[0-9][0-9][/][0-9][0-9][/][0-9][0-9][0-9][0-9]"
    if re.match(date_pattern, value):
        return True
    else:
        return False


def format_check_postcode(value):  # FIXED
    """POSTCODE FORMAT CHECK"""
    postcode_pattern_1 = r"[A-Z][A-Z][0-9][A-Z]\s[0-9][A-Z][A-Z]"  # [AA9A 9AA]
    postcode_pattern_2 = r"[A-Z][0-9][A-Z]\s[0-9][A-Z][A-Z]"  # [A9A 9AA]
    postcode_pattern_3 = r"[A-Z][0-9]\s[0-9][A-Z][A-Z]"  # [A9 9AA]
    postcode_pattern_4 = r"[A-Z][0-9][0-9]\s[0-9][A-Z][A-Z]"  # [A99 9AA]
    postcode_pattern_5 = r"[A-Z][A-Z][0-9]\s[0-9][A-Z][A-Z]"  # [AA9 9AA]
    postcode_pattern_6 = r"[A-Z][A-Z][0-9][0-9]\s[0-9][A-Z][A-Z]"  # [AA99 9AA]

    if re.match(postcode_pattern_1, value) or re.match(postcode_pattern_2, value) or re.match(postcode_pattern_3, value) or \
       re.match(postcode_pattern_4, value) or re.match(postcode_pattern_5, value) or re.match(postcode_pattern_6, value):
        return True
    else:
        return False


def format_check_lib_passwd(value):
    """PASSWORD FORMAT CHECK"""
    # Must have uppercase letters, lowercase letters, special symbols (e.g. ! * # % & - _ + =), digits
    # Must not have whitespaces
    if " " in value:
        return False  # no whitespaces allowed
    if re.search(r"[A-Z]", value) is not None:
        if re.search(r"[a-z]", value) is not None:
            if re.search(r"0-9", value) is not None:
                if re.search("[^A-Za-z0-9]", value) is not None:  # checks for special characters (whitespaces are special characters too, however their absence is checked in the first if statement
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False


def format_check_isbn(value):
    """ISBN FORMAT CHECK"""  # Can take a lot of time to code, probably not worthwhile
    pass


def format_check_email(value):
    """EMAIL FORMAT CHECK"""
    # only one repetition of @, one or more reps of .
    if len(re.findall(r"[@]", value)) == 1:
        if len(re.findall(r"[.]", value)) >= 1:
            return True
        else:
            return False
    else:
        return False


# Main program:
#test_tuple = ("a", "b")
#print(type(test_tuple))
#help(OptionMenu)

print(type_check_string("Hell"))
