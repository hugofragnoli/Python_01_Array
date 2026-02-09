import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    if end < start:
        tmp = end
        end = start
        start = tmp
    np_family = np.array(family)

    res = np_family.tolist()
    