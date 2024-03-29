import cv2                                                                                                                                                                                                     
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

def detect_faces(frame):
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
    
    return frame

if __name__ == "__main__":
    
    cap = cv2.VideoCapture(0)

    while True:
        
        ret, frame = cap.read()
        if not ret:
            break
        
        
        frame_with_faces = detect_faces(frame)
        
       
        cv2.imshow('Live Face Detection', frame_with_faces)
        
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    
    cap.release()
    cv2.destroyAllWindows() 