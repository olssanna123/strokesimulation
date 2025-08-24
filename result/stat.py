def seconds_to_minutes(seconds_list):
    """
    Convert a list of times in seconds (float) to minutes (float).

    Args:
        seconds_list (list of float): Times in seconds.

    Returns:
        list of float: Times in minutes.
    """
    return [sec / 60.0 for sec in seconds_list]