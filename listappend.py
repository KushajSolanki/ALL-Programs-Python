L1 = []
L2 = []
n = int(input("Enter number of elements:"))
for i in range(0,n):
    a = int(input("Enter a number:"))
    L1.append(a)
    if (a%2==0):
         L2.append(a)
print(L1)
print(L2)
