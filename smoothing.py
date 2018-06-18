import numpy as np

test = [1000, 2000, 1570, 2100, 1170, 1860, 2060, 2080, 3100]


def smooth_avg(l, o):
    new_l = l
    outliers = o
    count = 0
    m = np.mean(new_l)
    s = np.std(new_l, ddof=1)
    max_n = 0
    for x in range(len(new_l)):
        item = new_l[x]
        if item > m + s:
            outliers.append(item)
            new_l[x] = max_n
            count += 1
        else:
            pass
        if new_l[x] > max_n:
            max_n = new_l[x]
    if count == 0:
        return outliers
    else:
        return smooth_avg(new_l, outliers)

print(smooth_avg(test, []))
