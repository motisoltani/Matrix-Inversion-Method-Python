'''
Systems of Linear Algebraic Equations
Matrix Inversion Method 
language: Python

Motahare Soltani
soltani.wse@gmail.com

'''

import numpy as np
import scipy.linalg as la

A = np.array([[2,1],[1,1]])
b = np.array([1,-1]).reshape(2,1)

Ainv = la.inv(A)
x = Ainv @ b
print(x)
