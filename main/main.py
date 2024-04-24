"""
1. read file
2. extract ip, time, info

"""

import re 

def read_txtfile():
    filename = "../log files/" + input("filename: ") + '.txt'
    pattern = r"((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)"
    addys = []
    with open(filename, 'r') as file: 
        for line in file: 
            ip_add = re.search(pattern,line)
            #print(ip_add.group())
            addys.append(ip_add.group())
        print(addys)
            
        


read_txtfile()
