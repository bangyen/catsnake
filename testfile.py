def add(i, j):
    ans = i
    for n in range(j):
        ans = -~ans
    return ans

def sub(i, j):
    ans = i
    for n in range(j):
        ans = ~-ans
    return ans

print(sub(3, 5))