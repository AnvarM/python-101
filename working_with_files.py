# Working with files

handle = open("test.txt") # will open file in read-only mode
handle = open(r"C:\Users\mike\py101book\data\test.txt", "r") #  also will open file in read-only mode


handle = open("test.txt", "r")
data = handle.read() # will read all file content to string and assign it to data
handle.close()


handle = open("test.txt", "r")
data = handle.readline() # read just one line
handle.close()


handle = open("test.txt", "r")
data = handle.readlines() # read ALL the lines to data variable, data is list now
handle.close()


#Will read and print all file content line by line
handle = open("test.txt", "r")
for line in handle:
    print(line)
handle.close()


# Will read all file content by pieces with size = 1024 bytes
handle = open("test.txt", "r")
while True:
    data = handle.read(1024)
    print(data)
    if not data:
        break
        
        
#Will read file in binary mode        
handle = open("test.pdf", "rb")        



#Will open file in write mode and write one line to file:
handle = open("output.txt", "w")
handle.write("This is a test!")
handle.writelines(['a', 'b', 'c', 'd', 'e', 'f', 'g']) # will write each string from list to file, element by element
handle.close()



#Read file with help of "with" statement, with statement help to close file handler automatically after file processing
with open("test.txt") as file_handler:
    for line in file_handler:
        print(line)
        
        
        
#Catching Errors
#Regular try/except 
 try:
    file_handler = open("test.txt")
    for line in file_handler:
        print(line)
except IOError:
    print("An IOError has occurred!")
finally:
    file_handler.close()        
    
 
#With statement
try:
    with open("test.txt") as file_handler:
        for line in file_handler:
            print(line)
except IOError:
    print("An IOError has occurred!") 
 