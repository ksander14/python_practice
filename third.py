import random

N = 3
M = 5

a = [ [1, 2, 2, 4],
	  [2, -1, 3, 1],
	  [3, -4, 4, -2]
]

"""a = [ [1, 2, 3, 4, -2, 8],
	  [0, 0, 4, 7, 3, 10],
	  [0, 0, 0, 0, 6, 12],
	  [0, 0, 0, 0, 0, 0]
]"""

def printing(a):
	for i in range(len(a)):
		print(a[i])

# функция подсчета матрицы для проверки существования решения
def count_rang_matrix(a, column_bord):
	current_row = 0
	current_column = 0
	rang = 0
	
	# использовал метод гаусса для нахождения ранга
	while (current_column != column_bord and current_row != len(a)):
		i = current_row
		
		# ищем в текущем столбце ненулевой элемент
		while (i != len(a) and a[i][current_column] == 0 ):
			i += 1;
		
		# если столбец нулевой, то смещаем область видимости вправо, не изменяя ранга
		if i == len(a):
			current_column += 1;
			continue;
		
		# меняем текущую строку и строку с ненулевым элементов в столбце
		for j in range(current_column, len(a[current_row])):
			a[i][j], a[current_row][j] = a[current_row][j], a[i][j];
		
		# вычитанием первой строки с коэффициентом зануляем столбец
		for i in range(current_row + 1, len(a)):
			koef = - a[i][current_column] / a[current_row][current_column];
			for j in range(current_column, len(a[current_row])):
				a[i][j] += koef * a[current_row][j];
		
		# увеличиваем ранг и смещаем область видимости
		rang += 1
		current_row += 1
		current_column += 1
	return rang;	

matrix_rang = count_rang_matrix(a, len(a[0]))

# проверяем существование решения
if (matrix_rang != count_rang_matrix(a, len(a[0]) - 1)):
	print("There is no solution");
else:
	
	# списки для хранения базисных решений и решения
	basis_variables = [i for i in range(len(a[0]) - 1)]
	solution = [0 for i in range(len(a[0]) - 1)]
	i = 0
	j = 0
	
	# приводим к диагональному виду запоминая перестановки стобцов
	while (i != matrix_rang):
		while (a[i][j] == 0):
			j += 1
		if i != j:
			basis_variables[i], basis_variables[j] = basis_variables[j], basis_variables[i]
			for l in range(matrix_rang):
				a[l][i], a[l][j] = a[l][j], a[l][i]
		i += 1
	
	# для удобства решение по базисным переменным записываем в отдельный список
	# идем обратным ходом метода Гаусса вычисляя решение
	temp_solution = [0 for i in range(matrix_rang)]
	for l in range(matrix_rang):
		cur_solution = a[matrix_rang - 1 - l][len(a[0]) - 1]
		for k in range(l):
			cur_solution -= a[matrix_rang - 1 - l][matrix_rang - 1 - k]*temp_solution[matrix_rang - 1 - k]
		cur_solution /= a[matrix_rang - 1 - l][matrix_rang - 1 - l]
		temp_solution[matrix_rang - 1 - l] = cur_solution
		solution[basis_variables[matrix_rang - 1 - l]] = cur_solution

	print("X: ", solution)
	
	# проверка решения
	print("Checking:")
	for i in range(matrix_rang):
		left = 0
		for l in range(len(a[0]) - 1):
			left += a[i][l] * solution[basis_variables[l]]
		print("Solution: ", left, '  Right: ', a[i][len(a[0]) - 1])