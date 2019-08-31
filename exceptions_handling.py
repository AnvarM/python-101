# Exceptions handling

1 / 0
Traceback (most recent call last):
File "<string>", line 1, in <fragment>
ZeroDivisionError: integer division or modulo by zero

try:
    1 / 0
except ZeroDivisionError:
    print("You cannot divide by zero!")
# output will be: You cannot divide by zero!



my_dict = {"a":1, "b":2, "c":3}
try:
    value = my_dict["d"]
except KeyError:
    print("That key does not exist!")
# output will be: That key does not exist!

my_list = [1, 2, 3, 4, 5]
try:
    my_list[6]
except IndexError:
    print("That index is not in the list!")
# output will be: That index is not in the list!


my_dict = {"a":1, "b":2, "c":3}
try:
    value = my_dict["d"]
except IndexError:
    print("This index does not exist!")
except KeyError:
    print("This key is not in the dictionary!")
except:
    print("Some other error occurred!")
    
try:
    value = my_dict["d"]
except (IndexError, KeyError):
    print("An IndexError or KeyError occurred!")    
    
    
    
#The "finally" Statement    
my_dict = {"a":1, "b":2, "c":3}
try:
    value = my_dict["d"]
except KeyError:
    print("A KeyError occurred!")
finally:
    print("The finally statement has executed!")
#will return:
#A KeyError occurred!
#The finally statement has executed!
#Finally statement always executes


#try, except, or else
my_dict = {"a":1, "b":2, "c":3} 
try:
    value = my_dict["a"]
except KeyError:
    print("A KeyError occurred!")
else:
    print("No error occurred!")
    
    
    