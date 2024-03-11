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