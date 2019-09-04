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