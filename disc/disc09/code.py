def fit(total, n):
    def f(total, n, k):
        if n == 0 and total == 0:
            return True
        if total < k * k or n < 0:
            return False
        # Try including k^2 and moving to next square, or skip k^2
        return f(total - k * k, n - 1, k + 1) or f(total, n, k + 1)
    
    return f(total, n, 1)

def pair_up(s):
    # try with class Link
    if len(s) <= 3:
        return [s]
    else:
        return [s[:2]] + pair_up(s[2:])
