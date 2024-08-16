import cv2
import numpy as np
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    blur = cv2.GaussianBlur(hsv, (5, 5), 1)
    # Adaptive Threshold kullanarak daha esnek bir eşikleme yapıyoruz
    _,thresh = cv2.threshold(blur,120, 250,cv2.THRESH_BINARY)
    lower_hsv = np.array([0, 120, 0], dtype=np.uint8)   # Alt sınır
    upper_hsv = np.array([250, 155, 255], dtype=np.uint8)
    mask = cv2.inRange(blur,lower_hsv,upper_hsv)
    # Morfolojik işlemler ile küçük noktaları temizleme
    kernel = np.ones((5, 5), np.uint8)
    #mask = cv2.morphologyEx(mask, cv2.MORPH_ERODE, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_DILATE, kernel)
    # Konturları bulma
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    if contours:
        # En büyük konturu bul
        max_contour = max(contours, key=cv2.contourArea)
        hull =[]
        hull.append(cv2.convexHull(max_contour,returnPoints=True))
        # En büyük konturun alanı yeterince büyükse, çiz
        #if cv2.contourArea(max_contour) > 100000:
        #cv2.drawContours(frame, [max_contour], -1, (0, 0, 255), 3,cv2.LINE_4,hierarchy)
        cv2.drawContours(frame,hull,-1,(0,255,0),2,cv2.LINE_AA,hierarchy)
    cv2.imshow("mask", mask)
    cv2.imshow("Frame", frame)
    if cv2.waitKey(2) & 0xFF == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()