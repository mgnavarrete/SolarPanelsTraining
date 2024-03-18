# Asegúrate de que este script se ejecute en el entorno donde YOLOv7 está clonado y configurado.

import os
import subprocess

# Configura tus rutas y parámetros aquí
yolov7_repo_path = 'yolov7'  # Actualiza esto con la ruta al repositorio de YOLOv7
data_yaml_path = 'dataset/data.yaml'  # Actualiza esto con la ruta a tu archivo YAML
weights_path = 'yolov7.pt'  # O cualquier otro archivo de pesos inicial que quieras usar
img_size = 640
batch_size = 8
epochs = 10
name = 'SolarFailuresDetection'

# Cambia al directorio de YOLOv7
os.chdir(yolov7_repo_path)

# Comando para entrenar YOLOv7
train_command = [
    'python', 'train.py',
    '--batch', str(batch_size),
    '--cfg', 'cfg/training/yolov7.yaml',  # Asegúrate de que este archivo exista y esté configurado correctamente
    '--epochs', str(epochs),
    '--data', data_yaml_path,
    '--weights', weights_path,
    '--img', str(img_size),
    '--name', name
]

# Ejecutar el comando de entrenamiento
result = subprocess.run(train_command, capture_output=True, text=True)

# Imprimir la salida del comando de entrenamiento
print(result.stdout)

# Verificar y manejar errores si los hay
if result.returncode != 0:
    print("Error en el entrenamiento:")
    print(result.stderr)
