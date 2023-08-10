"""Area of one line = x*x*x
totalSquareArea for i line = for in range(1, x+1)
sum += i^3

x = 4
sum = 0
for i in range(1, x+1):
	sum += i^3
return sum

when i = 1, sum = 0 + 1^3 = 1
'' '' '' 2, '' '' 1 + 2^3 = 9
	3, 	9 + 3^3 = 36
	4	36 + 4^3 = 100
"""


def total_square_area(x):
    _sum = 0
    if x < 1:
        return 0
    if x == 1:
        return 1
    _sum = (x ** 3) + total_square_area(x - 1)
    return _sum

print(total_square_area(4))
