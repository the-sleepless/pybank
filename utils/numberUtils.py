def toNumber(input: int | str):
    try:
        return int(input)
    except ValueError:
        return None
