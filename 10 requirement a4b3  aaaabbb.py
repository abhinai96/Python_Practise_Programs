#a4b3c2
#aaaabbbcc
a="a4b3c2"
output=" "
for i in a:
        if i.isalpha():
                c=i
        else:
              output=output+c*int(i)
print(output)
