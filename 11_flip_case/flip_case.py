def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    flipped_phrase = []
    for char in phrase:
        if char.upper() == to_swap.upper():
            flipped_phrase.append(char.swapcase())
        else:
            flipped_phrase.append(char)
    return ''.join(flipped_phrase)

    # to_swap = to_swap.lower()
    # out = ""
    # for ltr in phrase:
    #     if ltr.lower() == to_swap:
    #         ltr = ltr.swapcase()
    #     out += ltr
    # return out

    # to_swap = to_swap.lower()
    # fixed = [
    #     (char.swapcase() if char.lower() == to_swap else char)
    #     for char in phrase
    # ]
    # return "".join(fixed)
