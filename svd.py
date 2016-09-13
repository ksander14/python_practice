N = 2
a = [[1, 3],
	[2, 7]]

# задаем начальное приближенние
U = [1 for i in range(N)]
V = [1 for i in range(N)]
L = [1 for i in range(N)]

dU = [0 for i in range(N)]
dV = [0 for i in range(N)]
dL = [0 for i in range(N)]

# функция подсчета ошибки
def error(a, U, V, L):
	err = 0
	for i in range(len(a)):
		for j in range(len(a)):
			err += (a[i][j] - U[i] * L[i] * V[j]) ** 2
	return err

# функция вычисления градиента
def grad(a, U, V, L):
	dU = [0 for i in range(N)]
	dV = [0 for i in range(N)]
	dL = [0 for i in range(N)]
	for i in range(N):
		for j in range(N):
			dU[i] -= V[j] * (a[i][j] - U[i] * L[i] * V[j])
			dL[i] -= V[j] * (a[i][j] - U[i] * L[i] * V[j])
			dV[i] -= U[j] * L[j] * (a[j][i] - U[j] * L[j] * V[i])
		dU[i] *= 2 * L[i]
		dL[i] *= 2 * U[i]
		dV[i] *= 2
	return dU, dV, dL

# переменные для ошибок и точности	
epsilon = 0.1
prev_error = 0
current_error = error(a, U, V, L)
iter_number = 0

# в цикле считаем градиент и новые значения переменных
while current_error > 0.01 and iter_number < 30:
	dU, dV, dL = grad(a, U, V, L)
	for i in range(N):
		U[i] -= epsilon * dU[i]
		V[i] -= epsilon * dV[i]
		L[i] -= epsilon * dL[i]
	prev_error = current_error
	current_error = error(a, U, V, L)
	if current_error > prev_error:
		epsilon /= 2
	iter_number += 1
	print("Iteration №", iter_number, "  Error: ", current_error)
	print("U = ", U, "\nV = ", V, "\nL = ", L, "\nEpsilon = ", epsilon)

print("U = ", U, "\nV = ", V)