def is_number(value):
    """ Checks if a value is an integer and returns the boolean result

    :param value: value to be checked
    :return bool: the check result
    """
    try:
        int(value)
        return True
    except ValueError:
        return False
