import cv2
# Leer la imágen con cv2 = computer vision
img = cv2.imread('perrobonito.jpg')
# determinar el tipo de imágen numpy.ndarray
print(type(img))
# mostrar pixeles (426, 718, 3)
print(img.shape)
# mostrar imagen en ventana barra de titulo 
cv2.imshow('perrito 0025', img)
## tiempo de espera
cv2.waitKey(0)
# destruir todas las ventanas
cv2.destroyAllWindows()