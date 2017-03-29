# Matrix Algebra

import numpy as np

a = np.mat(([1,2,3], [2,7,4]))
b = np.mat(([1,-1], [0,1]))
c = np.mat(([5,1], [9, 1], [6,0]))
d = np.mat(([3,-2,-1], [1,2,3]))
u = np.array(([6,2,-3,5]))
v = np.array([3,5,-1,4])
w = np.array(([1], [8], [0], [5]))

print('1.1:', a.shape)
print('1.2:', b.shape)
print('1.3:', c.shape)
print('1.4:', d.shape)
print('1.5:', u.shape)
print('1.6:', w.shape)

print('2.1:', u + v)
print('2.2:', u - v)
print('2.3:', 6 * u)
print('2.4:', np.dot(u,v))
print('2.5:', np.linalg.norm(u))

print('3.1: not defined')
print('3.2:', (a - c.transpose()))
print('3.3:', (c.transpose() + 3 * d))
print('3.4: not defined')
print('3.5:', (a.transpose() * b))
