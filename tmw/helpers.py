def avg(seq):
    """Returns the average of a sequence of items.

    :param seq: sequence of items.
    :returns: The sum of the items
    """
    length = len(seq)
    if length == 0:
        return 0
    else:
        return sum(seq) / length
