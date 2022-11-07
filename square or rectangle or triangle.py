x=int(input("enter your first side:"))
y=int(input("ener your second side:"))
z=int(input("enter your third side:"))
b=int(input("enter your fourth side:"))
if x==y and y==z and z==b:
    print("it is a square")
elif x==z and y==b:
    print("it is a rectangle")
elif  b==0:
    print("it is a triangle")
elif x!=y and y!=z and z!=b:
    print("it is a quadilateral")