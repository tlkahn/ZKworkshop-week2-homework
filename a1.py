from scipy.interpolate import lagrange
import numpy as np
from numpy.polynomial import polynomial as P

np.set_printoptions(precision=2)


def poly_interpolate(index, matrics):
    res = []
    for row in matrics:
        poly = lagrange(index, row).coef[::-1]
        res.append(poly)
    return np.array(res, dtype=object)


def polymuln(lst):
    if len(lst) == 0:
        return 1
    return P.polymul(lst[0], polymuln(lst[1:]))


def QAP(s, A, B, C):
    L = np.matmul(s, A)
    R = np.matmul(s, B)
    O = np.matmul(s, C)
    print(f"L: {L}")
    print(f"R: {R}")
    print(f"O: {O}")
    Q = P.polysub(P.polymul(L, R), O)
    print(f"T:\n {Q}")
    assert len(L) == len(R) == len(O)
    return P.polydiv(Q, Z(len(L)))


def Z(n):
    ns = [[-(1 + i), 1] for i, _ in enumerate(range(n))]
    return polymuln(ns)


def main(s, A, B, C):
    x = np.arange(1, len(A) + 1)

    resA = poly_interpolate(x, np.transpose(A))
    resB = poly_interpolate(x, np.transpose(B))
    resC = poly_interpolate(x, np.transpose(C))

    print(f"resA: \n {resA}")
    print(f"resB: \n {resB}")
    print(f"resC: \n {resC}")

    return QAP(s, resA, resB, resC)


# variables: \sim{one},x,y,z,xminu1,ytimesz,twoyminusz,l,r,\sim{out}
s = np.array([1, 0, 11, 5, 0, 55, 17, 0, -17, -17])

A = np.array(
    [
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
        [2, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    ]
)


B = np.array(
    [
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    ]
)

C = np.array(
    [
        [1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    ]
)

# print(main(s, A, B, C))

# A = np.array(
#     [
#         [0, 1, 0, 0, 0, 0],
#         [0, 0, 0, 1, 0, 0],
#         [0, 1, 0, 0, 1, 0],
#         [5, 0, 0, 0, 0, 1],
#     ]
# )

# B = np.array(
#     [
#         [0, 1, 0, 0, 0, 0],
#         [0, 1, 0, 0, 0, 0],
#         [1, 0, 0, 0, 0, 0],
#         [1, 0, 0, 0, 0, 0],
#     ]
# )

# C = np.array(
#     [
#         [0, 0, 0, 1, 0, 0],
#         [0, 0, 0, 0, 1, 0],
#         [0, 0, 0, 0, 0, 1],
#         [0, 0, 1, 0, 0, 0],
#     ]
# )

# A_ = np.array(
#     [
#         [-5.0, 9.166, -5.0, 0.833],
#         [8.0, -11.333, 5.0, -0.666],
#         [0.0, 0.0, 0.0, 0.0],
#         [-6.0, 9.5, -4.0, 0.5],
#         [4.0, -7.0, 3.5, -0.5],
#         [-1.0, 1.833, -1.0, 0.166],
#     ]
# )
# B_ = np.array(
#     [
#         [3.0, -5.166, 2.5, -0.333],
#         [-2.0, 5.166, -2.5, 0.333],
#         [0.0, 0.0, 0.0, 0.0],
#         [0.0, 0.0, 0.0, 0.0],
#         [0.0, 0.0, 0.0, 0.0],
#         [0.0, 0.0, 0.0, 0.0],
#     ]
# )
# C_ = [
#     [0.0, 0.0, 0.0, 0.0],
#     [0.0, 0.0, 0.0, 0.0],
#     [-1.0, 1.833, -1.0, 0.166],
#     [4.0, -4.333, 1.5, -0.166],
#     [-6.0, 9.5, -4.0, 0.5],
#     [4.0, -7.0, 3.5, -0.5],
# ]
# s = np.array([1, 3, 35, 9, 27, 30])

# print(main(s, A, B, C))
