import math

input_F_float = float(input("Enter the temperature in Fahrenheit: "))

C_float = round(float((input_F_float - 32)/1.8000), 3)

print("The temperature in Celsius is %f degrees" %C_float)