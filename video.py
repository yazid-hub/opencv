import cv2

# Ouvrir le fichier vidéo
video = cv2.VideoCapture("path/to/video.mp4")

# Boucle sur chaque frame de la vidéo
while True:
    # Lire le frame actuel
    ret, frame = video.read()
    
    # Si la lecture du frame a échoué, sortir de la boucle
    if not ret:
        break
    
    # Convertir en niveaux de gris
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Appliquer un seuil pour la détection de contours
    thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)[1]
    
    # Trouver les contours dans l'image
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Dessiner les contours sur l'image
    for c in contours:
        x, y, w, h = cv2.boundingRect(c)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
    # Afficher le résultat
    cv2.imshow("Video", frame)
    
    # Attendre pour continuer la lecture
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libérer les ressources
video.release()
cv2.destroyAllWindows()
