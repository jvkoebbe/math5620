# Math 5620 Homework 5

## Questions

The following questions should be completed.

---

**Question 1.** For the Logisitic Equation, defined
in Question 2, write out the details for finding the
carrying capacity for the system. You should be able
to do this without solving the ODE. Build a code
that will return the carrying capacity of the
population being modeled given appropriate input(s).

---

**Question 2.** Write a code that will implement the Explicit Euler Method on the Logisitic equation,
$$
  \frac{dP}{dt} = \alpha\ P - \beta\ P^2
$$
with $P(0)=10$. Test your code using the following cases:

* **(a.)** $\alpha=1.5, \beta=0.001$
* **(b.)** $\alpha=1.5, \beta=0.01$
* **(c.)** $\alpha=0.15, \beta=0.001$

Make sure that $\Delta t$ is small enough to be able
to resolve the solution and the see that the
carrying capacity is achieved.

---

**Question 3.** Repeat the work in Question 1 using
the Implicit Euler Method. Use some algebra to
figure out how to write out the algoritihm. As
discussed in class you will need to determine an appropriate for for the left hand side of the
equation.

---

**Question 4.** Repeat the work in Question 1. using a predictor-corrector method defined by explicit Euler for the prediction and implicit Euler for the correction step.
