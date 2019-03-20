# -*- coding: latin-1 -*-
from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt
from scipy import linalg

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
uall = np.array(uall)
# pour faire les plots un à un, il faut convertir uall en np.array (de taille shape=(niter, ng))
for i in range(ng):
    plt.plot(uall[:,i], label=r"N_{}".format(i))
plt.plot(np.sum(uall,axis=1), label=r"N")
# pour la population complète, np.sum avec la moyenne sur la deuxième dimension 'axis=1'
plt.legend()
plt.show()

eigvals = linalg.eigvals(A)
lam1 = np.max(np.absolute(eigvals))
# calcul de la v.p. de Perron-Frobenius (= rayon spectral)
plt.plot(np.real(eigvals), np.imag(eigvals), 'X', label=r"$\lambda$")
plt.plot(0,0, 'ob')
circle = plt.Circle((0, 0), lam1, color='r', fill=False)
plt.gcf().gca().add_artist(circle)
# il faut rajouter notre cercle à un axis
# plt.gcf() donne la figure actuelle 'current figure' et gca() donne le current axis
size = 1.1*lam1
plt.xlim((-size,size))
plt.ylim((-size,size))
plt.gcf().gca().set_aspect('equal')
# fait que les échelles sont les mêmes en x et en y
plt.ylabel('Im')
plt.xlabel('Re')
plt.legend()
plt.title(r"Nous avons $\lambda_1\approx${}".format(np.round(lam1,3)))
plt.show()
