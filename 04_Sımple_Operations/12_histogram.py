import cv2,numpy as np 
from matplotlib import pyplot as plt

#img=np.zeros((500,500),np.uint8)+50 #siyah ekran 500-500 ölçüde
img=cv2.imread("smile.jpg")
#cv2.rectangle(img,(0,60),(200,150),(255,255,255),-1)
#cv2.rectangle(img,(250,170),(350,200),(255,255,255),-1)
b,g,r=cv2.split(img)#görüntünün b,g,r deüerlerini alıp histogram şeklinde grafiklendiriyoruz
cv2.imshow("img",img)
plt.hist(b.ravel(),256,[0,256])
plt.hist(g.ravel(),256,[0,256])
plt.hist(r.ravel(),256,[0,256])
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()