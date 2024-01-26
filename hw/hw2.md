# Math 5620 Homework:

### Homework No. 2 Questions

The following questions should be completed. This assignment will start working
through the development of a finite difference approximation for the simplest of
two-point boundary value problem (2-pt BVP) of the form

$$
  u''(x) = f(x), \ \ \ \ \ x\in (a,b)
$$

with $u(0)=\alpha$ and $u(1)=\beta$.

<hr>

1. To start the process, put together routines that set up the computational
   parameters. Define functions to do the following.

   a. A function that will initialize the left endpoint of a one-dimensional
      domain or interval.

   b. A function that will initialize the right endpoint of a one-dimensional
      domain or interval.

   c. A function that will set the number of points including the endpoints of
      the domain. That is, the value of $m$ introduced in class. So, $a=x_0$ and
      $b=x_{m+1}$.

   d.  A function that evaluates the function, $f(x)$ that appears on the right
       hand side of the ODE. Below a test case will include the sine function.
  
<hr>

2. Next, we want to initialize the parameters we need to approximate the
   derivative. Define functions to do the following.

   a. A function to compute the increment for the distance between any two
      points in the mesh.

   b. A function to initialize an array/list of numbers for the points in the
      domain.

   c. A function to initialize an array to hold the approximation of the
      solution of the differential equation.

   d. A function to assign the left boundary condition to the appropriate
      location in the array.

   e. A function to assign the right boundary condition to the appropriate
      location in the array.

   f. A function to initialize an array/list of values for the function, $f(x)$,
      at the points in the domain.

<hr>

3. Now into the solution process. Define functions to do the following.

   a. A function that will set up the linear system of equations that results
      from applying the second order centered finite difference. This includes
      the storage for the matrix and right hand side vector.  

   b. A function that will perform Gaussian elimination on the resulting linear
      system of equations for the 2-point BVD using the Thomas algorithm
      discussed in class. In this case, use matrix storage that includes the
      zeros.

Make sure that the code reflects the

<hr>

4. Write code to test the code that involves approximating the solution of the
   2-pt BVP. Use $f(x)=sin(\pi x)$ with $\alpha-0$ and $\beta=1.0$. Since you
   are including a lot of zeros (that are not needed) the size of the test
   problem will need to be limited. Try your code on problems with $m=4,8,16$.
   Note that in the next homework, the issues related to the sparse nonzero
   structure will be addressed in the next homework. In addition, we will
   include alternative methods for solution of the linear system.

<hr>
