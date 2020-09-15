#a4k3b2
#aeknbd
a="a4k3b2"
output=" "

for i in a:
        if i.isalpha():
                output=output+i
                x=i
        else:
                d=int(i)
                new=chr(ord(x)+d)
                output=output+new
print(output)
        
        
