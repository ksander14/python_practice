import random

N = 6
M = 4

a = [ [1, 1, 1, 1],
	  [0, 1, 1, 1],
	  [0, 0, 1, 1],
	  [0, 0, 1, 0],
	  [0, 0, 1, 0],
	  [0, 0, 1, 0]
]

"""a = [ [0, 0, 1, 0, 0, 0],
	  [0, 0, 1, 0, 0, 0],
	  [0, 0, 1, 0, 0, 0],
	  [0, 0, 1, 0, 0, 0]
]"""

#a = [[random.randint(0, 2) for r in range(M)] for rr in range(N)]

print(a)

current_row = 0
current_column = 0
rang = 0

# использовал метод гаусса для нахождения ранга
while (current_column != M and current_row != N):
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

print(rang)