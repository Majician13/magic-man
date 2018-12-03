a=[12,3,5,8,90,11,44,66,8,9,34,56]
b=[12,3,3,3,3,3,3,3,3,3,3,3,3,3]
c=[]
for item in a:
    if item in b:
        if item not in c:
            c.append(item)

print (c)


        