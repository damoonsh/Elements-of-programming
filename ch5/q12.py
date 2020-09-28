"""
    R rectangle: if the sides are parallel to x and y-axis

    given two S and R are xy-aligned rectangles, write a functions that
    determines if the two have a nonempty intersectiona and if yes then
    return the properties of that rectangle.
"""

# (Rx, Ry, Rh, Rw)

def check_intersection(S, R) -> (int, int, int, int):
    (xs, ys, hs, ws), (xr, yr, hr, wr) = S, R
    x, y, h, w = -1, -1, 0, 0

    print('Cond1: ' ,xs <= xr <= xs + ws, ', Cond2:',xs <= xr + wr <= xs + ws)
    x_small_cond, x_big_cond = xs <= xr <= xs + ws, xs <= xr + wr <= xs + ws
    if x_small_cond: x, w = xr, xr - xs
    if x_small_cond: x, w = xs, xr + wr - xs
    if x_small_cond and x_big_cond: x, w = xr, 
    print('Cond1: ', ys <= yr <= ys + hs, ', Cond2:', ys <= yr + hr <= ys + hs)
    if ys <= yr <= ys + hs: y, h = yr, ys
    if ys <= yr + hr <= ys + hs: y, h = ys, yr - ys

    if x != -1 and y != -1:
        return (x, y, h + 1, w + 1)
    else:
        return (0, 0, 0, 0)