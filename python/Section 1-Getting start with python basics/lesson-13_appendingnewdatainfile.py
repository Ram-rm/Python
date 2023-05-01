file=open("file.txt",'a+')
file.seek(0)
print(file.read())
file.write("Hello this text has been add using the append() method\n")
file.close()

#how to read and write the same file

#file=open("file.txt",'a+')
#file.seek()=>this build in function is used to move the cursor to starting point of the data

#output:

# This line has been written by the write() function
# Hello this text has been add using the append() methodHello this text has been add using the append() method