name = "enes"
print("name: ",name)
age =23
print("MY NAME IS " ,name , ".","I am", age, " Years old.")
print("mete" , " han")
print("mete" + " han")
print("my name \n" , "is enes")#\n new line

x1=25
y1=50
z1=75
print(x1,y1,z1)# 25 50 75
print(x1,y1,z1,sep="-")#25-50-75
#output formatting
print("My name is {}. i am {} years old" .format(name,age))
#output formatting 1
print("my name is {0}. i am {1} years old".format(name,age))
print("my name is {1}. i am {0} years old".format(name,age))#name=0 age = 1 oluyor yani istediğimiz sırayla koyabiliriz.