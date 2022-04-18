def capitalize(phrase):
    """Capitalize first letter of first word of phrase.

        >>> capitalize('python')
        'Python'

        >>> capitalize('only first word')
        'Only first word'
    """
    output = []
    cap_phrase = phrase.split(' ')
    for word in cap_phrase:
        if word == cap_phrase[0]:
            output.append(word.capitalize())
        else:
            output.append(word)
    return ' '.join(output)

    # Didn't know .capitalize() would naturally only cap the first word in a string
    # there's a built-in method for this!
    # return phrase.capitalize()

    # or, doing it by hand:
    # return phrase[:1].upper() + phrase[1:]