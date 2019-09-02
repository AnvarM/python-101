#csv module
import csv

def csv_reader(file_obj):
    """
    Read a csv file
    get line from csv as string list, create one long string from strings in that list and print it
    """
    reader = csv.reader(file_obj)
    for row in reader:
        print(" ".join(row))
    
    
def csv_dict_reader(file_obj):
    """
    Read a CSV file using csv.DictReader
    get each line in csv as dict and print only values for particular keys
    """
    reader = csv.DictReader(file_obj, delimiter=',')
    for line in reader:
        print(line["first_column_header"], ", ", line["second_column_header"])
        
        
def csv_writer(data, path):
    """
    Write data to a CSV file path
    """
    with open(path, "w", newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for line in data:
            writer.writerow(line)

data = ["first_name,last_name,city".split(","),
        "Redric,Shuhart,Harmont".split(","),
        "Ron,Weasley,Surrey".split(","),
        "Mak,Sim,Masaraksh".split(",")
        ]
path = "output.csv"
csv_writer(data, path)   


def csv_dict_writer(path, fieldnames, data):
    """
    Writes a CSV file using DictWriter
    """
    with open(path, "w", newline='') as out_file:
        writer = csv.DictWriter(out_file, delimiter=',', fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow(row)         
            
data = ["first_name,last_name,city".split(","),
        "Redric,Shuhart,Harmont".split(","),
        "Ron,Weasley,Surrey".split(","),
        "Mak,Sim,Masaraksh".split(",")
        ]

my_list = []
fieldnames = data[0]
for values in data[1:]:
    inner_dict = dict(zip(fieldnames, values)) #create object like this: {'first_name' : 'Redric', 'last_name' : 'Shuhart', 'city' : 'Harmont'}
    my_list.append(inner_dict)
path = "dict_output.csv"
csv_dict_writer(path, fieldnames, my_list)
        
        

if __name__ == "__main__":
    csv_path = "pth_to_csv.csv"
    with open(csv_path, "r") as f_obj:
        csv_reader(f_obj)