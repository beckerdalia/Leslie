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
#------------------------------------------------
def exemple3():
    ngroupes=3
    u = np.zeros(ngroupes)
    u[0]=30
    u[1]=40
    u[2]=30
    A = np.empty(shape=(ngroupes,ngroupes))
    A[0] = [0, 6, 10]
    A[1] = [.5, 0, 0]
    A[2] = [0, 0.4, 0]
    print("A",A)
    return A, u

#------------------------------------------------
def solveOde(u, A, niter = 40):
    ng = u.shape[0]
    # on recup�re le nombre de groupes
    uall = []
    for k in range(niter):
        uall.append(u)
        u = A.dot(u)
    uall = np.array(uall)
    # pour faire les plots un � un, il faut convertir uall en np.array (de taille shape=(niter, ng))
    for i in range(ng):
        plt.plot(uall[:, i], label=r"N_{}".format(i))
    plt.plot(np.sum(uall, axis=1), label=r"N")
    # pour la population compl�te, np.sum avec la moyenne sur la deuxi�me dimension 'axis=1'
    plt.legend()
    plt.show()

#------------------------------------------------
def powerIteration(u, A, niter = 20):
    for iter in range(niter):
        v = A.dot(u)
        lam = np.sum(v) / np.sum(u)
        v /= np.sum(v)
        print("iter", iter, "lam", lam, "26*v=", 26 * v.T)
        u = v


#------------------------------------------------
def plotEigVals(A):
    eigvals = linalg.eigvals(A)
    print("eigvals", eigvals)
    lam1 = np.max(np.absolute(eigvals))
    # calcul de la v.p. de Perron-Frobenius (= rayon spectral)
    plt.plot(np.real(eigvals), np.imag(eigvals), 'X', label=r"$\lambda$")
    plt.plot(0, 0, 'ob')
    plt.plot([-lam1,lam1],[0,0], 'k-')
    circle = plt.Circle((0, 0), lam1, color='r', fill=False)
    plt.gcf().gca().add_artist(circle)
    # il faut rajouter notre cercle � un axis
    # plt.gcf() donne la figure actuelle 'current figure' et gca() donne le current axis
    size = 1.1 * lam1
    plt.xlim((-size, size))
    plt.ylim((-size, size))
    plt.gcf().gca().set_aspect('equal')
    # fait que les �chelles sont les m�mes en x et en y
    plt.ylabel('Im')
    plt.xlabel('Re')
    plt.legend()
    plt.title(r"Nous avons $\lambda_1\approx${}".format(np.round(lam1, 3)))
    plt.show()


# A = np.random.rand(8,8)
# print("A", A)
# plotEigVals(A)
# import sys
# sys.exit(1)
#
A, u = exemple2()
solveOde(u, A)
plotEigVals(A)
powerIteration(u, A)
