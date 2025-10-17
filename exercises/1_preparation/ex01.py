def get_even_letters(txt):
	even_letters = ""
	for i, letter in enumerate(txt):
		if i % 2 == 1:
			even_letters += letter
	return even_letters

def main():
	txt = "パタトクカシーー"
	even_letters = get_even_letters(txt)
	print(even_letters)

if __name__ == "__main__":
	main()

