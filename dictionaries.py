#Dictionaries
#Dictionary is mutable data structure

my_dict = {}
another_dict = dict()
my_other_dict = {"one":1, "two":2, "three":3}
my_other_dict #returns {'three': 3, 'two': 2, 'one': 1}
my_other_dict["one"] #will teturn 1
my_dict = {"name":"Fr", "address":"123 Elm street"}
my_dict["name"] #return 'Fr'

"name" in my_dict #will return True
"state" in my_dict #will return False

my_dict.keys() #will return dict_keys(['name', 'address'])

"name" in my_dict # this is good
"name" in my_dict.keys() # this works too, but is slower