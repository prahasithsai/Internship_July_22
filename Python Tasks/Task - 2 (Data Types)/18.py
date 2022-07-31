# Check Subset
T = int(input())
for i in range(T):
    A = int(input())
    setA = set(map(int,input().split()))
    B = int(input())
    setB = set(map(int,input().split()))
    if setA.issubset(setB):
        print(True)
    else:
        print(False)
