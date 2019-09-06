#os module
os.name # return name of operating system, in case of windows will return 'nt'
os.environ # return dictionary with operating system environment variables
os.getenv("TMP") # will return value for environment variable TMP
os.getcwd() # will return current path
os.chdir(r"C:\\temp") # will change current directory to C:\temp
os.mkdir("test") # will create "test" directory in current directory
os.mkdir(r'C:\temp\testldr') # will create diirectory by specified path, if path exists, or throw an error
os.makedirs(r'C:\temp\1\2\3\4') # will create a directory and all nested directories if they not existed
os.remove("test.txt") # will attempt to remove file "test.txt" from current directory
os.rmdir("pytest") # will attempt to remove directory "pytest" from corrent directory
os.removedirs() # with specified path will delete nested empty directories recursively
os.rename("test.txt", "pytest.txt") # will rename file test.txt to pytest.txt if file test.txt exists in current directory
os.startfile() # method start a file from argument with associated program
os.walk() # iterate over a root level path and return generator object, you may get elements from this object with help of next loop:
    for root, dirs, files in os.walk(path):
        print(root)
       
os.path.basename(r'C:\temp\1\2\1.txt') # will return just name of file - 1.txt       
os.path.dirname(r'C:\temp\1\2\1.txt') # will return just name of directory - C:\\temp\\1\\2       
os.path.exists() #  will tell you if a path exists or not, return boolean value
os.path.isdir(path) # will check if path is directory
os.path.isfile(path) # will check if path is file
os.path.join() # join method give you the ability to join one or more path components together using the appropriate separator. For example, on Windows, the separator is the backslash, but on Linux, the separator is the forward slash
os.path.join(r'C:\temp\1\2\3\4', 'test.py') # will return 'C:\\temp\\1\\2\\3\\4\\test.py'
os.path.split(path) # will split a path into a tuple that contains the directory and the file.
os.path.split(r'C:\temp\1\2\3.txt') # will return ('C:\\temp\\1\\2', '3.txt')
os.path.split(r'C:\temp\1\2\3') # will return ('C:\\temp\\1\\2', '3') if filename is absent in path, it will return tuple with path without last dir and last directory in that path