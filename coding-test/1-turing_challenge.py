"""Given a string s and letter t that exists once or more times in the string s.

return an array d where d[idx] is the minimum number of letters required to move from letter s[idx] to the closest letter t in s

s ='cdhgcgtfc'
t = g

d = [3, 2, 1, 0, 1, 0, 1, 2, 3]


"""


def distance_to_closest_letter(s, t):
    """"""
    if len(s) == 1 and s[0] == t:
        return [0]

    l = len(s)
    d = []

    for i in range(l):
        if s[i] == t:
            d.append(0)
            continue
        '''t_idx = s.index(t)
        print(t_idx)
        
        diff = t_idx - i
        d.append(diff)'''
        d_arr = []
        for j in range(i+1, l):
            if s[j] == t:
                fd = j - i
                d_arr.append(fd)
        for k in range(i-1, 0, -1):
            if s[k] == t:
                bd = i - k
                d_arr.append(bd)
        d.append(min(d_arr))

    return d


s = 'cdhgcgtfc'
t = 'g'

print(distance_to_closest_letter(s, t))
