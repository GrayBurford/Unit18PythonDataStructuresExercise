def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """

    if len(str(num1)) != len(str(num2)):
        return False

    dict_one = {}
    dict_two = {}
    
    for n in str(num1):
        dict_one[n] = dict_one.get(n, 0) + 1

    for n in str(num2):
        dict_two[n] = dict_two.get(n, 0) + 1

    if len(dict_one.keys()) != len(dict_two.keys()):
        return False

    return dict_one == dict_two