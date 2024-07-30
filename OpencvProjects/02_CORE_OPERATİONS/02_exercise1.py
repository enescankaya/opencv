import cv2
import numpy as np
import matplotlib.pyplot as plt
path="TEST_IMAGES\leaf.jpg"
img=cv2.imread(path)
#print(img)
corner=img[0:100,0:100]#0 ile 100 arasındaki bölgeleri cornera attık. ilk değer y_değeri ikinci değeri ise x_ değeri start ile end oluyorher ikisi de.
img[0:100,0:250]=(255,0,0)#belirlenen bölgedeki pixellerin değerini değitirdik.
cv2.imshow("Forest",img)
cv2.imshow("Corner",corner)
cv2.waitKey(0)
cv2.destroyAllWindows()