#!/usr/bin/python3

def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0
    roman_dic = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    result = 0
    x = 0
    if not roman_string:
        return 0
    if len(roman_string) == 1:
        return roman_dic[roman_string]
    else:
        while x < len(roman_string):
            if x+1 >= len(roman_string) and roman_dic[roman_string[x-1]] >= roman_dic[roman_string[x]]:
                result += roman_dic[roman_string[x]]
                break
            elif x+1 >= len(roman_string) and roman_dic[roman_string[x-1]] < roman_dic[roman_string[x]]:
                result -= roman_dic[roman_string[x]]
                break
            if roman_dic[roman_string[x]] >= roman_dic[roman_string[x+1]] or x+1 == len(roman_string)-1:
                result += roman_dic[roman_string[x]]+roman_dic[roman_string[x+1]]
                x += 1
            elif roman_dic[roman_string[x]] < roman_dic[roman_string[x+1]] or x+1 == len(roman_string)-1:
                result += roman_dic[roman_string[x+1]]-roman_dic[roman_string[x]]
            x += 1
    return result
