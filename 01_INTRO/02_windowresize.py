import cv2
cv2.namedWindow("Klon",cv2.WINDOW_NORMAL)
img =cv2.imread("Klon.jpg")
img=cv2.resize(img,(640,640))#özel olarak boyutlandırabiliyorum, ama resme uygun mu bilmiyorum sonraki ugulamada o var!
cv2.imshow("Klon",img)
cv2.waitKey(0)
cv2.destroyAllWindows()