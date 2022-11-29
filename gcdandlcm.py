a = int(input("Enter a number a:"))
b = int(input("Enter a number b:"))
#program for gcd
if(a<b):
    s = a
else:
    s = b
for i in range(1,s+1):
    if (a%i==0 and b%i==0):
        gcd = i
print("GCD is :",gcd)
#program for lcm
lcm = a*b/gcd
print("LCM is: ",lcm)
