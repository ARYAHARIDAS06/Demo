x={
    "name":"arya",
    "class":"mca",
    "roll no":"23"}
print(x)
print(type(x))
a=x["class"]
print(a)
for a in x:
    print(a)
for a in x:
    print(x[a])
for a,b in x.items():
    print(a,b)
for a in x.values():
    print(a)
x["age"]="20"
print(x)
for a,b in x.items():
    print(a,b)
x.pop("class")
print(x)
