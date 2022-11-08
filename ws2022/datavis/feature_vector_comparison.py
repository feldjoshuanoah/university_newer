def minkowski(x, y, p):
    d = [abs(x_i - y_i) for x_i, y_i in zip(x, y)];
    if (p == float("inf")):
        return max(d)
    return pow(sum([pow(d_i, p) for d_i in d]), 1 / p)

f1 = [3.3, 2.4, 1.9, 5.0, 3.8]
f2 = [2.8, 2.4, 1.1, 6.2, 4.3]

print("p = 1: delta(f1, f2) = " + str(minkowski(f1, f2, 1)))
print("p = 2: delta(f1, f2) = " + str(minkowski(f1, f2, 2)))
print("p = inf: delta(f1, f2) = " + str(minkowski(f1, f2, float("inf"))))