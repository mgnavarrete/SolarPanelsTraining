import subprocess
import os

# Configura las rutas y parámetros necesarios
yolov5_repo_path = 'yolov5'  # Asegúrate de ajustar esta ruta al directorio de YOLOv5
weights_path = '../oldModels/best_202309_20epoch.pt'  # Ruta al archivo de pesos del modelo.
data_yaml_path = '../dataset/data.yaml'  # Ruta al archivo YAML de configuración de los datos.
img_size = 640  # Tamaño de imagen utilizado durante el entrenamiento.
iou_threshold = 0.5  # Umbral de IoU para considerar predicciones correctas.
conf_threshold = 0.001  # Umbral de confianza para considerar detecciones.
results_name = 'test_results'  # Nombre del directorio de resultados.

# Cambia al directorio de YOLOv5
os.chdir(yolov5_repo_path)

# Comando para ejecutar la evaluación
command = [
    'python', 'val.py',  # En YOLOv5 se utiliza val.py para la evaluación
    '--weights', weights_path,
    '--data', data_yaml_path,
    '--task', 'test',  # Asegúrate de que 'test' está definido en data.yaml
    '--img', str(img_size),
    '--iou-thres', str(iou_threshold),
    '--conf-thres', str(conf_threshold),
    '--name', results_name,
    '--exist-ok'  # Permite la sobreescritura de los resultados antiguos
]

# Ejecutar el comando
subprocess.run(command)
