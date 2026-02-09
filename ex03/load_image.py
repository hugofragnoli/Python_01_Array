from PIL import Image
from numpy import array
import matplotlib.pyplot as plt
import numpy as np
from load_image import ft_load
import os

# Pil = biblio de ref pour ouvrir images en python
# os = pour verif si fichier bien la avant douvrir
# numpy car image est un array de nombres 3d pour rgb.

def ft_load(path: str) -> array:
    try:
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
