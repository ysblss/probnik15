def f(n):
    s = ''
    while n > 0:
        s = str(n%6) + s
        n//=6
    return s


def g(n):
    s = ''
    while n > 0:
        s = str(n%9) + s
        n//=9
    return s

s = open("17-418.txt").readlines()
s = [int(x) for x in s]

mn6 = 10 ** 10
for x in s:
    if x < mn6 and len and len(f(x)) == 4:
        mn6 = x

mn9 = 100000000000000
for x in s:
    if x < mn9 and len and len(g(x)) == 3:
        mn9 = x
k = 0
A = []
for i in range(len(s)-1):
    if (s[i] % 11 == mn6 % 5 and s[i+1] % 11 == mn6 % 5 ) or (s[i] % 11 == mn6 % 5 and s[i+1] % 11 != mn6 % 5 ) or (s[i] % 11 != mn6 % 5 and s[i+1] % 11 == mn6 % 5 ):
        if (s[i] % 7 == mn9 % 13 and s[i+1] % 7 == mn9 % 13) or (s[i] % 7 == mn9 % 13 and s[i+1] % 7 != mn9 % 13) or (s[i] % 7 != mn9 % 13 and s[i+1] % 7 == mn9 % 13):
            k+=1
            A.append(s[i] + s[i+1])
print(k, max(A))
