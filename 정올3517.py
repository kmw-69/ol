def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    
    return - 1
N = int(input())
arr = list(map(int, input().split()))

Q = int(input())
queries = list(map(int, input().split()))

for target in queries:
    print(binary_search(arr, target))