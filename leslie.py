# -*- coding: latin-1 -*-
from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt

#------------------------------------------------
def exemple1():
    ngroupes=3
    u = np.zeros(ngroupes)
    u[0]=1
    A = np.empty(shape=(ngroupes,ngroupes))
    A[0] = [0, 1, 5]
    A[1] = [.3, 0, 0]
    A[2] = [0, .5, 0]
    print("A",A)
    return A, u

#------------------------------------------------
def exemple2():
    ngroupes=2
    u = np.zeros(ngroupes)
    u[0]=1
    A = np.empty(shape=(ngroupes,ngroupes))
    A[0] = [0, 2]
    A[1] = [.75, 0]
    print("A",A)
    return A, u

A, u = exemple1()
ng = u.shape[0]
# on recupère le nombre de groupes
uall = []
niter = 40
for k in range(niter):
    uall.append(u)
    u = A.dot(u)
for i in range(ng):
    plt.plot(np.array(uall)[:,i], label=r"N_{}".format(i))
    # il faut convertir uall en np.array (de taille shape=(niter, ng))
plt.plot(np.sum(np.array(uall),axis=1), label=r"N")
# pour la population complète, np.sum avec la moyenne sur la deuxième dimension 'axis=1'
plt.legend()
plt.show()