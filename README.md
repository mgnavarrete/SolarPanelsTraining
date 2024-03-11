# Solar Panels Training

## Organización del conjunto de datos::

- En la carpeta principal llamada dataset, estan las carpetas train, val, y test, que corresponden a los conjuntos de entrenamiento, validación y prueba, respectivamente. En cada una de las subcarpetas (train, val, test), existen dos carpetas más images y labels.

    - La carpeta images debe contener las imágenes para el entrenamiento, la validación o las pruebas, según corresponda.
    - La carpeta labels debe contener los archivos .txt de anotaciones correspondientes a cada imagen, manteniendo los mismos nombres de archivos que las imágenes, pero con la extensión .txt y debe tener el siguiente formato,

Directorio de dataset

```python
# Directorio de dataset
dataset/
├── train/
│   ├── images/
│   │   ├── imagen1.jpg
│   │   ├── imagen2.jpg
│   │   └── ...
│   └── labels/
│       ├── imagen1.txt
│       ├── imagen2.txt
│       └── ...
├── val/
│   ├── images/
│   │   ├── imagen3.jpg
│   │   ├── imagen4.jpg
│   │   └── ...
│   └── labels/
│       ├── imagen3.txt
│       ├── imagen4.txt
│       └── ...
└── test/
    ├── images/
    │   ├── imagen5.jpg
    │   ├── imagen6.jpg
    │   └── ...
    └── labels/
        ├── imagen5.txt
        ├── imagen6.txt
        └── ...
```
Formato de labels:
``` python
# <clase> <x_centro> <y_centro> <ancho> <alto>
3 0.544531 0.161133 0.110937 0.0292969
5 0.523444 0 0.233444 0.123112
```

## Instalar los paquetes necesarios:

Instala el paquete ultralytics, que proporciona la API de Python para YOLO, facilitando la interacción con el modelo YOLOv8. Esto se puede hacer usando pip: 

```
pip install ultralytics​​.
```

## Entrenar el modelo:
- Para entrenar el modelo se corre el archivo `main.py`, este archivo debe contener los siguiente:
```python
from ultralytics import YOLO

# Inicializar el modelo.
model = YOLO('yolov8n.pt')

# Entrenar el modelo.
results = model.train(
   data='dataset/data.yaml',
   imgsz=640,
   epochs=10,
   batch=8,
   name='yolov8n_custom'
)
```
- Las variables de las funciones significan:

    - data: Este parámetro debe apuntar a un archivo YAML que describe tu conjunto de datos. Este archivo YAML debe contener rutas a tus imágenes de entrenamiento y validación, así como las clases que tu modelo necesita predecir. Por ejemplo, custom_data.yaml podría contener rutas a las carpetas train y val, y una lista de las clases.

    - imgsz: Este parámetro define el tamaño de la imagen con la que el modelo será entrenado. YOLOv8 redimensionará todas las imágenes a este tamaño cuadrado. Un valor común es 640, pero puedes aumentarlo si tu hardware lo permite, lo que podría mejorar la precisión pero también requerirá más memoria.

    - epochs: Define el número total de pasadas sobre el conjunto de datos completo durante el entrenamiento. Un "epoch" representa una iteración sobre todas las imágenes de entrenamiento. Un número mayor de épocas puede mejorar la precisión del modelo hasta cierto punto, pero también aumentará el tiempo de entrenamiento.

    - batch: Este parámetro define el número de imágenes que se procesarán en un grupo (batch) antes de que el modelo actualice sus parámetros internos. Un tamaño de lote más grande proporcionará estimaciones del gradiente más estables, pero también requerirá más memoria. Si tienes limitaciones de memoria, podrías necesitar disminuir el tamaño del lote.

    - name: Es una cadena de texto que se utilizará para nombrar el directorio de resultados donde se guardarán los outputs del entrenamiento, como los pesos del modelo y los gráficos de rendimiento. Esto te permite organizar y diferenciar entre diferentes entrenamientos.