# Matrix Algebra

import numpy as np

A = [[1,2,3],[2,7,4]]
B = [[1,-1],[0,1]]
C=[[5,-1],[9,1],[6,0]]
D=[[3,-2,-1],[1,2,3]]
u = [[6,2,-3,5]]
v = [[3,5,-1,4]]
w = [[1],[8],[0],[5]]

A = np.array(A)
B = np.array(B)
C = np.array(C)
D = np.array(D)
u = np.array(u)
v = np.array(v)
w = np.array(w)

print("Question 1")
print("Dimension of matrix A is " + str(A.shape) + " .")
print("Dimension of matrix B is " + str(B.shape) + " .")
print("Dimension of matrix C is " + str(C.shape) + " .")
print("Dimension of matrix D is " + str(D.shape) + " .")
print("Dimension of matrix u is " + str(u.shape) + " .")
print("Dimension of matrix v is " + str(v.shape) + " .")
print("Dimension of matrix w is " + str(w.shape) + " .")

alpha = 6
print("Question 2")
print("u + v =" + str(u+v))
print("u - v =" + str(u-v))
print("alpha*u =" + str(alpha*u))

print("u.v =" + str(np.dot(u,v.T)))
print("||u|| =" + str(np.linalg.norm(u)))

print("Question 3")
print("A + C = not defined")
print("")
print("A - Ct = ")
print(A-C.T)
print("")
print("Ct + 3D =")
print(C.T + 3*D))
print("")
print("BA = ")
print(np.dot(B,A))
print("")
print("BAt = not defined")

print("BONUS QUESTION")
print("BC = not defined")
print("CB =")
print(np.dot(C,B))
print("B^4 =")
print(np.linalg.matrix_power(B,4))
print("AAt = ")
print(np.dot(A,A.T))
print("DtD = ")
print(np.dot(D.T,D))
