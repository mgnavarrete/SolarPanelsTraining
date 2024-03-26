import os
import shutil

def move_and_rename_files(src_directory, dst_directory):
    class_folders = range(0, 9)  # Clases del 1 al 8
    phases = ['train', 'val', 'test']
    types = ['images', 'labels']

    for class_folder in class_folders:
        for phase in phases:
            for file_type in types:
                # Ruta de origen, por ejemplo: H:\SolarPanelsTraining\datasets\dataset\classes\1\train\image
                src_path = os.path.join(src_directory, str(class_folder), phase, file_type)
                
                # Ruta de destino, por ejemplo: H:\datasets\train\images
                dst_path = os.path.join(dst_directory, phase, file_type)  
                if not os.path.exists(dst_path):
                    os.makedirs(dst_path)
                
                file_counter = dict()  # Para llevar la cuenta de los archivos y evitar conflictos de nombres
                
                for filename in os.listdir(src_path):
                    if file_type not in file_counter:
                        file_counter[file_type] = 0
                    else:
                        file_counter[file_type] += 1
                    
                    # Genera un nuevo nombre de archivo para evitar conflictos, incluyendo el tipo y la clase
                    new_filename = f"{file_type}_{class_folder}_{file_counter[file_type]}_{filename}"
                    src_file_path = os.path.join(src_path, filename)
                    dst_file_path = os.path.join(dst_path, new_filename)
                    
                    # Mueve el archivo al destino con el nuevo nombre
                    shutil.move(src_file_path, dst_file_path)

# Define las rutas de origen y destino
src_directory = "H:\\SolarPanelsTraining\\datasets\\dataset\\classes"
dst_directory = "H:\\datasets"

# Llama a la función para iniciar el proceso
move_and_rename_files(src_directory, dst_directory)
