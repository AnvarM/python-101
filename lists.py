#Lists
#List is mutable data structure

#Empty list creation
my_list = []
my_list = list()


#Lists examples
my_list = [1, 2, 3]
my_list2 = ["a", "b", "c"]
my_list3 = ["a", 1, "Python", 5]

my_nested_list = [my_list, my_list2]
my_nested_list # return [[1, 2, 3], ['a', 'b', 'c']]


#Combine two lists together
#First way to use 'extend method'
combo_list = []
one_list = [4, 5]
combo_list.extend(one_list)
combo_list # return [4, 5]

#Second way just add one list to another
my_list = [1, 2, 3]
my_list2 = ["a", "b", "c"]
combo_list = my_list + my_list2
combo_list #return [1, 2, 3, 'a', 'b', 'c']


#List methods
a = [34, 23, 67, 100, 88, 2]
a.sort() # will sort list by ascendance IN PLACE, it mean that you cant use construction like this: a1 = a.sort() it will assign None value to a1
a.sort(reverse = True) # will sort by desc


#Slice operations are the same as with strings


