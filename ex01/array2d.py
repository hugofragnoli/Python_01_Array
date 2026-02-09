import numpy as np


def slice_me(family: list, start: int, end: int) -> list:

    np_family = np.array(family)

    print(f"My shape is : {np_family.shape}")

    res = np_family[start:end]
    # fct reshape peut changer la taille dun array instant'
    # ici on res devient un tableau numpy avec sstart inclus pour debut
    # et end exclus

    print(f"My new shape is : {res.shape}")

    return res.tolist()
    