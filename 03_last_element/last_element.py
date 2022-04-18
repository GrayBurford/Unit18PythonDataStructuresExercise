def last_element(lst):
    """Return last item in list (None if list is empty.
    
        >>> last_element([1, 2, 3])
        3
        
        >>> last_element([]) is None
        True
    """
    if len(lst) == 0:
        return None
    return lst[len(lst) - 1]

    # ANSWER
    # if lst:
    #   return lst[-1]
    # functions return None by default, and can use index [-1] in Python, unlike JavaScript