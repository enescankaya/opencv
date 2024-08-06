#siyah=0
# beyaz =1
#bitwise yaptığı şey aslında her bir frame i tek tek logical oparationlarla karşılaştırır ve bize bir result döndürür. and yaparsak her frame için 0 and 1 operation yapar ve
#bize 1 döndürür 
import cv2,numpy as np
img1=cv2.imread("bitwise_1.png")
img2=cv2.imread("bitwise_2.png")
bit_and=cv2.bitwise_and(img1,img2)
bit_or=cv2.bitwise_or(img1,img2)
bit_xor=cv2.bitwise_xor(img1,img2)
bit_not=cv2.bitwise_not(img1)
bit_not2=cv2.bitwise_not(img2)

cv2.imshow("img1",img1)
cv2.imshow("img2",img2)
cv2.imshow("bit_and",bit_and)
cv2.imshow("bit_or",bit_or)
cv2.imshow("xor",bit_xor)
cv2.imshow("img1 not",bit_not)
cv2.imshow("img2 not",bit_not2)
cv2.waitKey(0)
cv2.destroyAllWindows()
