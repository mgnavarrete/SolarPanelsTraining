import os

# Lista de nombres de las carpetas
carpetas = ['0', '1', '2', '3', '4', '5', '6', '7', '8']

# Crear la carpeta 'classes' en cada carpeta
for carpeta in carpetas:
    ruta_carpeta = os.path.join('classes', carpeta)
    os.makedirs(ruta_carpeta, exist_ok=True)
    
    # Crear las carpetas 'label' y 'images' dentro de 'classes'
    ruta_label = os.path.join(ruta_carpeta, 'labels')
    os.makedirs(ruta_label, exist_ok=True)
    
    ruta_images = os.path.join(ruta_carpeta, 'images')
    os.makedirs(ruta_images, exist_ok=True)