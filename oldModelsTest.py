import os
import subprocess

def test_yolo_model(base_dir, model_path, selected_classes):
    # Filtrar solo los directorios de clases seleccionados
    class_dirs = [d for d in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, d)) and d in selected_classes]

    # Archivo para almacenar los resultados generales
    with open(os.path.join(base_dir, 'test_results.txt'), 'w') as result_file:
        for class_dir in class_dirs:
            test_images_dir = os.path.join(base_dir, class_dir, 'test', 'images')
            
            # Crear un archivo que liste todas las imágenes de prueba
            test_images_list = os.path.join(test_images_dir, 'test_images.txt')
            with open(test_images_list, 'w') as f:
                for image in os.listdir(test_images_dir):
                    if image.endswith(('.png', '.jpg', '.jpeg')):
                        f.write(os.path.join(test_images_dir, image) + '\n')

            # Ejecutar la evaluación de YOLOv5
            command = f"python val.py --weights {model_path} --data {test_images_list} --img 640 --iou 0.65 --half --task test"
            process = subprocess.run(command, shell=True, capture_output=True, text=True)

            # Almacenar los resultados
            result_file.write(f"Results for class {class_dir}:\n")
            result_file.write(process.stdout)
            result_file.write('\n')

# Ejemplo de uso
base_dir = 'dataset/classes'  # Ruta al directorio base donde se almacenan las clases
model_path = 'best.pt'  # Ruta al modelo YOLO
selected_classes = ['0', '1', '2', '3', '4', '5', '7', '8']
test_yolo_model(base_dir, model_path, selected_classes)
