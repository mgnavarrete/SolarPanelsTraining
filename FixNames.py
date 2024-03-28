import os

def renombrar_archivos(directorio_dataset):
    # Recorre las carpetas principales: train, test, y val.
    for carpeta in ['train', 'test', 'val']:
        path_carpeta = os.path.join(directorio_dataset, carpeta)

        # Define las rutas para las subcarpetas 'images' y 'labels'.
        path_images = os.path.join(path_carpeta, 'images')
        path_labels = os.path.join(path_carpeta, 'labels')

        # Procesa las imágenes, eliminando el prefijo 'images_'.
        for nombre_archivo in os.listdir(path_images):
            if nombre_archivo.startswith('images_'):
                nuevo_nombre = nombre_archivo.replace('images_', '')
                os.rename(os.path.join(path_images, nombre_archivo),
                          os.path.join(path_images, nuevo_nombre))
        
        # Procesa los labels, eliminando el prefijo 'labels_'.
        for nombre_archivo in os.listdir(path_labels):
            if nombre_archivo.startswith('labels_'):
                nuevo_nombre = nombre_archivo.replace('labels_', '')
                os.rename(os.path.join(path_labels, nombre_archivo),
                          os.path.join(path_labels, nuevo_nombre))

# Ejemplo de uso
directorio_dataset = '/ruta/a/tu/carpeta/de/dataset'
renombrar_archivos(directorio_dataset)
