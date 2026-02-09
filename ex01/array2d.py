import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    if end < start:
        tmp = end
        end = start
        start = tmp
    np_family = np.array(family)
    np_family = np.reshape(np_family, start, end)

    return np_family.tolist()
    