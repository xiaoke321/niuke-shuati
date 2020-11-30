import copy

kvps = { '1' : 1, '2' : 2 }
# theCopy = kvps.copy()
theCopy = copy.copy(kvps)
# theCopy = kvps
kvps['1'] = 5
print(kvps)
print(theCopy)
sum = kvps['1'] + theCopy['1']
print(sum)