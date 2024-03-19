import os
import subprocess

# Configura tus rutas y parámetros aquí
yolov5_repo_path = 'yolov5'  # Asegúrate de que esta sea la ruta al repositorio de YOLOv5
data_yaml_path = '../dataset/data.yaml'  # Asegúrate de que esta sea la ruta a tu archivo YAML
img_size = 640
batch_size = 8
epochs = 10
name = 'SolarFailuresDetection'

# Cambia al directorio de YOLOv5
os.chdir(yolov5_repo_path)

# Comando para entrenar YOLOv5 sin pesos preentrenados
train_command = [
    'python', 'train.py',
    '--batch', str(batch_size),
    '--cfg', 'models/yolov5s.yaml',  # Ajusta según la configuración deseada
    '--epochs', str(epochs),
    '--data', data_yaml_path,
    '--weights', '',  # Deja esta cadena vacía para entrenar desde cero
    '--img', str(img_size),
    '--name', name,
    '--cache'  # Opcional: activa el caché de imágenes para entrenamientos más rápidos
]

# Ejecutar el comando de entrenamiento y capturar la salida
result = subprocess.run(train_command)

# Verificar y manejar errores si los hay
if result.returncode != 0:
    print("Error en el entrenamiento:", result.stderr)
else:
    print("Entrenamiento completado exitosamente. Salida:", result.stdout)
