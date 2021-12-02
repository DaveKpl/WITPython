def convert_string_to_number(myString):
    return int(myString)

def find_min(myList):
    return min(myList)

def print_list(myList):
    for i in myList:
        print(i)

def print_dict(myDict):
    for key,value in myDict.items():
        print(f'"{key}"',value)

def get_str_len(myStr):
    return len(myStr)

def remove_outer_characters(myStr):
    return myStr[1: (len(myStr)-1)]

def count_chars(myStr):
    myDict={}
    for i in myStr:
        myDict.update({i: myStr.count(i)})
    return myDict
