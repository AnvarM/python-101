# Dictionary Comprehensions

print( {i: str(i) for i in range(5)} ) # will print {0: '0', 1: '1', 2: '2', 3: '3', 4: '4'}

my_dict = {1:"dog", 2:"cat", 3:"hamster"}
print( {value:key for key, value in my_dict.items()} ) # will print {'hamster': 3, 'dog': 1, 'cat': 2}