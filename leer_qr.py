import cv2
img = cv2.imread('terceradosis.png')
dtector = cv2.QRCodeDetector()
dato, vertices, mapa = dtector.detectAndDecode(img)
print(dato)


