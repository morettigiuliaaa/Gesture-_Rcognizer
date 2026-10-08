import cv2
import os

#IMMAGINI
image_path = os.path.join('.', 'foto', 'foto.jpg') # Indico il percorso della foto
img = cv2.imread(image_path)# Leggo l'immagine dal percorso indicato
cv2.imwrite(os.path.join('.', 'foto', 'foto_out.jpg'), img) # Riscrivo l'immagine nello stesso percorso ma con un nome diverso
cv2.imshow('Immagine', img) # Creo una finestra con il titolo 'Immagine' e mostro l'immagine
cv2.waitKey(0) # Resto con l'immagine aperta finché non premo un tasto
cv2.waitKey(2000) # Resto con l'immagine aperta per 2 secondi
cv2.destroyAllWindows() # Chiudo tutte le finestre
print(img, img.shape) # Stampo le dimensioni dell'immagine e le informazioni dei canali BGR
new_img = cv2.resize(img, (500, 500)) # Ridimensiono l'immagine
cv2.imwrite(os.path.join('.', 'foto', 'foto_out_resized.jpg'), new_img) # Riscrivo l'immagine nello stesso percorso ma con un nome diverso
cv2.imshow('Immagine', new_img) # Creo una finestra con il titolo 'Immagine' e mostro l'immagine
cv2.waitKey(0) # Resto con l'immagine aperta finché non premo un tasto
cv2.waitKey(2000) # Resto con l'immagine aperta per 2 secondi
cv2.destroyAllWindows() # Chiudo tutte le finestre

#VIDEO
video_path = os.path.join('.', 'video', 'video.mp4') # Indico il percorso del video
video = cv2.VideoCapture(video_path) # Leggo il video dal percorso indicato
variabile = True # Creo una variabile booleana per il ciclo while
while variabile: # Creo un ciclo while che continua finché la variabile è vera
    variabile, frame = video.read() # Leggo il frame del video e aggiorno la variabile booleana, se non c'è frame è False
    if variabile: # Se la variabile è vera, mostro il frame
        cv2.imshow('Video', frame) # Creo una finestra con il titolo 'Video' e mostro il frame
        if cv2.waitKey(25) & 0xFF == ord('q'): # Se premo il tasto 'q', esco dal ciclo while
            break
video.release() #Rilascio il video dalla memoria
cv2.destroyAllWindows() #Chiudo tutte le finestre

#WEBCAM
webcam = cv2.VideoCapture(0) #Leggo la webcam del computer 0(camera principale), 1(secondaria), 2(terziaria), etc...
# Creo un ciclo while che continua finché la variabile è vera, nella webcam non c'è bisogno di una variabile booleana perché la webcam 
# è sempre attiva finché non la chiudo
while True:
    true, frame = webcam.read() # Leggo i frame dalla webcam
    cv2.imshow('Webcam', frame) # Creo una finestra di nome Webcam e faccio vedere i frame
    if cv2.waitKey(40) & 0XFF == ord('q'):
        break # Se premo il tasto 'q', esco dal ciclo while

webcam.release() # Rilascio la webcam dalla memoria
cv2.destroyAllWindows() # Chiudo tutte le finestre