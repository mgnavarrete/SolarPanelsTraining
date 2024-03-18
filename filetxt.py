import os

def generate_dataset_files(base_dir):
    train_files = []
    val_files = []
    test_files = []

    class_dirs = [d for d in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, d))]

    for class_dir in class_dirs:
        # Agregar las rutas de las imágenes de cada conjunto
        for subset in ['train', 'val', 'test']:
            subset_dir = os.path.join(base_dir, class_dir, subset, 'images')
            if os.path.exists(subset_dir):
                for filename in os.listdir(subset_dir):
                    if filename.endswith(('.jpg', '.jpeg', '.png')):
                        full_path = os.path.join(subset_dir, filename)
                        if subset == 'train':
                            train_files.append(full_path)
                        elif subset == 'val':
                            val_files.append(full_path)
                        elif subset == 'test':
                            test_files.append(full_path)

    # Crear archivos .txt con los rutas de las imágenes
    with open(os.path.join(base_dir, 'train.txt'), 'w') as f:
        for item in train_files:
            f.write("%s\n" % item)

    with open(os.path.join(base_dir, 'val.txt'), 'w') as f:
        for item in val_files:
            f.write("%s\n" % item)

    with open(os.path.join(base_dir, 'test.txt'), 'w') as f:
        for item in test_files:
            f.write("%s\n" % item)

# Ruta al directorio base donde se almacenan las clases
base_dir = 'classes'
generate_dataset_files(base_dir)
