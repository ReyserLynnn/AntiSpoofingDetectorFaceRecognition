# AntiSpoofingDetectorFaceRecognition

Este proyecto tiene como objetivo detectar si una cara es real o falsa usando un modelo entrenado con YOLO. Aquí se detallan los pasos para clonar, configurar e inicializar el repositorio en tu máquina.

## Clonar el repositorio

Para comenzar, debes clonar el repositorio en tu máquina local:

git clone https://github.com/ReyserLynnn/AntiSpoofingDetectorFaceRecognition.git
cd AntiSpoofingDetectorFaceRecognition

## Requisitos

Este proyecto requiere un entorno virtual en Python. Asegúrate de tener **Python 3.6+** instalado en tu sistema.

1. **Crear y activar el entorno virtual**:

   - **En Linux**:
     python3 -m venv venv
     source venv/bin/activate

   - **En Windows**:
     python -m venv venv
     .\venv\Scripts\activate

2. **Instalar dependencias**:

   Asegúrate de tener el archivo `requirements.txt` en el directorio raíz del repositorio. Instala todas las dependencias necesarias con el siguiente comando:

   pip install -r requirements.txt

## Estructura de Carpetas

Este proyecto utiliza una estructura específica de carpetas para organizar los datos y los resultados del entrenamiento. Debes crear las siguientes carpetas para asegurar que el proyecto funcione correctamente.

### **En Linux**

Puedes usar el siguiente comando para crear las carpetas necesarias:

mkdir -p Dataset/{all,DataCollect,Fake,Real,SplitData/{test/{images,labels},train/{images,labels},val/{images,labels}}}

### **En Windows**

Si estás trabajando en Windows, puedes crear las carpetas manualmente o usar el siguiente script de PowerShell para crear la estructura de carpetas:

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

## Uso

1. **Entrenamiento del modelo**:
   Después de configurar las carpetas y descargar el conjunto de datos, puedes comenzar a entrenar el modelo ejecutando el siguiente script:

   python train.py

2. **Ejecutar detección**:
   Para realizar predicciones utilizando el modelo entrenado, ejecuta:

   python main.py

## Contribuciones

Si deseas contribuir a este proyecto, por favor realiza un *fork* del repositorio y envía un *pull request*.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.