import numpy as np

f_1 = np.array([3.3, 2.4, 1.9, 5.0, 3.8])
f_2 = np.array([2.8, 2.4, 1.1, 6.2, 4.3])

l_1 = np.sum(np.abs(f_2 - f_1))
l_2 = np.sqrt(np.sum((f_2 - f_1) ** 2))
l_inf = np.max(f_2 - f_1)
l = np.array([l_1, l_2, l_inf])
print(f"a) L_1(f_1, f_2) = {l[0]}")
print(f"   L_2(f_1, f_2) = {l[1]}")
print(f"   L_inf(f_1, f_2) = {l[2]}")

s_log = 1 - np.log(1 + l)
s_exp = np.exp(-l)
print(f"b) (i)  s_(log, 1)(f_1, f_2) = {s_log[0]}")
print(f"        s_(log, 2)(f_1, f_2) = {s_log[1]}")
print(f"        s_(log, inf)(f_1, f_2) = {s_log[2]}")
print(f"   (ii) s_(exp, 1)(f_1, f_2) = {s_exp[0]}")
print(f"        s_(exp, 2)(f_1, f_2) = {s_exp[1]}")
print(f"        s_(exp, inf)(f_1, f_2) = {s_exp[2]}")

s_dot = np.dot(f_1, f_2)
s_cos = s_dot / (np.linalg.norm(f_1) * np.linalg.norm(f_2))
print(f"c) (i)  s_d(f_1, f_2) = {s_dot}")
print(f"   (ii) s_c(f_1, f_2) = {s_cos}")
