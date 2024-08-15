import cv2
import numpy as np

cap = cv2.VideoCapture("line.mp4")

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (740, 740))

    if not ret:
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        continue
        
    # NumPy vektörel işlemlerini kullanarak işlemi hızlandır
    mean_values = np.mean(frame, axis=2)
    mask = mean_values > 127
    frame[mask] = [255, 255, 255]
    frame[~mask] = [0, 0, 0]
    cv2.imshow("frame", frame)

    if cv2.waitKey(20) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
