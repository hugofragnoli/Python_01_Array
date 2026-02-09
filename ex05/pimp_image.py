import matplotlib.pyplot as plt
from numpy import array

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
    # on doit selectionner les canaux rouge et bleus
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
    # on doit selectionner les canaux rouges et verts
    # et modif leur values
    res = array.copy()
    res[:, :, 0] = res[:, :, 0] * 0
    res[:, :, 1] = res[:, :, 1] * 0
    plt.imshow(res)
    plt.title("Blue")
    plt.show()

    return res


def ft_grey(array) -> array:
    """Applies a grey filter to the image """
    # on divise la somme des canaux par 3 poura voir la moyenne
    # attention : rester en 3d pour la shape
    res = array.copy()
    # Somme des 3 canaux / 3
    grey_channel = (res[:, :, 0] / 3 + res[:, :, 1] / 3 + res[:, :, 2] / 3)
    # on remplace chaque canal par cette moyenne
    res[:, :, 0] = grey_channel
    res[:, :, 1] = grey_channel
    res[:, :, 2] = grey_channel
    # cmap = gray force a utiliser un echelle de couleurs allant du noir pur au blanc pur
    plt.imshow(res, cmap="gray")
    plt.title("Grey")
    plt.show()