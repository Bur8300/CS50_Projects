
near = set([1,2,3,4,5,6])
safes = set([1,2,4])

nears = [node for node in near if node not in safes]

print(nears)

print(safes.issubset(safes))