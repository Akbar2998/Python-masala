import numpy as np
z = np.array([[1,2,3],[1,2,3],[1,2,9]])
matrix_B = np.array([[4,2,1],[3,3,1],[2,2,1]])
nol = np.zeros((3,3))
bir = np.ones((3,3))
yetti = np.full((3,3),7)
iden_3 = np.eye(3)
rx = np.random.random((2,2))
matrix_A = np.array([[1,2,3],[4,5,6],[7,8,10]])
matrix_B = np.array([[1],[2],[3]])
x = np.linalg.solve(matrix_A,matrix_B)
matrix_A_inv = np.linalg.inv(matrix_A)
y = matrix_A_inv.dot(matrix_B)
print(x)
print("---------------------------------------")
print(y)
np.allclose(x,y)





