#presence(value), lookup(value), length(value, length), range(value, min, max), format(value, regex)


def presence_check(value):
    # Convert the value to string if it is of a different type
    if isinstance(value, str) == False:
        value_to_string = str(value)
    
    if len(value_to_string) == 0:
        # Code to be executed is value is absent
        print("There is no value.")
    else:
        # Code to be executed if value is present
        print("Value is present.")


def lookup(value, appropriate_values):
    # appropriate_values is a list
    # In appropriate_values, every letter should be capital
    if value in appropriate values:
        # Code to be executed if there is a match
        print("Value is appropriate.")
    else:
        # Code to be executed if the value is inappropriate
        print("Match not found.")
        
        
def length_check(value, length):
    # If value is str/list/tuple/dictionary, leave as is
    # If value is of a different type, convert to str
    pass


def format_check(value, regex):
    pass


def range_check(value, min, max):
    pass