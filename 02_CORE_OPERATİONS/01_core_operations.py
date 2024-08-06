import cv2 
import numpy as np
path="TEST_IMAGES\opencv_logo.png"
img = cv2.imread(path)
#print(img) controlling existing of image
px=img[0,0]#0,0 kordinatlarındaki pixel değerleri
"""print(px)"""
(b,g,r)=img[50,30]
print("(0,0)-Red: {},Green: {},Blue: {}".format(r,g,b))
"""
BGR/RGB(RED,GREEN,BLUE)
R:0-255
G:0-255
B:0-255
0-0-0: SİYAH
255-255-255: BEYAZ
"""
#Accessing pixel's Value-1
blue=img[100,100,0]#ilk ikisi 100,100 kordinatı üçüncüsü ise o kordinatın 0. değerini yani mavilik değerini yansıtır.
green=img[100,100,1]#1:green
red=img[100,100,2]#2:Red

#PİXEL DEĞERLERİNİ BLUE-GREEN-RED ŞEKLİNDE SIRALAMAYLA DÖNDÜRÜR: BGR
print("Before: ",img[100,100])
img[100,100]=[100,100,100]#bu şekilde değiştirebiliriz
print("After: ",img[100,100])#pixel değerlerini değiştirebiliriz bu şekilde

#Accessing pixel's Value-2
print("Before: ",img.item(10,10,2))#2. yani red değerini bu şekilde de alabiliriz
img[10,10,2]=100#veya bu şekilde de değiştirebiliriz.: 10,10 kordinatındaki 2. değeri yani red değerini 100 yapar.
print("After: ",img.item(10,10,2))