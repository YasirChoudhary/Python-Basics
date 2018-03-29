'''
The open() function is used to open files in our system, the filename is the
name of the file to be opened. 

The mode indicates, how the file is going to be opened "r" for reading,
"w" for writing and "a" for a appending. 

The open function takes two arguments, the name of the file and and the mode
for which we would like to open the file. 

By default, when only the filename is passed, the open function opens the file
in read mode.
'''
#rd_file = open('testfile.txt','r')


#read() reads character by character
#rd_file = open('testfile.txt').read()

#readline() read one line at a time and return that line
#rd_file = open('testfile.txt').readline()

#readlines() read multple lines and return tha lines


rd_file = open('testfile.txt').readlines()
for line in rd_file:
    print (line)



'''
rd_file = open('testfile.txt')
#print(rd_file.read())
#print(rd_file.readline())
#print(rd_file.readlines())
'''



