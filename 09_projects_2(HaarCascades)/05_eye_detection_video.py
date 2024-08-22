import cv2

# Yüz ve göz tespit sınıflarını yükleme
face_cascade = cv2.CascadeClassifier("D:\\opencv\\OpencvProjects\\haarCascades\\frontalface.xml")
eye_cascade = cv2.CascadeClassifier("D:\\opencv\\OpencvProjects\\haarCascades\\haarcascade_eye.xml")

# Video dosyasını açma
vid = cv2.VideoCapture("eyes.mp4")
#vid = cv2.VideoCapture(0)#for video frame

while True:
    ret, frame = vid.read()
    
    # Eğer video bitti ise döngüyü kır
    if not ret:
        break
    
    #frame = cv2.resize(frame, (480, 540))
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Yüz tespiti
    faces = face_cascade.detectMultiScale(gray, 1.1, 7)
    
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
        
        # Sadece yüz bölgesinde göz tespiti
        roi_frame = frame[y:y+h, x:x+w]
        roi_gray = gray[y:y+h, x:x+w]
        
        eyes = eye_cascade.detectMultiScale(roi_gray,1.1,6)
        for (ex, ey, ew, eh) in eyes:
            cv2.circle(roi_frame, (int(ex + ew/2), int(ey + eh/2)), int(ew/2), (255, 0, 0), 1)
    
    cv2.imshow("frame", frame)
    
    # Çıkmak için ESC tuşuna bas
    if cv2.waitKey(20) == 27:
        break

# Kaynakları serbest bırak
vid.release()
cv2.destroyAllWindows()
