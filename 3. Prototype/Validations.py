#presence(value), lookup(value), length(value, length), range(value, min, max), format(value, regex)


def presence_check(value):
    # Convert the value to string if it is of a different type
    if not isinstance(value, str):
        value_to_string = str(value)
    if len(value_to_string) == 0:
        # Code to be executed is value is absent
        flag = False
        return flag
    else:
        # Code to be executed if value is present
        flag = True
        return flag


def lookup(value, appropriate_values):
    # appropriate_values is a list
    # In appropriate_values, every letter should be capital
    if value in appropriate_values:
        # Code to be executed if there is a match
        flag = True
        return flag
    else:
        # Code to be executed if the value is inappropriate
        flag = False
        return flag
        
        
def length_check(value, length):
    # If value is str/list/tuple/dictionary, leave as is
    # If value is of a different type, convert to str
    pass


def format_check(value, regex):
    pass


def range_check(value, min, max):
    pass