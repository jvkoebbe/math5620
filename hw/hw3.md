# Math 5620 Homework 3:

### Questions

The following questions should be completed.

<hr>

**Question 1.** For the example problem

  $$
    u''(x) = f(x)
  $$

  with $f(x)=\cos(\frac{3\pi}{2} x)$ and boundary conditions $u(0)=0$ and
  $u(1)=1$, complete a computational convergence study to verify
  the order of accuracy analysis. Use the sequence of $h$ values

$$
  h_i = \left\lbrace \frac{1}{8}, \frac{1}{16}, \frac{1}{32}, \ldots, \frac{1}{2^8} \right\rbrace
$$

<hr>

**Question 2.** A couple of graphcs to see what is going on.

Using Matplotlib (or equivalent) graph the solutions obtained in the computational
convergence study.

<hr>

**Question 3.** An alternative method.

The finite difference scheme can be changed by including an alternative difference
quotient. Use the code written in Assignment/Homework 1 to produce coefficients for a
fourth order derivative approximation of $u''$. Use a centered difference quotient.
Describe problems that occur at the boundaries of the domain. How does the alternate
method incorporate the boundary conditions? If a reflection condition is applied at the
boundary points, determine if this effects the accuracy of the approximation.

<hr>

**Question 4.** A better f fix.

Use your code from Assignment/Homework 1 to produce a fourth order difference that
stays within the domain at the boundaries and use the foruth order central difference
at points where possible. Discuss how the matrix structure is effected. What advantages
are there to using the Jacobi iteration method over a Gaussian elimination approach?
 
<hr>
