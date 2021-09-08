def actual_recursive(n):
        if n < 0:
            return None
        if n == 0:
            return 1
        else:
            return n * actual_recursive(n-1)