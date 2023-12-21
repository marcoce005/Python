import cv2

# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Read the input image
img = cv2.imread('img/img4.jpg')

# Convert into grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces
#faces = face_cascade.detectMultiScale(gray, 1.1, 4)

# Configurazione che da facce che non esistono 
faces = face_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5,minSize=(30, 30))

# Configurazione che non rileva le facce inesistenti
faces = face_cascade.detectMultiScale(gray,scaleFactor=1.2,minNeighbors=5,minSize=(30, 30))

# Draw rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 5)

# Display the output
#cv2.imshow('img', img) per visuarizzarlo a schermo

cv2.imwrite('risultati/risultato.jpg', img)
cv2.waitKey()