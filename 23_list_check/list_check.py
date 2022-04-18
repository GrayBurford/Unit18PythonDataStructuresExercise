def list_check(lst):
    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """
    result = []
    for each in lst:
        if isinstance(each, list):
            result.append(True)
        else:
            result.append(False)
    return all(result)

    # for item in lst:
    # if not isinstance(item, list):
    #     return False

    # return True
