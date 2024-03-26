import os
import shutil
from pathlib import Path

# Define la ruta base donde están almacenadas las clases
base_path = Path("dataset/classes")

# Itera sobre cada directorio de clase en la ruta base
for class_dir in base_path.iterdir():
    if class_dir.is_dir():
        # Obtiene las rutas de las imágenes y las etiquetas
        images_dir = class_dir / "train/images"
        labels_dir = class_dir / "train/labels"
        
        # Lista todos los archivos de imagen y etiqueta, asumiendo que comparten el mismo nombre base
        image_files = sorted(images_dir.iterdir())
        label_files = sorted(labels_dir.iterdir())

        # Mantén solo las primeras 10,000 imágenes y etiquetas
        for image_file, label_file in zip(image_files[10000:], label_files[10000:]):
            os.remove(image_file)
            os.remove(label_file)

print("El proceso ha finalizado. Se han mantenido hasta 10,000 imágenes y etiquetas en cada clase.")
