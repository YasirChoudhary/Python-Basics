rd_file = open('testfile.txt',"r")
count = 0
for char in rd_file:
    count += 1
    print (char)
print("count of characters in file ",count)

