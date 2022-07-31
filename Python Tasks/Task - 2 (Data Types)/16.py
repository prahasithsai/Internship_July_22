# Set Mutations
A = int(input())
setA = set(map(int, input().split()))
N = int(input())
for i in range(N):
    name,length = input().split()
    B = set(map(int,input().split()))
    if name == 'intersection_update':
        setA.intersection_update(B)
    elif name == 'update':
        setA.update(B)
    elif name == 'symmetric_difference_update':
        setA.symmetric_difference_update(B)
    elif name == 'difference_update':
        setA.difference_update(B)
print(sum(setA))
