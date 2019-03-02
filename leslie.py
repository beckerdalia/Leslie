from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt


niter=20
ngroupes=3

u = np.zeros(ngroupes)
u[1]=1
A = np.empty(shape=(ngroupes,ngroupes))
A[0] = [0,1,5]
A[1] = [.3, 0, 0]
A[2] = [0, .5, 0]
print("A",A)

uall = []
for i in range(niter):
    uall.append(u)
    u = A.dot(u)
plt.plot(uall)
plt.show()