def main(a):
    """
    Given an integer a, check the following conditions:
    "positive odd number",
    "positive even number",
    "negative odd number",
    "negative even number",
    "the number is zero"

    Args:
        a: integer
    Returns:
        string: the message to print
    """
    if a>0:
        if a%2==0:
            return "positive even number"
        else :
            return "positive odd number"
    else:
        if a%2==0:
            return "negative even number"
        else:
            return "negative odd number"