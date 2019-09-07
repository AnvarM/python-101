# sys module
sys.argv # list of command line arguments that were passed to the Python script
argv[0] # return python script name. Depending on the platform that you are running on, the first argument may contain the full path to the script or just the file name

sys.executable # will return absolute path to python interpreter

sys.exit() # allows to exit from python. 
# The exit function takes an optional argument, typically an integer, that gives an exit status. Zero is considered a “successful termination”.
# Be sure to check if your operating system has any special meanings for its exit statuses so that you can follow them in your own application. Note that when you call exit, it will # raise the SystemExit exception, which allows cleanup functions to work in the finally clauses of try / except blocks.

# call_exit.py
import subprocess

code = subprocess.call(["python.exe", "exit.py"])
print(code)

# exit.py
import sys

sys.exit(0)

# result of executed call_exit.py will be 0


sys.path # retruns list of strings that specifies the search path for modules. 
# According to the Python documentation, sys.path is initialized from an environment variable called PYTHONPATH, plus an installation-dependent default.
sys.path.append("/path/to/my/module") # will add to sys.path new path to python module

sys.platform # will show OS platform, for Win10 will return 'win32'
#sys.platform may be used to perform platform-specific stuff:
if os == "win32":
    # use Window-related code here
    import _winreg
elif os.startswith('linux'):
    # do something Linux specific
    import subprocess
    subprocess.Popen(["ls, -l"])
    
   
sys.stdin / stdout / stderr
# The stdin, stdout and stderr map to file objects that correspond to the interpreter’s standard input, output and error streams, respectively. stdin is used for all input given to the interpreter except for scripts whereas stdout is used for the output of print and expression statements.
   