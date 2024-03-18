import os

# Ruta base donde se encuentran las carpetas de clases
base_path = 'dataset/classes/'

# Iterar sobre cada carpeta de clase en el directorio base
for class_folder in os.listdir(base_path):
    # Construir la ruta de la carpeta de etiquetas dentro de la carpeta de clase
    labels_path = os.path.join(base_path, class_folder, 'labels')
    
    # Verificar si la ruta de etiquetas existe y es un directorio
    if os.path.isdir(labels_path):
        # Iterar sobre cada archivo de etiqueta en la carpeta de etiquetas
        for label_file in os.listdir(labels_path):
            # Construir la ruta completa al archivo de etiqueta
            file_path = os.path.join(labels_path, label_file)
            
            # Verificar si el archivo actual es un archivo de texto
            if os.path.isfile(file_path) and label_file.endswith('.txt'):
                # Leer el contenido del archivo de etiqueta
                with open(file_path, 'r') as file:
                    content = file.readlines()
                
                # Reemplazar la clase incorrecta por la clase correcta (nombre de la carpeta de clase)
                with open(file_path, 'w') as file:
                    for line in content:
                        parts = line.split()
                        # Cambiar la clase (primer elemento) por el número de la carpeta de clase
                        parts[0] = class_folder
                        # Escribir la línea corregida de vuelta al archivo
                        file.write(' '.join(parts) + '\n')
