set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}
print(set1.union(set2))          #set1+set2
print(set1.intersection(set2))
print(set1.difference(set2))    #set1-set2

s1 = {1,2,3,4,5}   #superset
s2 = {1,2,3}       #subset
print(s2.issubset(s1))
print(s1.issuperset(s2))

s1 = {1,2,3,4,5}
s2 = {7,8}
s1.update({7,8})
print(s1)

print(1 in s1)