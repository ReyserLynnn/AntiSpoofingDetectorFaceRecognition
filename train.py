from ultralytics import YOLO

# Cargamos el modelo YOLO especificando el archivo del modelo preentrenado.
model = YOLO("yolo11n.pt")


def main():
    # Inicia el proceso de entrenamiento del modelo YOLO.
    model.train(
        data='Dataset/SplitData/DataOffline.yaml',  # Ruta al archivo de configuración del conjunto de datos.
        epochs=2,  # Número de épocas para entrenar el modelo.
        imgsz=640,  # Tamaño de las imágenes de entrada para el entrenamiento.
        patience=12
    )


if __name__ == '__main__':
    main()
