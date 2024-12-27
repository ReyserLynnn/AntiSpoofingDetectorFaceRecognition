import os
import random
import shutil
from itertools import islice

# Directorios de entrada y salida
outputFolderPath = "Dataset/SplitData"  # Carpeta donde se guardarán los datos divididos
inputFolderPath = "Dataset/all"  # Carpeta con las imágenes originales

# Proporción para dividir los datos en entrenamiento, validación y prueba. Clases validas
splitRatio = {"train": 0.7, "val": 0.2, "test": 0.1}
classes = ["fake", "real"]

# Eliminar la carpeta de salida si existe y crearla de nuevo
try:
    shutil.rmtree(outputFolderPath)
except OSError as e:
    os.mkdir(outputFolderPath)

# Crear las subcarpetas necesarias para el split de datos (train, val, test)
os.makedirs(f"{outputFolderPath}/train/images", exist_ok=True)
os.makedirs(f"{outputFolderPath}/train/labels", exist_ok=True)
os.makedirs(f"{outputFolderPath}/val/images", exist_ok=True)
os.makedirs(f"{outputFolderPath}/val/labels", exist_ok=True)
os.makedirs(f"{outputFolderPath}/test/images", exist_ok=True)
os.makedirs(f"{outputFolderPath}/test/labels", exist_ok=True)

# Obtener los nombres de las imágenes en la carpeta de entrada
listNames = os.listdir(inputFolderPath)

# Extraer los nombres de archivo sin extensión
uniqueNames = [name.split(".")[0] for name in listNames]
uniqueNames = list(set(uniqueNames))  # Eliminar nombres duplicados

# Barajar los nombres para aleatorizar la división
random.shuffle(uniqueNames)

# Calcular la cantidad de imágenes para cada conjunto (train, val, test)
lenData = len(uniqueNames)
lenTrain = int(lenData * splitRatio["train"])
lenVal = int(lenData * splitRatio["val"])
lenTest = int(lenData * splitRatio["test"])

# Ajustar el número de imágenes de entrenamiento si la suma no coincide
if lenData != lenTrain + lenVal + lenTest:
    remainingData = lenData - (lenTrain + lenVal + lenTest)
    lenTrain += remainingData

# Dividir los nombres en listas para cada conjunto
lengthToSplit = [lenTrain, lenVal, lenTest]
Input = iter(uniqueNames)
Output = [list(islice(Input, elem)) for elem in lengthToSplit]

# Imprimir la cantidad de imágenes por conjunto
print(f"Total Images: {lenData} \nSplit:{len(Output[0])} {len(Output[1])} {len(Output[2])}")

# Copiar las imágenes y etiquetas a las subcarpetas correspondientes
sequence = ['train', 'val', 'test']

for i, out in enumerate(Output):
    for filename in out:
        shutil.copy(f"{inputFolderPath}/{filename}.jpg", f"{outputFolderPath}/{sequence[i]}/images/{filename}.jpg")
        shutil.copy(f"{inputFolderPath}/{filename}.txt", f"{outputFolderPath}/{sequence[i]}/labels/{filename}.txt")

print("Split Process Completed...")

# Crear el archivo DataOffline.yaml con la configuración del dataset
absolute_path = os.path.abspath(outputFolderPath)

dataYaml = (f'path: {absolute_path}\n\
train: train/images\n\
val: val/images\n\
test: test/images\n\
\n\
nc: {len(classes)} \n\
names: {classes}\n\
')

# Guardar el archivo YAML
f = open(f"{outputFolderPath}/DataOffline.yaml", "a")
f.write(dataYaml)
f.close()

print("DataOffline.yaml file Created...")
