"""
-Laplace(u) = f in (0,1)x(0,1)
         u  = g on boundary
Choose exact solution as u(x,y) = sin(2*pi*x) cos(2*pi*y) so that the rhs 
is given by f(x,y) = (2*pi)^2 u(x,y). The BC g is obtained from exact solution.
"""
from dolfin import *

def Boundary(x, on_boundary):
   return on_boundary

degree = 1
mesh = UnitSquareMesh(20,20)
V = FunctionSpace(mesh, 'CG', degree)

u = TrialFunction(V)
v = TestFunction(V)

# Bilinear form
a = inner(grad(u), grad(v))*dx

# Linear functional
f = Expression('8*pi*pi*sin(2*pi*x[0])*cos(2*pi*x[1])',degree=degree)
L = f*v*dx

# Dirichlet bc
g = Expression('sin(2*pi*x[0])*cos(2*pi*x[1])',degree=degree)
bc= DirichletBC(V, g, Boundary)

# Solution variable
w = Function(V)
solve(a == L, w, bc)
File('sol.pvd') << w
