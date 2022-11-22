s1='nashik'
s2='123'
s3='number123'
s4='9673071580'
print(s1.islower())
print(s1.isupper())
print(s2.isnumeric())
print(s1.isalpha())
print(s3.isalnum())

if(s4.isnumeric() and len(s4)==10):
    print("Valid mobile number")
else:
    print("invalid")