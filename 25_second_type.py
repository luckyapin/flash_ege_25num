def count(n):
    d = 2
    dl = 0
    while d*d < n:
        if n % d == 0:
            if d % 2 != 0:
                dl += 1
            if (n//d) % 2 != 0:
                dl += 1
                d += 1
    if d*d == n:
        if d % 2 != 0:
            dl += 1
    return dl


for i in range(23094748, 23094848+1):
    cnt = count(i)
    if cnt == count(int(str(i)[::-1])) and cnt != 1:
        print(i, cnt)
