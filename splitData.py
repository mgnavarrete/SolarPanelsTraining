import os
import shutil
from sklearn.model_selection import train_test_split

def split_data(base_dir, train_size=0.7, val_size=0.15, test_size=0.15):
    class_dirs = [d for d in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, d))]

    for class_dir in class_dirs:
        # Paths for images and labels
        images_dir = os.path.join(base_dir, class_dir, 'images')
        labels_dir = os.path.join(base_dir, class_dir, 'labels')
        
        # Getting all filenames
        images = os.listdir(images_dir)
        labels = os.listdir(labels_dir)

        # Splitting data
        train_images, test_images, train_labels, test_labels = train_test_split(images, labels, train_size=train_size + val_size, test_size=test_size, random_state=42)
        val_images, train_images, val_labels, train_labels = train_test_split(train_images, train_labels, train_size=(train_size / (train_size + val_size)), test_size=(val_size / (train_size + val_size)), random_state=42)
        
        # Function to move files
        def move_files(files, source_dir, destination_dir):
            for f in files:
                shutil.move(os.path.join(source_dir, f), os.path.join(destination_dir, f))

        # Creating subdirectories and moving files
        for phase in ['train', 'val', 'test']:
            os.makedirs(os.path.join(base_dir, class_dir, phase, 'images'), exist_ok=True)
            os.makedirs(os.path.join(base_dir, class_dir, phase, 'labels'), exist_ok=True)
        
        move_files(train_images, images_dir, os.path.join(base_dir, class_dir, 'train', 'images'))
        move_files(val_images, images_dir, os.path.join(base_dir, class_dir, 'val', 'images'))
        move_files(test_images, images_dir, os.path.join(base_dir, class_dir, 'test', 'images'))
        move_files(train_labels, labels_dir, os.path.join(base_dir, class_dir, 'train', 'labels'))
        move_files(val_labels, labels_dir, os.path.join(base_dir, class_dir, 'val', 'labels'))
        move_files(test_labels, labels_dir, os.path.join(base_dir, class_dir, 'test', 'labels'))

base_dir = 'classes'  # Path to the base directory
split_data(base_dir)
