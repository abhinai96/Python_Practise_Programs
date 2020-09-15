#aaaabbcc
#abc
a="aaaabbcc"
"""output=" "
for i in a:
        if i not in output:
                output=output+i
print(output)"""
b=set(a)
print(b)
c=" ".join(b)
print((c))
