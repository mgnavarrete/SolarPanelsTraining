import os
import subprocess
import git
print("Successful import of git:", git.__version__)


# Configura tus rutas y parámetros aquí
yolov5_repo_path = 'yolov5'  # Asegúrate de que esta sea la ruta al repositorio de YOLOv5
data_yaml_path = 'dataset/data.yaml'  # Ruta relativa al archivo YAML desde la carpeta yolov5
img_size = 640
batch_size = 8
epochs = 10
name = 'SolarFailuresDetection'

# Verifica si el repositorio de YOLOv5 ya está clonado; de lo contrario, clónalo
if not os.path.exists(yolov5_repo_path):
    print("Clonando el repositorio YOLOv5...")
    subprocess.run(['git', 'clone', 'https://github.com/ultralytics/yolov5.git'])
    print("Repositorio YOLOv5 clonado correctamente.")

# Cambia al directorio de YOLOv5
os.chdir(yolov5_repo_path)

# Instala las dependencias de YOLOv5
print("Instalando dependencias requeridas para YOLOv5...")
subprocess.run(['pip', 'install', '-r', 'requirements.txt'])

# Construye el comando para entrenar el modelo
train_command = [
    'python', 'train.py',
    '--img', str(img_size),
    '--batch', str(batch_size),
    '--epochs', str(epochs),
    '--data', os.path.join('..', data_yaml_path),
    '--name', name,
    '--weights', 'yolov5s.pt'  # Usa pesos preentrenados; ajusta según necesidad
]

# Ejecuta el entrenamiento
print(f"Iniciando el entrenamiento de YOLOv5 para {name}...")
subprocess.run(train_command)

# Vuelve al directorio original
os.chdir('..')
print("Entrenamiento completado.")
