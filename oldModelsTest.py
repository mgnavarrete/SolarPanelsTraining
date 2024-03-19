import subprocess

# Configura las rutas y parámetros necesarios
yolov7_repo_path = 'yolov7' 
weights_path = 'best.pt'  # Ruta al archivo de pesos del modelo.
data_yaml_path = '../dataset/data.yaml'  # Ruta al archivo YAML de configuración de los datos.
img_size = 640  # Tamaño de imagen utilizado durante el entrenamiento.
iou_threshold = 0.5  # Umbral de IoU para considerar predicciones correctas.
conf_threshold = 0.001  # Umbral de confianza para considerar detecciones.
results_name = 'test_results'  # Nombre del directorio de resultados.



os.chdir(yolov7_repo_path)

# Comando para ejecutar la evaluación
command = [
    'python', 'val.py',
    '--weights', weights_path,
    '--data', data_yaml_path,
    '--task', 'test',
    '--img', str(img_size),
    '--iou-thres', str(iou_threshold),
    '--conf-thres', str(conf_threshold),
    '--name', results_name
]

# Ejecutar el comando
subprocess.run(command)
