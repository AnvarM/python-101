args = ["ping", "google.com"]
process = subprocess.Popen(args, stdout=subprocess.PIPE) #redirect standard out (stdout) to our subprocess so we can communicate with it
data = process.communicate() # returns a two-element tuple that contains what was in stdout and stderr.
for line in data:
    print(line)