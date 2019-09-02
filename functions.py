# Functions
def many(*args, **kwargs):
    print(args)
    print(kwargs)
many(1, 2, 3, name="Mike", job="programmer") #will print:
    (1, 2, 3)
    {'job': 'programmer', 'name': 'Mike'}