from fontTools.misc.iterTools import batched
from ultralytics import YOLO

# Cargamos el modelo YOLO especificando el archivo del modelo preentrenado.
model = YOLO("yolo11l.pt")


def main():
    model.train(
        data='Dataset/SplitData/DataOffline.yaml',
        epochs=5,
        imgsz=640,
        batch=8,
        workers=8,
        patience=5,
    )


if __name__ == '__main__':
    main()
