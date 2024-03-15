import os
import tensorflow as tf
from tkinter import filedialog
import numpy as np
import random

def select_directories():
    list_folders = []  
    path_root = filedialog.askdirectory(title='Seleccione el directorio raíz')
    while path_root:
        list_folders.append(path_root)
        path_root = filedialog.askdirectory(title='Seleccione otro directorio o cancele para continuar')
    if not list_folders:
        raise Exception("No se seleccionó ningún directorio")
    return list_folders

def adjust_label_for_flip(label_line, flip_type):
    parts = label_line.split()
    class_id, x_center, y_center, width, height = parts
    x_center, y_center = map(float, [x_center, y_center])

    if flip_type == 'horizontal':
        x_center = 1 - x_center
    elif flip_type == 'vertical':
        y_center = 1 - y_center

    return f"{class_id} {x_center:.6f} {y_center:.6f} {width} {height}\n"

def adjust_label_for_rotation(label_line, image_shape):
    parts = label_line.split()
    class_id, x_center, y_center, width, height = parts
    x_center, y_center = map(float, [x_center, y_center])

    new_x_center = y_center
    new_y_center = 1 - x_center

    return f"{class_id} {new_x_center:.6f} {new_y_center:.6f} {height} {width}\n"

def apply_random_augmentations(image, image_float, num_augmentations, image_idx, file_name, images_path, labels_path, original_labels):
    augmented_images_info = []

    augmentations = {
        'horizontal_flip': ('spatial', lambda img: tf.image.flip_left_right(img)),
        'vertical_flip': ('spatial', lambda img: tf.image.flip_up_down(img)),
        'rotate': ('spatial', lambda img: tf.image.rot90(img)),
        'brightness': ('non-spatial', lambda img: tf.image.random_brightness(img, max_delta=0.3)),
        'contrast': ('non-spatial', lambda img: tf.image.random_contrast(img, lower=0.8, upper=1.2)),
        'saturation': ('non-spatial', lambda img: tf.image.random_saturation(img, lower=0.8, upper=1.2)),
        'hue': ('non-spatial', lambda img: tf.image.random_hue(img, max_delta=0.04)),
        'noise': ('non-spatial', lambda img: tf.clip_by_value(img + tf.random.normal(tf.shape(img), mean=0.0, stddev=0.05), 0.0, 1.0)),
        'zoom': ('non-spatial', lambda img: tf.image.resize(tf.image.central_crop(img, central_fraction=0.8), tf.shape(img)[:2]))
    }

    for i in range(num_augmentations):
        selected_augmentations = random.sample(list(augmentations.keys()), k=random.randint(1, len(augmentations)))
        current_image = image_float
        adjusted_labels = original_labels.copy()

        for aug in selected_augmentations:
            aug_type, aug_func = augmentations[aug]
            current_image = aug_func(current_image)

            if aug_type == 'spatial':
                if aug == 'horizontal_flip':
                    adjusted_labels = [adjust_label_for_flip(label, 'horizontal') for label in adjusted_labels]
                elif aug == 'vertical_flip':
                    adjusted_labels = [adjust_label_for_flip(label, 'vertical') for label in adjusted_labels]
                elif aug == 'rotate':
                    adjusted_labels = [adjust_label_for_rotation(label, tf.shape(current_image)) for label in adjusted_labels]

        if 'noise' in selected_augmentations or any(aug in ['brightness', 'contrast', 'saturation', 'hue'] for aug in selected_augmentations):
            current_image = tf.image.convert_image_dtype(current_image, tf.uint8)

        augmented_image_path = os.path.join(images_path, f"{file_name}_aug_{image_idx}_{i}.JPG")
        tf.io.write_file(augmented_image_path, tf.image.encode_jpeg(current_image))

        augmented_label_path = os.path.join(labels_path, f"{file_name}_aug_{image_idx}_{i}.txt")
        with open(augmented_label_path, "w") as label_file:
            label_file.writelines(adjusted_labels)

        augmented_images_info.append((augmented_image_path, augmented_label_path))

    return augmented_images_info

list_classes = select_directories()

num_augmentations_required = 5000
num_original_images = sum([len(os.listdir(os.path.join(clase, "images"))) for clase in list_classes])
augmentations_per_image = (num_augmentations_required - num_original_images) // num_original_images

for clase in list_classes:
    labelsPATH = os.path.join(clase, "labels")
    imagesPATH = os.path.join(clase, "images")
    filesNames = [os.path.splitext(image)[0] for image in os.listdir(imagesPATH) if image.lower().endswith('.jpg')]

    for image_idx, file_name in enumerate(filesNames):
        imagePath = os.path.join(imagesPATH, f"{file_name}.JPG")
        labelPath = os.path.join(labelsPATH, f"{file_name}.txt")

        image = tf.io.read_file(imagePath)
        image = tf.image.decode_jpeg(image, channels=3)
        image_float = tf.image.convert_image_dtype(image, tf.float32)

        with open(labelPath, "r") as file:
            original_labels = file.readlines()

        apply_random_augmentations(image, image_float, augmentations_per_image, image_idx, file_name, imagesPATH, labelsPATH, original_labels)
