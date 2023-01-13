def get_bit(value, index):
    return value & pow(2, index) != 0

def get_sub_binary(value, inclusive_start, exclusive_end):
    bin_string = bin(value)[:1:-1]
    print(bin_string)
    bin_substring = bin_string[inclusive_start:exclusive_end]
    print(bin_substring)
    return int(bin_substring[::-1], 2)

def flip_bin(value):
    return int(str(value)[::-1])