def sheeps(x):
    if x < 1:
        return
    for i in range(1, x+1):
        print(f"{i} sheep ~ ", end='')

sheeps(6)
