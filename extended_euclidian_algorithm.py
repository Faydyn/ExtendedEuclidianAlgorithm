def eea(a, b, x0, x1, y0, y1, lst):
    if b == 0:
        iterations = [a, b, x0, None, y0, None, None]
        lst.append(iterations)
        return lst
    else:
        q = a // b
        iterations = [a, b, x0, x1, y0, y1, q]
        lst.append(iterations)
        a, b = b, a - q * b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
        return eea(a, b, x0, x1, y0, y1, lst)
