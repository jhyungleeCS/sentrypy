
def read_txtfile():
    filename = input("name of file") + '.txt'
    with open(filename, 'r') as file: 
        content = file.readlines()

``