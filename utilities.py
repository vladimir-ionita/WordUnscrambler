def is_number(value):
    try:
        int(value)
        return True
    except ValueError:
        return False
