#!/usr/bin/python3
def to_subtract(list_num):
    num1 = 0
    max_list = max(list_num)
    for num in list_num:
        if max_list > num:
            num1 += num
    return (max_list - num1)


def roman_to_int(roman_string):
    if not roman_string:
        return 0
    if not isinstance(roman_string, str):
        return 0
    rom_n = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    list_keys = list(rom_n.keys())
    num2 = 0
    last_rom = 0
    list_num = [0]
    for ch in roman_string:
        for r_num in list_keys:
            if r_num == ch:
                if rom_n.get(ch) <= last_rom:
                    num2 += to_subtract(list_num)
                    list_num = [rom_n.get(ch)]
                else:
                    list_num.append(rom_n.get(ch))
                last_rom = rom_n.get(ch)
    num2 += to_subtract(list_num)
    return (num2)
