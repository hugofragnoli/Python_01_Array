from load_image import ft_load
import matplotlib.pyplot as plt
from numpy import array
import numpy as np


def ft_rotate(path: str) -> array:
    img = ft_load(path)

    zoomed = img[100:800, 150:850, 1]
    print(f"The shape of image is: {zoomed.shape}")
    print(zoomed)

    # Créer un nouveau tableau vide de 400x400
    rows, cols = zoomed.shape
    rotated = np.zeros((cols, rows), dtype=zoomed.dtype)
    for i in range(rows):
        for j in range(cols):
            rotated[j][i] = zoomed[i][j]
    print(f"New shape after Transpose: {rotated.shape}")
    print(rotated)
    plt.imshow(rotated, cmap="gray")
    plt.show()


if __name__ == "__main__":
    ft_rotate("animal.jpeg")
