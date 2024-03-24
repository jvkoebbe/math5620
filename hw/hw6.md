# Math 5620 Homework 6

## Questions

The following questions should be completed. The
problems consider the solution of the heat equation.
In one spatial dimension (heat in a wire) defined by
$$
  \frac{\partial u}{\partial t}
     = \kappa\ \frac{\partial^2 u}{\partial x^2}
$$
with initial condition,
$$
  \begin{split}
    &u(x,0) = u_0(x), \\
    & \ \\
    &u(a,t) = \alpha, \\
    & \ \\
    &u(b,t) = \beta
  \end{split}
$$

---

**Question 1.** Write a code that will approximately solve heat equation using finite difference methods as discussed in class and presented in the book. Use an explicit Euler method for the discretization in $t$ and a central difference in $x$. Start with the unit interval as the domain and integrate in $t$ from $0$ to $1$, $\kappa=1$, and use
$$
  u_0(x) = \sin(\pi x)
$$
with boundary conditions $\alpha=0$ and $\beta=0$.

---

**Question 2.** Write a code to implement the
implicit Euler method on the same problem as given
in Question 1. Compare your results in this problem
to the results for Question 1. As a hint, this will
require a matrix inversion at each step. You should
have the good old Thomas Algorithm for this.

**Question 3.** Write an explicit method for the
heat equation that implements a fourth order in the
variable, $x$. Use the first order in $t$ explicit
Euler method as in Question 1. Try out the code on
the heat equation defined for Question 1 and
Question 2. Note that you will need to cut the time
step. Without much explanation, the time step will
be order $(\Delta x^4)$.

**Question 4.** Describe how to modify your code in
Question 3 to implement the Implicit Euler method
for the heat equation above. You do not need to
write the code. Just write a brief description of
how the modifications will effect the algorithm.
