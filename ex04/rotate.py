from load_image import ft_load
import matplotlib.pyplot as plt
from numpy import array


def ft_rotate(path: str) -> array:
    img = ft_load(path)

    zoomed = img[100:500, 450:850, 1]
    print(f"The shape of image is: {zoomed.shape}")
    print(zoomed)

    # Créer un nouveau tableau vide de 400x400






if __name__ == "__main__":
    ft_rotate("animal.jpeg")
