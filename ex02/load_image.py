from PIL import Image
from numpy import array
import numpy as np
import os

# Pil = biblio de ref pour ouvrir images en python
# os = pour verif si fichier bien la avant douvrir
# numpy car image est un array de nombres 3d pour rgb.

def ft_load(path: str) -> array:
    