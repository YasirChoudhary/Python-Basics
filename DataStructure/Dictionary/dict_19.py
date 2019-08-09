# Flipping dictionary

"""
Syntax: dict.setdefault(key[, default_value])

Parameters: It takes two parameters:
key – Key to be searched in the dictionary.
default_value (optional) – Key with a value default_value is inserted to the dictionary if key is not in the dictionary.
If not provided, the default_value will be None.

Returns:
Value of the key if it is in the dictionary.
None if key is not in the dictionary and default_value is not specified.
default_value if key is not in the dictionary and default_value is specified.
"""

def group_by_owners(files):
    flipped = {}
    for key, value in files.items():
        flipped.setdefault(value, []).append(key)
    return flipped

files = {
    'Input.txt': 'Randy',
    'Code.py': 'Stan',
    'Output.txt': 'Randy'
}
print(group_by_owners(files))

