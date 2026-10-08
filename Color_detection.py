import cv2
from util import get_limits


red = [255, 0, 0 ] # Rosso in RGB
#WEBCAM
webcam = cv2.VideoCapture(0) #Leggo la webcam del computer 0(camera principale), 1(secondaria), 2(terziaria), etc...
# Creo un ciclo while che continua finché la variabile è vera, nella webcam non c'è bisogno di una variabile booleana perché la webcam 
# è sempre attiva finché non la chiudo
while True:
    true, frame = webcam.read() # Leggo i frame dalla webcam
    HsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lowerLimit, upperLimit = get_limits(red)
    mask = cv2.inRange(HsvImage, lowerLimit, upperLimit)  
    cv2.imshow('Webcam', frame) # Creo una finestra di nome Webcam e faccio vedere i frame
    if cv2.waitKey(1) & 0XFF == ord('q'):
        break # Se premo il tasto 'q', esco dal ciclo while
webcam.release() # Rilascio la webcam dalla memoria
cv2.destroyAllWindows() # Chiudo tutte le finestre