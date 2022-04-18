def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    my_dict = {}
    my_set = {char for char in phrase}
    for each in my_set:
        my_dict[each] = phrase.count(each)
    return my_dict

    # counter = {}
    # for ltr in phrase:
    #     counter[ltr] = counter.get(ltr, 0) + 1
    # return counter