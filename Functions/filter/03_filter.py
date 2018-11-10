#Remove missing data

#Remove empty string
fruits = ["", "Apple", "Mango", "", "", "PineApple", "Banana"]
print(list(filter(None, fruits)))

#Remove zero
nums = [0, 0.1, 2, 2.2, 0.0, 9]
print(list(filter(None, nums)))

"""
False values:
"", 0, 0.0, 0j, [], (), False, None
"""