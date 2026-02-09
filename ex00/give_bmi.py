# 2. Formule MathématiquePour rappel, la formule de
# l'IMC est :$$BMI = \frac{poids}{taille^2}$$Le poids est en
# kg et la taille en mètres.
import numpy as np


def give_bmi(
    height: list[int | float],
    weight: list[int | float]
) -> list[int | float]:

    try:
        # On transforme les listes en tableaux NumPy
        np_height = np.array(height)
        np_weight = np.array(weight)
        if len(np_height) != len(np_weight):
            raise AssertionError("The lists don't have the same size")
        if (np_height <= 0).any() or (np_weight <= 0).any():
            raise ValueError("Height and weight must be positive numbers.")

    # NumPy comprend qu'il doit diviser chaque poids par le
    # carré de chaque taille correspondante.
        bmi_array = np_weight / (np_height ** 2)
        return bmi_array.tolist()

    except (AssertionError, ValueError) as e:
        print(f"{type(e).__name__}: {e}")
        return []


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    # On transforme la liste d'IMC en tableau NumPy
    np_bmi = np.array(bmi)
    # NumPy compare chaque élément du tableau à la limite d'un coup
    res = np_bmi > limit
    # On convertit le tableau de booléens en liste 
    return res.tolist()
