import os
import subprocess
import git
import torch

print("PyTorch version:", torch.__version__)
print("CUDA available:", torch.cuda.is_available())
print("CUDA version:", torch.version.cuda)
print("Successful import of git:", git.__version__)


# Configura tus rutas y parámetros aquí
yolov5_repo_path = 'yolov5'  # Asegúrate de que esta sea la ruta al repositorio de YOLOv5
data_yaml_path = 'dataset/data.yaml'  # Ruta relativa al archivo YAML desde la carpeta yolov5
img_size = 640
batch_size = 8
epochs = 10
name = 'SolarFailuresDetection'


# Cambia al directorio de YOLOv5
os.chdir(yolov5_repo_path)


# Construye el comando para entrenar el modelo
train_command = [
    'python', 'train.py',
    '--img', str(img_size),
    '--batch', str(batch_size),
    '--epochs', str(epochs),
    '--data', os.path.join('..', data_yaml_path),
    '--name', name,
    '--weights', '../oldModels/best_08_06.pt'  # Usa pesos preentrenados; ajusta según necesidad
]

# Ejecuta el entrenamiento
print(f"Iniciando el entrenamiento de YOLOv5 para {name}...")
subprocess.run(train_command)

# Vuelve al directorio original
os.chdir('..')
print("Entrenamiento completado.")
