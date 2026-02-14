from PIL import Image
from numpy import array
import numpy as np
import os

# Pil = biblio de ref pour ouvrir images en python
# os = pour verif si fichier bien la avant douvrir
# numpy car image est un array de nombres 3d pour rgb.
# matplotlib biblio de dessin Python. Transforme des données
# numériques en une fenetre visuelle avec axes gradés


def ft_load(path: str) -> array:
    """
    Charge une image à partir d'un chemin, affiche ses dimensions et retourne
    son contenu sous forme de tableau NumPy (RGB).

    Cette fonction effectue les vérifications suivantes :
    1. Existence du fichier sur le disque.
    2. Support du format (uniquement .jpg et .jpeg).

    Args:
        path (str): Le chemin vers le fichier image.

    Returns:
        np.array:Un tableau NumPy représentant l'img (Hauteur, Largeur, Canaux)
                  Retourne None en cas d'erreur.

    Raises:
        FileNotFoundError: Si le chemin spécifié n'existe pas.
        ValueError: Si le format de fichier n'est pas JPG ou JPEG.
    """
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
