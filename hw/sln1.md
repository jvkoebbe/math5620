# Math 5620 Homework 1 - Solutions:

### Questions

The following should give some idea of how the solutions for the homework
problems assigned in class.

---

**Question 1.** Write out the details for the accuracy analysis for

$$
  D_- f(\bar{x}) = \frac{f(\bar{x})-f(\bar{x}-h)}{h}
$$

Compute an expression for the error in terms of $h$ and a constant. What
restrictions must be satisfied in order to use this difference.?

---

To start the solution we can write down the shifted term as

$$
  f(\bar{x}-h) = f(\bar{x})
        + f'(\bar{x}) ( \bar{x} - ( \bar{x} + h ) )
        + \frac{1}{2!}\ f''(\bar{x}) ( \bar{x} - ( \bar{x} + h )^2 ) + \cdots \\
      = f(\bar{h}) - h\ f'(\bar{x}) + \frac{1}{2}\ f''(\xi)\ h^2
$$

for some value $\xi\in (\bar{x}-h,\bar{x})$. Then, the infinite Taylor series with remainder can
be subtracted from the function value as in the numerator above to obtain

$$
  f(\bar{x}) - f(\bar{x}-h) = h\ f'(\bar{x}) - \frac{h^2}{2}\ f''(\xi)
$$

Next, divide by $h$ to obtain an expression for the error

$$
  D_- f(\bar{x}) = \frac{f(\bar{x})-f(\bar{x}-h)}{h} = f'(\bar{x}) + \frac{h}{2}\ f''(\xi)
$$

Substracting the derivative gives an expression for the signed error in the derivative
of the form

$$
  E = D_- f(\bar{x}) - f'(\bar{x}) = \frac{h}{2}\ f''(\xi)
$$

Taking the absolute value of the error makes sure that we use a well defined positive
distance, so the error analysis is given by

$$
  |E| = \left| \frac{h}{2}\ f''(\xi) \right| \leq C\ h
$$

The error, $|E|$, will go to zero as $h$ goes to zero. The expression for the error gives that 
the discrete approximation of the derivative is order $h$ and the convergence is called linear.

---

**Question 2.** Write a code that returns the coefficients for a difference quotient
   approximating the first derivative of a function at a specified point
   $\bar{x}$ given an input array of points.

The code in the following block is written in monolithic style - sort of a top to
bottom approach where some inputs are initalized, followed by some computations that
come from the algorithm we discussed along with some intermediate steps. Finally,
the code will print out the resultant values.

If the goal in some project is to use this idea multiple times to set up difference
approximations for the derivatives and test ideas, it would be best to define a set
of reusable functions using the intrinsic python function, _def_ to define a
function in the code. What is written as a part of the solution of the question will
suffice.

<pre>
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

</pre>

---

**Question 3.** Write a code that will return the coefficients of a derivative of a given
   order specified at a minimal number of points specified by the user.

The code will basically be the same as the code above. However, there are a
couple of things that need to be understood about the question at hand. The
code will need to:

(a) set the derivative value and then

(b) set the number of points on the interval to one more than the degree of the derivative.

For example, if we need a derivative approximation for the third derivative, the
number of points will need to be at least four. So, the number of points that
provide the minimum number needed for the question and the minimum amount of work
to compute a consistent approximation for the derivative.

Note that the number of points is fixed in the code once the derivative being
approximated is specificed.

<pre>

#
# Minimal Points for a User Spec'd Derivative Approximation Code
#
# Author:               Joe Koebbe
# Programming Language: Python
# 
# Description:
#
# This is a brief routine for determining the coefficients for a difference
# quotient used in the approximation of derivatives at points. the code is
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
# following function will compute coefficients for a finite difference
# quotient that uses the least number of points possible to get any
# accuracy out of using the approximation.
#
# the only input needed is the order of the derivative the is to be
# approximated
# -------------
#
def diff_coeffs(nder):
    #
    # start by setting the domain and point in the domain where the
    # derivative is to be approximated
    # --------------------------------
    #
    xbar = 0.0
    a = -1.0
    b =  1.0
    print(a,b,xbar)
    #
    # for this code, the number of points used in the algorithm is going to
    # be fixed to be one more than the degree of the derivative desired.
    # ------------------------------------------------------------------
    #
    mp1 = nder + 1
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
    #
    # set the right hand side to match the correct derivative
    # -------------------------------------------------------
    #
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
    # return the coefficients computed above
    # --------------------------------------
    #
    return coeff
#
# set the derivative order by prompting the user.
# -----------------------------------------------
#
nder = int(input("Enter an Integer: "))
print("The derivative order you have spec'd is:", nder)
#
# test things by calling the function
# -------------------
#
my_coeffs = diff_coeffs(nder)
print(my_coeffs)

</pre>

Notice that the call to input has been typed to _(int)_ in the code so that a correct
value for the order of the derivative can be identified. Also, you should note that
the domain has been fixed, and the points are equally spaced in the code.

If a user executes the code above the first thing that will popup will be the
following prompt

    Enter an Integer:

Typing a value of 3 and then a carriage return/enter will result in the following output

    [ -0.5625  1.6875 -1.6875  0.5625]

The coefficients will produce a first order approximation for the third derivative of
a function at a given point using 4 points (nodes) that are equally spaced and symmetric
about the center point. $\bar{x}$.

---

**Question 4**. Write a code that will determine the accuracy of a specified difference
quotient. That is, instead of computing the coefficients, input the
coefficients and determine the number of equations that should be satisfied. 

The function implemented below, _check_coeffs()_, takes as input a set of points, the
location where the derivative is to be approximated, and the coefficients in an 
existing approximation. Instead of solving for the coefficients, the code reconstructs
the Vandermonde matrix using the given input points and center, and then computes the
matrix vector product

$$
  A\ \bar{c} = b
$$

where, $b$, should a vector made of zeros and ony one nonzero value. The output is the
vector $b$. If all goes according to the rules, the one nonzero value indicates the
order of the derivative being approximated.

<pre>

#
# Difference Quotient Coefficient Test Code
#
# Author:               Joe Koebbe
# Programming Language: Python
# 
# Description:
#
#  The code below will take as input a set of coefficients, the location
# of the nodes, and the point where the derivative is to be approximated,
# and produce output that can be used to determine the order of the derivative
# to be approximated.
import numpy as np
#
def check_coeffs(xpts, xbar, coeffs):
    #
    # for this code, the number of points used in the algorithm is going to
    # be fixed to be one more than the degree of the derivative desired.
    # ------------------------------------------------------------------
    #
    mp1 = len(coeffs)
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
    #
    # set the right hand side to match the correct derivative
    # -------------------------------------------------------
    #
    rhs = np.zeros(mp1)
    for i in range(mp1):
        sum = 0.0
        for j in range(mp1):
            sum = sum + amat[i][j] * coeffs[j]
        rhs[i] = sum
    #
    # return the coefficients computed above
    # --------------------------------------
    #
    return rhs
#
# test things by initializing an array of coefficients that occurs in the central
# difference quotient for the the first derivative and then calling the function
# ------------------------------------------------------------------------------
#
a = -1.0
b = 1.0
xbar = 0.0
coeffs = np.zeros(3)
coeffs[0] = -0.5
coeffs[1] = 0.0
coeffs[2] = 0.5
xpts = np.zeros(3)
xpts[0] = a
xpts[1] = xbar
xpts[2] = b
my_rhs = check_coeffs(xpts, xbar, coeffs)
print("results for the central diff. for first derivative:\n\n", my_rhs)
coeffs[1] = 0.01
my_rhs = check_coeffs(xpts, xbar, coeffs)
print("\n\nresults for a bad set of coefficients:\n\n", my_rhs)

</pre>

When you look at the results above, the first example results in the following output.

<pre>

results for the central diff. for the first derivative:

 [0. 1. 0.]

</pre>

and for the second case,

<pre>

results for a bad set of coefficients:

 [0.01, 1. 0.]

</pre>

So, the code is able to catch a set of coefficients that are not going to produce
any kind of accuracy.

---