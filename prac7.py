# FILE INPUT/OUTPUT 

#WRITE MODE/ OPENING A FILE FOR WRITING
f = open("example.txt", "w") # w -> write mode; r -> read mode (Default mode); a -> append mode; x -> create new file; t -> text mode (Default mode); b -> binary mode; + -> read and write mode
data = f.write("     , this is a test file.") # write data to the file
print(data)
f.close() # close the file after reading or writing to it

