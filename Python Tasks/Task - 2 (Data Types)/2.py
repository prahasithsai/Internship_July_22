# Find the Runner-Up Score!
n = int(input())
arr = map(int, input().split())
print(sorted(set(arr))[-2])

