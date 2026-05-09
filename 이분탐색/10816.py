import sys
input = sys.stdin.readline

N = int(input())
cards = list(map(int, input().split()))

count = {}
for c in cards:
    if c in count:
        count[c] += 1
    else:
        count[c] = 1

M = int(input())

targets = list(map(int, input().split()))

result = []
for t in targets:
    result.append(str(count.get(t, 0)))

print(' '.join(result))