#
# Difference Quotient Code
#
# Author:               Joe Koebbe
# Programming Language: Python
# 
# Description:
#
# This is a brief routine for determining the coefficients for a difference
# quotients used in the approximation of derivatives at points. the code is
# written in Python. The code takes as input:
#
# xpts  - A set of points where a function value will be obtained or given
# (a,b) - A domain on which the difference quotient will be computed.
# xbar  - A point at which the difference quotient will be computer.
# nder  - The order of the derivative that is being approximated.
# mp1   - The total 
#
# The output will be an array coefficients computed using Taylor Series
# expansion at each points
#
import numpy as np
import matplotlib.pyplot as plt
#
# Set problem input values as discussed above.
# --------------------------------------------
#
nder = 1
xbar = 0.0
a = -1.0
b =  1.0
mp1 = 7
m = mp1 - 1
h = ( b - a ) / m
#
# Initialize an array of equally spaced points
# --------------------------------------------
# 
xpts = np.zeros(mp1) 
for j in range(mp1):
    xpts[j] = a + j * h
#
# Intialize the matrix (Vandermond matrix) for the coefficient matrix and
# the associated right hand side for the approximation of a given derivative.
# ---------------------------------------------------------------------------
#    
amat = np.ones((mp1,mp1))
for i in range(1,mp1):
    for j in range(mp1):
        amat[i][j] = amat[i-1][j] * ( xpts[j] - xbar )
rhs = np.zeros(mp1)
rhs[nder] = 1.0
#
# Perform row reduction or Gaussian elimination of the system to an upper
# triangular matrix.
# -----------------
#
for k in range(m):
    for i in range(k+1,mp1):
        val = amat[i][k] / amat[k][k]
        for j in range(k+1,mp1):
            amat[i][j] = amat[i][j] - val * amat[k][j]
        rhs[i] = rhs[i] - val * rhs[k]
#
# Use backsubstitution to get the coefficients.
# ---------------------------------------------
#
coeff = np.zeros(mp1)
coeff[m] = rhs[m] / amat[m][m]
for i in range(m-1,-1,-1):
    sum = 0.0
    for j in range(i+1,mp1):
        sum = sum + amat[i][j] * coeff[j]
    coeff[i] = ( rhs[i] - sum ) / amat[i][i]
#
# print out the coefficients
# --------------------------
#
for i in range(mp1):
    print("i=", i, "\tx = ", xpts[i], "\t\t\tcoefficent: ", coeff[i])
#
# solve the Vandermond matrix linear system
# ------------------------------------------
#
#coef = np.ones(mp1)
#yold = np.zeros(mp1)
#ynew = np.zeros(mp1)
#res = np.zeros(mp1)
#tol = 0.0001
#error = 10.0 * tol
#maxiter = 2
#iter = 0
#
# solution loop
# -------------
#
#while (error > tol) and (iter < maxiter):
#    iter = iter + 1
#    # matrix-vector computational routine
#    for i in range(mp1):
#        sum = 0.0
#        for j in range(mp1):
#            sum = sum + amat[i][j] * yold[j]
#        res[i] = rhs[i] - sum
#    for i in range(m):
#        ynew[i] = yold[i] + res[i] / amat[i][i]
#    sum = 0.0
#    for i in range(mp1):
#        val = ynew[i] - yold[i]
#        sum = sum + val * val
#    error = np.sqrt(sum)
#    for i in range(mp1):
#        yold[i] = ynew[i]