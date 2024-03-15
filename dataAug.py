import os
import tensorflow as tf
from tkinter import filedialog
import numpy as np

def select_directories():
    list_folders = []  
    path_root = filedialog.askdirectory(title='Seleccione el directorio raíz')
    while path_root:
        list_folders.append(path_root)
        path_root = filedialog.askdirectory(title='Seleccione otro directorio o cancele para continuar')
    if not list_folders:
        raise Exception("No se seleccionó ningún directorio")
    return list_folders

def adjust_label_for_rotation(label_line, image_width, image_height):
    parts = label_line.split()
    class_id, x_center, y_center, width, height = parts
    x_center, y_center, width, height = map(float, [x_center, y_center, width, height])

    # Assuming 90-degree rotation
    new_x_center = y_center
    new_y_center = 1 - x_center
    new_width = height
    new_height = width
    
    return f"{class_id} {new_x_center:.6f} {new_y_center:.6f} {new_width:.6f} {new_height:.6f}\n"

def adjust_label_for_flip(label_line, flip_type, image_width, image_height):
    parts = label_line.split()
    class_id = parts[0]
    x_center = float(parts[1])
    y_center = float(parts[2])
    width = float(parts[3])
    height = float(parts[4])

    if flip_type == 'horizontal':
        x_center = 1 - x_center
    elif flip_type == 'vertical':
        y_center = 1 - y_center

    return f"{class_id} {x_center:.6f} {y_center:.6f} {width:.6f} {height:.6f}\n"

def apply_augmentations(image, original_labels, num_augmentations, image_idx, images_path, labels_path, file_name):
    augmented_images_info = []

    # Convert image to float32 for augmentation
    image_float = tf.image.convert_image_dtype(image, tf.float32)

    # Define augmentations here
    augmentations = [
        ('horizontal_flip', lambda img: tf.image.flip_left_right(img)),
        ('vertical_flip', lambda img: tf.image.flip_up_down(img)),
        ('rotate', lambda img: tf.image.rot90(img)),
        ('brightness', lambda img: tf.image.random_brightness(img, max_delta=0.3)),
        ('contrast', lambda img: tf.image.random_contrast(img, lower=0.8, upper=1.2)),
        ('saturation', lambda img: tf.image.random_saturation(img, lower=0.8, upper=1.2)),
        ('hue', lambda img: tf.image.random_hue(img, max_delta=0.04)),
        ('noise', lambda img: tf.clip_by_value(img + tf.random.normal(tf.shape(img), mean=0.0, stddev=0.05), 0.0, 1.0)),
        ('zoom', lambda img: tf.image.resize(tf.image.central_crop(img, central_fraction=0.8), tf.shape(img)[:2]))
    ]

    for i, (aug_name, aug_func) in enumerate(augmentations):
        # Apply augmentation
        aug_image = aug_func(image_float if aug_name != 'rotate' else image)

        # Convert back to uint8
        if aug_name != 'rotate':
            aug_image = tf.image.convert_image_dtype(aug_image, tf.uint8)

        # Adjust labels for spatial transformations
        if aug_name in ['horizontal_flip', 'vertical_flip', 'rotate']:
            if aug_name == 'horizontal_flip':
                adjusted_labels = [adjust_label_for_flip(label, 'horizontal', tf.shape(image)[1], tf.shape(image)[0]) for label in original_labels]
            elif aug_name == 'vertical_flip':
                adjusted_labels = [adjust_label_for_flip(label, 'vertical', tf.shape(image)[1], tf.shape(image)[0]) for label in original_labels]
            elif aug_name == 'rotate':
                adjusted_labels = [adjust_label_for_rotation(label, tf.shape(image)[1], tf.shape(image)[0]) for label in original_labels]
        else:
            adjusted_labels = original_labels

        augmented_image_path = os.path.join(images_path, f"{file_name}_aug_{image_idx}_{i}.JPG")
        augmented_label_path = os.path.join(labels_path, f"{file_name}_aug_{image_idx}_{i}.txt")

        # Save augmented image and label
        tf.io.write_file(augmented_image_path, tf.image.encode_jpeg(aug_image))
        with open(augmented_label_path, "w") as label_file:
            label_file.writelines(adjusted_labels)

        augmented_images_info.append((augmented_image_path, augmented_label_path))

        if len(augmented_images_info) >= num_augmentations:
            break

    return augmented_images_info

list_classes = select_directories()

num_augmentations_required = 5000
augmentations_per_image = num_augmentations_required // (len(list_classes) * len(os.listdir(list_classes[0] + "/images")))

for clase in list_classes:
    labelsPATH = os.path.join(clase, "labels")
    imagesPATH = os.path.join(clase, "images")
    filesNames = [os.path.splitext(image)[0] for image in os.listdir(imagesPATH) if image.lower().endswith('.jpg')]

    for image_idx, file_name in enumerate(filesNames):
        imagePath = os.path.join(imagesPATH, f"{file_name}.JPG")
        labelPath = os.path.join(labelsPATH, f"{file_name}.txt")

        image = tf.io.read_file(imagePath)
        image = tf.image.decode_jpeg(image, channels=3)

        with open(labelPath, "r") as file:
            original_labels = file.readlines()

        apply_augmentations(image, original_labels, augmentations_per_image * len(filesNames), image_idx, imagesPATH, labelsPATH, file_name)
