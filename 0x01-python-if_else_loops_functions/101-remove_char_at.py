#!/usr/bin/python3
def remove_char_at(str, n):
    stored = ""
    for i in range(len(str)):
        if n != i:
            stored += str[i]
    return stored
print(remove_char_at("Best School", 3))
print(remove_char_at("Chicago", 2))
print(remove_char_at("C is fun!", 0))
print(remove_char_at("School", 10))
print(remove_char_at("Python", -1))