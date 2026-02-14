from load_image import ft_load
import matplotlib.pyplot as plt
from numpy import array


def ft_zoom(path: str) -> array:
    """
    Charge une image, effectue un zoom par recadrage (slicing), convertit
    en niveaux de gris et affiche le résultat.

    La fonction utilise le slicing de tableau NumPy pour isoler une zone
    spécifique de l'image et ne conserver qu'un seul canal de couleur.

    Args:
        path (str): Le chemin vers l'image à traiter.

    Returns:
        np.array: Le tableau NumPy de l'image zoomée et grise.
                  Retourne None en cas d'erreur.

    Comportement du Slicing [100:500, 450:850, 0:1] :
        - 100:500 : Sélectionne les lignes de 100 à 500 (axe vertical/hauteur).
        - 450:850 : Sélectionne les colonnes de 450 à 850 (axe hor/lar).
        - 0:1     : Ne garde que le premier canal (Rouge), ce qui, combiné
                    au cmap="gray", permet un affichage en niveaux de gris.
    """
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
