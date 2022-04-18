def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    # list = phrase.split(' ')
    # new_phrase = []
    # for each in list:
    #     new_phrase.append(each.lower().capitalize())
    # return ' '.join(new_phrase)

    return ' '.join([each.lower().capitalize() for each in phrase.split(' ')])

    # built-in method:
    # return phrase.title()