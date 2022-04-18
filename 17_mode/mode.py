def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    # num/freq counter dictionary
    counter = {}

    # add 1 to each num's value for each frequency
    for num in nums:
        counter[num] = counter.get(num, 0) + 1
        # if counter[num]:
        #     counter[num] += 1
        # else:
        #     counter[num] = 1
        #Syntax only works in JS??
    
    # find max value (highest freuency)
    max_frequency = max(counter.values())

    # cross-check which num(key) had that frequency
    for val in counter.keys():
        if counter[val] == max_frequency:
            return val