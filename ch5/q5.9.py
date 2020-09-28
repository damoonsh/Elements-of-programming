""" 
    5.9 Elias Gamma Coding
    encodes and decodes an array of numbers
"""
def gamma_encoding(num: int):
    mod, div, bin_num = num % 2, num // 2, ""
    
    while div > 1:
        bin_num = str(mod) + bin_num

        mod, div = div % 2, div // 2

    bin_num = str(div) + str(mod) + bin_num

    return "0" * len(bin_num) + bin_num

def gamma_decoding(num):
    num = num[(len(num) - 1) // 2: len(num)]
    new_num, exp = 0, 0

    for digit in num:
        new_num += 2 ** (len(num) - 1 - exp) * int(digit)
        exp += 1

    return new_num

def encode_array(nums):
    new_arr = []

    for num in nums:
        new_arr.append(gamma_encoding(num))

    return new_arr

def decode_array(nums):
    new_arr = []

    for num in nums:
        new_arr.append(gamma_decoding(num))

    return new_arr