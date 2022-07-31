# Set .discard(), .remove() & .pop()
n = int(input())
mset = set(list(map(int,input().split())))
m = int(input())
for i in range(m):
    c = input().split()
    if len(c)>1:
        e = int(c[1])
    if c[0]=='remove':
        mset.remove(e)
    if c[0]=='discard':
        mset.discard(e)
    elif c[0]=='pop':
        mset.pop()
print(int(sum(mset)))
