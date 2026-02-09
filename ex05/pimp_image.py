from load_image import ft_load
import matplotlib.pyplot as plt
from numpy import array
import numpy as np

def ft_invert(array) -> array:
    """Inverts the color of the image received."""
    # Opérateur autorisés : =, +, -, *
    # Formule : 255 - couleur
    res = 255 - array
    plt.imshow(res)
    plt.title("Invert")
    plt.show()
    return res


# def ft_red(path: str) -> array:



# def ft_green(path: str) -> array:




# def ft_blue(path: str) -> array:



# def ft_grey(path: str) -> array;