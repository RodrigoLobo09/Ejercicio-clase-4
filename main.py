import numpy as np
import cv2 as cv

#-----------------------Cargar Imagen desde Archivo
#Leer imagen, el path es el de la carpeta del proyecto
image=cv.imread(“imagen.png”,cv.IMREAD_GRAYSCALE)
#Escribir imagen, el path es la carpeta del proyecto
cv.imwrite(“imagen.jpg", image)
#Mostrar ventana con imagen
cv.imshow("Original",image)
#Para mantener abierta la ventana hasta que se presione una tecla
cv.waitKey(0)

#------------------------Tomar fotografia de camara web

#Leer imagen, el path es el de la carpeta del proyecto
image=cv.imread(“imagen.png”,cv.IMREAD_GRAYSCALE)
#Escribir imagen, el path es la carpeta del proyecto
cv.imwrite(“imagen.jpg", image)
#Mostrar ventana con imagen
cv.imshow("Original",image)
#Para mantener abierta la ventana hasta que se presione una tecla
cv.waitKey(0)


#----------------------------Captura de Video

cap = cv.VideoCapture(0)
# Define the codec and create VideoWriter object
fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter('output.avi', fourcc, 20.0, (640, 480))
while cap.isOpened():
 ret, frame = cap.read()
 if not ret:
    print("Can't receive frame (stream end?). Exiting ...")
    break
 frame = cv.flip(frame, 180)
 # write the flipped frame
 out.write(frame)
 cv.imshow('frame', frame)
 if cv.waitKey(1) == ord('q'):
    break
# Release everything if job is finished
cap.release()
out.release()
cv.destroyAllWindows()

#--------------------------------Dibujo de líneas
import numpy as np #Importar los paquetes a emplear
import cv
#imagen de 300x300 a 3 canales, rojo, verde y azul
#uint8 entero sin signo 8 bits [0 a 255]
lienzo = np.zeros((300,300, 3), dtype = "uint8")
verde=(0,255,0)
cv.line(lienzo,(0,0),(300,300), verde)
cv.imshow("Lienzo",lienzo)
cv.waitKey(0)

#-----------------------------------Dibujo de rectángulos
cv.rectangle(lienzo,(10,10),(60,60),verde,3)
cv.imshow("Lienzo",lienzo)
cv.waitKey(0)
cv.rectangle(lienzo,(50,200),(200,225),rojo,5)
cv.imshow("Lienzo",lienzo)
cv.waitKey(0)

#--------------------------------------Dibujo de círculos
lienzo = np.zeros((300,300, 3), dtype = "uint8")
(CentroX,CentroY)=(lienzo.shape[1]//2,
lienzo.shape[0]//2)
blanco = (255,255,255)
for r in range (0, 175, 25):
cv.circle(lienzo,(CentroX,CentroY),r,blanco)
cv.imshow("Lienzo",lienzo)
cv.waitKey(0)