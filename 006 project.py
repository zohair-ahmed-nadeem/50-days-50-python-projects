# Fibonacci Series

def fibonacci(n):
   fib_sequence = [0, 1]
   while len(fib_sequence) < n:
       fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
   return fib_sequence



while True:
	try:
		num = int(input("Enter Number Which u calculate fibonacci: "))
		fib = fibonacci(num)
		print(f"The fibonacci Series of {num} is {fib}.")
	except ValueError:
		print("Enter Number Please.")