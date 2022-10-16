x=int(input("enter your age"))
y=int(input("enter your age"))
z=int(input("enter your age"))
if x>y and z<x:
    print("x is youngest")
elif y>z and x<y:
    print("y is  oldest")
elif z>x and y<z:
    print("z is oldest")
