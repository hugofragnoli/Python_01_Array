import matplotlib.pyplot as plt
from numpy import array


def ft_invert(array) -> array:
    """
    Inverse les couleurs de l'image (effet négatif).

    L'inversion est calculée en soustrayant la valeur de chaque pixel à 255
    (la valeur maximale pour un canal 8-bits).

    Args:
        array (array): Le tableau NumPy de l'image originale.

    Returns:
        array: L'image avec les couleurs inversées.
    """
    # Opérateur autorisés : =, +, -, *
    # Formule : 255 - couleur
    res = 255 - array
    plt.imshow(res)
    plt.title("Invert")
    plt.show()
    return res


def ft_red(array) -> array:
    """
    Applique un filtre rouge en isolant le canal G.

    Met à zéro les canaux Vert (indice 1) et Bleu (indice 2).

    Args:
        array (array): Le tableau NumPy de l'image originale.

    Returns:
        array: L'image filtrée en rouge.
    """
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
    """
    Applique un filtre vert en isolant le canal G.

    Met à zéro les canaux Rouge (indice 0) et Bleu (indice 2).

    Args:
        array (array): Le tableau NumPy de l'image originale.

    Returns:
        array: L'image filtrée en vert.
    """
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
    """
    Applique un filtre bleu en isolant le canal B.

    Met à zéro les canaux Rouge (indice 0) et Vert (indice 1).

    Args:
        array (array): Le tableau NumPy de l'image originale.

    Returns:
        array: L'image filtrée en bleu.
    """
    # on doit selectionner les canaux rouges et verts
    # et modif leur values
    res = array.copy()
    res[:, :, 0] = res[:, :, 0] * 0
    res[:, :, 1] = res[:, :, 1] * 0
    plt.imshow(res)
    plt.title("Blue filter")
    plt.show()

    return res


def ft_grey(array) -> array:
    """
    Applique un filtre gris en calculant la moyenne des canaux RGB.

    Chaque canal de l'image résultante reçoit la moyenne arithmétique
    des trois canaux originaux, transformant la couleur en intensité lumineuse.

    Args:
        array (array): Le tableau NumPy de l'image originale.

    Returns:
        array: L'image en niveaux de gris (conservant sa structure 3D).
    """
    # on divise la somme des canaux par 3 poura voir la moyenne
    # attention : rester en 3d pour la shape
    res = array.copy()
    # Somme des 3 canaux / 3
    grey_channel = (res[:, :, 0] / 3 + res[:, :, 1] / 3 + res[:, :, 2] / 3)
    # on remplace chaque canal par cette moyenne
    res[:, :, 0] = grey_channel
    res[:, :, 1] = grey_channel
    res[:, :, 2] = grey_channel
    # cmap = gray force a utiliser un echelle de
    # couleurs allant du noir pur au blanc pur
    plt.imshow(res, cmap="gray")
    plt.title("Grey filter")
    plt.show()
