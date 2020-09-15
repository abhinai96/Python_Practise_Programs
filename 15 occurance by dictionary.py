#find the occurance of char in string without using count method
"""d={}
d["a"]=100
d["b"]=200
d["a"]=300
print(d)
b=d.get("a")
c=d.get("k",0)#default value
print(c)"""

"""d={}
d["a"]=1
d["b"]=2
d["a"]=d.get("a",0)+1
print(d)"""

"""d={"c":100,"a":200,"b":300}
for k,v in sorted(d.items()):
        print(k,v)"""

c="abbacba"
d={}
for i in c:
        d[i]=d.get(i,0)+1
for k,v in d.items():
        print("{} occurs {}times".format(k,v))



