# FILE INPUT/OUTPUT 

#WRITE MODE/ OPENING A FILE FOR WRITING
f = open("example.txt", "w") # w -> write mode; r -> read mode (Default mode); a -> append mode; x -> create new file; t -> text mode (Default mode); b -> binary mode; + -> read and write mode
data = f.write("     , this is a test file.") # write data to the file
print(data)
f.close() # close the file after reading or writing to it

#APPEND MODE/ OPENING A FILE FOR APPENDING
f = open("example.txt", "a") # append mode; add data to the end of the file without overwriting the existing data
f.write("\nThis is a new line. aha") # append data to the file
f.close()



# READ MODE/ Methods of reading a file
f = open("example.txt", "r")
# #1. read() -> reads the whole file and returns it as a string
# data = f.read()
# print(data)

'''Once the file read all the data it will return an empty string if we try to read it again, because the file pointer is at the end of the file. To read the file again we need to move the file pointer back to the beginning of the file using f.seek(0)'''

# 2. readline() -> reads one line at a time and returns it as a string
f.seek(0) # to move the file pointer back to the beginning of the file
line1 = f.readline()
print(line1)
line2 = f.readline()
print(line2)

# 3. readlines() -> reads the whole file and returns it as a list of strings, where each string is a line in the file
# f.seek(0)
# lines = f.readlines()
# print(lines)
f.close()


#MODE r+ -> this will replace the existing data with new data from the beginning of the file
f = open("example.txt", "r+")
f.write("Hello") # this will replace the existing data with new data from the beginning of the file
f.close()

#MODE w+ -> this will transcate the file to zero length and then write new data to the file, so it will delete the existing data and write new data to the file
f = open("sample.txt", "w+")
print(f.read()) # this will return an empty string because the file is transcated to zero length
f.write("Hello World") # this will delete the existing data and write new data to the file
f.close()

#MODE a+ -> this will append new data to the end of the file without deleting the existing data, and we can also read the file in this mode
f = open("sample.txt", "a+")
print(f.read()) # this will return an empty string because the file pointer is at the end of the file, so we need to move the file pointer back to the beginning of the file using f.seek(0) to read the file
f.seek(0) # to move the file pointer back to the beginning of the file
print(f.read()) # this will return the existing data in the file which is "Hello World
f.write("\nThis is a new line.") # this will append new data to the end of the file without deleting the existing data
f.close()

#r+ -> read+ write mode; overwrite; no transcate; (pointer -> start of the file)
#w+ -> write+ read mode; overwrite; transcate; (pointer -> start of the file)
#a+ -> append+ read mode; append; no transcate; (pointer -> end of the file)


# with SYNTAX 
with open("example.txt", "r") as f: # this will automatically close the file after the block of code is executed, even if an error occurs
    data = f.read()
    print(data)
#f.close() # no need to close the file when using with syntax


# DELETING a FILE (for installing any module we need to use pip (or pip3) install module_name in the command prompt)
# import os
# os.remove("sample.txt") # this will delete the file named "sample.txt" from the current directory

