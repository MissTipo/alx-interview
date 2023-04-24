#!/usr/bin/python3
"""
UTF-8 Validation
Initialize a counter for the number of bytes in the current character
Loop through each byte in the data and as you do:
Check if the current byte is a valid start byte
If it is, then this is a single-byte character, so we don't need to do anything
If it is not, check if it is a valid start of a 2-byte character
If it is not, check if it is a valid start of a 3-byte character
If it is not, check if it is a valid start of a 4-byte character
If none of the above conditions are satisfied, then the current byte
is not a valid start of a character
For each subsequent byte in the character, check if it
is a valid continuation byte
Check if the byte is a continuation byte (i.e. starts with 0b10)
If we have gone through all the bytes without returning False,
then the data is a valid UTF-8 encoding
"""


def validUTF8(data):
    """Determines if a given data set represents a valid UTF-8 encoding"""
    byte_num = 0
    for byte in data:
        if byte_num == 0:
            if (byte & 0b10000000) == 0b00000000:
                byte_num = 0
            elif (byte & 0b11100000) == 0b11000000:
                byte_num = 1
            elif (byte & 0b11110000) == 0b11100000:
                byte_num = 2
            elif (byte & 0b11111000) == 0b11110000:
                byte_num = 3
            else:
                return False

        else:
            if (byte & 0b11000000) != 0b10000000:
                return False
            byte_num -= 1
    return byte_num == 0
