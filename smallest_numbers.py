import math
import array as arr


# take in the four real numbers
input_number1 = float(input("Enter the first number: "))
input_number2 = float(input("Enter the second number: "))
input_number3 = float(input("Enter the third number: "))
input_number4 = float(input("Enter the fourth number: "))

array_float = arr.array('f',[0,1,2,3])

array_float = [input_number1,input_number2,input_number3,input_number4]

input_method = input("Which method would you like, A or B: ")
#method A is what I devised, a simple array iteration to compare numbers
if input_method == "A":
	# compare all of them together
	n = 3
	smallest = array_float[0]
	for i in range(0, n):
		if (array_float[i] < smallest):
			smallest = array_float[i]

		
	print(smallest)
# B uses the function min() that I just found out exists
elif input_method == "B":
	smallest = min(array_float)
	print("the smallest number is %s " %smallest)
