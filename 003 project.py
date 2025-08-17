# Find Even or Odd Number


while True:
	try:
		print("--"*10)
		print(">> Enter Number Which you find out Odd or Even.")
		print(">> Enter 0 for Exit From Program.")
		print("--"*10)
		number = int(input("Enter The Number: "))

		if number == 0:
			print("Exit From Program")
			print("--"*10)
			exit()
		elif number % 2 == 0:
			print("--"*10)
			print(f"-{number} - Entered Number Is Odd")
			print("--"*10)
		else:
			print("--"*10)
			print(f"-{number} - Entred Number Is Even")
			print("--"*10)

	except ValueError as e:
		print("--"*10)
		print("Enter Number Which you find out Odd or Even ")
		print("--"*10)