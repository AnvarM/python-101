# time module
# The time module provides the Python developer access to various time-related functions. The time module is based around what it known as an epoch, the point when time starts. For   
#Unix systems, the epoch was in 1970. To find out what the epoch is on your system, try running the following:
import time
time.gmtime(0) # will return time.struct_time(tm_year=1970, tm_mon=1, tm_mday=1, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=3, tm_yday=1, tm_isdst=0)

#time.ctime
#will convert a time in seconds since the epoch to a string representing local time. If you don’t pass it anything, then the current time is returned. 
time.ctime() # will return 'Sun Sep  8 11:51:44 2019'
time.ctime(2384112639) # will return 'Thu Jul 20 00:30:39 2045'


#time.sleep
#gives the developer the ability to suspend execution of your script a given number of seconds. 
time.sleep(2)


#time.strftime
#it accepts for input: a tuple or a struct_time object, like those that are returned when you call time.gmtime() or time.localtime() 
time.strftime("%Y-%m-%d-%H.%M.%S", time.localtime()) # will return '2019-09-08-11.59.56'


#time.time
#will return the time in seconds since the epoch as a floating point number.
time.time() # will return 1567933304.5638804    