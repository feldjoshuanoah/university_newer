import numpy as np

h_1 = np.array([2, 4, 3, 0, 6, 2])
h_2 = np.array([3, 6, 4, 1, 5, 2])

d = np.count_nonzero(h_1 != h_2)
print(f"a) D(h_1, h_2) = {d}")

l_1 = np.linalg.norm(h_2 - h_1, 1)
l_2 = np.linalg.norm(h_2 - h_1, 2)
l_inf = np.linalg.norm(h_2 - h_1, np.inf)
l = np.array([l_1, l_2, l_inf])
print(f"b) L_1(h_1, h_2) = {l[0]}")
print(f"   L_2(h_1, h_2) = {l[1]}")
print(f"   L_inf(h_1, h_2) = {l[2]}")

hi_12 = np.sum(np.minimum(h_1, h_2)) / np.sum(h_2)
hi_21 = np.sum(np.minimum(h_1, h_2)) / np.sum(h_1)
print(f"c) HI(h_1, h_2) = {hi_12}")
print(f"   HI(h_2, h_1) = {hi_21}")

iou = np.sum(np.minimum(h_1, h_2)) / np.sum(np.maximum(h_1, h_2))
print(f"d) IoU(h_1, h_2) = {iou}")