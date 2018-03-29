#write() is used write to fixed sequences of characters to file


#writelines() is used write list of strings in a file

f1 = open("testfile.txt",'w')
lines=["first line", "second line", "third line"]

#f1.write("Hello world woroo")
f1.writelines(lines)
f1.close()
