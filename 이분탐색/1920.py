input()
l = map(int, input().split())
s = set(l)

m = int(input())
l = map(int, input().split())

for i in l:
    if i in s:
        print(1)
    else:
        print(0)