n = int(input("Enter number of rows:"))
print("Pyramid pattern:-")
for i in range(0,n):
    for j in range(n-i-1):
        print(end=" ")
    for k in range(0,i+1):
        print("*",end=" ")
    print()
