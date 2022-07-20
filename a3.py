from scipy.interpolate import lagrange
import numpy as np
from numpy.polynomial import polynomial as P
from a1 import poly_interpolate, Z

np.set_printoptions(precision=2)

Q = np.array(
    [
        [0, 0, 0, 2, 0, 0, 1],
        [0, 0, 0, -1, 0, 0, 1],
        [-1, 0, -1, -1, -1, -1, -1],
        [-1, 1, 1, 0, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0],
    ]
)
ABC = np.array(
    [
        [0, 0, 11, 11, 55, 17, 0],
        [1, -1, 5, 5, 0, -1, -17],
        [-1, 0, 55, 17, 0, -17, -17],
    ]
)


def PLONK(Q, ABC):
    index = np.arange(1, np.shape(Q)[1] + 1)
    q_L, q_R, q_O, q_M, q_C = [
        P.Polynomial(coeffs) for coeffs in poly_interpolate(index, Q)
    ]

    a, b, c = [P.Polynomial(coeffs) for coeffs in poly_interpolate(index, ABC)]

    # qL(x) - a(x) + qR(x) - b(x) + qO(x) - c(x) + qM(x) - (a(x) * b(x)) + qC(x)
    T = q_L - a + q_R - b + q_O - c + q_M - (a * b) + q_C
    z = Z(np.shape(ABC)[0])
    return P.polydiv(T.coef, z)


print(PLONK(Q, ABC))
