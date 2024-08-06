"""
1. int()
2. float()
3. complex()
    """
    
"""a=1
print(type(a))#int

complex_a=complex(a)
print(complex_a)"""

"""
1. range()
2.len()
3. random()
-pi
-e
"""
print(range(6))
for i in range(7):
    print(i)#range(sayı) demek 0 dan o sayıya kadar aralık demek
for i in range(2,6):
    print(i) #2 ile 6 arasındaki sayıları yazdırır. 2 ve 6 dahil değil
for i in range(3,30,5):# 3 ile 30 arası 5 er artmak demektir
    print(i)
for i in range(50,30,-6):#50 den 30 kadar 6 azalır
    print(i)
    
print("(.....................................)")
programming_languages=["python","java","c++","c#"]
for i in range(len(programming_languages)):#range kullanarak büyüklüğünü bilmediğim bir listeyi rahatlıkla yazdırıp sonuna kadar check edebiliyorum.
    print(programming_languages[i])
print("(.....................................)")
print("(.....................................)")
print("(.....................................)")

import random
print(random.random())#float döndürür kesirli
print(random.randint(1,100))
print(abs(-5))#mutlak değerini alır
from math import pi,e
print(pi)
print(e)