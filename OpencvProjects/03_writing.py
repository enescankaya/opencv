import numpy as np
import cv2
canvas=np.zeros((512,512,3),dtype=np.uint8)+255
font1=cv2.FONT_HERSHEY_SIMPLEX
font2=cv2.FONT_HERSHEY_COMPLEX
font3=cv2.FONT_HERSHEY_SCRIPT_COMPLEX
cv2.putText(canvas,"OpenCv",(20,100),font2,4,(0,0,0),cv2.LINE_AA)
cv2.imshow("CANVAS",canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()