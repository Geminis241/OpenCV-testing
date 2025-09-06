import cv2

# Cargar imagen desde archivo
imagen = cv2.imread("foto.jpg")  # Cambie "foto.jpg" por el nombre de su imagen

# Verificar si se cargó bien
if imagen is None:
    print("Error: no se pudo cargar la imagen.")
    exit()

# Convertir a escala de grises
gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

# Detectar bordes con Canny
bordes = cv2.Canny(gris, 100, 200)

# Mostrar resultados
cv2.imshow("Imagen Original", imagen)
cv2.imshow("Escala de Grises", gris)
cv2.imshow("Bordes", bordes)

# Esperar hasta que se presione una tecla
cv2.waitKey(0)
cv2.destroyAllWindows()
