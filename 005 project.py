# Factorial Calculator


def factorial(value):
	value = value + 1
	ans = 1
	for i in range(1,value):
		ans = ans * i
	print(f"The Factorial of {value-1} is {ans}.")

while True:
	try:
		print("_"*30)
		print("Factorial Calculate.")
		value = int(input("Enter the value u calculate factorial: "))
		factorial(value)
	except ValueError:
		print("Enter Number Only.")
	except KeyboardInterrupt:
		print("Exit From Program...")
		exit()