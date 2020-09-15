#ABBACBA
#A3 B3 C1
a="abbacba"
"""b=a.count("a")
print(b)"""

l=[]
for i in a:
        if i not in l:
                l.append(i)
print(l)

for i in sorted(l):
        print("{} occurs {}times".format(i,a.count(i)))

        
