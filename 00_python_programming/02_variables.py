#integer variable, int
x  = 5
print(x)
# type control
print(type(x))
print(type("x"))
#float variable,float
z=5.3
print(z)
print(type(z))
#type Casting
x=15
y="22"
z="tom"
x_to_string=str(x)
print(x_to_string)
print(type(x_to_string))
print(type(x))
y_to_int=int(y)
print(y_to_int)
print(type(y_to_int))
#z cant convert to int

# tips
x1=50
print(x1)
del x1# x1 silindi
#print(x1) hata alınır

x= 5 
y= 7
x, y =5,7#aynı şey
x,y,z,w,q,e=1,[2,3,4],"Antalya",4,5,6.3
print(x,y,z,w,q,e)
alll=x,y,z,w,q,e
print(alll)

#global local

def add(a,b):
    z_sum=a+b
    
#print(z_sum) you got error, z_sum is working only in the function of add
