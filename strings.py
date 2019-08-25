#Strings in python
#Strings in python are immutable data structure


#Quotes
singleQuotes = 'Single quotes string'
doubleQuotes = "Double quotes string"
tripleQuotesString = """Triple
                        Quotes 
                        String - may be multi-line"""
                        
tripleQuotesString2 = '''Triple
                        Quotes 
                        String - may be multi-line'''
                        
quotesInsideString = 'Quotes "inside"'
quotesInsideString = "Quotes 'inside'"

x = 123
x = str(x) #casting integer into string
x = int(x) #casting x back to integers                        
                        
               
#Concatenation
s1 = "Conca"
s2 = "tenated string"
s3 = s1 + s2


#String methods
testString = " Example string "
e1 = testString.upper() #assign to e1 string " EXAMPLE STRING "
e2 = testString.lower() #assign to e2 string " example string "               
e3 = testString.strip() #remove all the leading and trailing white space including \n, \t etc.
type(testString) # will return <class 'str'>


#Strings slicing
my_string = "I like Python!"
my_string[:1] #return 'I'
my_string[0:12] #return 'I like Pytho'
my_string[0:13] #return 'I like Python'
my_string[0:14] #return 'I like Python!'
my_string[0:-5] #return 'I like Py'
my_string[:] #return 'I like Python!'
my_string[2:] #return 'like Python!'


#String Formatting
my_string = "I like %s" % "Python"
my_string #return 'I like Python'
var = "cookies"
newString = "I like %s" % var
newString #return 'I like cookies'
another_string = "I like %s and %s" % ("Python", var) #if you have more than one variable to format string, you should enclose it with parentheses.
another_string #return 'I like Python and cookies'

my_string = "%i + %i = %i" % (1,2,3)
my_string #return '1 + 2 = 3'
float_string = "%f" % (1.23)
float_string #return '1.230000'
float_string2 = "%.2f" % (1.23)
float_string2 #return '1.23'
float_string3 = "%.2f" % (1.237)
float_string3 #return '1.24'

print("%(lang)s is fun!" % {"lang":"Python"}) #print 'Python is fun!'
print("%(value)s %(value)s %(value)s !" % {"value":"SPAM"}) #print 'SPAM SPAM SPAM !'
print("%(x)i + %(y)i = %(z)i" % {"x":1, "y":2}) #return key error, because dictionary is not contain 'z' key
print("%(x)i + %(y)i = %(z)i" % {"x":1, "y":2, "z":3}) #print '1 + 2 = 3'
"Python is as simple as {0}, {1}, {2}".format("a", "b", "c") # result: 'Python is as simple as a, b, c'
"Python is as simple as {1}, {0}, {2}".format("a", "b", "c") # result: 'Python is as simple as b, a, c'
xy = {"x":0, "y":10}
print("Graph a point at where x={x} and y={y}".format(**xy)) #print 'Graph a point at where x=0 and y=10' double asterisk - for correctly extracting values from dictionary
