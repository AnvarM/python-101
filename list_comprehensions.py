# List Comprehensions
x = [i for i in range(5)] # will assign to x list [0,1,2,3,4]

# If you need to parse some file and transform only strings which have some special contition:
if [i for i in file_read_descripter if "SOME TERM" in i]:
    # do something
    
x = ['1', '2', '3', '4', '5']
y = [int(i) for i in x]
y # will return [1, 2, 3, 4, 5]    
    
    
myStrings = [s.strip() for s in myStringList] # will apply strip() method to each string in stringlist


[[1,2,3], [4,5,6], [7,8,9]]
[num for elem in vec for num in elem] # will return [1, 2, 3, 4, 5, 6, 7, 8, 9]    

[(x, y) for x in [1,2,3] for y in [3,1,4] if x != y] # will return [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]