dict_file = {}
with open('1.txt', 'r', encoding='utf-8') as f:
    lines_1 = f.readlines()
    numb_lines = str(len(lines_1))
    name_file = "1.txt"
    lines_1.insert(0, name_file)
    lines_1.insert(1,numb_lines)

with open('2.txt', 'r', encoding='utf-8') as f:
    lines_2 = f.readlines()
    numb_lines = str(len(lines_2))
    name_file = "2.txt"
    lines_2.insert(0, name_file)
    lines_2.insert(1,numb_lines)

with open('3.txt', 'r', encoding='utf-8') as f:
    lines_3 = f.readlines()
    numb_lines = str(len(lines_3))
    name_file = "3.txt"
    lines_3.insert(0, name_file)
    lines_3.insert(1,numb_lines)

list_full = [lines_1, lines_2, lines_3]
list_sort = sorted(list_full, key=len)
string_join = ""
for sort in list_sort:
    string_join += "\n".join(sort) + "\n"

print(string_join)