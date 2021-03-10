def read_file(filename):
    source_file = open(filename, 'r')

    lines = source_file.readlines()

    source_file.close()
    
    return lines

def read_file_autoclose(filename):
    with open(filename, 'r') as source_file:
        return source_file.readlines()

def strip_newlines(items):
    return list(map(lambda s: s.rstrip('\n'), items))

def list_contains(item_to_find, items):
    return any(item_to_find in s for s in items)

def output_if_list_contains(item_to_find, items):
    in_list = list_contains(item_to_find, items)
    print('List contains ', item_to_find, ':', in_list)

# main

lines = read_file_autoclose('data/names.txt')
stripped_lines = strip_newlines(lines)

name_in_list = 'Alister'
name_not_in_list = 'not a real name'

output_if_list_contains(name_in_list, stripped_lines)
output_if_list_contains(name_not_in_list, stripped_lines)
