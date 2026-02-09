def slice_me(family: list, start: int, end: int) -> list:
    if end < start:
        tmp = end
        end = start
        start = tmp