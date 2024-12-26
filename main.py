import math
import time

import cv2
import cvzone
from ultralytics import YOLO

# Nivel mínimo de confianza para considerar una detección válida.
confidence = 0.6

# Inicialización de la cámara.
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

# Cargar el modelo YOLO con el archivo entrenado.
model = YOLO("models/n_version_8_2.pt")

# Nombres de las clases que el modelo puede detectar.
classNames = ["fake", "real"]

# Variables para calcular FPS.
prev_frame_time = 0
new_frame_time = 0

while True:
    new_frame_time = time.time()
    success, img = cap.read()

    # Realizar detecciones en el frame utilizando el modelo YOLO.
    results = model(img, stream=True, verbose=False)

    for r in results:
        boxes = r.boxes

        for box in boxes:
            # Obtener las coordenadas de la caja delimitadora.
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

            # Calcular el ancho y alto de la caja delimitadora.
            w, h = x2 - x1, y2 - y1

            # Obtener el nivel de confianza de la detección.
            conf = math.ceil((box.conf[0] * 100)) / 100

            # Obtener la clase detectada.
            cls = int(box.cls[0])

            # Validar si la detección cumple con el nivel mínimo de confianza.
            if conf > confidence:
                if classNames[cls] == 'real':
                    color = (0, 255, 0)  # Verde para "real".
                else:
                    color = (0, 0, 255)  # Rojo para "fake".

                # Dibujar una caja con esquinas redondeadas y mostrar el texto de la clase.
                cvzone.cornerRect(img, (x1, y1, w, h), colorC=color, colorR=color)
                cvzone.putTextRect(img, f'{classNames[cls].upper()} {int(conf * 100)}%',
                                   (max(0, x1), max(35, y1)), scale=2, thickness=4, colorR=color,
                                   colorB=color)

    # Calcular FPS: inverso del tiempo entre frames.
    fps = 1 / (new_frame_time - prev_frame_time)
    prev_frame_time = new_frame_time
    print(fps)

    cv2.imshow("Image", img)
    cv2.waitKey(1)
