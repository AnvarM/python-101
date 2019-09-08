# datetime module
datetime.date(2012, 12, 14) # will create datetime object, order should be: datetime.date(year, month, day)
d.year # will return 2012
d.month # will return 12
d.day # will return 14
datetime.date.today() # return datetime.date(2019, 9, 8)

datetime.datetime # datetime.datetime object contains all the information from a datetime.date plus a datetime.time object
d = datetime.datetime(2019, 3, 5, 12, 30, 10)
d.year # 2019
d.second # 10
d.hour # 12

datetime.datetime.today() # will return datetime.datetime(2019, 9, 8, 11, 6, 49, 384653)
datetime.datetime.now() # will return datetime.datetime(2019, 9, 8, 11, 7, 14, 788889)

#strftime 
#method allows the developer to create a string that represents the time in a more human readable format

datetime.datetime.today().strftime("%Y-%m-%d") # will return '2019-09-08'
today = datetime.datetime.today()
today.strftime("%m/%d/%Y") # will return '09/08/2019'
today.strftime("%Y-%m-%d %H:%M:%S") # will return '2019-09-08 11:09:54'
#If you want to go to a two-digit year, you can swap out the %Y for %y
today.strftime("%y-%m-%d %H:%M:%S") # will return '19-09-08 11:09:54'


#datetime.timedelta
#datetime.timedelta object represents a time duration. In other words, it is the difference between two dates or times. 
now = datetime.datetime.now()
now # will return datetime.datetime(2019, 9, 8, 11, 14, 52, 145217)
then = datetime.datetime(2019, 2, 26) # datetime.datetime(2019, 2, 26, 0, 0)
delta = now - then
type(delta) # will return <type 'datetime.timedelta'>
delta.days # will return 194
delta.seconds # will return 40492
seconds = delta.total_seconds() # will return total amount of seconds from delta