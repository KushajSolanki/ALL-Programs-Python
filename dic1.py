d1={"roll no.":20,"name":"Kushaj","age":18}
print(d1)
print(d1["name"])
d1.update({"city":"Nashik"})
print(d1)
d1["name"]="admin"
print(d1)
print(d1.get("name"))
d2=d1.copy()
print(d2)
print(len(d1))