num=[7,8,9,5]
it=iter(num)
print(type(it))
print(it.__next__())
print(it.__next__())
print(it.__next__())
for i in num:
        print(i)
