# Challenge 2: Two numbers are positive.

def check_positive_integers(a, b, c):
    try:
        # Validate that a, b, and c are integers
        if isinstance(a, int) and isinstance(b, int) and isinstance(c, int):
            # Check if at least two out of the three numbers are positive
            if (a > 0 and b > 0) or (a > 0 and c > 0):
                print(True)
            else:
                print(False)
        else:
            print("a, b, or c should be integers")
    except TypeError:
        # Handle the case where a, b, or c are not valid inputs.
        print("a, b, or c should be integers")


check_positive_integers(2, -3, "4")
