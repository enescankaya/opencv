import numpy as np
import cv2
canvas = np.zeros((1024,1024,3),dtype=np.uint8) + 255 #önce siyah tuval oluşturduk, daha sonra bu tuvala 255 eklersek 0 siyah olduğu için beyaza dönüşecek
#print(canvas) #bu kısımda oluşturduğumuz tuvalin matrix halini yazdırıyoruz
cv2.line(canvas,(0,0),(512,512),(255,0,0),thickness=5)
#renk seçiminde hangi renge 255 verip diğerlerine 0 verirsen 255 verdiğin renk değerini elde edersin
cv2.line(canvas,(256,256),(400,100),(0,0,200),3)#bu da başka bir çizgi
cv2.rectangle(canvas,(10,100),(50,300),(0,255,0),-1)#thicness değerini -1 verirsen içi dolu olur
cv2.circle(canvas,(512,512),100,(255,0,0))
p1=(700,800)
p2=(900,1000)
p3=(600,500)
cv2.line(canvas,p1,p2,(0,0,0),4)
cv2.line(canvas,p2,p3,(0,0,0),4)
cv2.line(canvas,p1,p3,(0,0,0),4)#üçgen için 3 line ihtiyacımız var.
points=np.array([[[110,200],[330,200],[100,100],[220,250]]],np.int32)
cv2.polylines(canvas,[points],True,(255,0,0),5)#çokgen çizimi için kullanırız true demek kapalı olsun her tarafı demek false girersek bir kenarı açık kalır 
cv2.ellipse(canvas,(512,512),(100,50),0,0,360,(0,0,255),-1)
cv2.imshow("canvas",canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()