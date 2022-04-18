def sum_range(nums, start=0, end=None):
    """Return sum of numbers from start...end.

    - start: where to start (if not provided, start at list start)
    - end: where to stop (include this index) (if not provided, go through end)

        >>> nums = [1, 2, 3, 4]

        >>> sum_range(nums)
        10

        >>> sum_range(nums, 1)
        9

        >>> sum_range(nums, end=2)
        6

        >>> sum_range(nums, 1, 3)
        9

    If end is after end of list, just go to end of list:

        >>> sum_range(nums, 1, 99)
        9
    """

    # Given solution:
    # if end is None:
    #     end = len(nums)
    # return sum(nums[start:end + 1])

    sum = 0

    if isinstance(start, int) and isinstance(end, int):
        if end >= len(nums):
            end = len(nums) - 1
        for num in range(start, end + 1):
            sum += nums[num]
        return sum

    elif isinstance(start, int):
        for num in range(start, len(nums)):
            sum += nums[num]
        return sum

    elif isinstance(end, int):
        for num in range(0, end + 1):
            sum += nums[num]
        return sum

    else:
        for num in range(len(nums)):
            sum += nums[num]
        return sum