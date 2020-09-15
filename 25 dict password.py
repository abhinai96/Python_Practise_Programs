a=int(input("enter password"))
passw=12345
if a==passw:
        print("correct password")
        print("please enter the name,age,bday")
d={"name":"abhinai","age":24,"bday":"april"}
for i in d:
        e=input("enter required name")
        if i==e:
                print(d.get(i))
"""d={"name":1,"age":23}
for i in d:
        print(i)"""
