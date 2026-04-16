from math import dist
s = open("27-78b.txt").readlines()
for i in range(len(s)):
    s[i] = s[i].replace(",", '.')
    s[i] = s[i].split()
    s[i][0] = float(s[i][0])
    s[i][1] = float(s[i][1])

def f(K):
    c = 0
    mn = 100000000000
    for t1 in K:
        sm = 0
        for t2 in K:
            sm += dist(t1, t2)
        if sm < mn:
            mn = sm
            c = t1
    return c

def cluster():
    k = [s.pop(0)]
    el = k[0]
    for el in k:
        for x in s[::]:
            if dist(el, x) < 1:
                k.append(x)
                s.remove(x)
    return k
clustrers = []
while len(s) > 0:
    cl = cluster()
    if len(cl) > 1:
        clustrers.append(cl)

K1 = clustrers[0]
K2 = clustrers[1]
K3 = clustrers[2]
C1 = f(K1)
C2 = f(K2)
C3 = f(K3)
mxs = 0

for t in K1:
    if dist(t, C1) > mxs:
        mxs = dist(t, C1)


mxm = 0
for l in K2:
    if dist(l, C2) > mxm:
        mxm = dist(l, C2)

mxo = 0
for n in K3:
    if dist(n, C3) > mxo:
        mxo = dist(n, C3)


print((mxs + mxm + mxo)/3 * 10000)
