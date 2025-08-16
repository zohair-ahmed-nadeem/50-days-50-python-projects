# Simple Calculator (Add, Subtract, Multiply, Divide)

while True:
	try:
		print("---"*5)
		print('''Selection Operation (1-5):\n1: Addintion\n2: Subtraction\n3: Multiplication\n4: Division\n5: Exit''')
		operation = input("Select AnyOne operation: ")
		
		if operation == "1":
			num1 = float(input("Enter 1st Number: "))
			num2 = float(input("Enter 2nd Number: "))
			ans = num1 + num2
			print(f"The Sum of {num1} or {num2} is {ans}.")

		elif operation == "2":
			num1 = float(input("Enter 1st Number: "))
			num2 = float(input("Enter 2nd Number: "))
			ans = num1 - num2
			print(f"The Diffrence of {num1} or {num2} is {ans}.")

		elif operation == "3":
			num1 = float(input("Enter 1st Number: "))
			num2 = float(input("Enter 2nd Number: "))
			ans = num1 * num2
			print(f"The Multiplication of {num1} or {num2} is {ans}.")

		elif operation == "4":
			num1 = float(input("Enter 1st Number: "))
			num2 = float(input("Enter 2nd Number: "))
			ans = num1 / num2
			print(f"The Division of {num1} or {num2} is {ans}.")

		elif operation == "5":
			print("Exit From Program...")
			exit()
		else:
			print("Enter correct Operation.")
	except ValueError as e:
		print("Enter Only Number.")
