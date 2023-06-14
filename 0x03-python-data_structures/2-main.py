#!/usr/bin/python3
replace_in_list = __import__('2-replace_in_list').replace_in_list

my_list = [1, 2, 3, 4, 5]
idx = 3
xlist = [1, 2, 3, 4, 6]
blist = []
new_element = 9
new_list = replace_in_list(my_list, idx, new_element)
xdlist = replace_in_list(xlist, 5, 7)
xxdlist = replace_in_list(blist, 2, 9)
print(xdlist)
print(new_list)
print(my_list)
