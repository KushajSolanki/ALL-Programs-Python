L1 = []
count=0
n = int(input("Enter number of elements:"))
for i in range(0,n):
    a = int(input("Enter a number:"))
    L1.append(a)
    if (a%2==0):
         count=count + 1
print(L1)
print(count)
