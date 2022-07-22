import linecache
import json
f = open("bimba.rg  ","r")
x = linecache.getline("bimba.rg",1)
x= x.split()
p = x[0]
q = x[1]
my_dictionary = []

y = int(p)
z = int(q)
for i in range (2,y+1):
    a = linecache.getline("bimba.rg", i)
    a = a.split()
    b = linecache.getline("bimba.rg", i+z)
    b = b.split()

    my_dictionary.append({'node_no':a[0], 'node_value':a[1],'node_type':a[2],'p0':b[0],'p1':b[1]})
    print(my_dictionary[i-2])

j = json.dumps({'dictionaries':my_dictionary})
#j = json.dumps(my_dictionary)
with open ('My_dictionary.json','w') as f:
    f.write(j)
    f.close()