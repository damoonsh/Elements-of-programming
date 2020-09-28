""" 
    5.9 Elias Gamma Coding
    encodes and decodes an array of numbers
"""

def convert_to_binary(num: int):
    mod, div, bin_num = num % 2, num // 2, ""
    
    while div > 2:
        bin_num = str(mod) + bin_num

        mod, div = div % 2, div // 2

    bin_num = str(div) + str(mod) + bin_num

    return 0 * len(bin_num) + bin_num

print(convert_to_binary(10))