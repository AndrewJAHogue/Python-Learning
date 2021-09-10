import math
import array as arr

squares_int_arr = arr.array('i',[])
i = 0
for i in range(0,200):
	i_2 = pow(i,2)
	if i_2 % 3 == 0 and i_2 % 7 == 0:
		squares_int_arr.append(i_2)
print(squares_int_arr)