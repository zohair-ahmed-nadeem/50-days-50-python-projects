# Number Guessing Game

import random

num = random.randrange(0,10)

while True:
	try:
		guess = int(input("Guess The Number, Range is (1 - 10) : "))
		if num == guess:
			print(f"Right, The number is {num}.")
			break
		else:
			print("Try Again!!!")
	except ValueError as e:
		print(f"Enter A Number {guess} is NAN.")
	
