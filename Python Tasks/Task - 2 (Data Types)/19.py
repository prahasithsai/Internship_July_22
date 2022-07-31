# Check Strict Superset
setA = set(input().split())
print(all([setA.issuperset(set(input().split())) for _ in range(int(input()))]))

