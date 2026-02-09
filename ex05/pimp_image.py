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


def ft_red(array) -> array:
    """Applies a red filter to the image """
    # on doit selectionner les canaux verts et bleus
    # et modif leur values
    res = array.copy()
    res[:, :, 1] = res[:, :, 1] * 0
    res[:, :, 2] = res[:, :, 2] * 0
    plt.imshow(res)
    plt.title("Red filter")
    plt.show()

    return res


def ft_green(array) -> array:
    """Applies a green filter to the image """
    # on doit selectionner les canaux verts et bleus
    # et modif leur values
    res = array.copy()
    res[:, :, 0] = res[:, :, 0] * 0
    res[:, :, 2] = res[:, :, 2] * 0
    plt.imshow(res)
    plt.title("Green filter")
    plt.show()

    return res



def ft_blue(array) -> array:
    """Applies a blue filter to the image """
    # on doit selectionner les canaux verts et bleus
    # et modif leur values
    res = array.copy()
    res[:, :, 0] = res[:, :, 0] * 0
    res[:, :, 1] = res[:, :, 1] * 0
    plt.imshow(res)
    plt.title("Blue")
    plt.show()

    return res



# def ft_grey(path: str) -> array;