# AntiSpoofingDetectorFaceRecognition

Este proyecto tiene como objetivo detectar si una cara es real o falsa usando un modelo entrenado con YOLO. El sistema utiliza la cámara en tiempo real para clasificar las caras como 'real' o 'fake' basándose en un modelo entrenado. A continuación se detallan los pasos para clonar, configurar e inicializar el repositorio en tu máquina.

## Clonar el repositorio

Para comenzar, debes clonar el repositorio en tu máquina local:

```bash
git clone https://github.com/ReyserLynnn/AntiSpoofingDetectorFaceRecognition.git
cd AntiSpoofingDetectorFaceRecognition
```

## Requisitos

Este proyecto requiere Python 3.10 o superior y las siguientes bibliotecas de Python:

- `cvzone`
- `ultralytics`
- `mediapipe`
- Otros paquetes listados en el archivo `requirements.txt`.

Asegúrate de tener **Python 3.10+** instalado en tu sistema y las herramientas necesarias para ejecutar comandos en la terminal (Windows PowerShell, Bash o similar). Además, debes tener **Git** instalado para clonar el repositorio.

## Instalación de Dependencias
1. **Crear y activar el entorno virtual**:

   - **En Linux**:

     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

   - **En Windows**:

     ```bash
     python3 -m venv venv
     .\venv\Scripts\activate
     ```

2. **Instalar dependencias**:

   Instala todas las librerías necesarias, incluyendo `cvzone`, `ultralytics` y `mediapipe`:

   ```bash
   pip install -r requirements.txt
   pip install cvzone ultralytics mediapipe
   ```

## Estructura de Carpetas

Este proyecto utiliza una estructura específica de carpetas para organizar los datos y los resultados del entrenamiento. Debes crear las siguientes carpetas para asegurar que el proyecto funcione correctamente.

### **En Linux**

Puedes usar el siguiente comando para crear las carpetas necesarias:

```bash
mkdir -p Dataset/{all,DataCollect,Fake,Real,SplitData/{test/{images,labels},train/{images,labels},val/{images,labels}}}
```

### **En Windows**

Si estás trabajando en Windows, puedes crear las carpetas manualmente o usar el siguiente script de PowerShell:

```ps1
New-Item -Path "Dataset\all" -ItemType Directory
New-Item -Path "Dataset\DataCollect" -ItemType Directory
New-Item -Path "Dataset\Fake" -ItemType Directory
New-Item -Path "Dataset\Real" -ItemType Directory
New-Item -Path "Dataset\SplitData\test\images" -ItemType Directory
New-Item -Path "Dataset\SplitData\test\labels" -ItemType Directory
New-Item -Path "Dataset\SplitData\train\images" -ItemType Directory
New-Item -Path "Dataset\SplitData\train\labels" -ItemType Directory
New-Item -Path "Dataset\SplitData\val\images" -ItemType Directory
New-Item -Path "Dataset\SplitData\val\labels" -ItemType Directory
```

## Uso
1. **Ejecutar detección**:
   Para realizar predicciones utilizando el modelo entrenado, ejecuta:

   ```bash
   python main.py
   ```

## Contribuciones

Si deseas contribuir a este proyecto, por favor realiza un *fork* del repositorio y envía un *pull request*.

## Notas Adicionales

- Se recomienda usar un IDE como PyCharm o Visual Studio Code. Asegúrate de seleccionar el intérprete de Python configurado en el entorno virtual creado previamente.
- Para más detalles y problemas durante la instalación, revisa la documentación oficial del proyecto en el repositorio de GitHub:  
  [Repositorio Oficial en GitHub](https://github.com/ReyserLynnn/AntiSpoofingDetectorFaceRecognition/blob/main/Readme.md)