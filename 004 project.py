# Palindrome Checker


def palindrome(word):
	word = word.lower()
	re_word = word[::-1]

	if word == re_word:
		return True
	else:
		return False
while True:
	print("---Palindrome Cheaker---")
	word = input("Enter The Word: ")
	
	if word.lower() == "exit":
		print("Exiting . . . ")
		exit()
		
	elif palindrome(word):
		print(f"The word {word} is palindrome.")

	else:
		print(f"The word {word} is not palindrome.")

	

