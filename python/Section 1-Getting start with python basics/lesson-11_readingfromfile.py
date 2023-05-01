# open() is a build in function that used to open the give file
file=open("file.txt","r")
print(file)

#output=<_io.TextIOWrapper name='file.txt' mode='r' encoding='cp1252'>
print(file.read())#read()=this is a build in function that used to read the data in the file

#output=Hello this file is going to get read