import cvzone
from cvzone.FaceDetectionModule import FaceDetector
import cv2
from time import time

# -----------------------------S
# Configuracion general
# -----------------------------
classID = 0  # 0 es "fake", 1 es "real".
outputFolderPath = 'Dataset/DataCollect'
confidence = 0.8  # Umbral minimo de confianza para detecciones validas.
save = True  # Habilitar o deshabilitar el guardado de datos.
debug = False  # Mostrar informacion adicional para depuracion.
blurThreshold = 35  # Umbral para determinar si una imagen esta desenfocada (valores mayores son mas enfocados).

offsetPercentW = 10  # Porcentaje de desplazamiento horizontal en las detecciones.
offsetPercentH = 20  # Porcentaje de desplazamiento vertical en las detecciones.
camWidth, camHeight = 640, 480  # Resolucion de la camara.
floatingPoint = 6  # Cantidad de decimales para normalizar coordenadas.

# -----------------------------
# Inicializacion de la camara y el detector
# -----------------------------
cap = cv2.VideoCapture(0)
cap.set(3, camWidth)
cap.set(4, camHeight)

# Inicializacion del detector de rostros.
detector = FaceDetector(minDetectionCon=0.5, modelSelection=0)

# -----------------------------
# Bucle principal
# -----------------------------
while True:
    # Capturar un frame desde la camara.
    success, img = cap.read()
    imgOut = img.copy()

    # Detectar rostros en el frame.
    img, bboxs = detector.findFaces(img, draw=False)

    # Listas para almacenar informacion sobre desenfoque y etiquetas.
    listBlur = []
    listInfo = []

    if bboxs:
        # bboxInfo - "id","bbox","score","center"
        for bbox in bboxs:
            x, y, w, h = bbox['bbox']
            score = float(bbox['score'][0])  # Confianza de la deteccion.

            # Verificar si la confianza supera el umbral.
            if score > confidence:
                # Ajustar la caja con un desplazamiento porcentual.
                offsetW = (offsetPercentW / 100) * w
                x, w = int(x - offsetW), int(w + offsetW * 2)

                offsetH = (offsetPercentH / 100) * h
                y, h = int(y - offsetH * 3), int(h + offsetH * 3.5)

                # Evitar valores negativos en las coordenadas.
                x, y, w, h = max(x, 0), max(y, 0), max(w, 0), max(h, 0)

                # Calcular el desenfoque de la region detectada.
                imgFace = img[y:y + h, x:x + w]
                cv2.imshow('imgFace', imgFace)
                blurValue = int(cv2.Laplacian(imgFace, cv2.CV_64F).var())

                # Verificar si el desenfoque supera el umbral.
                if blurValue > blurThreshold:
                    listBlur.append(True)
                else:
                    listBlur.append(False)

                # Normalizar las coordenadas.
                ih, iw, _ = img.shape
                xc, yc = x + w / 2, y + h / 2
                xcn, ycn = round(xc / iw, floatingPoint), round(yc / ih, floatingPoint)
                wn, hn = round(w / iw, floatingPoint), round(h / ih, floatingPoint)
                # print(xcn, ycn, wn, hn)

                # Limitar los valores normalizados a 1.
                xcn, ycn, wn, hn = min(xcn, 1), min(ycn, 1), min(wn, 1), min(hn, 1)

                # Agregar informacion normalizada a la lista.
                listInfo.append(f"{classID} {xcn} {ycn} {wn} {hn}\n")

                # Dibujar la caja y mostrar la informacion en la imagen.
                cvzone.cornerRect(imgOut, (x, y, w, h), 25, 8, 3, (255, 0, 0))
                cvzone.putTextRect(imgOut, f'Score: {int(score * 100)}% Blur: {blurValue}', (x, y - 10), scale=1.5,
                                   thickness=2)

                if debug:
                    cvzone.cornerRect(img, (x, y, w, h), 25, 8, 3, (255, 0, 0))
                    cvzone.putTextRect(img, f'Score: {int(score * 100)}% Blur: {blurValue}', (x, y - 10), scale=1.5,
                                       thickness=2)

        # Guardar los datos si todas las detecciones son validas.
        if save:
            if all(listBlur) and listBlur != []:
                # Save image
                timeNow = str(time()).replace('.', '')
                cv2.imwrite(f"{outputFolderPath}/{timeNow}.jpg", img)

                # Save label text file
                for info in listInfo:
                    f = open(f"{outputFolderPath}/{timeNow}.txt", "a")
                    f.write(info)
                    f.close()

    cv2.imshow("Image", imgOut)
    cv2.waitKey(1)
