from PIL import Image
from numpy import array
import matplotlib.pyplot as plt
import numpy as np
import os

# Pil = biblio de ref pour ouvrir images en python
# os = pour verif si fichier bien la avant douvrir
# numpy car image est un array de nombres 3d pour rgb.
# matplotlib biblio de dessin Python. Transforme des données
# numériques en une fenetre visuelle avec axes gradés

def ft_load(path: str) -> array:
    try:
        path = "animal.jpeg"
        if not os.path.exists(path):
            raise FileNotFoundError(f"No such file or directory: {path}")
        _, extension = os.path.splitext(path)
        if extension.lower() not in [".jpg", ".jpeg"]:
            raise ValueError("Unsupported File format. use JPG or JPEG")
        img = Image.open(path)
        img_array = np.array(img)

        print(f"The shape of image is: {img_array.shape}")

        return img_array

    except Exception as e:
        print(f"Error: {e}")
        return None

def display_image_info(path: str):
    img_array = ft_load(path)

    if img_array is not None:
        print(img_array)