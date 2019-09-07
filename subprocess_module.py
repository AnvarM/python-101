# subprocess
#call method allows you to call another program, wait for the command to complete and then return the return code.
import subprocess
subprocess.call("notepad.exe") # will open notepad.exe(if it exists), wait until notepad.exe will close and return the return code

code = subprocess.call(["ping", "google.com"]) # will ping google.com and assign the return code to code


# The Popen Class
# The Popen class executes a child program in a new process. Unlike the call method, it does not wait for
# the called process to end unless you tell it to using by using the wait() method. 

program = "notepad.exe"
subprocess.Popen(program) # will open notepad.exe and return message like: <subprocess.Popen object at 0x01EE0430>

program = "notepad.exe"
process = subprocess.Popen(program) # will open notepad.exe
code = process.wait() # wait until process closed and assign return code to code
print(code) # print 0 if processed was closed successfully
