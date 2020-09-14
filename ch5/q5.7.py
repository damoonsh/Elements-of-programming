"""
    5.7 Base Conversion:
    Write a function that gets b1, S, b2 and returns the number in
    s with the base of b2.
"""

def base_10(b1, s):
    """ Returns a number with its base 10 """
    val, i = 0, 0

    for num in s:
        val += b1 ** (len(s) - 1 - i) * int(num)
        i += 1

    return val

def convert_base(b1, s, b2):
    """ Converting a number from base b1 to b2 """
    num, new_num = base_10(b1, s), ""

    div, mod = num // b2, num % b2

    while (div > b2) :
        new_num = str(mod) + new_num

        div, mod = div // b2, div % b2

    return str(div) + str(mod) + new_num

        

print(convert_base(12, "236", 6))