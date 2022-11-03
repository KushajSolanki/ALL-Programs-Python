a = int(input("Enter side A of triangle:"))
b = int(input("Enter side B of triangle:"))
c = int(input("Enter side C of triangle:"))
s=(a+b+c)/2
a=(s*(s-a)*(s-b)*(s-c))**0.5
print("Area of Triangle is : ",a)