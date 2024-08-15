import cv2,numpy as np
img_filter=cv2.imread("filter.png")
img_median=cv2.imread("median.png")
img_bilateral=cv2.imread("bilateral.png")
blur=cv2.blur(img_filter,(11,11))#pozitif tek sayı sadece görseli blurlaştırıyoruz
blur2=cv2.GaussianBlur(img_filter,(5,5),cv2.BORDER_DEFAULT) # farklı blırlama şekli
median_blur=cv2.medianBlur(img_median,7)
gaussianblur_median=cv2.GaussianBlur(img_median,(7,7),cv2.BORDER_DEFAULT)
bilateral_median=cv2.bilateralFilter(img_bilateral,9,95,95)#blurlaştırma seviyesidir 9,95,95 değerleri bunları artırırsak blurlama artar
cv2.imshow("original filter",img_filter)
cv2.imshow("blur_filter",blur)
cv2.imshow("blur2_filter",blur2)
cv2.imshow("original median",img_median)
cv2.imshow("blur_median",median_blur)
cv2.imshow("gaussian blur",gaussianblur_median)
cv2.imshow("original bilateral",img_bilateral)
cv2.imshow("bilateral_median",bilateral_median)#median hali daha düzgün çı kıy or görüntü noise dan dolayı
cv2.waitKey(0) 
cv2.destroyAllWindows()