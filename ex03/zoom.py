from load_image import ft_load
import matplotlib.pyplot as plt
from numpy import array


def ft_zoom(path: str) -> array:
    # ici on dit :
    # Prends les pixels a partir de la ligne 100
    # jusqua ligne 500 (hauteur)
    # Prends de colonne 400 a 800 (largeur)
    # :1 on dit a Python de garder 1 canal pour le gris
    try:
        img = ft_load(path)
        if img is None:
            return None
        print(img)
        zoomed_img = img[100:500, 450:850, 0:1]

        print(f"New shape after slicing: {zoomed_img.shape}")
        print(zoomed_img)

        plt.imshow(zoomed_img, cmap="gray")
        plt.title("Zoomed animal.jpeg")
        plt.show()

        return zoomed_img

    except Exception as e:
        print(f"Error: {e}")
        return None


if __name__ == "__main__":
    ft_zoom("animal.jpeg")
