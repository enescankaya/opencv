import cv2,numpy as np
img = cv2.imread("starwars.jpg")
blurry_img=cv2.medianBlur(img,9)
laplacian= cv2.Laplacian(blurry_img,cv2.CV_64F).var()
print(laplacian)
if laplacian <500:
    print("it is a blurry image")
cv2.imshow("image",img)
cv2.imshow("blurry",blurry_img)
cv2.waitKey(0)
cv2.destroyAllWindows()