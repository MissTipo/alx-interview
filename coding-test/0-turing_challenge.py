"""A string contains a list of color a=names that are separated by a single space.

colors in str are mixed up, but each color has its original position at the end of the color name, positions
are 1-indexed. eg string black gold, white can be rearranged to gold2 black1 white3. str contains only upto 9 colors. 
Given a str with rearranged colors, sort the colors to original state and return the original str.

rearranged_str = 'gold2 black1 white3'
output = 'black gold white'
"""


def solution(s: str) -> str:
    """Sort the colors to original state and return the original str."""
    str_list = s.split(' ')
    sorted_list = sorted(str_list, key=lambda color: (color[-1]))
    new_list = []
    for color in sorted_list:
        new_list.append(color[:-1])

    return ' '.join(new_list)


s = 'gold2 black1 white3'
print(solution(s))
