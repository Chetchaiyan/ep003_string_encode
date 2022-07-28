"""
    Write a program that takes a string and encode it that the amount of symbols
    would be represented by interger and the symbol.

    Input : AAAABBBCCDAAA
    Output : 4A3B2C1D2A

    Input : PHP
    Output : 1P1H1P

    Input : CCoding
    Output : 2C1o1d1i1n1g
"""

def encode_string(input:str) -> str :
    result = ""
    latest_char = ""
    char_count = 0
    for c in input :
        if c != latest_char :
            if char_count > 0:
                result += f"{char_count}{latest_char}"
            char_count = 1
            latest_char = c
        else :
            char_count += 1
    if char_count > 0 :
        result += f"{char_count}{input[-1]}"
    return result 

if __name__ == "__main__" :
    input_str = input("Input : ")
    output_str = encode_string(input_str)
    print(f"Output : {output_str}")