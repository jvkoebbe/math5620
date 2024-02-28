# Math 5620 Homework 4

## Questions

The following questions should be completed.

---

**Question 1.** In this problem you will need to write code to approximately solve the elliptic partial differential equation (PDE). The following PDE is called the Poisson equation. Note that

$$
  \Delta u = f
$$

in $\Omega$ with boundary conditions defined by

$$
  u(x,y) = g(x,y)
$$

on $\partial\Omega$, the boundary of the region. This is a region in two spatial dimensions.
Write your code to use a domain defined by the unit square. That is, $\Omega=(0,1)\times(0,1)$.

Use equally spaced points in the finite different method in both directions as done in class.
Choose the same mesh size in both directions. Make sure that the code produced allows the user
to use different values of $h$. For the problems below, the code developed for this Question
needs to be able to set up the linear system of equations that results from application of the
5-point stencil as discussed in class. we will want to use values of $h$ in the following list.

$$
  h_i = \left\lbrace \frac{1}{8}, \frac{1}{16}, \frac{1}{32}, \ldots, \frac{1}{2^8} \right\rbrace
$$

The code for this Question should handle the setup to the problem up to the choice of linear
solver for the linear system of equations that results from the finite difference method.

Note: The boundary conditions and right hand side function for examples are given at the end of
the homework set.

---

**Question 2.** A couple of graphcs to see what is going on.

Using Matplotlib (or equivalent package) to graph the solutions obtained in the computational
convergence study. This means the use a contour plot, a density plot, or a streamline plot. This
question needs at least one of the three types of plots above for the question solution to be
considered completed. Make sure that your code accepts as input on the two dimensional grid used
to define the mesh. You can test this code by graphing the right hand side function in the problem
definition. It would pay dividends if the code written for this question could provide a function
that you pass the data for the right hand side function at the mesh points and provide
plots/graphics of the data. Then you will be able to reuse this code to plot the solutions for
the PDE.

---

**Question 3.** Linear Solution using Jacobi Iteration.

Build a piece of code or function that implements Jacobi iteration for the linear system that
results from the finite difference method used in this assignment. Use a sparse matrix approach
that stores only the nonzero entries in the matrix. This means using a vector for each of the
diagonals (5) that contain nonzero entries.

---

**Question 4.** Conjugate Gradient Liniear Solution.

Repeat the same work as in Question 3. Instead of using the Jacobi Iteration Method, use the
Conjugate Gradient method for the solution process. Compare the results on the finest resolution
chosen in the list of $h$ values, $h=\frac{1}{2^8}$. Show your results using the graphics code
from Question 2. Show graphs of both solution results as part of your write-up.

---

## The Rest Of The Story

For the PDE in this problem set use the following data.

$$
  f(x,y) = 3\ \sin(\pi\ x)\ \sin(4\pi\ y)
$$

and

$g(x,y)=0$ on the boundary of the unit square. If you feel adventurous, try another right hand
side function of the form

$$
  f(x,y) = 16\ (x-x^2)\ (y-y^2)\ e^{-\left(  (x-0.5)^2+(y-0.5)^2\right)}
$$

with the same homogeneous boundary conditions. Note that the second problem only requires a single
change in one line of your code provided the function is reusable.