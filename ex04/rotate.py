from load_image import ft_load
import matplotlib.pyplot as plt
from numpy import array
import numpy as np


def ft_rotate(path: str) -> array:
    """Take a path to an image, prints its rgb array, zoom on it,
    prints the new RGB ARRAY, rotate, display the image
    zoomed and rotate and return it"""
    img = ft_load(path)

    zoomed = img[100:500, 450:850, 0:1]
    print(f"The shape of image is: {zoomed.shape}")
    print(zoomed)

    # Créer un nouveau tableau vide de 400x400
    rows, cols, channels = zoomed.shape
    rotated = np.zeros((cols, rows), dtype=zoomed.dtype)
    for i in range(rows):
        for j in range(cols):
            rotated[j][i] = zoomed[i][j][0]
    print(f"New shape after Transpose: {rotated.shape}")
    print(rotated)
    plt.imshow(rotated, cmap="gray")
    plt.title("Rotated animal.jpeg")
    plt.show()

    return rotated


if __name__ == "__main__":
    ft_rotate("animal.jpeg")
