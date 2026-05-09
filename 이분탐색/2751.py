import sys
input = sys.stdin.readline
n = int(input())

l = []
for i in range(n):
    a = int(input())
    l.append(a)

#for _ in range(n - 1):
#    for i in range(1, n):
#        if l[i - 1] > l[i]:
#            l[i], l[i - 1] = l[i - 1], l[i]
l.sort()
print(*l , sep="\n")