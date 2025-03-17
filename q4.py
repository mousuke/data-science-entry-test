def string_reverse(s):
    """
    Task 1
    - Create a function that reverses a given string (s).
    - s must be a string.
    - Return the reversed string.
    """
    if isinstance(s, str): 
        return s[::-1]
    else:
        return "Error: input is not a string" 


# Task 2
# Invoke the function "string_reverse" using the following scenarios:
# - "Hello World"
# - "Python"
