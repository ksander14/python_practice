import random

N = 9
M = 3

a = [[random.randint(0, 2) for r in range(M)] for rr in range(N)]

# переменные отвечающие за положение текущего правого верхнего элемента диагонали
right_column = 0
right_row = 0

# переменные отвечающие за положение текущего левого нижнего элемента диагонали
left_column = 0
left_row = 0

current_number = 1

while (right_column != (len(a[0]) - 1) or right_row != (len(a) - 1)):
	
	# заполняем диагональ
	for i in range(left_row - right_row + 1):
		a[right_row + i][right_column - i] = current_number;
		current_number += 1;
		
	# смещаем левый нижний элемент диагонали вниз, если это возможно, или вправо в противном случае
	if left_row == (len(a) - 1):
		left_column += 1;
	else: left_row += 1;
	
	# смещение правого верхнего элемента
	if right_column == (len(a[0]) - 1):
		right_row += 1;
	else: right_column += 1;

a[len(a) - 1][len(a[0]) - 1] = current_number;

for i in range(len(a)):
	print(a[i])