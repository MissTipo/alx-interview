"""The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
(you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
 

Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
"""


def convert(s, numRows):
    """Converts a string into a zigzag according to given number of rows"""
    if numRows == 1:
        return s

    '''rows = []
    zig_row_count = 0
    zig_row = []
    if numRows < 2:
        zig_row_count = numRows - 2
    
    for char, idx in enumerate(s):
        if idx <= numRows:
            rows.append(char)
        elif idx 
'''

    """if numRows > 2:
        zag = numRows - 2

    col = []

    idx = 0
    while idx <= len(s):

        # zig = []
        zag = numRows - 2

        # slice from 0 to 3 : [PAY,*P*, ALI, *S*, HIR, *I*, NG* ]
        str_zig = s[idx: (idx + numRows)]
        if len(str_zig) < numRows:
            while len(str_zig) < numRows:
                str_zig += "*"
            col.append(str_zig)
            break
        col.append(str_zig)
        idx += numRows  # idx is now 3

        str_zag = "*" + s[idx:(idx + zag)] + "*"
        str_zag = str_zag[::-1]
        col.append(str_zag)
        idx += zag  # idx is now 4

    print(col)

    string = ""
    for i in range(numRows):
        for sub in col:
            print(string)
            if sub[i]:
                if sub[i] == '*':
                    continue
                string += sub[i]

    return string"""

    if numRows == 1:
        return s
    rows = [''] * numRows
    row = 0
    step = 1
    for char in s:
        rows[row] += char
        if row == 0:
            step = 1
        elif row == numRows - 1:
            step = -1
        row += step
    return ''.join(rows)


s = "PAYPALISHIRING"
numRows = 4

print(convert(s, numRows))
