import os
import shutil
from tqdm import tqdm
labelsPATH = "dataset/allData/labels"
imagesPATH = "dataset/allData/images"

labels = os.listdir(labelsPATH)

for label in tqdm(labels, desc="Dividiendo Imagenes"):
    filename = label.split(".")[0]
    
    with open(labelsPATH + "/" + label, "r") as file:
        lines = file.readlines()
        for line in lines:
            class_id = int(line.split()[0])
            # guardar linea en archivo correspondiente junto con la imagen
            with open("dataset/classes/" + str(class_id) + "/labels/" + filename + ".txt", "a") as newfile:
                newfile.write(line)
            shutil.copy(imagesPATH + "/" + filename + ".JPG", "dataset/classes/" + str(class_id) + "/images/" + filename + ".jpg")    
        file.close()