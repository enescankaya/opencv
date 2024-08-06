"""
1. numerical types
1:int
2:float
3:complex
"""

x=10
y=1.1
z=10+3j
print("x: {} y:{} z:{}".format(x,y,z))

#2. strings
first_message = "Hello World"
print(first_message)
print(first_message[6])#6. indexi yazdırır
print(first_message[2:7])#2. den 7 ye kadar yazdırır
print(first_message[2:])#den sonrası
print(first_message[:4])#başan 4 e kadar
print(first_message + " enes")

#print(first_message+ x ) => error
print(first_message + str(x))#solution

#3. Lists
first_list=["enes","ali",10,0.3,"5"]
print(first_list)
print(first_list[0:3])

#Tuple
first_tuple=("enes","ali",10,0.3,"5")
print(first_tuple)
print(first_tuple[:2])
print(first_tuple[1:3])

#Dictionary
first_dict={"name":"enes","surname":"çankaya","age":23}
print(first_dict)
print(first_dict["name"])#enes
print(first_dict[   "surname"])
print(first_dict.keys())
print(first_dict.values())

#boolean
a=True
b=False
c=None
print(a)
print(b)
print(c)
print(type(c))